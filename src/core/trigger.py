class Trigger:
    """
    Base class for different types of triggers which can be created by Watchers and passed to the Dispatcher.
    """
    def __init__(self, data):
        self.data = data
        self.env = None # environment context, used for dev/prod separation
    
class ButtonTrigger(Trigger):
    """
    Specialized Trigger for Button-related events.
    """
    def __init__(self, data, action_type=None, triggered_at=None, associated_dbs=[], payload={}):
        super().__init__(data)
        # Additional initialization for ButtonTrigger can be added here
        self.action_type = action_type
        self.triggered_at = triggered_at
        self.associated_dbs = associated_dbs
        self.payload = payload
        
    @property
    def type(self):
        return __class__.__name__
