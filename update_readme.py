import requests
import matplotlib.pyplot as plt
from datetime import datetime

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
      userAvatar
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
  userContestRankingHistory(username: $username) {
    attended
    rating
    ranking
    problemsSolved
    contest {
      title
      startTime
    }
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
contest_history = [
    c for c in data.get("userContestRankingHistory", []) if c.get("attended")
]

# === Problem Stats ===
stats = {s["difficulty"]: s for s in user.get("submitStats", {}).get("acSubmissionNum", [])}
easy = stats.get("Easy", {"count": 0, "submissions": 0})
medium = stats.get("Medium", {"count": 0, "submissions": 0})
hard = stats.get("Hard", {"count": 0, "submissions": 0})

total_solved = easy["count"] + medium["count"] + hard["count"]
total_submissions = easy["submissions"] + medium["submissions"] + hard["submissions"]
acceptance_rate = round((total_solved / total_submissions) * 100, 2) if total_submissions > 0 else 0.0

# === Pie Chart ===
plt.figure(figsize=(5, 5))
plt.pie(
    [easy["count"], medium["count"], hard["count"]],
    labels=["Easy", "Medium", "Hard"],
    autopct="%1.1f%%",
    startangle=140,
    colors=["#4CAF50", "#FFC107", "#F44336"]
)
plt.title("Problem Solving Distribution")
plt.savefig(STATS_IMAGE)
plt.close()

# === Recent 5 Contests ===
contest_rows = ""
for c in sorted(contest_history, key=lambda x: x['contest']['startTime'], reverse=True)[:5]:
    date_str = datetime.fromtimestamp(c['contest']['startTime']).strftime("%Y-%m-%d")
    contest_rows += f"| {c['contest']['title']} ({date_str}) | {c['rating']:.2f} | {c['ranking']} | {c['problemsSolved']} |\n"
if not contest_rows:
    contest_rows = "| No recent contests | - | - | - |\n"

# === Contest Leaderboard Bar ===
leaderboard_rows = ""
for c in sorted(contest_history, key=lambda x: x['rating'], reverse=True)[:5]:
    max_rating = 4000
    bar_length = int((c['rating'] / max_rating) * 20)
    bar = "█" * bar_length + "░" * (20 - bar_length)
    date_str = datetime.fromtimestamp(c['contest']['startTime']).strftime("%Y-%m-%d")
    leaderboard_rows += f"| {c['contest']['title']} ({date_str}) | {c['rating']:.2f} | {bar} |\n"
if not leaderboard_rows:
    leaderboard_rows = "| No recent contests | - | - |\n"

# === Dynamic Badges ===
base_badge_url = "https://img.shields.io/badge"
acceptance_badge = f"{base_badge_url}/Acceptance-{acceptance_rate}%25-brightgreen"
solved_badge = f"{base_badge_url}/Solved-{total_solved}-blue"
ranking_badge = f"{base_badge_url}/Ranking-{user.get('profile', {}).get('ranking', 'N/A')}-orange"
contests_badge = f"{base_badge_url}/Contests-{contest.get('attendedContestsCount', 'N/A')}-purple"

# === Polished README Template ===
readme_content = f"""
# 🏆 LeetCode Journey by Sandeep Kumar  

![Acceptance Rate]({acceptance_badge}) 
![Total Solved]({solved_badge}) 
![Ranking]({ranking_badge}) 
![Contests Attended]({contests_badge})

[Visit my LeetCode profile](https://leetcode.com/u/{USERNAME}/)  

Welcome to my repository, where I document my journey of solving coding challenges on LeetCode.  

---

## 🚀 Contest Performance  
- **Contest Rating**: {contest.get("rating", "N/A")}  
- **Global Ranking**: {contest.get("globalRanking", "N/A")} / {contest.get("totalParticipants", "N/A")}  
- **Contests Attended**: {contest.get("attendedContestsCount", "N/A")}  
- **Top Rank Achieved**: {contest.get("topPercentage", "N/A")}%  

### 📈 Recent Contests
| Contest | Rating | Rank | Problems Solved |
|---------|--------|------|----------------|
{contest_rows}

### 📊 Contest Leaderboard
| Contest | Rating | Progress |
|---------|--------|---------|
{leaderboard_rows}

---

## 💡 Problem-Solving Stats  
- **Acceptance Rate**: {acceptance_rate}%  

| Difficulty | Solved | Submissions |
|------------|--------|-------------|
| 🟢 Easy    | {easy['count']} | {easy['submissions']} |
| 🟡 Medium  | {medium['count']} | {medium['submissions']} |
| 🔴 Hard    | {hard['count']} | {hard['submissions']} |

---

## 📊 Problem Solving Distribution

![LeetCode Stats]({STATS_IMAGE})

---

## 📚 About This Repository  
This repository contains solutions to various LeetCode problems in the form of `.ipynb` notebooks and other formats.  

---

## 💬 Connect with Me  
📧 Email: sksandy3869@gmail.com
🔗 LeetCode Profile: [{USERNAME}](https://leetcode.com/u/{USERNAME}/)  

---

## 💖 Support My Work

If my LeetCode journey or open-source projects have inspired or helped you, consider supporting my work to keep it going strong!  

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-fafbfc?logo=github&style=for-the-badge)](https://github.com/sponsors/sandeepkumar3869)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-sksandy3869-yellow?logo=buy-me-a-coffee&style=for-the-badge)](https://captainsandeepkumar.blogspot.com/search?q=UPI)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-sandeepkumar3869-FF5E5B?logo=kofi&style=for-the-badge)](https://captainsandeepkumar.blogspot.com/search?q=UPI)

📬 **Other ways to connect or contribute:**  
- 💼 [PayPal](https://www.paypal.me/8986578410) 
- 📱 **UPI:** `sksandy3869-1@oksbi`  
- 💻 [LeetCode Profile](https://leetcode.com/u/SKSANDY2396/)  
- ✉️ **Email:** [sksandy3869@gmail.com](mailto:sksandy3869@gmail.com)

---

## 📄 License  

This project is licensed under the MIT License.
"""

# === Write README ===
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated successfully!")
