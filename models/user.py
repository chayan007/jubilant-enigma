from sqlalchemy import Column, Integer, Sequence, String, LargeBinary

from config.database import GlobalDBHelper


class User(GlobalDBHelper().BASE):

    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    fullname = Column(String(50))
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    hashed_password = Column(String(255))

    def __repr__(self):
        return f"<User(name='{self.fullname}', username='{self.username}')>"