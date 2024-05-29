import json

def sort_json_by_status_priority(json_data):
  """
  Sorts a JSON array by status (NOT_OK on top, OK on bottom) and then by priority (HIGH, MEDIUM, LOW).

  Args:
      json_data: A list containing JSON objects.

  Returns:
      A new list with the sorted JSON objects.
  """
  def sort_key(item):
    # Priority mapping (higher value means higher priority)
    priority_map = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    return (item["status"] == "NOT_OK", priority_map[item["priority"]])

  return sorted(json_data, key=sort_key, reverse=True)

# Sample JSON data (replace with your actual data)
json_data = [
    {"status": "OK", "priority": "HIGH"},
    {"status": "NOT_OK", "priority": "LOW"},
    {"status": "OK", "priority": "MEDIUM"},
    {"status": "NOT_OK", "priority": "HIGH"},
]

# Sort the JSON array
sorted_data = sort_json_by_status_priority(json_data)

# Print the sorted data (optional)
print(json.dumps(sorted_data, indent=2))
