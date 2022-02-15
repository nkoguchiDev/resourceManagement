import requests
import time


def main():
    plotcol = "http"
    host_name = "localhost"
    port = 7474

    while True:
        try:
            response = requests.get(f"{plotcol}://{host_name}:{port}")
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        else:
            if response.status_code == 200:
                break
            else:
                time.sleep(1)


if __name__ == "__main__":
    main()
