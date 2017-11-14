import tkinter
import tkinter.ttk as ttk
import editor
from util_frames import NewGameFrame, LoadGameFrame
from cbs_window import *
from world import world, set_world
from main_frames import PlayerActorFrame, CurrentLocationFrame
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
        self.editor_frame = editor.EditorMasterFrame(self)
        self.main_notebook.add(self.editor_frame, text='Editor')

    def create_top_menu(self):
        top = self.winfo_toplevel()
        self.menu_bar = tkinter.Menu(top)
        top['menu'] = self.menu_bar
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self._b_new_game)
        self.file_menu.add_command(label='Load', command=self._b_load_game)

    def _b_new_game(self):
        w = CBSWindow(self, 'New', 10, 10)
        new_game_frame = NewGameFrame(w, self)
        new_game_frame.grid()
        new_game_frame.grab_set()

    def _b_load_game(self):
        w = CBSWindow(self, 'New', 10, 10)
        load_game_frame = LoadGameFrame(w, self)
        load_game_frame.grid()
        load_game_frame.grab_set()

    def start_new(self, new_db):
        set_world(new_db)
        player_actor_frame = PlayerActorFrame(self)
        current_location_frame = CurrentLocationFrame(self)
        self.main_notebook.add(player_actor_frame, text='Character')
        self.main_notebook.add(current_location_frame, text='Location')
        self.main_notebook.hide(self.editor_frame)
        self.main_notebook.bind('<<NotebookTabChanged>>', player_actor_frame.refresh)

    def create_new_save(self, name, player_actor):
        new_dir = 'saves\\' + name
        os.makedirs(new_dir)
        new_db = new_dir + '\\database.db'
        shutil.copyfile('database.db', new_db)
        f = open(new_dir + '\\save.info', mode='w')
        f.write(str(player_actor.actor_id))
        world.player_actor = player_actor
        self.start_new(new_db)

    def load_save(self, name):
        f = open('saves\\' + name + '\\save.info', mode='r')
        actor_id = int(f.readline())
        world.set_player_actor_id(actor_id)
        new_db = 'saves\\' + name + '\\database.db'
        self.start_new(new_db)


app = Application()
app.master.title("CBS")
app.mainloop()
