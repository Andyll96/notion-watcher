from src.core import Trigger

class Dispatcher:
    """
    This module defines the Dispatcher class, responsible for handling events or 
    triggers emitted by the Watcher.

    Responsibilities:
    - Receive notifications about detected changes from the Watcher.
    - Determine the appropriate response (e.g., log event, send message, 
    trigger automation, or update another Notion database).
    - Maintain modular, pluggable actions (e.g., Slack notifications, 
    email alerts, API requests, etc.).

    The Dispatcher acts as the “brain” of the automation system — deciding 
    how to respond to changes observed by the Watcher.
    """
    # TODO: IN THE FUTURE I MAY WANT TO IMPLEMENT DIFFERENT TYPES OF DISPATCHERS
    def __init__(self, notion_helper):
        self.nh = notion_helper
        self.handlers = {
            # dictionary that lists Action classes
            # this should be somewhere more global?
        }
        
    def handler(self, trigger: Trigger):
        # dispatcher is used by trigger watcher. When watcher gets a trigger, it passes it here so we can figure out what action the trigger wants to perform, then instantiate and run that Action class
        pass