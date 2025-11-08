import os
import importlib
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

def init_db():
    for root, dirs, files in os.walk('models'):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                module_name = os.path.join(root, file).replace('.py', '').replace('/', '.')
                try:
                    importlib.import_module(module_name)
                except Exception as e:
                    raise e
    Base.metadata.create_all(bind=engine) 