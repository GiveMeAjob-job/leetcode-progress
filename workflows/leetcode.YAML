name: Update LeetCode Stats

on:
  schedule:
    # 每天 UTC 时间晚上 12 点自动更新
    - cron: "0 0 * * *"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install requests
      - name: Run LeetCode Progress Update Script
        run: |
          python your_script.py
      - name: Commit results
        run: |
          git config --global user.name 'your_github_username'
          git config --global user.email 'your_email@example.com'
          git add .
          git commit -m 'Update LeetCode progress'
          git push
