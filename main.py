import os
import asyncio

from dotenv import load_dotenv

from src.notion import NotionHelper
from src.core import Watcher, ButtonTriggerLogWatcher, JobApplicationWatcher
from src.core import Dispatcher

load_dotenv()

async def main():
    """_summary_
    """
    # environment variables
    notion_token = os.getenv("NOTION_TOKEN")
    btn_logs_db_src_id = os.getenv("BTN_LOGS_DB_SRC_ID")
    job_app_db_src_id = os.getenv("JOB_APP_DB_SRC_ID")
    
    nh = NotionHelper(notion_token) # one shared api client
    dispatcher = Dispatcher(nh) # one shared action manager
    
    btn_trigger_filter = {
        "filter": {
            "property": "Status",
            "status": {
                "equals": "Not started"
            }
        }
    }
    
    # multiple watchers, watchers run asynchronously
    watchers = [
        # TODO: I NEED TO IMPLEMENT A BETTER BASE CLASS FOR WATCHERS
        Watcher(btn_logs_db_src_id, nh, dispatcher, interval=10)
        # ButtonTriggerLogWatcher(btn_logs_db_src_id, nh, dispatcher, filters=btn_trigger_filter, interval=10),
        # JobApplicationWatcher(job_app_db_src_id, nh, dispatcher, interval=10)
    ]
    
    for watcher in watchers:
        await watcher.run()

if __name__ == "__main__":
    asyncio.run(main())