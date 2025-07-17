# -*— coding:utf-8 -*—
import os
from app import create_app, db
from flask_migrate import Migrate
from flask_script import Manager
from app.models import User, Book

app = create_app('default')

migrate = Migrate(app, db)

manager = Manager(app)


# 建表，删除表，首次部署时执行（调试过程中不要执行，否则数据将全部删除）
# db.drop_all()
# db.create_all()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Book=Book)


if __name__ == '__main__':
    app.run()
