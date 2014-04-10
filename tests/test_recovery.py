import unittest

from src.gametdb import GametDb

class TestRecovery(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_retrieve_single(self):
    d = GametDb(output=False)
    r30p01 = d.retrieve_single("R3OP01")
    self.assertTrue(type(r30p01['cover'] == bool), "must be true")
    self.assertTrue(type(r30p01['disc'] == bool), "must be true")
    self.assertTrue(type(r30p01['full'] == bool), "must be true")
    self.assertTrue(type(r30p01['3d'] == bool), "must be true")

  def test_retrieve_multi(self):
    d = GametDb(output=False)
    list = ["R3OP01", "S5BPKM"]
    mlt = d.retrieve_multi(list)
    self.assertTrue(type(mlt["R3OP01"] == dict), "must be a dict")
    self.assertTrue(type(mlt["S5BPKM"] == dict), "must be a dict")

if __name__ == '__main__':
  unittest.main()