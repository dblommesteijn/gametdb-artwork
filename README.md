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

2. Clone github repository

```bash
$ git clone https://github.com/dblommesteijn/gametdb-artwork
```

3. Install the application onto your system

```bash
$ cd gametdb-artwork/
$ chmod +x setup.py
$ sudo ./setup.py install --record installation_files.txt
```

4. Uninstalling

```bash
# some files may require you to become root
$ sudo cat installation_files.txt | xargs rm -rf
```

## Using the CLI

```bash
# download artwork to `./tmp/<UUID>/BLES01807.jpg`
$ gametdb-artwork BLES01807
# print command options
$ gametdb-artwork -h
```

## Using the programmatical interface

```python
from src.gametdb import GametDb
# collect covers for R30P01 (downloads them to the current directory)
# NOTE: GametDb by default creates a structure for the stored covers with `./tmp/<UUID>/<ids>.png`
GametDb(target="./", output=True, debug=True).retrieve_single("R3OP01")
```

*NOTE: by default all types and platforms will be iterated to find a match for the given ID or serial. By limiting the scope of extensions and platforms less requests have to be made to the URL (so it's faster).*

```python
# retrieve Wii covers (png files)
GametDb(platforms='wii', extensions=['png']).retrieve_single("R3OP01")
# retrieve PS3 covers (jpg files)
GametDb(platforms='ps3', extensions=['jpg']).retrieve_single("BLES01807")
```


## Testing

You can verify TestCases running the following command

```bash
$ python -m unittest discover tests
```
