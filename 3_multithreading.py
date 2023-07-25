import json
from threading import Thread

import requests


def get_data_to_list(url, content_list):
    r = requests.get(url)
    data = {"url": url, "content": r.json()}
    content_list.append(data)
    return data


def write_data_to_file(data, file_path):
    with open(file_path, "w") as file:
        file.write(json.dumps(data))


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
    content = []
    threads = []

    for url in urls:
        t = Thread(target=get_data_to_list, args=[url, content])
        threads.append(t)
        t.start()

    for thread in threads:
        x = thread.join()

    write_data_to_file(content, file_path)
