import sqlalchemy as sq
import configparser
from sqlalchemy.orm import sessionmaker
from models import create_tables, add_json, Publisher, Shop, Book, Stock, Sale
from task2 import publisher_info

settings = configparser.ConfigParser()
settings.read('setting.ini')
engine = sq.create_engine(settings['DEFAULT']['DSN'])

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

add_json(session)


print('Введите имя или идентификатор издателя:')
publisher = input()

q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
if publisher.isdigit():
    query = q.filter(Publisher.id == publisher).all()
else:
    query = q.filter(Publisher.name == publisher).all()

publisher = []
for title, name, price, date_sale in query:
    publisher.append([title, name, price, date_sale])

publisher_info(publisher)
