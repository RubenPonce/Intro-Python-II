# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, name, items=[]):
        self.name = name
        self.room = room
        self.items = items
    def __str__(self):
        return f"{self.room} this is a room you're in {self.name}\n"
