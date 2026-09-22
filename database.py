from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/tracker.db"

engine = create_engine(DATABASE_URL)

print("Database connected successfully!")