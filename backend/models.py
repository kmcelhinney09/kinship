from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    role = Column(String) # 'parent' or 'kid'
    avatar_url = Column(String, nullable=True)
    points = Column(Integer, default=0)

    events = relationship("Event", back_populates="user")
    chores = relationship("Chore", back_populates="assigned_to_user")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    description = Column(Text, nullable=True)
    google_id = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Null for family events

    user = relationship("User", back_populates="events")

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    ingredients = Column(Text) # JSON or newline separated
    instructions = Column(Text)
    image_url = Column(String, nullable=True)

    meal_plans = relationship("MealPlan", back_populates="recipe")

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    meal_type = Column(String) # 'dinner', 'lunch', etc.
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    recipe = relationship("Recipe", back_populates="meal_plans")

class GroceryItem(Base):
    __tablename__ = "grocery_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_checked = Column(Boolean, default=False)
    category = Column(String, default="General")

class Chore(Base):
    __tablename__ = "chores"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    points = Column(Integer)
    status = Column(String, default="open") # 'open', 'pending', 'verified'
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)

    assigned_to_user = relationship("User", back_populates="chores")
