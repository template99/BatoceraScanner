import constants
import os
import unittest


class SambaBatoceraTest(unittest.TestCase):

    def setUp(self):
        print('starting samba test(s)')

    def test_samba_dir(self):        
        x = os.listdir('\\\\' + constants.AUT + '\\share')
        for thisFile in x:
            print(' > ' + thisFile)    # write a file on a Samba share


    def test_file_output(self):
        print('outputting text')
        x = open(constants.logDir + "testlog.txt","w")
        x.write("here's a test log writeout")
        

    def tearDown(self):
        print("teardown")

  