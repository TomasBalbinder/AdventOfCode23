
#part one
class Value():

    def __init__(self):
        with open("day01.txt", 'r') as day01:
            self.obsah = day01.read().split()

    def spliting(self):
        result = []
        for item in self.obsah:
            current_numbers = []
            result.append(current_numbers)
            for char in item:
                if char.isdigit():
                    if len(char) == 1:
                        current_numbers.extend([char, char])
                    else:
                        current_numbers.append(char)
        return result

    def addition(self):
        total = 0
        for item_numbers in self.spliting():
            digit_count = len(item_numbers)
            first_and_last = item_numbers[0::digit_count - 1]
            combined_number = int(first_and_last[0] + first_and_last[1])
            total += combined_number
        return total

calibration_value = Value()
print(calibration_value.addition())


#part two, not finished

test = ['two1nine', 'eightwothree','4nineeightseven2']
numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

end = []
for s in test:
    next = []
    for i, j in numbers.items():
        if i in s:
            next.append(int(j))
    end.append(next)

print(end)