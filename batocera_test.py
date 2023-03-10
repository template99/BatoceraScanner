import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
import json

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
outFile = "C:\\temp\\batotestlog.txt"
mySystem = 'a2600'
#AUT = 'minicab'
AUT = 'hp'
platforms = []
delayBetweenGames = 3
delayDuringGame =3


class BatoceraTest(unittest.TestCase):
    def setUp(self):
        print('firing up')
        #self.driver = webdriver.Chrome() # not really needed
        self.baseSite =  'http://'+AUT+':1234/'

    def test_batocera_apiCall(self):
        rq = requests.get('http://'+AUT+':1234')
        self.assertEqual(rq.ok, True)
        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assert_(1==1)
        

        

    def test_list_systems(self):
        print('listing systems...')
        rq = requests.get('http://'+AUT+':1234/systems')            
        json = rq.json()
        print('>>total systems: '+str(len(json)))
        for x in json:
            print(" > " + x["name"])
            platforms.append(x["name"]) # add to list
        print(" ")

        

    def closeEmulator(self):
        print("** shutting down emulator **")
        requests.post('http://'+AUT+':1234/emukill')
        
    def test_atari_games(self):
        print('starting Atari 2600 games')
        thisPlatform = 'a2600'
        print("getting games for platform " + thisPlatform)
        rq = requests.get('http://'+AUT+':1234/systems/"+thisPlatform)')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for x in json:
            print(" > " + x["name"])
            platforms.append(x["name"]) # add to list
        print(" ")





    # //div[@id='systemList']  -- gets you the systems
    def get_systems(self):
        print("getting systems")
        zopz = self.driver.find_elements(By.XPATH,"") 

    def tearDown(self):
        print('done')

if __name__ == "__main__":
    print("running....")
    unittest.main()