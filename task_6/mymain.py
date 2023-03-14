import mygame

#adding streets
Stryiska = mygame.Street('вул. Стрийська')
Stryiska.set_description('Довжилезна вулиця з нескінченними корками')

Kozelnytska = mygame.Street('вул. Козельницька')
Kozelnytska.set_description('Чиста і гарна вулиця, поблизу видніється Стрийський парк')

Franka = mygame.Street('вул. І.Франка')
Franka.set_description('Ця вулиця навиває спогади автору. Від різноманітності магазинів вам розбігаються очі')

Shevchenka = mygame.Street('пр.Т.Шевченка')
Shevchenka.set_description('Зненацька вам чомусь захотілось перекусити')

Staroevr = mygame.Street('вул. Староєврейська')
Staroevr.set_description('Старовинна вулиця в центрі міста. Здається тут всі веселяться')

#adding directions
Stryiska.link_street(Kozelnytska, 'схід')
Kozelnytska.link_street(Stryiska, 'захід')
Kozelnytska.link_street(Franka, 'північ')
Franka.link_street(Kozelnytska, 'південь')
Franka.link_street(Shevchenka, 'захід')
Shevchenka.link_street(Franka, 'схід')
Shevchenka.link_street(Staroevr, 'північ')
Staroevr.link_street(Shevchenka, 'південь')

#creating items
pistol = mygame.Item('пістолет')
pistol.set_description('Там є 1 патрон. . .')

wallet = mygame.Item('гаманець')
wallet.set_description('Тут вистачить хіба що на чікушку')

cigarettes = mygame.Item('сигарети')
cigarettes.set_description('Парламент Night Blue, не з дешевих')

burger = mygame.Item('бігмак')
burger.set_description('Хтось викинув недоїджений бургер')

revo = mygame.Item('рево')
revo.set_description('Повна банка алкогольного напою. Але ви не любите рево...')

#creating characters
lazyman = mygame.Friend('Лайдак', 'Виглядає дружелюбно і безтурботно. Він щось хоче вам сказати')
lazyman.set_conversation('О, я бачу, що ти мандруєш до центра міста! Що ж, побажаю тобі удачі й краще не гуляй до ночі')

batyar = mygame.Batyar('Батяр', '*хитається* Ви бачите, як він підходить до вас')
batyar.set_conversation('Ти мене поважаєш?')
batyar.set_weakness('гаманець')

stranger = mygame.Stranger('Самотній', 'Він здався вам сумним, не зводить з вас очей')
stranger.set_conversation('Люблю тихі вечори, тоді я вихожу на балкон, курю, довго думаю...')
stranger.set_weakness('сигарети')

bandit = mygame.Bandit('Бандюга', 'Агресивно підходить до вас')
bandit.set_conversation('Ти не з нашого району, чи не так?')
bandit.set_weakness('рево')

homeless = mygame.Homeless('Бездомний', 'Вам стало його жаль і ви хочете йому допомогти')
homeless.set_conversation('Якби ти мені міг би щось дати...')
homeless.set_weakness('бігмак')

# adding items
Stryiska.set_item(pistol)
Kozelnytska.set_item(cigarettes)
Franka.set_item(burger)
Shevchenka.set_item(wallet)
Staroevr.set_item(revo)

# adding characters
Stryiska.set_character(lazyman)
Kozelnytska.set_character(stranger)
Shevchenka.set_character(homeless)
Staroevr.set_character(batyar)

# game module
current_street = Stryiska
backpack = []
lose = False

final = False

while lose == False:
    print('\n')
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command.lower() in ['північ', 'південь', 'схід', 'захід']\
        and inhabitant is None:
        try:
            current_street = current_street.move(command)
        except KeyError:
            print('Туди немає дороги')
        if current_street == Staroevr:
            final = True
        if final == True and current_street == Franka:
            Franka.set_character(bandit)
            bandit = None
        if final == True and current_street == Stryiska:
            print('Ви пройшли гру, молодці:)')
            lose = True
            
    if command.lower() in ['північ', 'південь', 'схід', 'захід']\
        and inhabitant is not None:
        print('Сперше виконайте взаємодію з персонажем')

    elif command.lower() == 'говорити':
        if inhabitant == lazyman:
            inhabitant.talk()
            print(f'{lazyman.char} йде своєю дорогою')
            current_street.set_character(None)
        elif inhabitant is not None:
            inhabitant.talk()
            print(f'Що ви виберете? {backpack}')
            fight_with = input()

            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print('Ви пройшли!')
                    current_street.set_character(None)
                else:
                    print('Ви програли')
                    print('Кінець гри')
                    lose = True
            else:
                print(f'Ви не маєте {fight_with}')
        else:
            print('Тут нікого немає')
    
    elif command.lower() == 'взяти':
        if item is not None:
            print(f'Ви поклали {item.get_name()} у ваш рюкзак')
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print('Тут немає що взяти')
    elif command.lower() not in ['північ', 'південь', 'схід', 'захід']:
        print('Невідома команда, список доступних: [говорити, взяти, північ, південь, захід, схід]')
