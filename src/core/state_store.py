class StateStore():
    def __init__(self):
        
        self.store = {}  
        """ {
            database_id: {
                page_id: {
                    (property_name, property_type): property_value
                    }
                }
            }
        """