import requests
import time


def main():
    plotcol = "http"
    host_name = "localhost"
    port = 7474

    while True:
        response = requests.get(f"{plotcol}://{host_name}:{port}")

        if response.status_code == 200:
            break
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
