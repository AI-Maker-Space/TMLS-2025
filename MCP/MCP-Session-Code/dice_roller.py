import random
import re

class DiceRoller:
    def __init__(self, notation, num_rolls=1):
        self.notation = notation
        self.num_rolls = num_rolls
        self.dice_pattern = re.compile(r"(\d+)d(\d+)(k(\d+))?")

    def roll_dice(self):
        match = self.dice_pattern.match(self.notation)
        if not match:
            raise ValueError("Invalid dice notation")

        num_dice = int(match.group(1))
        dice_sides = int(match.group(2))
        keep = int(match.group(4)) if match.group(4) else num_dice

        rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]
        rolls.sort(reverse=True)
        kept_rolls = rolls[:keep]

        return rolls, kept_rolls

    def roll_multiple(self):
        """Roll the dice multiple times according to num_rolls"""
        results = []
        for _ in range(self.num_rolls):
            rolls, kept_rolls = self.roll_dice()
            results.append({
                "rolls": rolls,
                "kept": kept_rolls,
                "total": sum(kept_rolls)
            })
        return results

    def __str__(self):
        if self.num_rolls == 1:
            rolls, kept_rolls = self.roll_dice()
            return f"ROLLS: {', '.join(map(str, rolls))} -> RETURNS: {sum(kept_rolls)}"
        else:
            results = self.roll_multiple()
            result_strs = []
            for i, result in enumerate(results, 1):
                result_strs.append(f"Roll {i}: ROLLS: {', '.join(map(str, result['rolls']))} -> RETURNS: {result['total']}")
            return "\n".join(result_strs)

if __name__ == "__main__":
    notation = input("Enter dice notation (e.g., 2d20k1): ")
    num_rolls = int(input("Number of rolls: ") or "1")
    dice_roller = DiceRoller(notation, num_rolls)
    print(dice_roller) 