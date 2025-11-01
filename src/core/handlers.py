class Handler:
    """
    The Handler module is responsible for executing specific actions 
    based on the triggers received from the Dispatcher.
    """
    def __init__(self):
        pass
            
    def handle(self, trigger):
        # Each subclass will implement its own handling logic
        pass
    
class ButtonTriggerHandler(Handler):
    """
    Handler for ButtonTrigger events.
    Executes actions based on the ButtonTrigger received from the Dispatcher.
    """
    async def handle(self, trigger):
        # Implement the specific handling logic for ButtonTrigger
        # print(f"Handling ButtonTrigger with payload: {trigger.payload}")
        # Add more logic as needed to process the trigger
        print(f"ButtonTriggerHandler: Action Type: {trigger.action_type}, Triggered At: {trigger.triggered_at}, Payload: {trigger.payload}")
        return True