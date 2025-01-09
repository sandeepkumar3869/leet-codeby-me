<!-- Here’s a beautifully structured README for your GitHub repository:

---

# 🏆 LeetCode Journey by Sandeep Kumar  
[Visit my LeetCode profile](https://leetcode.com/u/SKSANDY2396/)  

Welcome to my repository, where I document my journey of solving coding challenges on LeetCode. Here, you'll find my solutions, approaches, and reflections on the problems I tackle.  

---

## 🚀 Contest Performance  
- **Contest Rating**: N/A  
- **Global Ranking**: 731819 / N/A  
- **Contests Attended**: 1  
- **Top Rank Achieved**: 77.84% (100/3,399)  

---

## 💡 Problem-Solving Stats  
- **Acceptance Rate**: 36.82%  
|----------------|---------------------|---------------------|----------------|  
| 🟢 Easy        | 114 / 849          | 36.82%              |
| 🟡 Medium      | 35 / 1779         | 36.82%             |
| 🔴 Hard        | 4 / 788            | 36.82%             |

---

## 🔥 Submission Stats  
- **Total Submissions**: N/A  
- **Attempts**:  
  - 🟢 Easy: 41  
  - 🟡 Medium: 15  
  - 🔴 Hard: 7  

---

## 🏅 Achievements and Badges  
- **Total Badges**: 1  
- **Most Recent Badge**: N/A  

---

## 📚 About This Repository  
This repository contains solutions to various LeetCode problems in the form of `.ipynb` notebooks and other formats. Each solution is accompanied by explanations and alternative approaches (where applicable).  

---

## 🌟 How to Use This Repository  
1. Browse through the directory to find solutions categorized by problem difficulty.  
2. Refer to the explanations provided alongside each solution to enhance your understanding.  
3. Feel free to contribute or suggest improvements!

---

## 💬 Connect with Me  
For suggestions, discussions, or collaboration:  
📧 Email: sandeep.kumar@science.christuniversity.in  
🔗 LeetCode Profile: [SKSANDY2396](https://leetcode.com/u/SKSANDY2396/)  

---
 -->

<!-- 
# 🏆 LeetCode Journey by Sandeep Kumar  
[Visit my LeetCode profile](https://leetcode.com/u/SKSANDY2396/)  

Welcome to my repository, where I document my journey of solving coding challenges on LeetCode. Here, you'll find my solutions, approaches, and reflections on the problems I tackle.  

---

## 🚀 Contest Performance  
- **Contest Rating**: N/A  
- **Global Ranking**: 731819 / N/A  
- **Contests Attended**: 1  
- **Top Rank Achieved**: 77.84% (100/3,399)  

---

## 💡 Problem-Solving Stats  
- **Acceptance Rate**: 36.82%  

| Difficulty | Solved / Total | Acceptance Rate |
|------------|----------------|-----------------|
| 🟢 Easy        | 114 / 849          | 36.82%              |
| 🟡 Medium      | 35 / 1779         | 36.82%             |
| 🔴 Hard        | 4 / 788            | 36.82%             |

---

## 🔥 Submission Stats  
- **Total Submissions**: N/A  
- **Attempts**:  
  - 🟢 Easy: 41  
  - 🟡 Medium: 15  
  - 🔴 Hard: 7  

---

## 🏅 Achievements and Badges  
- **Total Badges**: 1  
- **Most Recent Badge**: N/A  

---

## 📚 About This Repository  
This repository contains solutions to various LeetCode problems in the form of `.ipynb` notebooks and other formats. Each solution is accompanied by explanations and alternative approaches (where applicable).  

---

## 🌟 How to Use This Repository  
1. Browse through the directory to find solutions categorized by problem difficulty.  
2. Refer to the explanations provided alongside each solution to enhance your understanding.  
3. Feel free to contribute or suggest improvements!

---

## 💬 Connect with Me  
For suggestions, discussions, or collaboration:  
📧 Email: sandeep.kumar@science.christuniversity.in  
🔗 LeetCode Profile: [SKSANDY2396](https://leetcode.com/u/SKSANDY2396/)  

---
## 📄 License

This project is licensed under the MIT License. Feel free to fork, modify, and use it as needed! -->

readme_template = f"""
# 🏆 LeetCode Journey by Sandeep Kumar  
[Visit my LeetCode profile](https://leetcode.com/u/SKSANDY2396/)  

Welcome to my repository, where I document my journey of solving coding challenges on LeetCode. Here, you'll find my solutions, approaches, and reflections on the problems I tackle.  

---

## 🚀 Contest Performance  
- **Contest Rating**: {contest_rating or "N/A"}  
- **Global Ranking**: {stats['ranking']}  
- **Contests Attended**: {contests_attended or "N/A"}  
- **Top Rank Achieved**: {top_rank or "N/A"}  

---

## 💡 Problem-Solving Stats  
- **Acceptance Rate**: {stats['acceptanceRate']}%  

| Difficulty | Solved / Total | Acceptance Rate |
|------------|----------------|-----------------|
| 🟢 Easy        | {stats['easySolved']} / {stats['totalEasy']} | {stats['acceptanceRate']}% |
| 🟡 Medium      | {stats['mediumSolved']} / {stats['totalMedium']} | {stats['acceptanceRate']}% |
| 🔴 Hard        | {stats['hardSolved']} / {stats['totalHard']} | {stats['acceptanceRate']}% |

---

## 🔥 Submission Stats  
- **Total Submissions**: {total_submissions or "N/A"}  
- **Attempts**:  
  - 🟢 Easy: {easy_attempts}  
  - 🟡 Medium: {medium_attempts}  
  - 🔴 Hard: {hard_attempts}  

---

## 🏅 Achievements and Badges  
- **Total Badges**: {total_badges}  
- **Most Recent Badge**: {recent_badge or "N/A"}  

---
...
"""

with open("README.md", "w") as file:
    file.write(readme_template)
