import asyncio

from src.notion import NotionRequest, NotionRequestQueue
from src.core.events_queue import EventsQueue
from src.core.state_store import StateStore

class Watcher():
    # Watcher must submit a query request to the notion request queue at regular intervals (5 mins), for each database it's monitoring
    # The Watcher compares all the pages from the response and cross references that with the last edit times of the values in StateStore
    # If the last edit time is later than what's already stored from the last time, then we get the relevant properties from that page and update them in State Store, and then emit a ChangeEvent and push it onto the EventsQueue
    def __init__(self, routing_table: dict, events_queue: EventsQueue, notion_request_queue: NotionRequestQueue) -> None:
        
        self.store_state = StateStore()
        
        self.events_queue = events_queue
        self.notion_request_queue = notion_request_queue
        
        self.routing_table = routing_table  # {database_id: [handler_instance, handler_instance]}
        self.database_ids = list(set(routing_table.keys()))
        

    async def run(self) -> None:
        """Main loop for the Watcher, spawns tasks to monitor each database"""
        tasks = []
        for database_id in self.database_ids:
            task = asyncio.create_task(
                self._monitor_database(database_id)
            )
            tasks.append(task)
        await asyncio.gather(*tasks)
    
    async def _monitor_database(self, database_id: str) -> None:
        """Monitors a specific database for changes by submitting requests to the NotionRequestQueue""" 
        database_handlers = self.routing_table[database_id]
        # while True:
        
        # maybe I should gather all the properties at once, this way I'm not gathering common properties multiple times
        critical_properties = {}
        for handler in database_handlers:
            current_critical_properties = handler.get_properties()
            for prop_name, prop_type in current_critical_properties.items():
                if prop_name not in critical_properties:
                    critical_properties[prop_name] = prop_type
            # I don't think I need to loop through the properties, I need to submit a request to get all the pages with only the list of properties
        request = NotionRequest(database_id, critical_properties)
        self.notion_request_queue.add_request(request)
        
        # REMEMBER THESE SPECIFIC PROPERTIES ARE JUST THE ONES THAT WE'RE MONITORING TO PICKUP EVENTS, THE HANDLER MAY NEED ADDITIONAL PROPERTIES LATER WHEN IT PROCESSES THE EVENT, SO THE HANDLER I GUESS WILL NEED THE PAGE ID TO GET THE NECESSARY PROPERTIES LATER
