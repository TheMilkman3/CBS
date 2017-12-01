import tkinter
import tkinter.ttk as ttk
from world import world
from actor import Actor


class EditorMasterFrame(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)
        self.resource_select_frame = EditorResourceSelectFrame(self)
        self.resource_select_frame.grid()
        self.active_frame = self.resource_select_frame

    def switch_active_frame(self, frame):
        if self.active_frame is not None:
            self.active_frame.grid_remove()
            del self.active_frame
        frame.on_switch()
        frame.grid()
        self.active_frame = frame


class EditorBaseFrame(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)

    def on_switch(self):
        pass


class EditorResourceSelectFrame(EditorBaseFrame):
    def __init__(self, parent=None):
        EditorBaseFrame.__init__(self, parent)
        self.actors_button = ttk.Button(self, text='Actors',
                                        command=lambda:
                                        self.master.switch_active_frame(EditorListFrame(self.master, mode='actors')))

        #self.actors_button.grid()


class EditorListFrame(EditorBaseFrame):
    def __init__(self, parent=None, mode='actors'):
        EditorBaseFrame.__init__(self, parent)
        self.grid()

        # create widgets
        self.listbox = tkinter.Listbox(self)
        self.listbox.config(exportselection='False')
        self.add_button = ttk.Button(self, text='Add', command=self._b_add)
        self.modify_button = ttk.Button(self, text='Modify', command=self._b_modify)

        # grid widgets
        self.listbox.grid(row=0, column=0, rowspan=4)
        self.add_button.grid(row=0, column=1)
        self.modify_button.grid(row=1, column=1)

        self.mode = mode
        self.resource_ids = []

    def refresh_list_box(self):
        self.resource_ids.clear()
        self.listbox.delete(0, self.listbox.size() - 1)
        resource_list = None
        if self.mode == 'actors':
            resource_list = world.get_actor_list()
            resource_list.sort(key=lambda a: a[1])
        for resource_id, name in resource_list:
            self.listbox.insert(tkinter.END, name)
            self.resource_ids.append(int(resource_id))

    def on_switch(self):
        self.refresh_list_box()

    def _b_add(self):
        parent = self.master
        detail_frame = EditorActorDetailFrame(parent, 'add')
        parent.switch_active_frame(detail_frame)

    def _b_modify(self):
        parent = self.master
        index = self.listbox.curselection()
        if len(index) > 0:
            detail_frame = EditorActorDetailFrame(parent, 'modify', self.resource_ids[index[0]])
            parent.switch_active_frame(detail_frame)


class EditorActorDetailFrame(EditorBaseFrame):
    def __init__(self, parent=None, mode='add', actor_id=None):
        EditorBaseFrame.__init__(self, parent)
        self.actor = Actor()
        self.mode = mode
        self.actor_id = actor_id
        if self.actor_id is not None:
            self.load_actor()

        # create widgets
        name_frame = ttk.LabelFrame(self, text='Name')
        self.name_entry = ttk.Entry(name_frame, textvariable=self.actor.get_name_var())
        alignment_frame = ttk.LabelFrame(self, text='Alignment')
        self.alignment_combobox = \
            ttk.Combobox(alignment_frame, values=('Hero', 'Anti-Hero', 'Villain', 'Civilian', 'Wild Card'),
                         textvariable=self.actor.get_alignment_var())
        self.alignment_combobox.set(self.actor.alignment)
        self.save_button = ttk.Button(self, text='Save', command=self._b_save)
        self.back_button = ttk.Button(self, text='Back', command=self._b_back)

        # grid widgets
        self.name_entry.grid()
        self.alignment_combobox.grid()
        name_frame.grid(column=0, row=0)
        alignment_frame.grid(column=1, row=0)
        self.save_button.grid(column=10, row=0)
        self.back_button.grid(column=11, row=0)

    def load_actor(self):
        self.actor = world.get_actor_by_id(self.actor_id)

    def _b_save(self):
        if self.mode == 'add':
            world.add_actor(self.actor)
        elif self.mode == 'modify':
            world.update_actor(self.actor)

    def _b_back(self):
        self.master.switch_active_frame(EditorListFrame(self.master, mode='actors'))
