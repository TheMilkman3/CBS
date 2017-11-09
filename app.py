import tkinter
import tkinter.ttk as ttk
import editor
from util_frames import NewGameFrame



class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, width=1000, height=500)
        self.grid()
        self.grid_propagate(0)
        self.file_menu = None
        self.menu_bar = None
        self.create_top_menu()
        self.main_notebook = ttk.Notebook(self)
        self.main_notebook.grid()
        self.main_notebook.add(editor.EditorMasterFrame(self), text='Editor')
        self.new_game_frame = None

    def create_top_menu(self):
        top = self.winfo_toplevel()
        self.menu_bar = tkinter.Menu(top)
        top['menu'] = self.menu_bar
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self._b_new_game)
        self.file_menu.add_command(label='Load')

    def _b_new_game(self):
        w = tkinter.Toplevel()
        self.new_game_frame = NewGameFrame(w)
        self.new_game_frame.grid()
        self.lock()

    def lock(self, cur=None):
        if cur is None:
            cur = self
        for child in cur.winfo_children():
            try:
                child.config(state='disabled')
            except tkinter.TclError:
                pass
            self.lock(child)

    def unlock(self, cur=None):
        if cur is None:
            cur = self
        for child in cur.children:
            child.config(state='enabled')
            self.unlock(child)


app = Application()
app.master.title("CBS")
app.mainloop()
