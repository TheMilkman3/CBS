import tkinter
import tkinter.ttk as ttk
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
        self.app.start_new(self.name_entry.get(), player)
        self.master.cancel()
