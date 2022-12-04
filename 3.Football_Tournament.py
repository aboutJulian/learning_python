#This programm is supposed to simulate a football tournament with python
import random


class Player:
    stamina = int(random.randrange(start=60,stop=101))
    skill_level = int(random.randrange(start=1,stop=10))
    nameOfPlayer = "Player"


class Team:
    nameOfTeam = "Team"
    amountOfPlayers = 13
    PlayersInTeam = []


global ListOfTeams
ListOfTeams = []


def searchingForTeam(pTeam):
    for Team in ListOfTeams:
        currentTeam = Team
        if str(pTeam) == currentTeam.nameOfTeam:
            return currentTeam

def searchingForPlayerInTeam(pTeam, pPlayer):
    for Player in pTeam.PlayersInTeam:
        currentPlayer = Player
        if str(pPlayer) == Player.nameOfPlayer:
            return currentPlayer


def createAPlayer(pNameOfPlayer):
    pNameOfPlayer = str(pNameOfPlayer)
    pNameOfPlayer = Player()
    return pNameOfPlayer
    

def createATeam(pAmountOfPlayers, pNameOfTeam):
    #Make sure the values are strings or ints
    pNameOfTeam = str(pNameOfTeam)
    global NameOfTeam
    NameOfTeam = str(pNameOfTeam)
    pAmountOfPlayers = int(pAmountOfPlayers)
    AmountOfPlayers = int(pAmountOfPlayers)

    #create the new team and assign the new name and amount of players
    NameOfTeam = Team()
    NameOfTeam.nameOfTeam = pNameOfTeam
    NameOfTeam.amountOfPlayers = pAmountOfPlayers

    #create a for loop to assign players to the list in the team
    i = 0
    while i < NameOfTeam.amountOfPlayers:
        currentPlayer = createAPlayer("Player"+str(i+1))
        NameOfTeam.PlayersInTeam.append(currentPlayer)
        currentPlayer.nameOfPlayer = ("Player"+str(i+1))
        i=i+1
    return NameOfTeam


def creatingAllTeams(pAmountOfTeams):
    AmountOfTeams = int(pAmountOfTeams)
    i = 0
    while i < AmountOfTeams:
        new_team = createATeam(13, "Team"+str(i+1))
        ListOfTeams.append(new_team)
        print("The new team " + new_team.nameOfTeam + " has been created")
        i=i+1

def printAllPlayersOfTeam(pTeam):
    Team = searchingForTeam(str(pTeam))
    i=0
    while i < Team.amountOfPlayers:
        Player = searchingForPlayerInTeam(Team, "Player" + str(i+1))
        print(Player.nameOfPlayer)
        i=i+1


def printStaminaAndSkill(pTeam, pPlayer):
    Team = searchingForTeam(str(pTeam))
    Player = searchingForPlayerInTeam(Team, str(pPlayer))
    print(Player.nameOfPlayer + " has a skill level of " + str(Player.skill_level) + " and a stamina of " + str(Player.stamina) + ".")

def getRandomTeam():
    return ListOfTeams[random.randrange(start=1, stop=int(ListOfTeams.count)+1)].nameOfTeam
    
def 


def startGame(pTeams):
    creatingAllTeams(pTeams)
    print("What do you wanna do?")
















