"""Load the 5K-per-language IndicCorpV2 assignment subset."""
from pathlib import Path

DATA = Path(__file__).parent / "data"

def load(code: str, n: int | None = None) -> list[str]:
    lines = (DATA / f"{code}.txt").read_text(encoding="utf-8").splitlines()
    lines = [l for l in lines if l.strip()]
    return lines if n is None else lines[:n]

if __name__ == "__main__":
    import csv
    with open(Path(__file__).parent / "manifest.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            code = row["code"]
            got = len(load(code))
            print(f"{code:5} {got:5} (manifest {row['samples']})")
