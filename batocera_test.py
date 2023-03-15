import unittest
import requests
import time
import constants

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
outFile = "C:\\temp\\batotestlog.txt"
mySystem = 'atari2600'
#AUT = '192.168.101.162'
#AUT = 'minicab'
AUT = 'basement'
#AUT = 'hp'
ignoredSystems = ['all','screenshots','favorites']
platforms = []
delayBetweenGames = 13
delayDuringGame = 5
passedGames = []
failedGames = []


class BatoceraTest(unittest.TestCase):
    def setUp(self):
        print('firing up')
        self.baseSite =  'http://'+constants.AUT+':1234/'

    def test_web_interface(self):
        print('testing web interface')
        theURL = 'http://'+constants.AUT+':1234/'
        rq = requests.get(url=theURL)


    def test_batocera_apiCall(self):
        rq = requests.get('http://'+constants.AUT+':1234')
        self.assertEqual(rq.ok, True)

        
    def test_isRUnningGame(self):
        self.closeEmulator()
        thisGame = '/userdata/roms/atari2600/Xevious.bin'
        print('simple test for running game')
        rq = requests.post('http://' + constants.AUT + ':1234/launch/',thisGame)
        time.sleep(delayDuringGame)
        print(self.is_emulator_running())

    # flesh this out, true or false
    # 
    def is_emulator_running(self):
        rq = requests.get("http://"+constants.AUT+":1234/runningGame")
        if '200 NO GAME' in rq.text:
            return False
        else:
            return True 

    def test_list_systems(self):
        print('listing systems...')
        request = requests.get('http://'+constants.AUT+':1234/systems')            
        json = request.json()
        print('>>total systems: '+str(len(json)))
        for x in json:
            platforms.append(x["name"]) # add to list
            #print(" > " + x["name"])
        print(" ")
      

    def closeEmulator(self):
        print("** shutting down emulator **")
        rq = requests.get('http://'+constants.AUT+':1234/emukill')
        #print('kill response: ' + str(rq.status_code))


        
    def test_list_atari_games(self):
        gamelist = []  # games to run
        thisPlatform = 'atari2600'
        print('starting Atari 2600 games')        
        print("getting games for platform " + thisPlatform)
        rq = requests.get('http://'+constants.AUT+':1234/systems/atari2600/games')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for x in json:
            print("game > " + x["path"])
            gamelist.append(x["path"]) # add to list
        print(" ")


    def get_games_for_platform(self,platform):
        theGames = []
        rq = requests.get('http://'+constants.AUT+':1234/systems/'+platform+'/games')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for thisGame in json:
            print(" > " + thisGame["path"])
            theGames.append(thisGame["path"]) # add to list
        return theGames
    
    # launches each game, sees if it runs
    # 
    def test_atari_run_games(self):
        myPlatform = 'atari2600'
        self.closeEmulator()
        marker = 0; 
        time.sleep(delayBetweenGames)
        theGames = self.get_games_for_platform(myPlatform)
        for thisGame in theGames:
            print('(' + marker + '/' + theGames.count +') >starting game > ' + thisGame)
            rq = requests.post('http://' + constants.AUT + ':1234/launch/',thisGame)
            time.sleep(delayDuringGame)
            if self.is_emulator_running() == True:
                passedGames.append(thisGame)
                currentlyRunningGame = requests.get('http://' + constants.AUT + ':1234/runningame')    
                print(currentlyRunningGame.text[2])            
            else:
                print(">Game " + thisGame +  " failed to launch " + str(rq.ok))
                failedGames.append(thisGame)
            self.closeEmulator()
            time.sleep(delayBetweenGames)
            marker+=1
        print("post-run report for system " + myPlatform )
        print("****************")
        print('total passed games:  ' + str(passedGames.count))
        print('total failed games:  ' + str(failedGames.count))
        print('')




    # function launchGame(game) {
    # 	var xhr = new XMLHttpRequest();
    # 	xhr.open('POST', '/launch');
    # 	xhr.send(game);
    # }
    def test_run_one_game(self):
        self.closeEmulator() # pre-close
        print('running one game, and shutting down')
        rq = requests.post('http://' + constants.AUT + ':1234/launch','/userdata/roms/atari2600/Berzerk.bin')
        time.sleep(delayDuringGame)
        if rq.ok == True:            
            print(self.is_emulator_running())
            # append to running game list
        else:
            print('game run failed')
            # append to failed game list
        self.closeEmulator()

    def test_close_enulator(self):
        self.closeEmulator()


    def tearDown(self):
        print('done')

if __name__ == "__main__":
    print("running....")
    unittest.main()