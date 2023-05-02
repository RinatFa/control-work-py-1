from datetime import datetime


def all_note(sStroka):
    sStroka3 = []
    count = 0
    for i in range(len(sStroka)):
        if (sStroka[i][0] != ''):
            count += 1
            sStroka3.append(sStroka[i])
            print(
                f'{sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    print(f'***** Найдены все {count} заметок')
    return sStroka3


def find_note(sStroka, iN):
    sStroka3 = []
    count = 0
    if (iN == 1):
        sIns = input("Введите часть строки поля Дата: ")
    elif (iN == 2):
        sIns = input("Введите часть строки поля Заголовок: ")
    if (sIns != ''):
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                if sIns in sStroka[i][iN]:
                    count += 1
                    sStroka3.append(sStroka[i])
                    print(
                        f'{sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    print(f'***** Найдено {count} заметок')
    return sStroka3


def findDate_note(sStroka, iN):
    sStroka3 = []
    count = 0
    print("Введите первую Дату: ")
    sToday = datetime.today().strftime("%d.%m.%Y")
    sIns = dateIn(sToday)
    print("  " + sIns)
    print("Введите вторую Дату - 1 или Всё до Даты - 2 или Всё после Даты - 3: ")
    s1 = "Введите 1, 2 или 3: "
    s2 = "Введите натуральное число!"
    s3 = "3"
    numberA = InputNumb(s1, s2, s3)
    if numberA == 1:
        sIns2 = dateIn(sToday)
        print("  " + sIns2)
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                if (sIns2 > sIns):
                    sDt = str(datetime.strptime(sIns, '%d.%m.%Y'))
                    sDt2 = str(datetime.strptime(sIns2, '%d.%m.%Y'))
                else:
                    sDt = str(datetime.strptime(sIns2, '%d.%m.%Y'))
                    sDt2 = str(datetime.strptime(sIns, '%d.%m.%Y'))
                if (sDt2 >= str(datetime.strptime(sStroka[i][iN], '%d.%m.%Y'))):
                    if (sDt <= str(datetime.strptime(sStroka[i][iN], '%d.%m.%Y'))):
                        count += 1
                        sStroka3.append(sStroka[i])
                        print(
                            f'{sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    elif numberA == 2:
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                sDt = str(datetime.strptime(sIns, '%d.%m.%Y'))
                if (sDt >= str(datetime.strptime(sStroka[i][iN], '%d.%m.%Y'))):
                    count += 1
                    sStroka3.append(sStroka[i])
                    print(
                        f'{sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    elif numberA == 3:
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                sDt = str(datetime.strptime(sIns, '%d.%m.%Y'))
                if (sDt <= str(datetime.strptime(sStroka[i][iN], '%d.%m.%Y'))):
                    count += 1
                    sStroka3.append(sStroka[i])
                    print(
                        f'{sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    print(f'***** Найдено {count} заметок')
    return sStroka3


def replace_note(sStroka):
    sStroka3 = []
    count = 0
    sIns = input("Введите часть строки Заголовка заметки: ")
    if (sIns != ''):
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                if sIns in sStroka[i][2]:    # поиск по Заголовку
                    count += 1
                    print(
                        f' *** найдено:  {sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}\n    {sStroka[i][3]}')
    if (count == 1):
        bYN = input('Редактировать найденное (да - 7)? ')
        if (bYN == '7'):
            for i in range(len(sStroka)):
                if (sStroka[i][0] != ''):
                    if sIns in sStroka[i][2]:
                        sID = sStroka[i][0]
                        sH = input('Введите Заголовок (не менять - Enter): ')
                        if (sH == ''):
                            sH = sStroka[i][2]
                        sStroka[i][2] = sH
                        print("  " + sH)
                        print('Введите Дату (не менять - Enter)')
                        sDt = dateIn(sStroka[i][1])
                        sStroka[i][1] = sDt
                        print("  " + sDt)
                        sS = input(
                            'Введите текст Заметки (не менять - Enter): ')
                        if (sS == ''):
                            sS = sStroka[i][3]
                        sS = sS[:2000]
                        sStroka[i][3] = sS
                        print("  " + sS)
                sStroka3.append(sStroka[i])
            sStroka = []
            for i in range(len(sStroka3)):
                if (sStroka3[i][0] != ''):
                    sStroka.append(sStroka3[i])
                    print(
                        f'{sStroka3[i][0]}:  {sStroka3[i][1]} - {sStroka3[i][2]}\n    {sStroka3[i][3]}')
            print()
            print("=" * 9 + " Отредактированая Заметка " + "=" * 70)
            print(f'{sID}:  {sDt} - {sH}\n    {sS}')
            print("=" * 105)
        else:
            print("***** Не отредактировано!")
    elif (count != 0):
        print("***** Выбрано несколько заметок!")
    elif (count == 0):
        print("***** Не выбрано заметок!")
    return sStroka


def del_note(sStroka):
    sStroka3 = []
    count = 0
    countDel = 0
    sIns = input("Введите часть строки Заголовка заметки: ")
    if (sIns != ''):
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                if sIns in sStroka[i][2]:    # поиск по Заголовку
                    count += 1
                    print(
                        f' *** найдено:  {sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}')
    if (count != 0):
        bYN = input('Удалить выборочно найденное (да - 6)? ')
        if (bYN == '6'):
            for i in range(len(sStroka)):
                if (sStroka[i][0] != ''):
                    if sIns in sStroka[i][2]:
                        print(
                            f'  выборочно:  {sStroka[i][0]}:  {sStroka[i][1]} - {sStroka[i][2]}')
                        bYN = input('Удалить эту заметку (да - 6)? ')
                        if (bYN == '6'):
                            bYN = ''
                            countDel += 1
                        else:
                            sStroka3.append(sStroka[i])
                    else:
                        sStroka3.append(sStroka[i])
            sStroka = []
            for i in range(len(sStroka3)):
                if (sStroka3[i][0] != ''):
                    sStroka.append(sStroka3[i])
                    print(
                        f'{sStroka3[i][0]}:  {sStroka3[i][1]} - {sStroka3[i][2]}\n    {sStroka3[i][3]}')
            print(f'***** Удалено {countDel} заметок')
        else:
            print("***** Не удалено!")
    else:
        print("***** Не найдены заметки!")
    return sStroka


def InputNumb(sStr, s2, s3):  # ввод числа
    numberA = " "
    while (type(numberA) != int):
        numberA = input(sStr)
        if (numberA.isdigit() == False):
            print(s2)
        else:
            numberA = int(numberA)
            if (numberA <= 0) or (numberA > int(s3)):
                print("Введите число от 1 до " + s3 + " !")
                numberA = " "
    return numberA


def dateIn(sTod):  # ввод латы
    sStr = ""
    while sStr == "":
        sDtIn = input('Введите Дату в формате ДД.ММ.ГГГГ : ')
        if (sDtIn == ''):
            sDtIn = sTod
        try:
            datetime.strptime(sDtIn, '%d.%m.%Y')
            sStr = "s"
        except ValueError:
            print("Это не дата!")
    return sDtIn
