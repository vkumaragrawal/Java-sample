import json
import os

# Load the JSON file containing team and keyword data
with open('data.json', 'r') as f:
    data = json.load(f)

# Get the issue body from the environment variable
issue_body = os.environ['ISSUE_BODY'].lower()

# Find matching teams based on keywords in the issue body
matched_teams = set()
for entry in data:
    keywords = [k.strip().lower() for k in entry['resource_keywords']]
    if any(keyword in issue_body for keyword in keywords):
        matched_teams.add(entry['owning_team'])

# If no teams are matched, assign the "Hero Team"
if not matched_teams:
    matched_teams.add("Hero Team")

# Output the matched teams as a comma-separated string
print(f"::set-output name=teams::{', '.join(matched_teams)}")
