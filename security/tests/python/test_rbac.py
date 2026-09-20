import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'lab'))
from rbac import allowed
class T(unittest.TestCase):
 def test_default_deny(self): self.assertFalse(allowed('unknown','view_public'))
 def test_no_foreign_result(self): self.assertFalse(allowed('learner','view_own_result',owner=False)); self.assertTrue(allowed('learner','view_own_result',owner=True))
 def test_visitor(self): self.assertFalse(allowed('visitor','manage_demo_config'))
if __name__=='__main__':unittest.main()
