import time
import httpx
import json
import asyncio


class WatcherGroup:
    def __init__(self):
        pass
    
    def run(self): # TODO: make async
        pass

class Watcher:
    def __init__(self, interval = 15):
        pass
        
    async def run(self):
        pass
        # while True:
        #     async with httpx.AsyncClient() as client:
        #         tasks = [
        #             self.nh.fetch_get(client, self.db_id, self.filters)
        #         ]
        #         data = await asyncio.gather(*tasks)
        #     if data:
        #         print(json.dumps(data, indent=4))
        #         for page in data.get("results", []):
        #             trigger = Trigger(page)
        #             await self.dispatcher.handler(trigger)
        #     time.sleep(self.interval)


    
    async def run(self):
        while True:
            async with httpx.AsyncClient() as client:
                tasks = [
                    self.nh.fetch_get(client, self.db_id, self.filters)
                ]
                data = await asyncio.gather(*tasks)
                print(data)