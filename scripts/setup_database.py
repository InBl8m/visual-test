from app.database import Base, engine


def setup_database():
    Base.metadata.create_all(bind=engine)
