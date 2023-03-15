import constants
import glob, os
import unittest


class SambaBatoceraTest(unittest.TestCase):

    def setUp(self):
        print('starting samba test(s)')

    def test_samba_dir(self):        
        x = os.listdir('\\\\' + constants.AUT + '\\share')
        for thisFile in x:
            print(' > ' + thisFile)    # write a file on a distant Samba share


    def test_file_output(self):
        print('outputting text')
        

    def tearDown(self):
        print("teardown")

    

    # for f in glob.glob(r'\\USER1-PC\Users\**\*', recursive=True):
    #     print(f)   # glob works too
    #     if os.path.isfile(f):
    #         print(os.path.getmtime(f))  # we can get filesystem information