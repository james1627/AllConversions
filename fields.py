from tkinter import Tk, Label, Button, Entry, Menu
from functools import partial
import Convert


class field:
	def __init__(self, master, typeOfUnit):
		self.setType(typeOfUnit)
		self.start = 0
		self.master = master

		self.menubar = Menu(master)

		self.unitmenu = Menu(self.menubar, tearoff=0)

		self.en = Entry(master, width=30)
		self.en.grid(columnspan = 10, sticky="N")

		t = 0
		r = 1
		for i in range(Convert.numberOfUnits(self.ty)):
			
			self.unitmenu.add_command(label=Convert.unitName(self.ty, i), command=partial(self.toChange, i))
			self.button = Button(master, height=2, width=5, text=Convert.unitName(self.ty, i), command=partial(self.changeType, i))
			self.button.grid(row = r, column = i-(r-1)*4)

			if t > 2:
				t = 0
				r += 1
			else:
				t += 1
			

		self.menubar.add_cascade(label="start unit", menu=self.unitmenu)
		master.config(menu=self.menubar)

		self.label = Label(self.master)

	def setType(self, typeOfUnit):
		if typeOfUnit == "distance":
			from Convert import distance as ty
		elif typeOfUnit == "area":
			from Convert import area as ty
		elif typeOfUnit == "mass":
			from Convert import mass as ty
		elif typeOfUnit == "volume":
			from Convert import volume as ty
		elif typeOfUnit == "temperature":
			from Convert import temperature as ty
		elif typeOfUnit == "energy":
			from Convert import energy as ty
		self.ty = ty

	def toChange(self, value):
		self.start = value
		self.menubar.entryconfig(1, label=Convert.unitName(self.ty, value))

	def changeType(self, newType):
		number = self.en.get()
		self.label.destroy()
		try:
			number = float(number)
		except:
			self.label = Label(self.master, text="type in a number please")
			self.label.grid(columnspan = 12, sticky="SE")
			return False

		value = Convert.newUnit(self.ty, number, Convert.unitName(self.ty, self.start), Convert.unitName(self.ty, newType))
		self.en.delete(0, 20)
		
		self.label = Label(self.master, height=3, text=str(value)+" "+Convert.unitName(self.ty, newType))
		self.label.grid(columnspan = 12, sticky="SE")