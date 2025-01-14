import requests

class Names:
    def __init__(self, Requests):
        self.Requests = Requests
        
    def get_names_puuid(self, puuid):
        response = requests.put(self.Requests.pd_url + "/name-service/v2/players", headers=self.Requests.get_headers(), json=[puuid], verify=False)
        return response.json()[0]["GameName"] + "#" + response.json()[0]["TagLine"]