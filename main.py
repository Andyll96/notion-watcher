import os
import asyncio

from dotenv import load_dotenv

from notion import NotionHelper
from core import Watcher
from core import Dispatcher

load_dotenv()

async def main():
    notion_token = os.getenv("NOTION_TOKEN")
    btn_logs_db_src_id = os.getenv("BTN_LOGS_DB_SRC_ID") 
    
    nh = NotionHelper(notion_token) # one shared api client
    dispatcher = Dispatcher(nh) # one shared action manager
    
    # multiple watchers, watchers run asynchronously
    watchers = [
        Watcher(btn_logs_db_src_id, nh, dispatcher, 10),
    ]
    
    for watcher in watchers:
        await watcher.run()

if __name__ == "__main__":
    asyncio.run(main())
