#!/usr/bin/env python

from distutils.core import setup
import os

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "gametdb-artwork",
  version = "0.0.1",
  author = "Dennis Blommesteijn",
  author_email = "dennis@blommesteijn.com",
  description = ("Artwork downloader tool for gametdb."),
  license = "MIT",
  keywords = "artwork download cover tool gametdb",
  url = "https://github.com/dblommesteijn/gametdb-artwork",
  packages = ['gametdbartwork'],
  package_dir = {'gametdbartwork': "src/"} ,
  long_description = read('README.md'),
  scripts = ["scripts/gametdb-artwork"]
)