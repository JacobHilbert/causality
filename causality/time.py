month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

class Time:
	# initialization
	def __init__(self,year=0,month=0,day=0,hour=0):
		self.year=year
		self.month=month
		self.day=day
		self.hour=hour
		
	# representation of the class
	
	def attribute_list(self):
		return list(self.__dict__.values())
	def value(self):
		span_list=[10**6,10**4,10**2,1]
		return sum( [ i*j for i,j in zip(self.attribute_list(),span_list) ] )
	def copy(self):
		return Time(*self.attribute_list())
	
	def __repr__(self):
		return "Time(year={},month={},day={},hour={})".format(*self.attribute_list())
	def __str__(self):
		return "{:04d}:{:02d}:{:02d}:{:02d}".format(*self.attribute_list())
	
	# comparation 
	
	def __eq__(self,other):
		return self.value() == other.value()
	def __lt__(self,other):
		return self.value() < other.value()
	def __le__(self,other):
		return (self==other or self<other)
	
	# calculation
    
   
