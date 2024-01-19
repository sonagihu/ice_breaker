import requests

if __name__ == "__main__":
    gist_reponse = requests.get(
        "https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt"
    )

    print(gist_reponse.json())
