

class Game:
    def __init__(self):
        self.current_roll = 0
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def score(self):
        score = 0
        frame_index = 0

        for _ in range(0, 10):
            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score
