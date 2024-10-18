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
            line = f"- **Total Solved**: ![Progress](https://progress-bar.dev/{data['totalSolved']}/?scale=500&title=solved&width=200&color=babaca)\n"
        elif "Easy" in line:
            line = f"- **Easy**: ![Progress](https://progress-bar.dev/{data['easySolved']}/?scale=200&title=easy&width=200&color=green)\n"
        elif "Medium" in line:
            line = f"- **Medium**: ![Progress](https://progress-bar.dev/{data['mediumSolved']}/?scale=150&title=medium&width=200&color=orange)\n"
        elif "Hard" in line:
            line = f"- **Hard**: ![Progress](https://progress-bar.dev/{data['hardSolved']}/?scale=50&title=hard&width=200&color=red)\n"
        
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

