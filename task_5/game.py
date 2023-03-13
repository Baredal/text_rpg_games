'''
RPG
'''

class Character:
    '''
    Main class for characters
    '''
    def __init__(self, char: str, descrpt) -> None:
        '''
        Init of all attributes of character
        '''
        self.char = char
        self.descrpt = descrpt
        self.convers = ''
    def set_description(self, descrpt: str):
        '''
        Adds description about character
        '''
        self.descrpt = descrpt
    def set_conversation(self, convers: str):
        '''
        Conversation (talks) of character
        '''
        self.convers = convers
    def describe(self):
        '''
        Describes character
        '''
        if isinstance(self, Enemy):
            print(f'{self.char} is here! (enemy)\n{self.descrpt}')
        else:
            print(f'{self.char} is here! (friend)\n{self.descrpt}')
    def talk(self):
        '''
        Character talking
        '''
        print(f'[{self.char} says]: {self.convers}')

class Room:
    '''
    Includes rooms
    '''
    def __init__(self, room: str) -> None:
        '''
        Init of all usable attributes of room
        '''
        self.room = room
        self.char = None
        self.item = None
        self.directions = {}
        self.descrpt = ''
    def set_description(self, descrpt: str):
        '''
        Adds about current room
        '''
        self.descrpt = descrpt
    def set_character(self, unk_char: str):
        '''
        Add character tp the room
        '''
        self.char = unk_char
    def get_character(self):
        '''
        Returns character
        '''
        return self.char
    def link_room(self, room: str, direction: str):
        '''
        Adds directions
        '''
        self.directions[direction] = room
    def set_item(self, item: str):
        '''
        Add item
        '''
        self.item = item
    def get_item(self):
        '''
        Returns item
        '''
        return self.item
    def move(self, direction: str):
        '''
        Moving on current direction
        '''
        return self.directions[direction]
    def get_details(self):
        '''
        Full info about current room
        '''
        ways = '\n'.join(f'The {value.room} is {key}' for key, value in self.directions.items())
        print(f'{self.room}\n--------------------\n{self.descrpt}\n{ways}')
        
class Enemy(Character):
    '''
    Includues enemies characters
    '''
    loses = 0
    def __init__(self, char: str, descrpt: str) -> None:
        '''
        Init all useful attributes for enemy
        '''
        super().__init__(char, descrpt) # str
        self.weakness = None
    def set_weakness(self, weakness: str):
        '''
        Weakness of enemy
        '''
        self.weakness = weakness
    def fight(self, item: str):
        '''
        Fighting with item from backpack with enemy
        '''
        if item == self.weakness or isinstance(self.weakness, type(None)):
            Enemy.loses +=1
            return True
        print(f'{self.char} crushes you, puny adventurer!')
        return False
    def get_defeated(self):
        '''
        Returns wins against enemies (enemies loses)
        '''
        return self.loses

class Friend(Character):
    '''
    Attributes for friend
    '''
    def __init__(self, char: str, descrpt) -> None:
        '''
        Init of friend (gives tips)
        '''
        super().__init__(char, descrpt)

class Item:
    '''
    Includes items
    '''
    def __init__(self, item: str) -> None:
        '''
        Init of all useful attributes for item
        '''
        self.item = item
        self.descrpt = ''
    def set_description(self, descrpt: str):
        '''
        Info about item
        '''
        self.descrpt = descrpt
    def describe(self):
        '''
        Returns info about item
        '''
        print(f'The [{self.item}] is here - {self.descrpt}')
    def get_name(self):
        '''
        Returns name of item
        '''
        return self.item
