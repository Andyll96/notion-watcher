import asyncio

from src.notion import NotionRequestQueue
from src.core.events_queue import EventsQueue
from src.core.state_store import StateStore

class Watcher():
    # Watcher must query the database, at regular intervals, for when it was last edited and compare that to the last known edit time
    # If there is a new edit, we store the metadata of that edit and push an event to the Dispatcher
    # The watcher will have multiple watcher tasks for each database it is monitoring. This way we're not creating multiple instances of the Watcher class.
    
    # The Watcher will submit a request to the request queue at regular intervals, and the request queue is responsible for managing the requests limit
    
    def __init__(self, routing_table: dict, events_queue: EventsQueue, notion_request_queue: NotionRequestQueue) -> None:
        
        self.store_state = StateStore()
        
        self.events_queue = events_queue
        self.notion_request_queue = notion_request_queue
        
        self.routing_table = routing_table  # {database_id: [handler_instance, handler_instance]}
        self.database_ids = list(set(routing_table.keys()))
        

    async def run(self) -> None:
        tasks = []
        for database_id in self.database_ids:
            task = asyncio.create_task(
                self._monitor_database(database_id)
            )
            tasks.append(task)
        await asyncio.gather(*tasks)
    
    async def _monitor_database(self, database_id: str) -> None:
        while True:
            pass