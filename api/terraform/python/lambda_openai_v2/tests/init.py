"""Shared code for testing the lambda function"""
import json


def get_event(filespec):
    """Load a JSON file and return the event"""
    with open(filespec, "r") as f:
        event = json.load(f)
        return event
