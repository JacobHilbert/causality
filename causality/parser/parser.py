import re
from inspect import getmembers
import pyparsing

class ParserError(Exception):
    pass

def only_attributes(obj):
    return [ i[0] for i in getmembers(obj) if (not i[0].startswith("_") and not callable(i[1])) ]

def filter_comments(text):
    r = text
    inline_comments = re.findall(r"\/\*[\s\S]+\*\/",r) # Match "/* any text */"
    line_comments = re.findall(r"\/\/.*",r) # Match "// any text until end of line", excluding the end of line
    for s in inline_comments+line_comments:
        r = r.replace(s,"")
    return r

def capture_env(text,env):
    '''
    Returns contents of text between "env {" and "} end env"
    Raise ParseError if there is anything but one env defined in text.
    '''
    env_match = re.findall(env+r" {[\s\S]*} end "+env,filter_comments(text))
    if len(env_match) != 1:
        raise ParseError(f"No \'{env}\' environment") if not env_match else ParseError("Multiple \'{env}\' environments")
    return env_match[0][len(env)+2:-len(env)-5]

class Head:
    title = ""
    time = ""
    place = ""
    tags = "#NoTag"
    arc = ""
    chapter = ""
    scene = ""
    vis = False
    _required=["title","time","place"]

    def parse_head(text):
        head_body = capture_env(text,"head").replace("\t","")

        for attr in only_attributes(Head):
            value =  Head.__dict__[attr]
            try:
                value = re.findall(attr+":.*",head_body)[0][len(attr)+2:]
            except IndexError:
                if attr in Head._required:
                    raise ParserError
            setattr(Head,attr,value)
