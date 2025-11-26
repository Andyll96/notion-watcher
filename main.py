import os
import asyncio

from dotenv import load_dotenv

from src.notion import NotionRequestQueue
from src.core.handlers import CoverLetterHandler
from src.core.events_queue import EventsQueue
from src.core import Watcher
from src.core import Dispatcher


load_dotenv()


async def main():
    """    
    Get database ids
    Instantiate NotionRequestQueue, a queue of requests that will be sent to notion as per the notion request rate limit. Should use asyncio.Queue?
    Instantiate EventsQueue; a queue of events, events are pushed to the queue by the watcher when something happens in notion and events are popped by the dispatcher. Uses asyncio.Queue
    Both Watcher and Dispatcher need information about the databases and the associated handlers, this information is consolidated in a ROUTING_TABLE
    Instantiate Watcher and Dispatcher
    Run Main Loops for Watcher and Dispatcher
    """

    # Database IDs to monitor
    job_apps_db_src_id = os.getenv("JOB_APPS_DB_SRC_ID")

    # NotionRequestQueue, manages the rate of requests to Notion
    notion_request_queue = NotionRequestQueue()

    # EventsQueue, pushed to by Watcher, consumed from by Dispatcher
    events_queue = EventsQueue()

    # ROUTING_TABLE, contains database IDs for the Watcher also the properties in the Handles so the Watcher knows what properties should be tracked in the StateStore
    # Dispatcher will use ROUTING_TABLE to pass events from the EventsQueue to the appropriate Handlers
    ROUTING_TABLE = {
        job_apps_db_src_id: [CoverLetterHandler()]
        }

    watcher = Watcher(ROUTING_TABLE, events_queue, notion_request_queue)
    dispatcher = Dispatcher(ROUTING_TABLE, events_queue, notion_request_queue)

    # run Watcher and Dispatcher event loops
    await notion_request_queue.run()
    await watcher.run()
    await dispatcher.run()


if __name__ == "__main__":
    asyncio.run(main())
