from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    RegionID = Column(String(255), primary_key=True)
    RegionName = Column(String(255))


engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
region = session.query(Region).filter(Region.RegionID == '110101').one()
print('RegionName is %s' % region.RegionName)
# 关闭session:
session.close()
