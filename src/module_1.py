from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for declarative class definitions
Base = declarative_base()

class Book(Base):
    """
    SQLAlchemy ORM model for the 'books' table.
    Represents a book with title, author, ISBN, and publication year.
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    year = Column(Integer, nullable=False)

# SQLite in-memory database engine
engine = create_engine('sqlite:///:memory:', echo=False)

# Session factory bound to the engine
SessionLocal = sessionmaker(bind=engine)

# Create all tables in the database
Base.metadata.create_all(bind=engine)