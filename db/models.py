from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from .base import Base

class SystemRequirements(Base):
   __tablename__ = "system-requirements"

   snapshotTime = Column(String, primary_key=True)

   cpuCount = Column(Integer)
   cpuFrequency = Column(Integer)

   totalRam = Column(Integer)

   totalStorage = Column(String)

class SystemLoadStatistic(Base):
   __tablename__ = "system-load-statistic"

   snapshotTime = Column(String, primary_key=True)

   usedCpuPercent = Column(Integer)

   availableRam = Column(Integer)
   usedRam = Column(Integer)
   usedRamPercent = Column(Integer)

   availableStorage = Column(String)
   usedStorage = Column(String)
   usedStoragePercent = Column(String)