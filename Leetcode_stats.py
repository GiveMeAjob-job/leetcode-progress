import requests
import matplotlib.pyplot as plt
import numpy as np
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

def generate_progress_bar(solved, total, title, color, filename):
    """生成一个紧凑的水平进度条图像"""
    fig, ax = plt.subplots(figsize=(4, 0.4))  # 更加紧凑的大小
    percentage = solved / total if total > 0 else 0

    # 生成进度条
    ax.barh([0], [percentage], color=color, height=0.5)

    # 设置进度条背景
    ax.barh([0], [1], color='#f0f0f0', height=0.5, zorder=-1)

    # 添加文字标签，显示当前进度和总数
    ax.text(percentage / 2, 0, f"{solved}/{total}", va='center', ha='center', color='white', fontsize=10)
    
    # 删除多余的边框和坐标轴
    ax.set_xlim(0, 1)
    ax.axis('off')

    # 保存图片
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    plt.close()

def update_readme(data):
    # 生成图像的保存路径
    image_dir = "images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # 生成各类进度条图像
    generate_progress_bar(1, 3323, "Total Solved", "green", "images/total_solved.png")
    generate_progress_bar(1, 830, "Easy", "lightgreen", "images/easy_solved.png")
    generate_progress_bar(0, 1738, "Medium", "orange", "images/medium_solved.png")
    generate_progress_bar(0, 755, "Hard", "red", "images/hard_solved.png")


    # 读取当前的 README.md 内容
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    # 更新 README.md 内容
    new_content = []
    for line in readme_content:
        if "Total Solved" in line:
            line = "- **Total Solved**: ![Progress](./images/total_solved.png)\n"
        elif "Easy" in line:
            line = "- **Easy**: ![Progress](./images/easy_solved.png)\n"
        elif "Medium" in line:
            line = "- **Medium**: ![Progress](./images/medium_solved.png)\n"
        elif "Hard" in line:
            line = "- **Hard**: ![Progress](./images/hard_solved.png)\n"
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

