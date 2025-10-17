import os

from dotenv import load_dotenv

from notion import NotionHelper
from core import Watcher
from core import Dispatcher

load_dotenv()

def main():
    notion_token = os.getenv("NOTION_TOKEN")
    btn_trigger_logs_db_id = os.getenv("BUTTON_TRIGGER_LOGS_DB") # rename this to reflect that this is a data_source_id, not a database_id
    print(f"==>> notion_token: {notion_token}")
    print(f"==>> db_id: {btn_trigger_logs_db_id}")
    
    nh = NotionHelper(notion_token) # My notion client
    dispatcher = Dispatcher(nh)
    watcher = Watcher(btn_trigger_logs_db_id, nh, dispatcher, 10)
    
    watcher.run()


if __name__ == "__main__":
    main()
