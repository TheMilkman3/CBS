from tkinter import StringVar

# alignment constants
ALIGNMENTS = ('Hero', 'Anti-Hero', 'Villain', 'Civilian', 'Wild Card')
# gender constants
GENDERS = ('Male', 'Female', 'Other', 'N/A')
# tier constants
TIERS = ('Pathetic', 'Weak', 'Average', 'Superior', 'Peak', 'Inhuman', 'Super', 'Legendary', 'Godlike',
         'Cosmic')


class Actor:
    def __init__(self, actor_id=None, name=None, image=None,
                 gender='N/A', alignment='Hero', location=None,
                 health_per=1.0, energy_per=1.0,
                 strength_tier=3, strength_rank=1, power_tier=3, power_rank=1,
                 speed_tier=3, speed_rank=1, brawl_tier=3, brawl_rank=1,
                 accuracy_tier=3, accuracy_rank=1, toughness_tier=3, toughness_rank=1):
        self._alignment = StringVar()
        self._gender = StringVar()
        self._name = StringVar()
        self._image = None
        self._location = None
        self.actor_id = actor_id
        self.name = name
        self.image = image
        self.gender = gender
        self.alignment = alignment
        self.location = location
        self.health_per = health_per
        self.energy_per = energy_per
        self.strength_tier = strength_tier
        self.strength_rank = strength_rank
        self.power_tier = power_tier
        self.power_rank = power_rank
        self.speed_tier = speed_tier
        self.speed_rank = speed_rank
        self.brawl_tier = brawl_tier
        self.brawl_rank = brawl_rank
        self.accuracy_tier = accuracy_tier
        self.accuracy_rank = accuracy_rank
        self.toughness_tier = toughness_tier
        self.toughness_rank = toughness_rank

    @property
    def name(self):
        return self._name.get()

    @name.setter
    def name(self, value):
        self._name.set(value)

    def get_name_var(self):
        return self._name

    @property
    def alignment(self):
        return self._alignment.get()

    @alignment.setter
    def alignment(self, value):
        if value in ALIGNMENTS:
            self._alignment.set(value)

    def get_alignment_var(self):
        return self._alignment

    @property
    def gender(self):
        return self._gender.get()

    @gender.setter
    def gender(self, value):
        if value in GENDERS:
            self._gender.set(value)

    def get_gender_var(self):
        return self._gender

    @staticmethod
    def _calc_attribute_value(tier, rank):
        return 10**(tier-1) * rank

    @staticmethod
    def _attribute_display_string(attribute, tier, rank):
        return '{tier} {attribute} [{rank}]'.format(tier=TIERS[tier-1], attribute=attribute, rank=rank)

    def strength_value(self):
        return self._calc_attribute_value(self.strength_tier, self.strength_rank)

    def strength_display_str(self):
        return self._attribute_display_string('Strength', self.strength_tier, self.strength_rank)

    def power_value(self):
        return self._calc_attribute_value(self.power_tier, self.power_rank)

    def power_display_str(self):
        return self._attribute_display_string('Power', self.power_tier, self.power_rank)

    def speed_value(self):
        return self._calc_attribute_value(self.speed_tier, self.speed_rank)

    def speed_display_str(self):
        return self._attribute_display_string('Speed', self.speed_tier, self.speed_rank)

    def brawl_value(self):
        return self._calc_attribute_value(self.brawl_tier, self.brawl_rank)

    def brawl_display_str(self):
        return self._attribute_display_string('Brawl', self.brawl_tier, self.brawl_rank)

    def accuracy_value(self):
        return self._calc_attribute_value(self.accuracy_tier, self.accuracy_rank)

    def accuracy_display_str(self):
        return self._attribute_display_string('Accuracy', self.accuracy_tier, self.accuracy_rank)

    def toughness_value(self):
        return self._calc_attribute_value(self.toughness_tier, self.toughness_rank)

    def toughness_display_str(self):
        return self._attribute_display_string('Toughness', self.toughness_tier, self.toughness_rank)

    def health_total(self):
        return self.toughness_value()

    def health_current(self):
        return self.health_total() * self.health_per

    def energy_total(self):
        return (self.power_value() + self.toughness_value())/2

    def energy_current(self):
        return self.energy_total() * self.energy_per
