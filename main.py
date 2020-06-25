from tkinter import Tk, Label, Button, Entry
import mainFrame
from functools import partial

class MENU:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label = Label(master, text="What do you want to convert?")
		self.label.grid()

		self.button = []
		t = 0
		for total in range(6):
			self.button.append(Button(master, width=10, text=mainFrame.methodName(total), command=partial(self.convert, total)))
			self.button[total].grid()
			t += 1
			if(t == 2):
				t = 0

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.grid(sticky="SE")

	def convert(self, argument):
		mainFrame.method(Tk(), argument)

def main():
	root = Tk()
	my_gui = MENU(root)
	root.mainloop()
main()