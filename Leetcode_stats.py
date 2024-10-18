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

    # 更新内容
    new_content = []
    for line in readme_content:
        if "Total Solved" in line:
    line = f"- **Total Solved**: {data['totalSolved']} / {data['totalQuestions']}\n"
        if "Easy" in line:
    line = f"- **Easy**: {data['easySolved']} / {data['totalEasy']}\n"
        if "Medium" in line:
    line = f"- **Medium**: {data['mediumSolved']} / {data['totalMedium']}\n"
        if "Hard" in line:
    line = f"- **Hard**: {data['hardSolved']} / {data['totalHard']}\n"
        new_content.append(line)

    # 写回更新后的内容到 README.md
    with open("README.md", "w") as file:
        file.writelines(new_content)

if __name__ == "__main__":
    username = "GiveMeAJob9"  # 使用LeetCode用户ID
    progress = get_leetcode_progress(username)

    if progress:
        update_readme(progress)
        print(f"Fetched data: {progress}")  # 在最后打印获取到的数据
    else:
        print("Failed to fetch LeetCode data.")

