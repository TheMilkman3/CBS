import tkinter
import tkinter.ttk as ttk
import editor
from util_frames import NewGameFrame
from cbs_window import *
from world import world, set_world
from main_frames import PlayerActorFrame
import os
import shutil


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
        w = CBSWindow(self, 'New', 10, 10)
        self.new_game_frame = NewGameFrame(w, self)
        self.new_game_frame.grid()
        self.new_game_frame.grab_set()

    def start_new(self, name, player_actor):
        new_dir = 'saves\\' + name
        os.makedirs(new_dir)
        new_db = new_dir + '\\database.db'
        shutil.copyfile('database.db', new_db)
        set_world(new_db)
        world.player_actor = player_actor
        self.main_notebook.add(PlayerActorFrame(self), text='Character')



app = Application()
app.master.title("CBS")
app.mainloop()
