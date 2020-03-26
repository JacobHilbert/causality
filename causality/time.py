month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

class Time:
	# initialization
	def __init__(self,year=0,month=0,day=0,hour=0):
		self.year=year
		self.month=month
		self.day=day
		self.hour=hour
		self.update_repeated()
		
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
		max_days=month_days.get(self.month,float("inf"))+(self.month==2)*self.leap()
		if self.day>max_days:
			self.day-=max_days
			self.month+=1
		if self.day<1:
			self.day+=max_days
			self.month-=1
			
	def update_hour(self):
		if self.hour>23:
			self.hour-=24
			self.day+=1
		if self.hour<0:
			self.hour+=24
			self.day-=1
			
	def update(self):
		self.update_month()
		self.update_day()
		self.update_hour()

	def update_repeated(self):
		before=self.value()
		self.update()
		while self.value()!=before:
			before=self.value()
			self.update()
	
	# calculation
	
	def add_hours(self,num):
		self.hour+=num
		self.update_repeated()
		return self
	def add_days(self,num):
		self.day+=num
		self.update_repeated()
		return self
	def hours_to(self,other):
		if self==other:
			return True
		elif self < other:
			h=0
			selfcopy=self.copy()
			while selfcopy < other:
				selfcopy.add_hours(1)
				h+=1
			return h
		elif self > other:
			return -other.hours_to(self)
	
	def days_to(self,other):
		if abs(self.value()-other.value())<100:
			return 0
		elif self < other:
			d=0
			selfcopy=self.copy()
			while selfcopy < other:
				d+=1
				selfcopy.add_days(1)
			return d
		elif self > other:
			return -other.days_to(self)
	
	def leap(self):
		return False if self.year%4!=0 else (True if self.year%100!=0 else (False if self.year%400!=0 else True))
	
