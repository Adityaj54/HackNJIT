from sqlalchemy.util import timezone

from database import Base
from sqlalchemy import Column, INTEGER, String, BOOLEAN, TIMESTAMP, text


class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    positions = Column(String)
    link = Column(String)
    comments = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Users(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
