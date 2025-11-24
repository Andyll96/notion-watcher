import os
import asyncio

from dotenv import load_dotenv

from src.notion import NotionHelper
from src.core.handlers import CoverLetterHandler
from src.core.events_queue import EventsQueue
from src.core import Watcher
from src.core import Dispatcher


load_dotenv()


async def main():
    """get env vars
    instantiate NotionHelper, StateStore, and necessary Handlers
    create instance of the Dispatcher, passing it event type to handler mappings
    setup asyncio.Queue for Watcher to push events and Dispatcher to consume from
    Setup Watcher to monitor Notion databases for changes
    start Watcher and Dispatcher event loops using asyncio.gather()
    """

    # environment variables
    notion_token = os.getenv("NOTION_TOKEN")
    job_apps_db_src_id = os.getenv("JOB_APPS_DB_SRC_ID")

    # NotionHelper
    notion_helper = NotionHelper(notion_token)

    # EventsQueue. Pushed to by Watcher, consumed from by Dispatcher
    events_queue = EventsQueue()

    ROUTING_TABLE = {job_apps_db_src_id: [CoverLetterHandler()]}

    # Watcher needs to know which databases to monitor and what properties each handler cares about in order to track them in the StateStore
    # TODO: should watcher and dispatcher have the same parent class?
    watcher = Watcher(ROUTING_TABLE, events_queue, notion_helper)

    dispatcher = Dispatcher(ROUTING_TABLE, events_queue, notion_helper)

    # run Watcher and Dispatcher event loops
    await watcher.monitor_databases()
    await dispatcher.run()


if __name__ == "__main__":
    asyncio.run(main())
