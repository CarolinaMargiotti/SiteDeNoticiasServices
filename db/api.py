import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost/db1?charset=utf8mb4")