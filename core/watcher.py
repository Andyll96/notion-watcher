import time
import httpx
import asyncio
class Watcher:
    """
    This module defines the Watcher class, which monitors changes in one or more 
    Notion databases.

    Responsibilities:
    - Periodically poll Notion databases for new, updated, or deleted entries.
    - Compare current state with previously stored state to detect changes.
    - Emit events or signals when specific triggers are met (e.g., new entries, 
    status changes, deadline updates).
    - Pass detected changes to the Dispatcher for further action.

    The Watcher acts as the “eyes” of the system — constantly observing Notion 
    for updates that should trigger automation workflows.
    """
    # TODO: IN THE FUTURE, I MAY WANT TO IMPLEMENT DIFFERENT TYPES OF WATCHERS
    def __init__(self, database_id, notion_helper, dispatcher, interval = 15):
        # I may want to remove the interval parameter and replace with something that comes from the config directory
        # TODO: I WANT TO BE ABLE TO HAVE A DEFAULT INTERVAL, BUT HAVE A TRIGGER THAT INDICATES THAT INTERVAL SHOULD BE SMALLER LIKE 2 SECONDS
        self.db_id = database_id
        self.nh = notion_helper
        self.dispatcher = dispatcher
        self.interval = interval
        
    def run(self):
        # this will be our main loop for the app, that'll use notion helper to check the database for new entries(filtering by status property). When detected it'll pass it to dispatcher
        # TODO: MAY WANT TO REMOVE CONCURRENCY DEPENDING ON WORKFLOW
        while True:
            
            with httpx.Client() as client:
                print(f"GET: {self.nh.fetch_get(client, self.db_id)}")
            time.sleep(self.interval)