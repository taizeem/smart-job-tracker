import requests
import json


def fetch_jobs():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    return data


def format_jobs(posts):
    jobs = []

    for post in posts[:10]:
        jobs.append({
            "id": post["id"],
            "title": post["title"],
            "description": post["body"],
            "status": "new"
        })

    return jobs


def save_jobs(jobs):
    with open("jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)


def main():
    data = fetch_jobs()
    jobs = format_jobs(data)
    save_jobs(jobs)


if __name__ == "__main__":
    main()