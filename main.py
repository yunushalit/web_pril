from flask import Flask, render_template
from models.news import News
from models.news import News2
from models.news import News3
from models import db_session
app = Flask(__name__)
db_session.global_init('sqlite.db')


@app.route('/')
def index():
    session = db_session.create_session()
    return render_template(
        'base.html',
        news=session.query(News).order_by(News.date.desc()),
        news2=session.query(News2).order_by(News2.stazh.desc()),
        news3=session.query(News3).order_by(News3.zarplata.desc())
    )


if __name__ == '__main__':
    app.run('127.0.0.1', 8000, True)
