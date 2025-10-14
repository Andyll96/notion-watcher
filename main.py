import os

from dotenv import load_dotenv

from notion import NotionHelper
from core import Watcher
from core import Dispatcher

load_dotenv()

def main():
    notion_token = os.getenv("NOTION_TOKEN")
    db_id = os.getenv("BUTTON_TRIGGER_LOGS_DB")
    print(f"==>> notion_token: {notion_token}")
    print(f"==>> db_id: {db_id}")
    
    nh = NotionHelper(notion_token) # My notion client
    dispatcher = Dispatcher(nh)
    watcher = Watcher(nh, dispatcher, 10)
    
    watcher.run()


if __name__ == "__main__":
    main()
