import os

from src.notion import NotionHelper

class NotionRequest():
    def __init__(self, database_src_id: str, properties: dict):
        self.database_src_id = database_src_id
        self.properties = properties

class NotionRequestQueue():
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
    
    def run(self):
        while True:
            # needs to run at 3 requests per second
            if len(self.request_queue) > 0:
                request = self.request_queue.pop()
                database_src_id = request.database_src_id
                properties = request.properties
                self.notion_helper.fetch_get()
