from datetime import date
import codecs

VERSION = '0.1b'

WELCOME_LINE = (83, '<div class="pathtitle menutitile">Вітаємо, %content%</div>')
NAME_LINE = (320, '<div class="name">%content%</div>')
BIRTHDAY_LINE = (307, '<div class="date">Дата народження: %content%</div>')
NUMBER_LINE = (310, '<div class="number">Номер: %content%</div>')
IPN_NUMBER_LINE = (358, '<div class="number">%content%</div>')
IPN_NAME_LINE = (351, '<div class="name">%content%</div>')
IPN_BIRTHDAY_LINE = (354, '<div class="date">Дата народження: %content%</div>')


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def date_from_string(string: str):
    elements = string.split('.')
    if len(elements) != 3:
        return date(1, 1, 1)
    return date(int(elements[2]), int(elements[1]), int(elements[0]))


if __name__ == '__main__':
    print(f'Дія.Maker v{VERSION}\n')
    name = input('ПІБ: ')
    birthday = input('Дата народження: ')
    number = input('Номер паспорта: ')
    ipn = input('РНОКПП: ')
    age = calculate_age(date_from_string(birthday))

    print()

    print(f'ПІБ: {name}\n'
          f'Дата народження: {birthday} ({age})\n'
          f'Номер паспорта: {number}\n'
          f'РНОКПП: {ipn}\n')

    verified = input('Продовжити? [y/N]: ').lower()
    if verified != 'y':
        print('Відміна.')
        exit(0)

    file = codecs.open('index.html', encoding='utf-8', mode='r+')
    lines = file.readlines()
    file.close()
    lines[WELCOME_LINE[0] - 1] = WELCOME_LINE[1].replace('%content%', name.split(' ')[1])
    lines[NAME_LINE[0] - 1] = NAME_LINE[1].replace('%content%', name)
    lines[BIRTHDAY_LINE[0] - 1] = BIRTHDAY_LINE[1].replace('%content%', birthday)
    lines[NUMBER_LINE[0] - 1] = NUMBER_LINE[1].replace('%content%', number)
    lines[IPN_NAME_LINE[0] - 1] = IPN_NAME_LINE[1].replace('%content%', name)
    lines[IPN_BIRTHDAY_LINE[0] - 1] = IPN_BIRTHDAY_LINE[1].replace('%content%', birthday)
    lines[IPN_NUMBER_LINE[0] - 1] = IPN_NUMBER_LINE[1].replace('%content%', ipn)
    file = codecs.open('index.html', encoding='utf-8', mode='w')
    file.writelines(lines)
    file.close()

    print('Готово.')
