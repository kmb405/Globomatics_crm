class Database:
    
    def __init__(self, path):
        
        with open(path, "r") as handle:
            #import json
            #self.data = json.load(handle)
            
            import yaml
            self.data = yaml.safe_load(handle)
    
    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            #return int(acct["due"]) - int(acct["paid"])
            bal = float(acct["due"]) - float(acct["paid"])
            return f"$ {bal:.2f}"
        return None