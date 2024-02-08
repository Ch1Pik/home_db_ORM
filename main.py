import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:postgres@localhost:5432/home_db_ORM"
engine = sq.create_engine(DSN)

create_tables(engine)

p1 = Publisher(name='Пушкин', books = [
    Book(title="Евгений Онегин"),
    Book(title="Сказка о царе Салтане"),
    Book(title="Медный всадник")])
p2 = Publisher(name='Глуховский', books = [
    Book(title="Метро 2033"),
    Book(title="Метро 2034"),
    Book(title="Метро 2035")])
b1 = Book(title="Текст", publisher=p2)
b2 = Book(title="Будущее", publisher=p2)
b3 = Book(title="Сказка о рыбаке и рыбке", publisher=p1)

shop1 = Shop(name="Литрес")
stock1 = Stock(book=b1, shop=shop1, count=30)
sale1 = Sale(price=470, stock=stock1, count=20)
stock2 = Stock(book=b3, shop=shop1, count=50)
sale2 = Sale(price=320, stock=stock2, count=20)

shop2 = Shop(name="Эксмо")
stock3 = Stock(book=b2, shop=shop2, count=50)
sale3 = Sale(price=510, stock=stock3, count=35)
stock4 = Stock(book=b2, shop=shop2, count=40)
sale4 = Sale(price=380, stock=stock4, count=15)

Session = sessionmaker(bind=engine)
s = Session()
s.add_all([p1, p2, b1, b2, b3, shop1, shop2, stock1, stock2, stock3, stock4, sale1, sale2, sale3, sale4])
s.commit()

def searching_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите имя (name) издателя: ')
    query_result = query_join.filter(Publisher.publisher_name == query_publisher_name)
    for result in query_result.all():
        print(f'Издатель "{query_publisher_name}" найден в магазине "{result.name}" с идентификатором {result.id}')

def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id_publisher == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')

if __name__ == '__main__':
    searching_publisher_name()
    searching_publisher_id()

s.close()
