import tkinter
import tkinter.ttk as ttk
import os
from world import world


class NewGameFrame(ttk.Frame):
    def __init__(self, master=None, app=None):
        ttk.Frame.__init__(self, master)
        self.app = app
        # create widgets
        self.actor_list_label = ttk.Label(self, text='Select Character')
        self.actor_listbox = tkinter.Listbox(self)
        self.actor_id_list = []
        for actor_id, name in world.get_actor_list():
            self.actor_listbox.insert(tkinter.END, name)
            self.actor_id_list.append(int(actor_id))
        self.confirm_button = ttk.Button(self, text='Confirm', command=self._b_confirm)
        self.name_entry = ttk.Entry(self)
        self.name_entry_label = ttk.Label(self, text='File Name')

        # grid widgets
        self.actor_listbox.grid(column=0, row=1, rowspan=3)
        self.actor_list_label.grid(column=0, row=0)
        self.confirm_button.grid(column=1, row=2)
        self.name_entry_label.grid(column=1, row=0)
        self.name_entry.grid(column=1, row=1)

    def _b_confirm(self):
        player = world.get_actor_by_id(self.actor_id_list[self.actor_listbox.curselection()[0]])
        self.app.create_new_save(self.name_entry.get(), player)
        self.master.cancel()


class LoadGameFrame(ttk.Frame):
    def __init__(self, master=None, app=None):
        ttk.Frame.__init__(self, master)
        self.app = app
        # create widgets
        self.save_listbox = tkinter.Listbox(self)
        for d in os.scandir('saves\\'):
            if d.is_dir():
                self.save_listbox.insert(tkinter.END, d.name)
        self.confirm_button = ttk.Button(self, text='Confirm', command=self._b_confirm)

        # grid widgets
        self.save_listbox.grid(rowspan=3)
        self.confirm_button.grid(column=1, row=0)

    def _b_confirm(self):
        index = self.save_listbox.curselection()[0]
        self.app.load_save(self.save_listbox.get(index))
        self.master.cancel()


class ActorStatsFrame(ttk.Frame):
    def __init__(self, master=None, actor=None):
        ttk.Frame.__init__(self, master)
        self.actor = actor

        # create widgets
        self.frames = {'strength': ttk.Frame(self), 'power': ttk.Frame(self), 'speed': ttk.Frame(self),
                       'brawl': ttk.Frame(self), 'accuracy': ttk.Frame(self), 'toughness': ttk.Frame(self)}
        self.strength_label = ttk.Label(self.frames['strength'])
        self.power_label = ttk.Label(self.frames['power'])
        self.speed_label = ttk.Label(self.frames['speed'])
        self.brawl_label = ttk.Label(self.frames['brawl'])
        self.accuracy_label = ttk.Label(self.frames['accuracy'])
        self.toughness_label = ttk.Label(self.frames['toughness'])

        # grid widgets
        self.frames['strength'].grid(row=0, columnspan=2, sticky=tkinter.W)
        self.frames['power'].grid(row=1, columnspan=2, sticky=tkinter.W)
        self.frames['speed'].grid(row=2, columnspan=2, sticky=tkinter.W)
        self.frames['brawl'].grid(row=3, columnspan=2, sticky=tkinter.W)
        self.frames['accuracy'].grid(row=4, columnspan=2, sticky=tkinter.W)
        self.frames['toughness'].grid(row=5, columnspan=2, sticky=tkinter.W)
        self.strength_label.grid(sticky=tkinter.W)
        self.power_label.grid(sticky=tkinter.W)
        self.speed_label.grid(sticky=tkinter.W)
        self.brawl_label.grid(sticky=tkinter.W)
        self.accuracy_label.grid(sticky=tkinter.W)
        self.toughness_label.grid(sticky=tkinter.W)

    def refresh(self, _=None):
        if self.actor is not None:
            for stat in self.frames:
                label = self.__getattribute__(stat + '_label')
                func = self.actor.__getattribute__(stat + '_display_str')
                label.config(text=func())
                self.frames[stat].config(borderwidth=1, relief='groove')
