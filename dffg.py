from random import *
from time import sleep
KMN = ['Камень' , 'Ножницы' , 'Бумагу']
ORgame = ['О' , 'Р']
KN = [1,2,3,4,5,6]

while True:
    print('Во что поиграем?')
    game = input('1-КМН; 2-Монетка; 3-настолка; 4-UNO: ')
    if game == '1':
        print('играем в КМН')
        sleep(1)
        pl = 1
        pl = input('Камень - 1 , Ножницы - 2 , Бумага - 3 :')
        rand = randint(0,2)
        sleep(0.5)
        o = randint(0,2)
        print('Соперник выбрал' , KMN[o])
        sleep(0.5)
        if (pl == '1' and o == 1) or (pl == '2' and o == 2) or (pl == '3' and o == 0):
            print('победа')
            sleep(1)
        elif (o == 0 and pl == '2') or (o == 1 and pl == '3') or (o == 2 and pl == '1'):
            print('Порожение')
            sleep(1)
        else:
            print('Ничья')
            sleep(1)



    elif game == '2':
        print('играем в Монетку')
        pl = input('Орёл - 1 , Решка - 2 :')
        if pl == '1':
            print('тогда Соперник Решка')
            sleep(1)
        elif pl == '2':
            print('тогда Соперник Орёл')
            sleep(1)
        else:
            print('Конч?')
        
        if pl == randint(1,2):
            print('Ты победил')
            sleep(1)
        else:
            print('Ты проиграл')
            sleep(1)



    elif game == '3':
        print('играем в Класик Настолку')
        mestopl = 0
        mestoan = 0
        sleep(1)
        Nklet = randint(20,60)
        print('Всего', Nklet , 'клеток')
        Klet = {}
        for i in range(Nklet):
            Klet[i] = randint(1,6)
        def KN_Hod_PL():
            global mestopl
            global mestoan
            global Klet
            global Nklet
            print("Твой ход")
            bros = input('Бросить кубик (нажать Enter)')
            kub = randint(1,6)
            print('Выпало ', kub)
            mestopl += kub
            sleep(1)

            if mestopl <= Nklet:
                sob = Klet[mestopl]
            else:
                sob = 7
            if sob >= 1 and sob <= 3:
                print('Ничего не произошло')
            elif sob == 4:
                print('Ты пропускаешь ход')
                sleep(1)
                print("Ты на", mestopl ,"Клетке")
                print("Соперник по прежнему на" , mestoan , "клетке")
                sleep(2)
                KN_Hod_AN()
            elif sob == 5:
                print('Ты получаешь доп ход')
                sleep(1)
                print("Ты на", mestopl ,"Клетке")
                print("Соперник по прежнему на" , mestoan , "клетке")
                sleep(2)
                KN_Hod_PL()
            elif sob == 6:
                print('Ты двгаешся на случайное кол-во клеток')
                sleep(0.2)
                dophod = randint(-5,5)
                if dophod > 0:
                    print('Ты двгаешся на' , dophod , 'клеток вперёд')
                    sleep(1)
                elif dophod < 0:
                    print('Ты двгаешся на' , dophod , 'клеток назад')
                    sleep(1)
                else:
                    print('А нет не двгаешся(выпал 0)')
                    sleep(1)
                mestopl += dophod
        def KN_Hod_AN():
            global mestoan
            global mestopl
            global Klet
            global Nklet
            print("Ход Соперника")
            sleep(0.5)
            print('Он бросает кубик')
            sleep(0.5)
            kub = randint(1,6)
            print('Выпало ', kub)
            mestoan += kub
            sleep(1)

            if mestoan <= Nklet:
                sob = Klet[mestoan]
            else:
                sob = 7
            if sob >= 1 and sob <= 3:
                print('Ничего не произошло')
                sleep(1)
            elif sob == 4:
                print('Соперник пропускает ход')
                sleep(1)
                print("Соперник на", mestoan ,"клетке")
                print("Ты по прежнему на" , mestopl , "клетке")
                sleep(2)

                KN_Hod_PL()
            elif sob == 5:
                print('Соперник получает доп ход')
                sleep(1)
                print("Соперник на", mestoan ,"клетке")
                print("Ты по прежнему на" , mestopl , "клетке")
                sleep(2)

                KN_Hod_AN()
            elif sob == 6:
                print('Соперник двгается на случайное кол-во клеток')
                dophod = randint(-5,5)
                sleep(0.5)
                if dophod > 0:
                    print('Соперник двигается на' , dophod , 'клеток вперёд')
                    sleep(1)
                elif dophod < 0:
                    print('Соперник двигается на' , dophod , 'клеток назад')
                    sleep(1)
                else:
                    print('А нет не двигаюсь(выпал 0)')
                    sleep(1)
                mestoan += dophod
        while mestopl <= Nklet or mestoan <= Nklet:
            KN_Hod_PL()
            sleep(1)
            print("Ты на", mestopl ,"клетке")
            print("Соперник по прежнему на" , mestoan , "клетке")
            sleep(2)
            KN_Hod_AN()
            sleep(1)
            print("Соперник на", mestoan ,"клетке")
            print("Ты по прежнему на" , mestopl , "клетке")
            sleep(2)
        if mestoan > Nklet:
            print('Ты проиграл')
        elif mestopl > Nklet:
            print('Ты Победил')
    elif game == '4':
        print('играем в UNO')
        
        def give_card(nach):
            colors = ['Синий','Красный', 'Зелёный','Жёлтый']
            if nach == 1:
                i = randint(0,9)
            elif nach == 0:
                i = randint(0,13)
            otv = [None,None]
            if i < 10:
                otv[0] = str(i)
            elif i == 10:
                otv[0] = '-+2-'
            elif i == 11:
                otv[0] = '-(/)-'
            elif i == 12:
                otv[0] = '_смена цвета_'
            elif i == 13:
                otv[0] = '_+4_'
            if i > 11:
                otv[1] = 'Чёрный'
            else:
                otv[1] = colors[randint(0,3)]
            return otv
        predK = give_card(1)
        colodpl = []
        colodan = []
        for i in range(1,7,1):
            colodpl.append(give_card(0))
        for i in range(7):
            colodan.append(give_card(0))
        def UNO_Hod_PL():
            global predK
            global colodpl
            global colodan
            colors = ['Синий','Красный', 'Зелёный','Жёлтый']
            colodpl.sort()
            print('Ваш ход')
            sleep(0.5)
            for i in colodpl:
                if i[0] == predK[0] or i[1] == predK[1] or i[1] == 'Чёрный' or (predK[0]=='_+4_' and i[0] == "-+2-"):
                    vozm = True
                    break
                else:
                    vozm = False
            while not vozm:
                print('У вас нет подходящих карт')
                E = input('Взять карту (Enter)')
                sleep(1)
                vz = give_card(0)
                print('Вы взяли карту' , vz[0] , vz[1])
                colodpl.append(vz)
                if vz[0] == predK[0] or vz[1] == predK[1] or vz[1] == 'Чёрный' or (predK[0]=='_+4_' and vz[0] == "-+2-"):
                    vozm = True
            print('У вас есть подходящие карты')
            sleep(1)
            print('У вас', len(colodpl) , 'карт')
            sleep(1)
            for i in range(len(colodpl)):
                print(i+1,'-',colodpl[i][0],colodpl[i][1])
            sleep(1)
            print('Предыдущая карта - ',predK[0],predK[1])
            while True:
                sleep(1)
                print('Если хочешь взять карту напиши \'-1\'')
                print('Если хочешь увидеть колоду с предыдущей картой напиши \'0\'')
                print('Если хочешь использовать карту напиши нимер')
                takecard = int(input("Действие:")) - 1
                sleep(1.5)
                if takecard == -1:
                    for i in range(len(colodpl)):
                        print(i+1,'-',colodpl[i][0],colodpl[i][1])
                    print('Предыдущая карта - ',predK[0],predK[1])                    
                elif  takecard == -2:
                    vz = give_card(0)
                    print('Вы взяли карту' , vz[0] , vz[1])
                    colodpl.append(vz)
                elif colodpl[takecard][0] == predK[0] or colodpl[takecard][1] == predK[1] or colodpl[takecard][1] == 'Чёрный' or (predK[0]=='_+4_' and takecard[0] == "-+2-"):
                    break
                else:
                    print('Такого написанно не было')
            while colodpl[takecard][1] == 'Чёрный':
                print('Введите цвет')
                color = int(input('1 - Синий, 2 - Красный, 3 - Зелёный, 4 - Жёлтый'))
                if color < 5 and color > 0:
                    colodpl[takecard][1] = colors[color-1]
            sleep(1)

            print('Вы использовали',colodpl[takecard][0],colodpl[takecard][1])
            predK = colodpl[takecard]
            colodpl.pop(takecard)
            sleep(1)
            if predK[0] == '-+2-':
                print('Соперник берёт 2 карты')
                for i in range(2):
                    colodan.append(give_card(0))
                
            elif predK[0] == '-(/)-' and len(colodpl) != 0:
                print('Соперник пропускает ход')
                UNO_Hod_PL() 
            elif predK[0] == '_+4_':
                print('Соперник берёт 4 карты')
                for i in range(4):
                    colodan.append(give_card(0))
            colodpl.sort()
            sleep(1)
            if len(colodpl) > 0:
                UNO_Hod_AN()
            else:
                print('Ты победидил')
        def UNO_Hod_AN():
            global colodan
            global colodpl
            global predK
            colors = ['Синий','Красный', 'Зелёный','Жёлтый']
            colodan.sort()
            print('Ход соперника')
            sleep(1)
            vozmcard = []
            for i in colodan:
                if i[0] == predK[0] or i[1] == predK[1] or i[1] == 'Чёрный' or (predK[0]=='_+4_' and i[0] == "-+2-"):
                    vozm = True
                    vozmcard.append(i)
                else:
                    vozm = False
            while not vozm:
                print('Соперник берёт карту')
                vz = give_card(0)
                colodan.append(vz)
                if vz[0] == predK[0] or vz[1] == predK[1] or vz[1] == 'Чёрный' or (predK[0]=='_+4_' and vz[0] == "-+2-"):
                    vozm = True
                    vozmcard.append(vz)
                sleep(1)
            print('У соперника', len(colodan) , 'карт')
            sleep(1)
            takecard = choice(vozmcard)
            if takecard[1] == 'Чёрный':
                takecard[1] = choice(colors)
            predK = takecard
            colodan.remove(takecard)
            print('Соперник использовал', predK[0],predK[1])
            sleep(1)
            if predK[0] == '-+2-':
                print('Ты берёшь 2 карты')
                for i in range(2):
                    colodpl.append(give_card(0))     
            elif predK[0] == '-(/)-' and len(colodan) != 0:
                print('Ты пропускаешь ход')
                UNO_Hod_AN() 
            elif predK[0] == '_+4_':
                print('Ты берёшь 4 карты')
                for i in range(4):
                    colodpl.append(give_card(0))
            colodan.sort()       
            sleep(1) 
            if len(colodan) > 0:
                UNO_Hod_PL()
            else:
                print('Ты проиграл')
        UNO_Hod_PL()
    else:
        print('тебе норм?')
