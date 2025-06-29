
# import requests # type: ignore

# def fetch_leetcode_stats(username):
#     url = f"https://leetcode-stats-api.herokuapp.com/{username}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception("Failed to fetch data from LeetCode API")

# def update_readme(stats, repo_path="README.md"):
#     with open(repo_path, "r") as file:
#         readme = file.readlines()

#     for i, line in enumerate(readme):
#         if "**Contest Rating**" in line:
#             readme[i] = f"- **Contest Rating**: {stats.get('contestRating', 'N/A')}  \n"
#         elif "**Global Ranking**" in line:
#             readme[i] = f"- **Global Ranking**: {stats.get('ranking', 'N/A')} / {stats.get('totalRanking', 'N/A')}  \n"
#         elif "**Top Percentage**" in line:
#             readme[i] = f"- **Top Percentage**: {stats.get('topPercentage', 'N/A')}%  \n"
        
#         elif "**Acceptance Rate**" in line:
#             readme[i] = f"- **Acceptance Rate**: {stats.get('acceptanceRate', 'N/A')}%  \n"
#         elif "**Beats Stats**" in line:
#             readme[i] = f"- **Beats**: {stats.get('beats', 'N/A')}  \n"
#         elif "| 🟢 Easy" in line:
#             readme[i] = f"| 🟢 Easy        | {stats.get('easySolved', 0)} / {stats.get('totalEasy', 0)}          | {stats.get('acceptanceRate', 0):.2f}%              |\n"
#         elif "| 🟡 Medium" in line:
#             readme[i] = f"| 🟡 Medium      | {stats.get('mediumSolved', 0)} / {stats.get('totalMedium', 0)}         | {stats.get('acceptanceRate', 0):.2f}%             |\n"
#         elif "| 🔴 Hard" in line:
#             readme[i] = f"| 🔴 Hard        | {stats.get('hardSolved', 0)} / {stats.get('totalHard', 0)}            | {stats.get('acceptanceRate', 0):.2f}%             |\n"
#         elif "**Total Solved**" in line:
#             readme[i] = f"- **Total Solved**: ({stats.get('easySolved', 0)}+{stats.get('mediumSolved', 0)} +{stats.get('hardSolved', 0)})/ {stats.get('totalQuestions', 'N/A')}  \n"
#         elif "**Badges**" in line:
#             readme[i] = f"- **Badges**: {stats.get('badges', 'N/A')}  \n"
#         elif "**Most Recent Badge**" in line:
#             readme[i] = f"- **Most Recent Badge**: {stats.get('mostRecentBadge', 'N/A')}  \n"
#         elif "**Total Submissions in the past year**" in line:
#             readme[i] = f"- **Total Submissions in the past year**: {stats.get('submissionsLastYear', 'N/A')}  \n"
#         elif "**Total Active Days**" in line:
#             readme[i] = f"- **Total Active Days**: {stats.get('totalActiveDays', 'N/A')}  \n"
#         elif "**Max Streak**" in line:
#             readme[i] = f"- **Max Streak**: {stats.get('maxStreak', 'N/A')}  \n"

#     with open(repo_path, "w") as file:
#         file.writelines(readme)
#     print("README.md updated successfully.")


# if __name__ == "__main__":
#     leetcode_username = "SKSANDY2396"
#     stats = fetch_leetcode_stats(leetcode_username)
#     # print("Fetched Stats:", stats)  # Debugging
#     update_readme(stats)

import requests
import plotly.graph_objects as go

# Fetch data from the LeetCode API
def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("❌ Failed to fetch data from LeetCode API")

# Generate donut chart and save it as a PNG
def plot_difficulty_distribution(stats, image_path="leetcode_stats.png"):
    fig = go.Figure(data=[go.Pie(
        labels=["Easy", "Medium", "Hard"],
        values=[
            stats.get("easySolved", 0),
            stats.get("mediumSolved", 0),
            stats.get("hardSolved", 0)
        ],
        hole=0.5,
        marker=dict(colors=["#2ECC71", "#F1C40F", "#E74C3C"]),
    )])
    fig.update_layout(
        title_text="📊 Problem Solving Distribution",
        annotations=[dict(text='LeetCode', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    try:
        fig.write_image(image_path)
        print(f"[INFO] Chart saved to {image_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save chart image: {e}")

# Update README.md with new stats
def update_readme(stats, repo_path="README.md"):
    with open(repo_path, "r") as file:
        readme = file.readlines()

    for i, line in enumerate(readme):
        if "**Contest Rating**" in line:
            readme[i] = f"- **Contest Rating**: {stats.get('contestRating', 'N/A')}  \n"
        elif "**Global Ranking**" in line:
            readme[i] = f"- **Global Ranking**: {stats.get('ranking', 'N/A')} / {stats.get('totalRanking', 'N/A')}  \n"
        elif "**Top Rank Achieved**" in line:
            readme[i] = f"- **Top Rank Achieved**: {stats.get('topPercentage', 'N/A')}%  \n"
        elif "**Acceptance Rate**" in line:
            readme[i] = f"- **Acceptance Rate**: {stats.get('acceptanceRate', 'N/A')}%  \n"
        elif "| 🟢 Easy" in line:
            readme[i] = f"| 🟢 Easy        | {stats.get('easySolved', 0)} / {stats.get('totalEasy', 0)}          | {stats.get('acceptanceRate', 0):.2f}%              |\n"
        elif "| 🟡 Medium" in line:
            readme[i] = f"| 🟡 Medium      | {stats.get('mediumSolved', 0)} / {stats.get('totalMedium', 0)}         | {stats.get('acceptanceRate', 0):.2f}%             |\n"
        elif "| 🔴 Hard" in line:
            readme[i] = f"| 🔴 Hard        | {stats.get('hardSolved', 0)} / {stats.get('totalHard', 0)}            | {stats.get('acceptanceRate', 0):.2f}%             |\n"
        elif "**Total Submissions**" in line:
            readme[i] = f"- **Total Submissions**: {stats.get('totalSubmissions', 'N/A')}  \n"
        elif "**Total Badges**" in line:
            readme[i] = f"- **Total Badges**: {stats.get('badges', 'N/A')}  \n"
        elif "**Most Recent Badge**" in line:
            readme[i] = f"- **Most Recent Badge**: {stats.get('mostRecentBadge', 'N/A')}  \n"

    with open(repo_path, "w") as file:
        file.writelines(readme)

    print("[INFO] README.md updated successfully.")

# Main Execution
if __name__ == "__main__":
    print("[DEBUG] Fetching LeetCode stats...")
    leetcode_username = "SKSANDY2396"
    stats = fetch_leetcode_stats(leetcode_username)

    print("[DEBUG] Creating donut chart...")
    plot_difficulty_distribution(stats)

    print("[DEBUG] Updating README.md...")
    update_readme(stats)

    print("[SUCCESS] All updates complete. README and chart are up-to-date.")