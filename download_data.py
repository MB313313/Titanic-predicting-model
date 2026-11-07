"""Download the classic Kaggle-format Titanic CSVs into data/ if they are missing."""

from pathlib import Path
from urllib.request import urlretrieve

DATA_DIR = Path(__file__).resolve().parent / "data"

FILES = {
    "train.csv": [
        "https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv",
        "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/titanic/train.csv",
    ],
    "test.csv": [
        "https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/test.csv",
        "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/titanic/test.csv",
    ],
}


def download(name, urls, dest):
    last_error = None
    for url in urls:
        try:
            print("Downloading {} from {} ...".format(name, url))
            urlretrieve(url, dest)
            print("  saved {} ({} bytes)".format(dest, dest.stat().st_size))
            return
        except Exception as exc:
            last_error = exc
            print("  failed: {}".format(exc))
    raise RuntimeError("Could not download {}".format(name)) from last_error


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for name, urls in FILES.items():
        download(name, urls, DATA_DIR / name)


if __name__ == "__main__":
    main()
