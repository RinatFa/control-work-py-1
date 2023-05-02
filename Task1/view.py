def rd_csv(path):
    try:
        f = open(path, 'r', encoding="utf-8")
        data = f.read()  # чтение
        f.close()
        return data
    except IOError:
        print('Файл отсутствует или недоступен!')
        return


def wr_csv(path, sStroka):
    with open(path, 'w', encoding="utf-8") as f:  # запись
        for i in range(len(sStroka)):
            if (sStroka[i][0] != ''):
                f.write(
                    f'{sStroka[i][0]};{sStroka[i][1]};{sStroka[i][2]};{sStroka[i][3]}\n')


def app_csv(path, sID, sDate, sHeader, sString):
    with open(path, 'a', encoding="utf-8") as f:  # добавление
        f.write(f'{sID};{sDate};{sHeader};{sString}\n')
