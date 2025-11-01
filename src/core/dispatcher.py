import importlib
from src.core.trigger import Trigger
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
    
    HANDLER_MAPPINGS = {
        "ButtonTrigger": "ButtonTriggerHandler",
        # Add more mappings as needed
    }
    
    def __init__(self, notion_helper):
        self.nh = notion_helper
        self.handlers = {}
        
    async def execute(self, trigger: Trigger):
        # dispatcher is used by trigger watcher. When watcher gets a trigger, it passes it here so we can figure out what action the trigger wants to perform, then instantiate and run that Action class
        handler_class_name = self.HANDLER_MAPPINGS.get(trigger.type)
        if not handler_class_name:
            raise RuntimeError(f"No handler found for trigger type: {trigger.type}")
        
        if handler_class_name not in self.handlers:
            module = importlib.import_module("src.core.handlers")
            handler_class = getattr(module, handler_class_name)
            self.handlers[handler_class_name] = handler_class()

        await self.handlers[handler_class_name].handle(trigger)