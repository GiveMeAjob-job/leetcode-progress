import requests
import json

def get_leetcode_progress(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{GiveMeAjob-job}"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

get_leetcode_progress("GiveMeAjob-job")
