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
	
	# update
	
	def update_month(self):
		if self.month>12:
			self.year+=1
			self.month-=12
		if self.month<1:
			self.year-=1
			self.month+=12
	
	def update_day(self):
		max_days=month_days.get(self.month,default=float("inf"))+(self.month==2)*self.leap()
		if self.days>max_days:
			self.days-=max_days
			self.month+=1
		if self.days<1:
			self.days+=max_days
			self.month-=1
			
	def update_hour(self):
		if self.hour>23:
			self.hour-=24
			self.day+=1
		if self.hour<0:
			self.hour+=24
			self.day-=1
			
	def update(self):
		self.update_hour()
		self.update_day()
		self.update_month()
		
	def update_repeated(self):
		before=self.copy()
		self.update()
		while self!=before:
			before=self.copy()
			self.update()
	
	# calculation
	
	def leap(self):
		return False if self.year%4!=0 else (True if self.year%100!=0 else (False if self.year%400!=0 else True))
	
 
	
	
		
		
		
		
		
		
		
