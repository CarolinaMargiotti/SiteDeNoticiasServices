import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:fatec@localhost/db1?charset=utf8mb4")