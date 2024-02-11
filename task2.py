from prettytable import PrettyTable


def publisher_info(name):
    info = PrettyTable()
    info.field_names = ["Название книги", "Название магазина", "Стоимость покупки", "Дата покупки"]
    for i in name:
        info.add_row(i)
    print(info)
