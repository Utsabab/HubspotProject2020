from process import Process
import json
import requests

FETCH_URL = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=96b4181685c624cf69130c83e4a1'
POST_URL = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=96b4181685c624cf69130c83e4a1'


def fetch_data(url):
    """Fetch json content from specified url."""
    response = requests.get(url)
    return response.json()


def post_data(url, data):
    """Post json data to specified url."""
    res = requests.post(url, data=json.dumps(data))
    print ("Response from post", res.status_code)


def main():
    data = fetch_data(FETCH_URL)
    p = Process()
    result = p.process_data(data)
    post_data(POST_URL, result)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
