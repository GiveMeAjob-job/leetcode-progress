import requests
import os

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

def generate_html_progress_bar(solved, total, title, color):
    percentage = solved / total * 100 if total > 0 else 0
    return f'''
    <div style="width: 100%; background-color: #333; border-radius: 10px; overflow: hidden; box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.7); margin-bottom: 10px;">
        <div style="width: {percentage}%; height: 20px; background: linear-gradient(90deg, rgba(0, 255, 255, 0.3), rgba(0, 255, 255, 0.6), rgba(0, 255, 255, 1)); animation: glowing 2s infinite; border-radius: 10px; text-align: center; line-height: 20px; color: white;">
            {solved}/{total}
        </div>
    </div>

    <style>
    @keyframes glowing {{
        0% {{ box-shadow: 0 0 5px rgba(0, 255, 255, 0.3); }}
        50% {{ box-shadow: 0 0 15px rgba(0, 255, 255, 0.9); }}
        100% {{ box-shadow: 0 0 5px rgba(0, 255, 255, 0.3); }}
    }}
    </style>
    '''

def update_readme(data):
    # 生成各类进度条的 HTML
    total_solved_html = generate_html_progress_bar(data['totalSolved'], data['totalQuestions'], "Total Solved", "green")
    easy_solved_html = generate_html_progress_bar(data['easySolved'], data['totalEasy'], "Easy", "lightgreen")
    medium_solved_html = generate_html_progress_bar(data['mediumSolved'], data['totalMedium'], "Medium", "orange")
    hard_solved_html = generate_html_progress_bar(data['hardSolved'], data['totalHard'], "Hard", "red")

    # 读取当前的 README.md 内容
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    # 更新 README.md 内容
    new_content = []
    for line in readme_content:
        if "Total Solved" in line:
            line = f"- **Total Solved**: {total_solved_html}\n"
        elif "Easy" in line:
            line = f"- **Easy**: {easy_solved_html}\n"
        elif "Medium" in line:
            line = f"- **Medium**: {medium_solved_html}\n"
        elif "Hard" in line:
            line = f"- **Hard**: {hard_solved_html}\n"
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

