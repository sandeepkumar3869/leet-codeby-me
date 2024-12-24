import requests

def fetch_leetcode_stats(username):
    # Replace with a community API or scraping logic if required
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from LeetCode API")

def update_readme(stats, repo_path="README.md"):
    with open(repo_path, "r") as file:
        readme = file.readlines()

    # Update specific sections in README
    for i, line in enumerate(readme):
        if "**Contest Rating**" in line:
            readme[i] = f"- **Contest Rating**: {stats['contest_rating']}  \n"
        elif "| 🟢 Easy" in line:
            readme[i] = f"| 🟢 Easy        | {stats['easy_solved']} / {stats['total_easy_questions']}          | {stats['acceptance_rate']}%              | Beats {stats['acceptance_rate']}%  |\n"
        elif "| 🟡 Medium" in line:
            readme[i] = f"| 🟡 Medium      | {stats['medium_solved']} / {stats['total_medium_questions']}         | {stats['acceptance_rate']}%             | Beats {stats['acceptance_rate']}%  |\n"
        elif "| 🔴 Hard" in line:
            readme[i] = f"| 🔴 Hard        | {stats['hard_solved']} / {stats['total_hard_questions']}            | {stats['acceptance_rate']}%             | Beats {stats['acceptance_rate']}%  |\n"

    with open(repo_path, "w") as file:
        file.writelines(readme)

if __name__ == "__main__":
    leetcode_username = "SKSANDY2396"
    stats = fetch_leetcode_stats(leetcode_username)
    update_readme(stats)
