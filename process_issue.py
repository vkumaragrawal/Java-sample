import json
import os

# Load the JSON file containing team and keyword data
with open('data.json', 'r') as f:
    data = json.load(f)

# Get issue details from environment variables
issue_title = os.environ['ISSUE_TITLE'].lower()
issue_body = os.environ['ISSUE_BODY'].lower()

# Combine title and body for matching
combined_issue_content = f"{issue_title} {issue_body}"

# Find matching teams based on keywords in the combined issue content
matched_teams = set()
for entry in data:
    keywords = [k.strip().lower() for k in entry['resource_keywords']]
    if any(keyword in combined_issue_content for keyword in keywords):
        matched_teams.add(entry['owning_team'])

# If no teams are matched, assign the "Hero Team"
if not matched_teams:
    matched_teams.add("Hero Team")

# Output the matched teams as a comma-separated string
print(f"::set-output name=teams::{', '.join(matched_teams)}")
