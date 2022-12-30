import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "8281168"))
    API_HASH = os.environ.get("API_HASH", "445ff67ec34858448ac184c7479ce917")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2055718473:AAHGch-ioqCoYkzTkMtw0SDG1UkYK91IQWc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1011394081")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://123:123@cluster0.fr6gfgg.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7g2FgIDFGJidbjiqfYwzDZss6fXeQG9iyGZfDmROQnAg1wMXp/lwPtzje/2bP5T2+9dLeTbHA/xBVKIybmdjE3jBaoUiu+IyMFQjS7Yl0opr5XvYlhVTKK2wWPHiuJuDYWFXjLrpjAVDjWezj9vHJL7fPVvMbNyQqlWKY3r18nyD+7+C3Z7VcNhGUupgD8eM/GBoNDxFPtEBI/PIiBashYOanBBoQWrj6YXevQFWqcTZeekH5tTRx81k37tQrd8F2MwzMiFUEUHFda8XZtuRhZvsyQ6sgaSPLeJUg9jLIase/5GR5xF0x/92eVsXsypyoFNuCvvWyi8uXy6D5SNbvrw==")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001696546419"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
