from src.notion import NotionRequestQueue
from src.core.events_queue import EventsQueue

class Dispatcher():
    
    def __init__(self, routing_table: dict, events_queue: EventsQueue, notion_request_queue: NotionRequestQueue):
        
        self.events_queue = events_queue
        self.notion_request_queue = notion_request_queue
        
        self.routing_table = routing_table  # {database_id: [handler_instance, handler_instance]}      
    
    async def run(self):
        pass