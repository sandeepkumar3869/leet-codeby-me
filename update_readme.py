

# import requests
# import plotly.graph_objects as go

# # Fetch data from the LeetCode API
# def fetch_leetcode_stats(username):
#     url = f"https://leetcode-stats-api.herokuapp.com/{username}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception("❌ Failed to fetch data from LeetCode API")

# # Generate donut chart and save it as a PNG
# def plot_difficulty_distribution(stats, image_path="leetcode_stats.png"):
#     fig = go.Figure(data=[go.Pie(
#         labels=["Easy", "Medium", "Hard"],
#         values=[
#             stats.get("easySolved", 0),
#             stats.get("mediumSolved", 0),
#             stats.get("hardSolved", 0)
#         ],
#         hole=0.5,
#         marker=dict(colors=["#2ECC71", "#F1C40F", "#E74C3C"]),
#     )])
#     fig.update_layout(
#         title_text="📊 Problem Solving Distribution",
#         annotations=[dict(text='LeetCode', x=0.5, y=0.5, font_size=20, showarrow=False)]
#     )
#     try:
#         fig.write_image(image_path)
#         print(f"[INFO] Chart saved to {image_path}")
#     except Exception as e:
#         print(f"[ERROR] Failed to save chart image: {e}")

# # Update README.md with new stats
# def update_readme(stats, repo_path="README.md"):
#     with open(repo_path, "r") as file:
#         readme = file.readlines()

#     for i, line in enumerate(readme):
#         if "**Contest Rating**" in line:
#             readme[i] = f"- **Contest Rating**: {stats.get('contestRating', 'N/A')}  \n"
#         elif "**Global Ranking**" in line:
#             readme[i] = f"- **Global Ranking**: {stats.get('ranking', 'N/A')} / {stats.get('totalRanking', 'N/A')}  \n"
#         elif "**Top Rank Achieved**" in line:
#             readme[i] = f"- **Top Rank Achieved**: {stats.get('topPercentage', 'N/A')}%  \n"
#         elif "**Acceptance Rate**" in line:
#             readme[i] = f"- **Acceptance Rate**: {stats.get('acceptanceRate', 'N/A')}%  \n"
#         elif "| 🟢 Easy" in line:
#             readme[i] = f"| 🟢 Easy        | {stats.get('easySolved', 0)} / {stats.get('totalEasy', 0)}          | {stats.get('acceptanceRate', 0):.2f}%              |\n"
#         elif "| 🟡 Medium" in line:
#             readme[i] = f"| 🟡 Medium      | {stats.get('mediumSolved', 0)} / {stats.get('totalMedium', 0)}         | {stats.get('acceptanceRate', 0):.2f}%             |\n"
#         elif "| 🔴 Hard" in line:
#             readme[i] = f"| 🔴 Hard        | {stats.get('hardSolved', 0)} / {stats.get('totalHard', 0)}            | {stats.get('acceptanceRate', 0):.2f}%             |\n"
#         elif "**Total Submissions**" in line:
#             readme[i] = f"- **Total Submissions**: {stats.get('totalSubmissions', 'N/A')}  \n"
#         elif "**Total Badges**" in line:
#             readme[i] = f"- **Total Badges**: {stats.get('badges', 'N/A')}  \n"
#         elif "**Most Recent Badge**" in line:
#             readme[i] = f"- **Most Recent Badge**: {stats.get('mostRecentBadge', 'N/A')}  \n"

#     with open(repo_path, "w") as file:
#         file.writelines(readme)

#     print("[INFO] README.md updated successfully.")

# # Main Execution
# if __name__ == "__main__":
#     print("[DEBUG] Fetching LeetCode stats...")
#     leetcode_username = "SKSANDY2396"
#     stats = fetch_leetcode_stats(leetcode_username)
#     # print("Fetched Stats:", stats)

#     print("[DEBUG] Creating donut chart...")
#     plot_difficulty_distribution(stats)

#     print("[DEBUG] Updating README.md...")
#     update_readme(stats)

#     print("[SUCCESS] All updates complete. README and chart are up-to-date.")

import requests
import matplotlib.pyplot as plt

# === CONFIG ===
USERNAME = "SKSANDY2396"
README_FILE = "README.md"
STATS_IMAGE = "leetcode_stats.png"

# === GRAPHQL QUERY ===
url = "https://leetcode.com/graphql/"

query = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
      reputation
      starRating
    }
    submitStats: submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
    }
  }
  userContestRanking(username: $username) {
    attendedContestsCount
    rating
    globalRanking
    totalParticipants
    topPercentage
  }
}
"""

variables = {"username": USERNAME}
response = requests.post(url, json={"query": query, "variables": variables})

if response.status_code != 200:
    raise Exception(f"GraphQL query failed: {response.text}")

data = response.json().get("data", {})
user = data.get("matchedUser", {})
contest = data.get("userContestRanking", {})

# === Extract problem stats ===
stats = {s["difficulty"]: s for s in user.get("submitStats", {}).get("acSubmissionNum", [])}
easy = stats.get("Easy", {"count": 0, "submissions": 0})
medium = stats.get("Medium", {"count": 0, "submissions": 0})
hard = stats.get("Hard", {"count": 0, "submissions": 0})

total_solved = easy["count"] + medium["count"] + hard["count"]
total_submissions = easy["submissions"] + medium["submissions"] + hard["submissions"]
acceptance_rate = round((total_solved / total_submissions) * 100, 2) if total_submissions > 0 else 0.0

# === Generate Pie Chart ===
labels = ["Easy", "Medium", "Hard"]
sizes = [easy["count"], medium["count"], hard["count"]]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=["#4CAF50","#FFC107","#F44336"])
plt.axis("equal")
plt.title("Problem Solving Distribution")
plt.savefig(STATS_IMAGE)
plt.close()

# === Generate README.md content ===
readme_content = f"""
# 🏆 LeetCode Journey by Sandeep Kumar  
[Visit my LeetCode profile](https://leetcode.com/u/{USERNAME}/)  

Welcome to my repository, where I document my journey of solving coding challenges on LeetCode.  

---

## 🚀 Contest Performance  
- **Contest Rating**: {contest.get("rating", "N/A")}  
- **Global Ranking**: {contest.get("globalRanking", "N/A")}  
- **Contests Attended**: {contest.get("attendedContestsCount", "N/A")}  
- **Top Rank Achieved**: {contest.get("topPercentage", "N/A")}%  

---

## 💡 Problem-Solving Stats  
- **Acceptance Rate**: {acceptance_rate}%  

| Difficulty | Solved | Submissions |
|------------|--------|-------------|
| 🟢 Easy        | {easy['count']} | {easy['submissions']} |
| 🟡 Medium      | {medium['count']} | {medium['submissions']} |
| 🔴 Hard        | {hard['count']} | {hard['submissions']} |

---

## 📊 Problem Solving Distribution

![LeetCode Stats]({STATS_IMAGE})

---

## 🏅 Achievements and Badges  
- **Ranking**: {user.get("profile", {}).get("ranking", "N/A")}  
- **Reputation**: {user.get("profile", {}).get("reputation", "N/A")}  
- **Star Rating**: {user.get("profile", {}).get("starRating", "N/A")}  

---

## 📚 About This Repository  
This repository contains solutions to various LeetCode problems in the form of `.ipynb` notebooks and other formats.  

---

## 💬 Connect with Me  
📧 Email: sandeep.kumar@science.christuniversity.in  
🔗 LeetCode Profile: [{USERNAME}](https://leetcode.com/u/{USERNAME}/)  

---

## 📄 License  

This project is licensed under the MIT License.
"""

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated successfully!")
