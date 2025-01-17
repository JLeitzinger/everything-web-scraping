"""
To check if your implementation is correct run test.py

*NOTE: Don't change the method names, as that's what's used in the tester.
        but, feel free to add anything else to test and debug your code.
"""
import requests

def extract_feed():
    """
        Return an array of all the post objects on the feed page.
    """
    feedList = []
    page = 0

    while True:
        r = requests.get(f"http://localhost:8000/feed/{page}")
        page+=1
        newPage = r.json()['posts']

        if len(newPage) == 0:
            break

        else: feedList.extend(newPage)

    return feedList

def extract_emails():
    """
        Return an array of all the emails on the discover page.
    """

    return []

def username_exists(username):
    """
        username - The username to check if exists,  without @ (ex: username="davidteather")
        This function will return True if the provided username already exists, and false if it doesn't
    """

    return False

if __name__ == "__main__":
    # Optional: You can call your methods here if you want to test them without running the tester
    # print(extract_feed())
    pass