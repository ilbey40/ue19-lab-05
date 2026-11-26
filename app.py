import requests

URL = "https://v2.jokeapi.dev/joke/Any?safe-mode"


def main():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    joke = response.json()

    if joke["type"] == "single":
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])


if __name__ == "__main__":
    main()
