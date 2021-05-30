from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # def __repr__(self):


# if a is greater than b return 1 it means ascending order
# if a is greater than b return -1 then it means descending order

# ascending = from lowtohigh ↓
# a is lower than d so a is first
# example jones is lower than smith so jones will be the higher
# descending = from high to low ↓

# Time Complexity of O(n) Space complexity of o(n)with the nature of the sort
# we used extra memory on the data and we basically looped through all the data in the array
# but if we don't con't how the module works then it is O(1) for time and
# O(n) for space

    def comparator(a, b):
        # descending by score
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            # ascending by name
            if a.name > b.name:
                return 1
            else:
                return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
