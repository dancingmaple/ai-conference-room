from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Room(Base):
    __tablename__ = "rooms"
    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    topic      = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status     = Column(String(20), default="idle")
    agents     = relationship("Agent", back_populates="room", cascade="all, delete")
    messages   = relationship("Message", back_populates="room", cascade="all, delete")

class Agent(Base):
    __tablename__ = "agents"
    id            = Column(Integer, primary_key=True, index=True)
    room_id       = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    name          = Column(String(50), nullable=False)
    provider      = Column(String(30), nullable=False)
    model         = Column(String(80), nullable=False)
    api_key       = Column(Text, nullable=False)
    base_url      = Column(Text, nullable=True)
    system_prompt = Column(Text, nullable=True)
    temperature   = Column(Float, default=0.7)
    avatar_color  = Column(String(10), default="#6366f1")
    order_index   = Column(Integer, default=0)
    room          = relationship("Room", back_populates="agents")

class Message(Base):
    __tablename__ = "messages"
    id         = Column(Integer, primary_key=True, index=True)
    room_id    = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    agent_id   = Column(Integer, ForeignKey("agents.id"), nullable=True)
    agent_name = Column(String(50), nullable=False)me,from sqlalchemy 
    content    = Column(Text, nullable=False)
    round_num  = Column(Integer, default=1)
    created_at = Column(DateTi


































