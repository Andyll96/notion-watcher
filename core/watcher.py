class Watcher:
    def __init__(self, notion_helper, dispatcher, interval = 15):
        # I may want to remove the interval parameter and replace with something that comes from the config directory
        self.nh = notion_helper
        self.dispatcher = dispatcher
        self.interval = interval
        
    def run():
        # this will be our main loop for the app, that'll use notion helper to check the database for new entries(filtering by status property). When detected it'll pass it to dispatcher
        pass