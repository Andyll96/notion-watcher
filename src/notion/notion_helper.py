import httpx

class NotionHelper:
    """
    This module defines the NotionHelper class, which serves as the client interface 
    for communicating with the Notion API.

    Responsibilities:
    - Authenticate using the Notion API token.
    - Fetch and update data from Notion databases and pages.
    - Provide utility methods for querying, filtering, and creating records.
    - Abstract raw API requests into higher-level helper functions for other modules.

    This class acts as the backbone of the application’s interaction layer with Notion, 
    ensuring consistent and secure communication.
    """
    def __init__(self, token:str):
        self.base_url = "https://api.notion.com/v1/data_sources"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2025-09-03",
            "Content-Type": "application/json"
        }
        print(self.headers)
    
    async def fetch_get(self, client: httpx.AsyncClient, db_id):
        url = f"{self.base_url}/{db_id}/query"
        print(url)
        response = await client.post(url, headers=self.headers, json={})
        return response.json()
    
    """
    get(),
        get (general) database entity, filter parameter, returns json
        find_one(), finds a specific entry, filter for database, properties, returns json
        find(), returns multiple entries, filter for database, properties, returns json
        specific methods for the Button Logs Database, get button link (or something), get button parent page, get associated database(s) information, need to make sure that environment property is handled correctly

    post(create), 
        create database ?
        create database page
        create regular page
    put(update), 
        general update methods
        update Trigger Log status, update Output property (returns error message, or information confirming success)
            maybe instead of an output property, I can update the page contents to include the output
    delete
        delete Database entry/page
        delete database
        
"""