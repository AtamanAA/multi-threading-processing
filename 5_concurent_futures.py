import concurrent.futures

import requests


def get(url):
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    urls = [
        "https://hub.dummyapis.com/products?noofRecords=100&idStarts=1001&currency=usd",
    ] * 50
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for url in urls:
            future = executor.submit(get, url)
            results.append(future)
        for future in concurrent.futures.as_completed(results):
            print(future.result())
