import concurrent.futures
import json

import requests


def get_data(url):
    r = requests.get(url)
    data = {"url": url, "content": r.json()}
    return data


if __name__ == "__main__":
    urls = [
        "https://dummyapi.online/api/movies",
        "https://dummyapi.online/api/blogposts",
        "https://dummyapi.online/api/users",
        "https://dummyapi.online/api/pokemon",
        "https://dummyapi.online/api/products",
        "https://hub.dummyapis.com/employee?noofRecords=100&idStarts=1001",
        "https://hub.dummyapis.com/products?noofRecords=100&idStarts=1001&currency=usd",
    ]
    file_path = "content.json"
    results = []
    content = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for url in urls:
            future = executor.submit(get_data, url)
            results.append(future)
        for future in concurrent.futures.as_completed(results):
            content.append(future.result())

        with open(file_path, "w") as file:
            file.write(json.dumps(content))
