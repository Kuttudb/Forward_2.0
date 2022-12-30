import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "8281168"))
    API_HASH = os.environ.get("API_HASH", "445ff67ec34858448ac184c7479ce917")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2055718473:AAHGch-ioqCoYkzTkMtw0SDG1UkYK91IQWc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1011394081")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQBpPEHLr-n6xkaLCKMq1wyIr3j1kerqQWwLMlQpGjQJGJYpyiZYQk9I3ozc57FLrU5sbhcht_OpG9JG8apH_xXej59ZM60ICF4Kq8pxEWDNF-3sgWL9ArqI8b5v9v80L7308s-ySf5-XfT6YiEdD4EoGs2dTgj-S-Rdj5tgaDQqZhonyrHdasQqLqIrotdOYAnSO3ER4JINd8aMEchRWl7WaZWo9glh65XsTBM41dYHLtYjY1hGh5LfXVHQbiCk8neQY60Ojy3r6lXT0y3BDKpcEPtNV9yl786yRVgBeZTaCDVQnQey4-WELamL6MUqYQbtN2gVGtAvY7HNsyNLV-9iPEimIQA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001696546419"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
