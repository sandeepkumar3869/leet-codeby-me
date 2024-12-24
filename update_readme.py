import requests

def fetch_leetcode_stats(username):
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
            # Use .get() to avoid KeyError if 'contest_rating' is missing
            contest_rating = stats.get('contest_rating', 'N/A')  # Default to 'N/A' if not present
            readme[i] = f"- **Contest Rating**: {contest_rating}  \n"
        elif "| 🟢 Easy" in line:
            readme[i] = f"| 🟢 Easy        | {stats.get('easySolved', 0)} / {stats.get('totalEasy', 0)}          | {stats.get('acceptanceRate', 0):.2f}%              |\n"
        elif "| 🟡 Medium" in line:
            readme[i] = f"| 🟡 Medium      | {stats.get('mediumSolved', 0)} / {stats.get('totalMedium', 0)}         | {stats.get('acceptanceRate', 0):.2f}%             |\n"
        elif "| 🔴 Hard" in line:
            readme[i] = f"| 🔴 Hard        | {stats.get('hardSolved', 0)} / {stats.get('totalHard', 0)}            | {stats.get('acceptanceRate', 0):.2f}%             |\n"

    with open(repo_path, "w") as file:
        file.writelines(readme)

if __name__ == "__main__":
    leetcode_username = "SKSANDY2396"
    stats = fetch_leetcode_stats(leetcode_username)
    update_readme(stats)
    # print(stats)

