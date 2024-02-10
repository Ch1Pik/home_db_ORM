import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Sale, Book, Stock

DSN = "postgresql://postgres:postgres@localhost:5432/home_db_ORM"
engine = sq.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Глуховский')

session.add(publisher1)
session.add(publisher2)

book1 = Book(title='Евгений Онегин', publisher=publisher1)
book2 = Book(title='Сказка о царе Салтане', publisher=publisher1)
book3 = Book(title='Медный всадник', publisher=publisher1)
book4 = Book(title='Метро 2033', publisher=publisher2)
book5 = Book(title='Метро 2034', publisher=publisher2)
book6 = Book(title='Метро 2035', publisher=publisher2)
session.add_all([book1, book2, book3, book4, book5, book6])


shop1 = Shop(name='Литрес')
shop2 = Shop(name='Эксмо')
session.add_all([shop1, shop2])


stock1 = Stock(book=book1, shop=shop2, count=10)
stock2 = Stock(book=book3, shop=shop2, count=5)
stock3 = Stock(book=book2, shop=shop1, count=1)
session.add_all([stock3, stock2, stock1])


sale1 = Sale(price='100.8', data_sale="2023-12-25T15:43:24.552Z", stock=stock1, count=2)
sale2 = Sale(price='50.5', data_sale="2024-01-25T12:46:24.552Z", stock=stock1, count=4)
session.add_all([sale1, sale2])
session.commit()

session.close()


def publisher_data(class_):
    id_ = input('Введите id издателя:')
    name = input('Введите name издателя:')
    if id_:
        for c in session.query(class_).filter(class_.id == id_).all():
            print(c)

    elif name:
        for c in session.query(class_).filter(class_.name == name).all():
            print(c)


def publisher_shop(class_):
    id_ = input('Введите id издателя:')
    name = input('Введите name издателя:')
    query = session.query(Shop)
    query = query.join(Stock)
    query = query.join(Book)
    query = query.join(Publisher)
    if id:
        for c in query.filter(class_.id == id_).all():
            print(c)

    elif name:
        for c in query.filter(class_.name == name).all():
            print(c)


if __name__ == "__main__":
    publisher_data(Publisher)
    publisher_shop(Publisher)
