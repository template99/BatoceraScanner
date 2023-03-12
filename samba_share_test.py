import constants
import glob, os
import unittest


class SambaBatoceraTest(unittest.TestCase):

    def setUp(self):
        print('starting samba test(s)')

    def test_samba_share_write(self):        
        with open(r'\\'+constants.AUT+r'\share\system\logs\tester.txt', 'r') as f:
            f.write('hello from unit test')    # write a file on a distant Samba share


    def tearDown(self):
        print("torn down")

        
    # for f in glob.glob(r'\\USER1-PC\Users\**\*', recursive=True):
    #     print(f)   # glob works too
    #     if os.path.isfile(f):
    #         print(os.path.getmtime(f))  # we can get filesystem information