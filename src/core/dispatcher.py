from src.notion import NotionHelper
from src.core.handlers import Handler
from src.core.events_queue import EventsQueue

class Dispatcher():
    
    def __init__(self, notion_helper: NotionHelper, events_queue: EventsQueue, handler_list: list[Handler]):
        self.notion_helper = notion_helper
        self.events_queue = events_queue        
        self.handler_list = handler_list
    
    async def run(self):
        pass