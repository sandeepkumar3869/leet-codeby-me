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
            readme[i] = f"- **Contest Rating**: {stats.get('contest_rating', 'N/A')}  \n"
        elif "| 🟢 Easy" in line:
            readme[i] = f"| 🟢 Easy        | {stats.get('easy_solved', 0)} / {stats.get('total_easy_questions', 0)}          | {stats.get('acceptance_rate', '0')}%              | Beats {stats.get('acceptance_rate', '0')}%  |\n"
        elif "| 🟡 Medium" in line:
            readme[i] = f"| 🟡 Medium      | {stats.get('medium_solved', 0)} / {stats.get('total_medium_questions', 0)}         | {stats.get('acceptance_rate', '0')}%             | Beats {stats.get('acceptance_rate', '0')}%  |\n"
        elif "| 🔴 Hard" in line:
            readme[i] = f"| 🔴 Hard        | {stats.get('hard_solved', 0)} / {stats.get('total_hard_questions', 0)}            | {stats.get('acceptance_rate', '0')}%             | Beats {stats.get('acceptance_rate', '0')}%  |\n"

    with open(repo_path, "w") as file:
        file.writelines(readme)


if __name__ == "__main__":
    leetcode_username = "SKSANDY2396"
    stats = fetch_leetcode_stats(leetcode_username)

    # Debug: Print the fetched stats to check for missing keys
    print(stats)

    update_readme(stats)

