import httpx

class NotionHelper:
    # Notion client
    
    def __init__(self, token:str):
        self.base_url = None
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2025-09-03",
            "Content-Type": "application/json"
        }
    
    
    # get(),
        # get (general) database entity, filter parameter, returns json
        # find_one(), finds a specific entry, filter for database, properties, returns json
        # find(), returns multiple entries, filter for database, properties, returns json
        # specific methods for the Button Logs Database, get button link (or something), get button parent page, get associated database(s) information, need to make sure that environment property is handled correctly

    # post(create), 
        # create database ?
        # create database page
        # create regular page
    # put(update), 
        # general update methods
        # update Trigger Log status, update Output property (returns error message, or information confirming success)
            # maybe instead of an output property, I can update the page contents to include the output
    # delete
        # delete Database entry/page
        # delete database
        
