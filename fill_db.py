from models import db_session
from models.news import News
from models.news import News2
from models.news import News3
from datetime import date

db_session.global_init('sqlite.db')

post = News()
post.fam = 'Фамилия'
post.name = 'Имя'
post.date = date.fromisoformat('2020-01-01')

session = db_session.create_session()
session.add(post)
session.commit()
