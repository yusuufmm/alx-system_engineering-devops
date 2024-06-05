#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """Fetch user data"""
    USERNAME = res.json().get('username')
    """Extract username"""
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        """Extract task completion status"""
        TASK_TITLE = task.get('title')
        """Extract task title"""
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """Write data to JSON file"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
