import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

# See REST Api list on https://github.com/batocera-linux/batocera-emulationstation/blob/master/es-app/src/services/HttpServerThread.cpp#L25
#
# GET  /restart
# GET  /quit
# GET  /emukill
# GET  /reloadgames
# POST /messagebox												-> body must contain the message text as text/plain
# POST /notify													-> body must contain the message text as text/plain
# POST /launch													-> body must contain the exact file path as text/plain
# GET  /runningGame
# GET  /isIdle
# GET  /systems
# GET  /systems/{systemName}
# GET  /systems/{systemName}/logo
# GET  /systems/{systemName}/games/{gameId}		
# POST /systems/{systemName}/games/{gameId}						-> body must contain the game metadatas to save as application/json
# GET  /systems/{systemName}/games/{gameId}/media/{mediaType}
# POST /systems/{systemName}/games/{gameId}/media/{mediaType}		-> body must contain the file bytes to save. Content-type must be valid.

# port 1234 for all API calls
#
hostSite = "http://minicab:1234"



class BatoceraTest(unittest.TestCase):
    def setUp(self):
        print('firing up')
        self.driver = webdriver.Chrome() # not really needed

    def test_batocera_test(self):
        print('starting run')
        driver = self.driver
        driver.get(hostSite)
        self.assertIn("EmulationStation", driver.title)
        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assert_(1==1)

    def test_two(self):
        print('here is another test')

    def closeEmulator(self):
        print("shutting down emulator")
                # <input class="toolbarbutton" type="button" value="Kill running emulator" onclick="emuKill()">
        
    def getGamesforPlatform(self,thisPlatform):
        print("getting games for platform " + thisPlatform)
        x = requests.get(hostSite + "/systems/"+thisPlatform)






    # //div[@id='systemList']  -- gets you the systems
    def get_systems(self):
        print("getting systems")
        zopz = self.driver.find_elements(By.XPATH,"") 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    print("running....")
    unittest.main()