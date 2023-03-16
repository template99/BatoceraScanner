import unittest
import constants
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RunGameLists(unittest.TestCase):

    def setUp(self):
        print("setup")
        # init log files here?         



    def getAllSystems(self):
        platforms = []
        request = requests.get('http://'+constants.AUT+':1234/systems')            
        json = request.json()        
        for x in json:
            platforms.append(x["name"]) # add to list
        # remove 'all' favorites, etc
        for thisSystem in constants.ignoredSystems:
            if thisSystem in platforms:
                platforms.remove(thisSystem)
        print('>>total platforms: '+str(len(platforms)))            
        return platforms
    
    def getGamesPerSystem(self,thisPlatform):
        print("getting games for system " + thisPlatform)
        gamelist = []  # games to run
        print("getting games for platform " + thisPlatform)
        rq = requests.get('http:/'+constants.AUT+':1234/systems/'+thisPlatform+'/games')         
        json = rq.json()
        print('>>total games: '+str(len(json)))
        for thisGame in json:
            print("Game > " + thisGame["path"])
            gamelist.append(thisGame["path"]) # add to list
        print(" ")  
        return gamelist      

    # this will take forever
    #
    def test_all_systems(self):
        currentSystem = 0
        systemsList = []
        print(">Starting all the games list test")
        # grab all the systems
        systemsList = self.getAllSystems()
        for thisPlatform in systemsList:
            currentSystem+=1
            print(str(currentSystem) + ' > System: ' + thisPlatform)
            # do the individual platform
            gameList = []
            gameList = self.getGamesPerSystem(thisPlatform)
            if len(gameList)>0:
                print("running the games")
                for thisGame in gameList:
                    print('Run game:' + thisGame )


    def tearDown(self):
        print(">teardown")
        # close any files? 

if __name__ == "__main__":
    print("running....")
