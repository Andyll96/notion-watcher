import asyncio

class EventsQueue():
    def __init__(self):
        
        self._queue = asyncio.Queue() #TODO: RESEARCH
    
    def enqueue(self, event):
        """Watcher uses this to put an item (ChangeEvent) into the queue

        Args:
            event (_type_): _description_
        """
        pass
    
    def dequeue(self):
        """Dispatcher uses this to get an item (ChangeEvent) from the queue"""
        pass
    
    def task_done(self):
        """Indicate that a formerly enqueued task is complete."""
        pass
    
    def join(self):
        """Blocks until all items in the queue have been gotten and processed."""
        pass