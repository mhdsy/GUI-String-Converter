#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from functions import *

class Handler():
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("main.glade")
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("main")
		self.window.connect("destroy", Gtk.main_quit)
		self.window.show_all()

		#button = self.window = self.builder.get_object("btn1")
		#button.connect("clicked",self.button_clicked)

		self.result =  self.builder.get_object("result")
		self.resultb = self.result.get_buffer()

		self.bt1 = self.builder.get_object("hex")
		self.bt2 = self.builder.get_object("octal")
		self.bt3 = self.builder.get_object("decimal")
		self.bt4 = self.builder.get_object("bin")
		
	
	def button_clicked(self, widget):
		tv1 = self.builder.get_object("txt")
		buf= tv1.get_buffer()
		text=buf.get_text(buf.get_start_iter(), buf.get_end_iter(),True)
		if self.bt1.get_active()==True:self.resultb.set_text(encodeToHex(text))
		if self.bt2.get_active()==True:self.resultb.set_text(encodeToOctal(text))
		if self.bt3.get_active()==True:self.resultb.set_text(encodeToDec(text))
		if self.bt4.get_active()==True:self.resultb.set_text(encodeToBinary(text))


if __name__ == '__main__':
	myApp = Handler()
	Gtk.main()
