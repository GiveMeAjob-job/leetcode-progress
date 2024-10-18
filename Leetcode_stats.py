import requests
import os

def get_leetcode_progress(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Check for error status
        if data.get("status") == "error":
            print(f"Error: {data.get('message')}")
            return None
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from LeetCode API: {e}")
        return None

def generate_svg_progress_bar(solved, total, title, filename):
    """Generates an SVG file representing the progress bar."""
    percentage = solved / total * 100 if total > 0 else 0
    
    svg_content = f'''
    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="40">
        <defs>
            <linearGradient id="gradient">
                <stop offset="0%" stop-color="#0ff" />
                <stop offset="100%" stop-color="#00f" />
            </linearGradient>
            <style>
                .progress-bar {{
                    fill: url(#gradient);
                    animation: glowing 2s infinite;
                }}
                @keyframes glowing {{
                    0%, 100% {{ width: 0; }}
                    50% {{ width: {percentage}%; }}
                }}
            </style>
        </defs>
        <rect x="0" y="0" width="100%" height="10" fill="#ccc" />
        <rect x="0" y="0" class="progress-bar" height="10" width="{percentage}%" />
        <text x="50%" y="25" font-size="12" text-anchor="middle" fill="#fff">{solved}/{total} {title}</text>
    </svg>
    '''
    
    # Save the SVG to a file
    with open(filename, 'w') as file:
        file.write(svg_content)
    print(f"SVG file {filename} generated.")

def update_readme(data):
    # Generate SVG files for each progress bar
    generate_svg_progress_bar(data['totalSolved'], data['totalQuestions'], "Total Solved", "images/total_solved.svg")
    generate_svg_progress_bar(data['easySolved'], data['totalEasy'], "Easy", "images/easy_solved.svg")
    generate_svg_progress_bar(data['mediumSolved'], data['totalMedium'], "Medium", "images/medium_solved.svg")
    generate_svg_progress_bar(data['hardSolved'], data['totalHard'], "Hard", "images/hard_solved.svg")

    # Read current README.md content
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    # Update README.md content with SVGs
    new_content = []
    for line in readme_content:
        if "Total Solved" in line:
            line = f"- **Total Solved**: ![Progress](./images/total_solved.svg)\n"
        elif "Easy" in line:
            line = f"- **Easy**: ![Progress](./images/easy_solved.svg)\n"
        elif "Medium" in line:
            line = f"- **Medium**: ![Progress](./images/medium_solved.svg)\n"
        elif "Hard" in line:
            line = f"- **Hard**: ![Progress](./images/hard_solved.svg)\n"
        new_content.append(line)

    # Write updated content back to README.md
    if new_content != readme_content:
        with open("README.md", "w") as file:
            file.writelines(new_content)
        print("README.md updated successfully.")
    else:
        print("No changes made to README.md.")

if __name__ == "__main__":
    username = "GiveMeAJob9"  # Your LeetCode username
    progress = get_leetcode_progress(username)

    if progress:
        update_readme(progress)
        print(f"Fetched data: {progress}")  # Print fetched data for debugging
    else:
        print("Failed to fetch LeetCode data.")

