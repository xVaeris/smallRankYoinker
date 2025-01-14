import requests

class Requests:
    def __init__(self):
        self.pd_url = f"https://pd.eu.a.pvp.net"
        self.glz_url = f"https://glz-eu-1.eu.a.pvp.net"
        
    
        
    def fetch(self, url_type: str, method: str, endpoint: str, rate_limit_seconds = 5):
        if url_type == "glz":
            response = requests.request(method, self.glz_url + endpoint, headers="" , verify=False)
            return response.json
        elif url_type == "pd":
            response = requests.request(method, self.pd_url + endpoint, headers="" , verify=False)
            return response
        
    def get_headers():
        return