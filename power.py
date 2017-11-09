from rng import rng


class Power:
    def __init__(self, name, effect_type, effect_class, effect, strength_based):
        self.name = name
        self.effect_type = effect_type
        self.effect_class = effect_class
        self.effect = effect
        self.strength_based = strength_based


class PowerEffect:
    def __init__(self, power):
        self.power = power

    def apply(self, user, target):
        pass

    def check_hit(self, user, target):
        if self.power.effect_type == 'melee':
            user_score = user.brawl_value()
            target_score = target.brawl_value()
        elif self.power.effect_type == 'ranged':
            user_score = user.accuracy_value()
            target_score = user.speed_value()
        else:
            user_score = 0
            target_score = 0
        user_result = self._roll(user_score)
        target_result = self._roll(target_score)
        return user_result >= target_result

    @staticmethod
    def _roll(score):
        # roll 3 numbers between 0 and the score, use middle roll
        rolls = [rng.randint(0, score) for _ in range(3)]
        rolls.sort()
        return rolls[1]


class DamageEffect(PowerEffect):
    def apply(self, user, target):
        if self.power.strength_based:
            user_score = self.user.strength_value()
        else:
            user_score = self.user.power_value()
        user_result = self._roll(user_score)
        damage = user_result/target.toughness_value()
        target.health_per = max(target.health_per - damage, 0)
