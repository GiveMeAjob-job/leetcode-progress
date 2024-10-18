import requests

def get_leetcode_progress(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data for {username}")
        return None

# LeetCode 用户名
username = "GiveMeAjob-job"
progress = get_leetcode_progress(username)
if progress:
    print(f"Total Solved: {progress['totalSolved']}")
    print(f"Easy: {progress['easySolved']}")
    print(f"Medium: {progress['mediumSolved']}")
    print(f"Hard: {progress['hardSolved']}")
