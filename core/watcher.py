import time
import httpx
import json
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
    def __init__(self, database_id, notion_helper, dispatcher, interval = 15):
        self.db_id = database_id
        self.nh = notion_helper
        self.dispatcher = dispatcher
        self.interval = interval
        
    async def run(self):
        while True:
            async with httpx.AsyncClient() as client:
                tasks = [
                    self.nh.fetch_get(client, self.db_id)
                ]
                results = await asyncio.gather(*tasks)
            for result in results:
                print(json.dumps(result, indent=4))
            time.sleep(self.interval)