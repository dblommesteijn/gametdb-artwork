
import urllib2
import uuid
import os
import sys

class GametDb():

  def __init__(self, **kwargs):
    self.url = "http://art.gametdb.com"
    if 'url' in kwargs:
      self.url = kwargs['url']
    self.output = False
    if 'output' in kwargs:
      self.output = kwargs['output']
    self.platform = ["wii", "ps3"]
    if 'platform' in kwargs:
      self.platform = [kwargs['platform']]
    self.languages = ["EN", "US", "JA", "NL", "DE", "FR"]
    if 'languages' in kwargs:
      self.languages = kwargs['languages']
    self.extensions = ["png", "jpg"]
    if 'extensions' in kwargs:
      self.extensions = kwargs['extensions']
    self.target = "tmp/" + str(uuid.uuid1())
    if 'target' in kwargs:
      self.target = kwargs['target']
    self.debug = False
    if 'debug' in kwargs:
      self.debug = kwargs['debug']
    # required fixed attributes for storing and recovering types
    self.type = {"cover": "", "cover3D": "3d", "disc": "disc", "coverfullHQ": "full", "coverfull": "full"}

  def retrieve_multi(self, ids):
    downloads = {}
    for id in ids:
      downloads[id] = self.retrieve_single(id)
    return downloads
  
  def retrieve_single(self, id):
    downloaded = {}
    if self.output:
      sys.stdout.write(id + "... ")
      sys.stdout.flush()
    for p in self.platform:
      for t in self.type.keys():
        t_target = self.type[t]
        for l in self.languages:
          for e in self.extensions:
            found = False
            cover_url = self.url + "/" + p + "/" + t + "/" + l + "/" + id + "." + e
            try:
              u = urllib2.urlopen(cover_url)
              t_target_name = t_target
              if t_target_name == '':
                t_target_name = "cover"
              # download and report
              downloaded[t_target_name] = self.__download(u, cover_url, t_target)
              if self.output:
                sys.stdout.write(t + " ")
                sys.stdout.flush()
              found = True
            except Exception as e:
              if self.debug:
                print cover_url
                print e
              pass
            if found:
              break
    if self.output:
      sys.stdout.write("\n")
      sys.stdout.flush()
    return downloaded
  
  def __download(self, handle, url, type):
    file_name = url.split('/')[-1]
    path_target = self.target + "/" + type
    if not os.path.exists(path_target):
      os.makedirs(path_target)
    download_target = path_target + "/" + file_name
    f = open(download_target, 'wb')
    meta = handle.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    # print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
      buffer = handle.read(block_sz)
      if not buffer:
          break
      file_size_dl += len(buffer)
      f.write(buffer)
      # status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
      # status = status + chr(8)*(len(status)+1)
    f.close()
    return download_target
    # return file_size_dl == file_size





