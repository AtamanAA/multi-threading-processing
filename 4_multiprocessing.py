from multiprocessing import Pool

import requests


def get(url):
    r = requests.get(url)
    return r.json()


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

    with Pool(5) as p:
        print(p.map(get, urls))
