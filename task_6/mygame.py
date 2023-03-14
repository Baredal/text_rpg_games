'''
Wanderer RPG Game (streets)
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
            print(f'Ви зустріли {self.char}! (ворог)\n{self.descrpt}')
        else:
            print(f'Ви зустріли {self.char}! (друг)\n{self.descrpt}')
    def talk(self):
        '''
        Character talking
        '''
        print(f'[{self.char} говорить]: {self.convers}')

class Street:
    '''
    Includes streets
    '''
    def __init__(self, street: str) -> None:
        '''
        Init of all usable attributes of street
        '''
        self.street = street
        self.char = None
        self.item = None
        self.directions = {}
        self.descrpt = ''
    def set_description(self, descrpt: str):
        '''
        Adds about current street
        '''
        self.descrpt = descrpt
    def set_character(self, unk_char: str):
        '''
        Add character tp the street
        '''
        self.char = unk_char
    def get_character(self):
        '''
        Returns character
        '''
        return self.char
    def link_street(self, street: str, direction: str):
        '''
        Adds directions
        '''
        self.directions[direction] = street
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
        Full info about current street
        '''
        ways = '\n'.join(f'{value.street} -> {key}' for key, value in self.directions.items())
        print(f'{self.street}\n--------------------\n{self.descrpt}\n{ways}')
        
class Enemy(Character):
    '''
    Includues enemies characters
    '''
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
            return True
        return False

class Batyar(Enemy):
    '''
    Batyar skills
    '''
    def __init__(self, char: str, descrpt: str) -> None:
        super().__init__(char, descrpt)
    def fight(self, item: str):
        '''
        Fighting with item from backpack with enemy
        '''
        if item == self.weakness or isinstance(self.weakness, type(None)):
            print(f'{self.char} задолений, він вас відпускає')
            return True
        else:
            print(f'{self.char} відправляє вас в нокаут!')
            return False

class Stranger(Enemy):
    '''
    Lotr skills
    '''
    def __init__(self, char: str, descrpt: str) -> None:
        '''
        Init of lotr attributes
        '''
        super().__init__(char, descrpt)
    def fight(self, item: str):
        '''
        Fighting with item from backpack with enemy
        '''
        if item == self.weakness or isinstance(self.weakness, type(None)):
            print(f'[{self.char} говорить]: Братан, ти мене виручив!')
            return True
        else:
            print(f'{self.char} зневажливо посміхається. Схоже вам не пройти цього разу')
            return False

class Bandit(Enemy):
    '''
    Bandit skills
    '''
    def __init__(self, char: str, descrpt: str) -> None:
        '''
        Init of bandit attributes
        '''
        super().__init__(char, descrpt)
    def fight(self, item: str):
        '''
        Fighting with item from backpack with enemy
        '''
        if item == self.weakness or isinstance(self.weakness, type(None)):
            print(f'[{self.char} говорить]: Будемо вважати це як плату. На цей раз я відпускаю тебе')
            return True
        elif item == 'пістолет':
            print(f'Ви не встигаєте дістати пістолет, як {self.char} дістає зброю й вистрілює у вас...')
            return False
        elif item == 'гаманець':
            print(f"Він лише сміється, дивлячись на цей дріб'язок грошей. {self.char} дістає зброю й вистрілює у вас...")
            return False
        elif item == 'сигарети':
            print(f"Схоже йому це не потрібно. {self.char} дістає зброю й вистрілює у вас...")
            return False
        elif item == 'бігмак':
            print(f"Він дивиться на вас, як на ненормального. {self.char} дістає зброю й вистрілює у вас...")
            return False
        else:
            print(f'{self.char} дістає зброю й вистрілює у вас..."')
            return False

class Homeless(Enemy):
    '''
    Homeless skills
    '''
    def __init__(self, char: str, descrpt: str) -> None:
        '''
        Attributes of homeless
        '''
        super().__init__(char, descrpt)
    def fight(self, item: str):
        '''
        Fighting with item from backpack with enemy
        '''
        if item == self.weakness or isinstance(self.weakness, type(None)):
            print(f'[{self.char} говорить]: Нарешті я зможу поїсти. Дякую що допоміг!')
            return True
        else:
            print(f'{self.char} лише сумно на вас глянув...')
            return False

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
        print(f'Тут є [{self.item}] - {self.descrpt}')
    def get_name(self):
        '''
        Returns name of item
        '''
        return self.item
