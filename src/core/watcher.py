import time
import httpx
import json
import asyncio

from src.core import Trigger, ButtonTrigger
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
    def __init__(self, database_id, notion_helper, dispatcher, filters = {}, interval = 15):
        self.db_id = database_id
        self.nh = notion_helper
        self.dispatcher = dispatcher
        self.interval = interval
        self.filters = filters
        
    async def run(self):
        while True:
            async with httpx.AsyncClient() as client:
                # TODO: as subclasses are created, each subclass will have its own way of fetching data and handling it. i.e. different tasks for different watchers
                tasks = [
                    self.nh.fetch_get(client, self.db_id, self.filters)
                ]
                data = await asyncio.gather(*tasks)
            if data:
                print(json.dumps(data, indent=4))
                for page in data.get("results", []):
                    trigger = Trigger(page)
                    await self.dispatcher.handler(trigger)
            time.sleep(self.interval)
            
class ButtonTriggerLogWatcher(Watcher):
    """
    Specialized Watcher for monitoring Button Trigger Logs database.
    """
    async def run(self):
        while True:
            async with httpx.AsyncClient() as client:
                tasks = [
                    self.nh.fetch_get(client, self.db_id, self.filters)
                ]
                data = await asyncio.gather(*tasks)
            
            for page in data.get("results", []):
                status = page["properties"]["Status"]["status"]["name"]
                action_type = page["properties"]["Action Type"]["select"]["name"]
                triggered_at = page["properties"]["Triggered At"]["created_time"]
                # TODO: associated_dbs = None 
                payload = page["Payload"]["rich_text"]
                
                if status == "Not started":
                    # Add associated_dbs
                    trigger = ButtonTrigger(page, action_type=action_type, triggered_at=triggered_at, payload=payload)
                    await self.dispatcher.handler(trigger)

            time.sleep(self.interval)