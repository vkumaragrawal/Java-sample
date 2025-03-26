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
if len(matched_teams) == 1:
    # If a single team is matched, add only that owning team
    output_labels = ", ".join(matched_teams)
elif len(matched_teams) > 1:
    # If multiple teams are matched, add only Virtuoso Team label
    output_labels = "Virtuoso Team"
else:
    # If no teams are matched, add only Virtuoso Team label
    output_labels = "Virtuoso Team"

# Output the matched labels as a comma-separated string
print(f"::set-output name=labels::{output_labels}")
