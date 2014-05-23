# gametdb-artwork

This tool allows you to download GameTDB artwork, and store it to your local machine. It's written in Python, provides command line, and programatical interface.

*NOTE: GameTDB (http://www.gametdb.com/) provides game artwork for Consoles (Wii(U), PS3).*

## Installation

Gametdb-artwork should run on all platforms that have Python2.7 installed.

**Install Python2.7**

OSX (via homebrew):

```bash
$ brew install python
# verify latest pip & setuptools
$ pip install --upgrade setuptools
$ pip install --upgrade pip
```

Ubuntu/ Debian (Linux):

```bash
$ sudo apt-get install python
# verify latest pip & setuptools
$ sudo pip install --upgrade setuptools
$ sudo pip install --upgrade pip
```

**Clone github repository**

```bash
$ git clone https://github.com/dblommesteijn/gametdb-artwork
```

**Install the application onto your system**

```bash
$ cd gametdb-artwork/
$ chmod +x setup.py
$ sudo ./setup.py install --record installation_files.txt
```

**Uninstalling**

```bash
# some files may require you to become root
$ cat installation_files.txt | xargs sudo rm -rf
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
from gametdbartwork.gametdb import GametDb
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
