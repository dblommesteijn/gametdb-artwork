import unittest

from src.gametdb import GametDb

class TestRecovery(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_retrieve_single_wii(self):
    d = GametDb(output=False, platform='wii', extensions=['png'])
    r30p01 = d.retrieve_single("R3OP01")
    self.assertTrue(type(r30p01['cover'] == bool), "must be true")
    self.assertTrue(type(r30p01['disc'] == bool), "must be true")
    self.assertTrue(type(r30p01['full'] == bool), "must be true")
    self.assertTrue(type(r30p01['3d'] == bool), "must be true")
    # TODO: fix assert to string path

  def test_retrieve_multi_wii(self, platform='wii', extensions=['png']):
    d = GametDb(output=False)
    list = ["R3OP01", "S5BPKM"]
    mlt = d.retrieve_multi(list)
    self.assertTrue(type(mlt["R3OP01"] == dict), "must be a dict")
    self.assertTrue(type(mlt["S5BPKM"] == dict), "must be a dict")

  def test_retrieve_single_ps3(self):
    d = GametDb(output=False, platform='ps3', extensions=['jpg'])
    BLES01807 = d.retrieve_single("BLES01807")
    self.assertTrue(type(BLES01807['cover'] == bool), "must be true")
    # TODO: fix assert to string path

  def test_retrieve_multi_ps3(self, platform='ps3', extensions=['jpg']):
    d = GametDb(output=False)
    list = ["BLES01807", "BLJS10257"]
    mlt = d.retrieve_multi(list)
    print mlt
    self.assertTrue(type(mlt["BLES01807"] == dict), "must be a dict")
    self.assertTrue(type(mlt["BLJS10257"] == dict), "must be a dict")

if __name__ == '__main__':
  unittest.main()
  