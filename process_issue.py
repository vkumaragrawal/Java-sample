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

# Prepare output based on matches found
if matched_teams:
    # If multiple teams are matched, include FR_FALLBACK label only once.
    if len(matched_teams) > 1:
        matched_teams.add("FR_FALLBACK")
else:
    # If no teams are matched, assign FR_FALLBACK label.
    matched_teams.add("FR_FALLBACK")

# Output the matched teams as a comma-separated string (excluding FR_FALLBACK)
print(f"::set-output name=teams::{', '.join([team for team in matched_teams if team != 'FR_FALLBACK'])}")
