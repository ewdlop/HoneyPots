import requests

# GitHub Personal Access Token
github_token = 'YOUR_GITHUB_PERSONAL_ACCESS_TOKEN'

# GitHub API URL to list repositories for the authenticated user
url = 'https://api.github.com/user/repos'

# Headers for the request, including the authorization token
headers = {
    'Authorization': f'token {github_token}'
}

# Send a GET request to the GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repos = response.json()
    
    # Print the names of the repositories
    print("Repositories:")
    for repo in repos:
        print(f"  {repo['name']}")
else:
    print(f"Failed to retrieve repositories: {response.status_code}")
