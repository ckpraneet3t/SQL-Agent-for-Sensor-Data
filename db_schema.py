import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# --- This points to the database file you created earlier ---
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///netcdf_database.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definition of the Ocean Data table
class OceanData(Base):
    __tablename__ = "ocean_data"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    depth = Column(Float)
    so = Column(Float)       # Sea Water Salinity
    thetao = Column(Float)   # Sea Water Potential Temperature
    uo = Column(Float)       # Eastward Sea Water Velocity
    vo = Column(Float)       # Northward Sea Water Velocity
    zos = Column(Float)      # Sea Surface Height Above Geoid