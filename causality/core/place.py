import os

class Place:
	def __init__(self,geo_path):
		self.geo_path = geo_path
		self.name = geo_path.split("/")[-1]
		self.placed_here = []
		self.make_geo_path()

	def __repr__(self):
		return "Place({})".format(self.geo_path)

	def make_geo_path(self,parent_dir="./places"):
		os.makedirs(parent_dir+self.geo_path, exist_ok=True)

	def add_event(self,event):
		self.placed_here.append(event)


	# def __del__
