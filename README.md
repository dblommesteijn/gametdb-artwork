# gametdb-artwork

Gametdb Artwork Downloader


## Installation

**OS X (Mavericks)**

1. Install Python2.7

```bash
$ brew install python
# verify latest pip & setuptools
$ pip install --upgrade setuptools
$ pip install --upgrade pip
```

2. Install the application onto your system

```bash
$ chmod +x setup.py
$ sudo ./setup.py install
```

## Using the CLI

```bash
# download a single 
$ gametdb-artwork 
* stub
```

## Using the programmatical interface

```python
from src.gametdb import GametDb
# collect covers for R30P01 (downloads them to the current directory)
# NOTE: GametDb by default creates a structure for the stored covers with `./tmp/<UUID>/<ids>.png`
GametDb(target="./", output=True, debug=True).retrieve_single("R3OP01")
```

**Options:**

  * target: alternate directory
  * output: stdout output
  * debug: error reporting



## Testing

You can verify TestCases running the following command

```bash
$ python -m unittest discover tests
```
