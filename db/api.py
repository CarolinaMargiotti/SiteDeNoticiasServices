import sqlalchemy
from models.envVariables import databaseDBName,databasePassword,databaseUser,databaseHost

engineURL=f'mysql+pymysql://{databaseUser}:{databasePassword}@{databaseHost}/{databaseDBName}?charset=utf8mb4'

engine = sqlalchemy.create_engine(engineURL)