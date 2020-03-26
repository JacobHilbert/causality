# causality

This is intented to be a writing application where one could visualize the causal connections between events on a plot, manage references, tags, and timelines.

The main goal here is to write a python package that takes a bunch of correlated folders (events) and text files (events' parts) and turns them into:

1. A transitable webpage-like html structure via [markdown2](https://github.com/trentm/python-markdown2) and [regular expression](https://github.com/python/cpython/blob/master/Lib/re.py) parsing.

2. A tree structure of cause-consecuence relations bewteen events.

And as extras, maybe:

3. A document that list every `Event` that has certain `#Tag` ---maybe a docuemnt for each tag, and a parent index...

4. A timeline.

5. A graph structure of reference relations.

More information (the code structure and documentation) will be put in the Docuemntation.md

This is a personal proyect. 

## The standard input format

The main concept here is the `Event`, a thing that happens in a time and a space. All events must be 


## To do:

- [ ] Write the abstract python classes structure.
    - [x] Implement my own way to manage time-date data.
        - [x] This includes full calendary functionality,
        - [x] Timespan between date objects
        - [x] And pretty formatting.
    - [ ] Implement my own way to manage places. (Maybe like the directory management on unix-like systems...)
    - [ ] Implement `Tags`
    - [ ] Implement `Parts`
    - [ ] Implement `Events`
- [ ] Develop an standard input format.
    - [ ] Maybe develop a GUI application to write in this format.
- [ ] Save the causes-consecuences realtion graph in a suitable format.
- [ ] Implement a tag system.
- [ ] Implement a referencing system.
- [ ] Automatically generate webpage-like presentation via markdown:
    - [ ] Produce `html` documents to present the information,
    - [ ] Make the local linking work programatically
    - [ ] And an index.
