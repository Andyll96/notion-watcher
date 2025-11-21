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
    
    # TODO: HANDLER_MAPPINGS SHOULD BE MOVED TO A CONFIG FILE
    # HANDLER_MAPPINGS = {
    #     "ButtonTrigger": "ButtonTriggerHandler",
    #     # Add more mappings as needed
    # }
    
    def __init__(self, notion_helper):
        self.nh = notion_helper
        self.handlers = {}
        