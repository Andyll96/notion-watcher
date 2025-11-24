from src.notion import NotionHelper
from src.core.events_queue import EventsQueue
from src.core.state_store import StateStore

class Watcher:
    # Watcher must query the database, at regular intervals, for when it was last edited and compare that to the last known edit time
    # If there is a new edit, we store the metadata of that edit and push an event to the Dispatcher
    # The watcher will have multiple watcher tasks for each database it is monitoring. This way we're not creating multiple instances of the Watcher class.
    
    def __init__(self, routing_table: dict, events_queue: EventsQueue, notion_helper: NotionHelper):
        
        self.store_state = StateStore()
        
        self.events_queue = events_queue
        self.notion_helper = notion_helper
        
        self.routing_table = routing_table  # {database_id: [handler_instance, handler_instance]}
        self.database_ids = list(set(routing_table.keys()))
        

    async def monitor_databases(self):
        pass
    
    async def _monitor_database(self, database_id: str):
        pass