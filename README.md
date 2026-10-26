# IndicCorpV2 — 5K Samples per Language (Assignment Subset)

Stratified mini-subset of [ai4bharat/IndicCorpV2](https://huggingface.co/datasets/ai4bharat/IndicCorpV2)
for classroom / assignment use. First **5,000 non-empty lines** per language,
streamed in file order (no shuffling, no filtering beyond blank-line removal).

- 24 languages, **118,243** lines total (Kashmiri `ks` has only 3,243 lines in the source — everything available was taken).
- One file per language in `data/<code>.txt`, one sample per line, UTF-8.
- License of the source data: **CC-0** (public domain), per the dataset card.
  Models/code from the original project are MIT. This subset inherits CC-0 for the text.
- Citation: Doddapaneni et al., ACL 2023 — "Towards Leaving No Indic Language Behind"
  (https://aclanthology.org/2023.acl-long.693).

## Languages

| code | language | samples | source file(s) |
|------|----------|---------|----------------|
| as | Assamese | 5000 | as.txt |
| bd | Bodo | 5000 | bd.txt |
| bn | Bengali | 5000 | bn.txt |
| dg | Dogri | 5000 | dg.txt |
| en | English | 5000 | en.txt |
| gom | Konkani (Goan) | 5000 | gom.txt |
| gu | Gujarati | 5000 | gu.txt |
| hi | Hindi | 5000 | hi-1.txt (+hi-2/hi-3 if needed) |
| kha | Khasi | 5000 | kha.txt |
| kn | Kannada | 5000 | kn.txt |
| ks | Kashmiri | 3243 | ks.txt (full file — only 3,243 non-empty lines exist) |
| mai | Maithili | 5000 | mai.txt |
| ml | Malayalam | 5000 | ml.txt |
| mni | Manipuri | 5000 | mni.txt |
| mr | Marathi | 5000 | mr.txt |
| ne | Nepali | 5000 | ne.txt |
| or | Odia | 5000 | or.txt |
| pa | Punjabi | 5000 | pa.txt |
| sa | Sanskrit | 5000 | sa.txt |
| sat | Santali | 5000 | sat.txt |
| sd | Sindhi | 5000 | sd.txt |
| ta | Tamil | 5000 | ta.txt |
| te | Telugu | 5000 | te.txt |
| ur | Urdu | 5000 | ur.txt |

## Usage

```python
from pathlib import Path
def load(code, n=None):
    p = Path("data") / f"{code}.txt"
    lines = p.read_text(encoding="utf-8").splitlines()
    return lines if n is None else lines[:n]
bn = load("bn", 100)
print(len(bn), bn[0][:120])
```

Or see `load_example.py`.

## Reproducibility

Extracted 2026-10-26 by streaming the source `.txt` files from
`https://huggingface.co/datasets/ai4bharat/IndicCorpV2/resolve/main/data/`
and keeping the first 5,000 non-empty stripped lines per language
(`hi` streams `hi-1.txt → hi-2.txt → hi-3.txt` in order).
Script: see `extract.py` (kept alongside this repo build, not committed).
