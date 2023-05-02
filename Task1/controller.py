import model
import view
from datetime import datetime
from random import randint


def button_click():
    sStop = ""
    while sStop == "":
        s1 = "\n***** Выберите необходимое действие:\n"
        s1 += "  1. Список заметок                                    "
        s1 += "  2. Сделать выборку по Дате или части поля Дата     \n"
        s1 += "  3. Найти заметку по заголовку                        "
        s1 += "  4. Сделать выборку заметок по диапазону Дат        \n"
        s1 += "  5. ===== Создать заметку ====================        "
        s1 += "  6. Удалить заметку                                 \n"
        s1 += "  7. ===== Редактировать заметку ==============        "
        s1 += "  8. Закончить работу\n"
        s1 += "Введите номер необходимого действия (1 - 8): "
        s2 = "Введите натуральное число!"
        s3 = "8"
        numberA = model.InputNumb(s1, s2, s3)
        print()

        if numberA == 8:
            print("***** Выход из программы!")
            print()
            exit()
        elif numberA == 1:
            print("  1. Вывод полного списка заметок")
        elif numberA == 2:
            print("  2. Выборка заметок по части даты", end=".  ")
        elif numberA == 3:
            print("  3. Поиск заметки по заголовку", end=".  ")
        elif numberA == 4:
            print("  4. Выборка заметок по диапазону Дат", end=".  ")
        elif numberA == 5:
            print("  5. Создание заметки")
        elif numberA == 6:
            print("  6. Удаление заметки")
        elif numberA == 7:
            print("  7. Редактирование заметки", end=".  ")
        
        # path1 = 'dir//note.csv'
        path1 = 'note.csv'
        data = view.rd_csv(path1)  # считывание .csv
        if data is None:
            print('Создаем новый файл заметок!')
            numberA = 4
            sStroka = []
        else:
            NoteBase = data.split('\n')
            sStroka = [i.split(';') for i in NoteBase]

        if numberA == 8:
            exit()
        elif numberA == 1:
            sStroka3 = model.all_note(sStroka)  # поиск всех записей
        elif numberA == 2:
            iNumb = 1
            sStroka3 = model.find_note(sStroka, iNumb)  # поиск по части Даты
        elif numberA == 3:
            iNumb = 2
            sStroka3 = model.find_note(sStroka, iNumb)  # поиск по Заголовку
        elif numberA == 4:
            iNumb = 1
            sStroka3 = model.findDate_note(
                sStroka, iNumb)  # поиск по диапазону Дат
        elif numberA == 5:
            list1 = []
            for i in range(len(sStroka)):
                if (sStroka[i][0] != ''):    # если ID не пустое
                    list1.append(int(sStroka[i][0]))
            print()
            if (len(sStroka) != 0):
                imax = max(list1) + 1
            else:
                imax = 1
            sID = str(imax)
            sH = input(
                'Введите Заголовок (выход в меню: 9)(по умолчанию "Заголовок" - Enter): ')
            if (sH == ''):
                sH = "Заголовок " + str(randint(1000, 9999))
            print("  " + sH)
            if sH != "9":
                print('Введите Дату (по умолчанию Сегодня - Enter)')
                sToday = datetime.today().strftime("%d.%m.%Y")
                sDt = model.dateIn(sToday)
                print("  " + sDt)
                print(
                    'Введите текст Заметки до 2000 символов (по умолчанию "Содержимое Заметки" - Enter)')
                sS = input('Введите текст Заметки: ')
                if (sS == ''):
                    sS = "Содержимое Заметки " + str(randint(1000000, 9999999))
                view.app_csv(path1, sID, sDt, sH, sS)  # добавление в .csv
                print()
                print("=" * 15 + " Новая Заметка " + "=" * 75)
                print(f'{sID}:  {sDt} - {sH}\n    {sS}')
                print("=" * 105)
        elif numberA == 6:
            sStroka3 = model.all_note(sStroka)
            print()
            sStroka = model.del_note(sStroka3)
            view.wr_csv(path1, sStroka)  # запись в .csv
        elif numberA == 7:
            sStroka3 = model.replace_note(sStroka)  # замена по полям
            view.wr_csv(path1, sStroka3)
