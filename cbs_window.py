from tkinter import Toplevel


class CBSWindow(Toplevel):
    def __init__(self, parent, title=None, x_offset=0, y_offset=0):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        if title:
            self.title(title)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+x_offset,
                                  parent.winfo_rooty()+y_offset))

    def cancel(self):
        self.parent.focus_set()
        self.destroy()
