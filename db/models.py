from sqlalchemy import Column, String, Integer

from .controller import base

class SystemInfo(base):
   __tablename__ = "SystemInfo"

   snapshotTime = Column(String, primary_key=True)

   cpuCount = Column(Integer)
   cpuFrequency = Column(Integer)

   totalRam = Column(Integer)

   totalStorage = Column(String)

class SystemStatistic(base):
   __tablename__ = "SystemStatistic"

   snapshotTime = Column(String, primary_key=True)

   usedCpuPercent = Column(Integer)

   availableRam = Column(Integer)
   usedRam = Column(Integer)
   usedRamPercent = Column(Integer)

   availableStorage = Column(String)
   usedStorage = Column(String)
   usedStoragePercent = Column(String)