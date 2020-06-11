#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self, title):
        Gtk.Window.__init__(self, title=title)
        

window = MainWindow("pad")
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
