import tkinter
import tkinter.ttk as ttk
from world import world
from PIL import Image, ImageTk
import fonts


class PlayerActorFrame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.actor_image = None

        # create widgets
        self.details_label_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.details_label_frame, font=fonts.DETAIL_NAME_FONT)
        self.alignment_label_frame = ttk.LabelFrame(self.details_label_frame, text='Alignment')
        self.alignment_label = ttk.Label(self.alignment_label_frame)
        self.gender_label_frame = ttk.LabelFrame(self.details_label_frame, text='Gender')
        self.gender_label = ttk.Label(self.gender_label_frame)
        self.image_box = ttk.Label(self, borderwidth=5, relief=tkinter.RIDGE)

        # grid widgets
        self.details_label_frame.grid()
        self.alignment_label_frame.grid(column=0, row=1, sticky=tkinter.NW)
        self.gender_label_frame.grid(column=1, row=1, sticky=tkinter.NW)
        self.name_label.grid(column=0, row=0)
        self.gender_label.grid()
        self.alignment_label.grid()
        self.image_box.grid(column=2, row=0, rowspan=8)

        self.refresh()

    def refresh(self, _=None):
        player_actor = world.player_actor
        self.name_label.config(text=player_actor.name)
        self.alignment_label.config(text=player_actor.alignment)
        self.gender_label.config(text=player_actor.gender)
        if player_actor.image is not None:
            image = Image.open(player_actor.image)
            image = image.resize((200, 300), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(image)
            self.actor_image = tkimage
            self.image_box.config(image=tkimage)


class ActionSelectionFrame(ttk.Frame):
    def __init__(self):
        pass
