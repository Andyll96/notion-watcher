import os
import asyncio

from src.notion import NotionHelper

class NotionRequest():
    def __init__(self, database_src_id: str, properties: dict):
        self.database_src_id = database_src_id
        self.properties = properties
        
    async def process(self):
        # Placeholder for processing logic
        pass

class NotionRequestQueue():
    
    REQUESTS_PER_SECOND = 3  # Notion API rate limit
    
    def __init__(self):
        self.request_queue = []
        
        notion_token = os.getenv("NOTION_TOKEN")
        self.notion_helper = NotionHelper(notion_token)
        
    def add_request(self, request: NotionRequest):
        self.request_queue.append(request)
    
    def remove_request(self, request: NotionRequest):
        # TODO: CHECK THAT THE REQUEST/REQUEST ID IS IN THE QUEUE AND THEN REMOVE IT
        self.request_queue.remove(request)
        
    def get_next_request(self):
        if self.request_queue:
            return self.request_queue.pop(0)
        return None
    
    def get_last_request(self):
        if self.request_queue:
            return self.request_queue[-1]
        return None
    
    def get_queue_length(self):
        return len(self.request_queue)
    
    async def run(self):
        print("Starting NotionRequestQueue...")
        
        while True:
            loop_start_time = asyncio.get_event_loop().time()
            tasks_to_schedule = [] # the task object tracks whether the co-routine finished, raised an exception, or was cancelled
            # TODO: I NEED TO HANDLE TASKS THAT RUN INTO ERRORS TO REQUEUE THEM AGAIN OR LOG THEM SOMEWHERE, OTHERWISE I RUN THE RISK OF THE PROGRAM ENDING BEFORE TASKS ARE HANDLED PROPERLY
            
            if len(self.request_queue) > 0:
                batch_size = min(self.REQUESTS_PER_SECOND, len(self.request_queue))
                if batch_size > 0:
                    print(f"[{loop_start_time:.2f}] Processing {batch_size} requests from NotionRequestQueue...")
                    for _ in range(batch_size):
                        request = self.get_next_request()
                        if request:
                            database_src_id = request.database_src_id
                            properties = request.properties
                            
                            # Here you would process the request using NotionHelper
                            print(f"Processing request for database {request.database_src_id} with properties {request.properties}")
                            # Example: await self.notion_helper.fetch_get(...)
                            task = asyncio.create_task(request.process())
                            tasks_to_schedule.append(task)
                            
                # 
                elapsed_time = asyncio.get_event_loop().time() - loop_start_time
                sleep_duration = max(0, 1 - elapsed_time)
                await asyncio.sleep(sleep_duration)
