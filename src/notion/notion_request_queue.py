import os

from notion_helper import NotionHelper

class NotionRequestQueue():
    def __init__(self):
        self.request_queue = []
        
        notion_token = os.getenv("NOTION_TOKEN")
        self.notion_helper = NotionHelper(notion_token)
        
    def add_request(self, request):
        self.request_queue.append(request)
    
    def remove_request(self, request):
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
            pass
            