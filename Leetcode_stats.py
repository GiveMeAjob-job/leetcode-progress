import requests

def get_leetcode_progress(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 检查是否返回错误状态
        if data.get("status") == "error":
            print(f"Error: {data.get('message')}")
            return None
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from LeetCode API: {e}")
        return None

def update_readme(data):
    # 读取当前的 README.md 内容
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    # 更新 README.md 内容
    new_content = []
    for line in readme_content:
        if "Total Solved" in line:
            line = f"- **Total Solved**: {data['totalSolved']} / {data['totalQuestions']}\n"
        elif "Easy" in line:
            line = f"- **Easy**: {data['easySolved']} / {data['totalEasy']}\n"
        elif "Medium" in line:
            line = f"- **Medium**: {data['mediumSolved']} / {data['totalMedium']}\n"
        elif "Hard" in line:
            line = f"- **Hard**: {data['hardSolved']} / {data['totalHard']}\n"
        
        new_content.append(line)

    # 仅当内容有变化时才更新 README.md
    if new_content != readme_content:
        with open("README.md", "w") as file:
            file.writelines(new_content)
        print("README.md updated successfully.")
    else:
        print("No changes made to README.md.")

if __name__ == "__main__":
    username = "GiveMeAJob9"  # 使用LeetCode用户ID
    progress = get_leetcode_progress(username)

    if progress:
        update_readme(progress)
        print(f"Fetched data: {progress}")  # 打印获取到的数据
    else:
        print("Failed to fetch LeetCode data.")

