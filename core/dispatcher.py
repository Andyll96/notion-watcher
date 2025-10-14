class Dispatcher:
    def __init__(self, notion_helper):
        self.nh = notion_helper
        self.handlers = {
            # dictionary that lists Action classes
            # this should be somewhere more global?
        }
        
    def handler(self, trigger):
        # dispatcher is used by trigger watcher. When watcher gets a trigger, it passes it here so we can figure out what action the trigger wants to perform, then instantiate and run that Action class
        pass