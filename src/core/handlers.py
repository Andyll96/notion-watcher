class Handler():
    """
    The Handler module is responsible for executing specific actions 
    based on the Events received from the Dispatcher.
    """
    def __init__(self):
        # TODO: I should eventually find a way to specify async handlers and sequential handlers
        
        self.db_properties = {} # Define properties that the handler is interested in. {property_name: property_type}
        
    def get_properties(self):
        return self.db_properties
    
# TODO: SHOULD ADD A HANDLER FOR SENDING NOTIFICATIONS
class CoverLetterHandler(Handler):
    # TODO: make CoverLetterHandler more generic. make it more about checking for a button press and the activation of the checkbox, then deactivate the checkbox after the action is taken
    # SHOULD I? Because I need to specify the property names for each handler anyway... Maybe I need to standardize property names across databases?
    def __init__(self):
        super().__init__()
        
        self.db_properties = {
            "Generate Cover Letter Trigger": "checkbox"
        }