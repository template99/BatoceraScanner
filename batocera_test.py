import unittest
import requests
import time

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
mySystem = 'atari2600'
AUT = '192.168.101.162'
#AUT = 'hp'
ignoredSystems = ['all','screenshots','favorites']
platforms = []
delayBetweenGames = 9
delayDuringGame = 9 


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
        

    def is_emulator_running(self):
        rq = requests.get("http://"+AUT+":1234/runningGame")
        return str(rq.text) 

    def test_list_systems(self):
        print('listing systems...')
        request = requests.get('http://'+AUT+':1234/systems')            
        json = request.json()
        print('>>total systems: '+str(len(json)))
        for x in json:
            print(" > " + x["name"])
            platforms.append(x["name"]) # add to list
        print(" ")

        

    def closeEmulator(self):
        print("** shutting down emulator **")
        requests.get('http://'+AUT+':1234/emukill')
        
    def test_list_atari_games(self):
        gamelist = []  # games to run
        print('starting Atari 2600 games')
        thisPlatform = 'atari2600'
        print("getting games for platform " + thisPlatform)
        rq = requests.get('http://hp:1234/systems/atari2600/games')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for x in json:
            print(" > " + x["path"])
            gamelist.append(x["path"]) # add to list
        print(" ")

    def get_games_for_platform(self,platform):
        theGames = []
        rq = requests.get('http://hp:1234/systems/atari2600/games')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for thisGame in json:
            print(" > " + thisGame["path"])
            theGames.append(thisGame["path"]) # add to list
        return theGames
    
    def test_atari_run(self):
        self.closeEmulator()
        theGames = self.get_games_for_platform("atari2600")
        for thisGame in theGames:
            print('running game > ' + thisGame)
            rq = requests.post('http://hp:1234/launch/',thisGame)
            time.sleep(delayDuringGame)
            print("is ok? "  + str(rq.ok))
            # TODO: check here
            runGame = requests.request('http://hp:1234/runningame')

            self.closeEmulator()
            time.sleep(delayBetweenGames)





    # function launchGame(game) {
    # 	var xhr = new XMLHttpRequest();
    # 	xhr.open('POST', '/launch');
    # 	xhr.send(game);
    # }
    def test_run_one_game(self):
        print('running one game, and shutting down')
        rq = requests.post('http://hp:1234/launch',"/userdata/roms/atari2600/Berzerk.bin")
        time.sleep(delayDuringGame)
        print("is ok? "  + str(rq.ok))
        print(self.is_emulator_running())
        self.closeEmulator()

    def test_close_enulator(self):
        self.closeEmulator()


    def tearDown(self):
        print('done')

if __name__ == "__main__":
    print("running....")
    unittest.main()