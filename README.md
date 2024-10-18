if "Total Solved" in line:
    line = f"- **Total Solved**: {data['totalSolved']} / {data['totalQuestions']}\n"
if "Easy" in line:
    line = f"- **Easy**: {data['easySolved']} / {data['totalEasy']}\n"
if "Medium" in line:
    line = f"- **Medium**: {data['mediumSolved']} / {data['totalMedium']}\n"
if "Hard" in line:
    line = f"- **Hard**: {data['hardSolved']} / {data['totalHard']}\n"
