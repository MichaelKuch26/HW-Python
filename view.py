import model


def input_class():
    return input('С каким классом работаем? ').upper()


text = 'литература'


def input_subject():
    return input('Какой предмет? ').lower()


def who_answer():
    return input('Кто будет отвечать? ').title()


def what_mark():
    return input('На какую оценку ответил? ')


def not_name():
    return print('Такого ученика нет в журнале. Введите имя заново! ')


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')


def mark_par():
    return print('Введите корректную оценку (от 1 до 5)!')
