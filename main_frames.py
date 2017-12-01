import tkinter
import tkinter.ttk as ttk
from world import world
from util_frames import ActorStatsFrame
from PIL import Image, ImageTk
import fonts


class PlayerActorFrame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.actor_image = None

        # create widgets
        self.details_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.details_frame, font=fonts.DETAIL_NAME_FONT)
        self.alignment_label_frame = ttk.LabelFrame(self.details_frame, text='Alignment')
        self.alignment_label = ttk.Label(self.alignment_label_frame)
        self.gender_label_frame = ttk.LabelFrame(self.details_frame, text='Gender')
        self.gender_label = ttk.Label(self.gender_label_frame)
        self.image_box = ttk.Label(self, borderwidth=5, relief=tkinter.RIDGE)
        self.actor_stats_frame = ActorStatsFrame(self)

        # grid widgets
        self.details_frame.grid()
        self.alignment_label_frame.grid(column=0, row=1, sticky=tkinter.NW)
        self.gender_label_frame.grid(column=1, row=1, sticky=tkinter.NW)
        self.name_label.grid(column=0, row=0)
        self.gender_label.grid()
        self.alignment_label.grid()
        self.image_box.grid(column=2, row=0, rowspan=8)
        self.actor_stats_frame.grid(column=0, row=2, sticky=tkinter.NW)

        self.refresh()

    def refresh(self, _=None):
        player_actor = world.player_actor
        self.name_label.config(text=player_actor.name)
        self.alignment_label.config(text=player_actor.alignment)
        self.gender_label.config(text=player_actor.gender)
        if player_actor.image != '' and player_actor.image is not None:
            image = Image.open('images\\' + player_actor.image)
            image = image.resize((200, 300), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(image)
            self.actor_image = tkimage
            self.image_box.config(image=tkimage)
        self.actor_stats_frame.actor = player_actor
        self.actor_stats_frame.refresh()


class CurrentLocationFrame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        # create widgets
        self.name_label = ttk.Label(self, font=fonts.DETAIL_NAME_FONT)
        self.actor_listbox_label_frame = ttk.LabelFrame(self, text='Characters at Location')
        self.actor_listbox = tkinter.Listbox(self.actor_listbox_label_frame)
        self.actor_listbox.config(exportselection='False')
        self.actor_id_listbox = []
        self.area_label_frame = ttk.LabelFrame(self, text='Area')
        self.dimension_label_frame = ttk.LabelFrame(self, text='Dimension')
        self.timeframe_label_frame = ttk.LabelFrame(self, text='Timeframe')
        self.area_label = ttk.Label(self.area_label_frame)
        self.dimension_label = ttk.Label(self.dimension_label_frame)
        self.timeframe_label = ttk.Label(self.timeframe_label_frame)

        # grid widgets
        self.name_label.grid(column=0, row=0, sticky=tkinter.NW)
        self.actor_listbox_label_frame.grid(column=0, row=1)
        self.actor_listbox.grid()

        self.refresh()

    def refresh(self, _=None):
        location = world.get_current_location()
        self.actor_listbox.delete(0, self.actor_listbox.size()-1)
        self.actor_id_listbox.clear()
        self.name_label.config(text=location.name)
        actor_list = world.get_actor_list_from_loc(location.location_id)
        for location_id, name in actor_list:
            self.actor_listbox.insert(tkinter.END, name)
            self.actor_id_listbox.append(location_id)


class ActionSelectionFrame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(master)
