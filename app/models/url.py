import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class URL(Base):

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
    created_at = Column(
        String, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    click_count = Column(Integer, default=0)
