import tkinter
import tkinter.ttk as ttk
from world import world


class PlayerActorFrame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        # create widgets
        self.actor_name_label = ttk.Label(self, text=world.player_actor.name)

        # grid widgets
        self.actor_name_label.grid()


class ActionSelectionFrame(ttk.Frame):
    pass
