#-*- coding:cp949 -*-
from werewolf.database.DATABASE import DATABASE
from werewolf.game.GAME_STATE import GAME_STATE
from werewolf.game.entry.Entry import Truecharacter
from werewolf.game.entry.Entry import Race
from werewolf.game.rule.BasicRule import BasicRule
import random
import copy

class HamsterRule(BasicRule):
    min_players = 11
    max_players = 17

    # �⺻ ����
    temp_truecharacter ={}
    temp_truecharacter[11] =  [1,1,1,1,2,3,4,5,5,6]
    temp_truecharacter[12] =  [1,1,1,1,1,2,3,4,5,5,6]
    temp_truecharacter[13] =  [1,1,1,1,1,1,2,3,4,5,5,6]
    temp_truecharacter[14] =  [1,1,1,1,1,1,1,2,3,4,5,5,6]
    temp_truecharacter[15] =  [1,1,1,1,1,1,1,2,3,4,5,5,5,6]
    temp_truecharacter[16] =  [1,1,1,1,1,1,2,3,4,5,5,5,6,7,7]    
    temp_truecharacter[17] =  [1,1,1,1,1,1,2,3,4,5,5,5,6,7,7,8]    

    def __init__(self,game):
        WerewolfRule.__init__(self, game)
        logging.debug("Hamstar Rule")

    def nextTurn(self):
        if self.game.state== GAME_STATE.READY:
            if self.min_players <= self.game.players and self.game.players <= self.max_players:
                logging.logging("���� �ʱ�ȭ ����")
                self.initGame()                
            else:
                self.game.deleteGame()
        elif self.game.state==GAME_STATE.PLAYING:
            if self.game.day == 1:
                if self.game.players == 17:
                    self.nexeTurn_2day()                    
                else:
                    BasicRule.nexeTurn_2day(self)
            else:
                if self.game.players == 17:
                    self.nextTurn_Xday()
                else:
                    BasicRule.nextTurn_Xday(self)

    def initGame(self):
        logging.info("init Hamstar")
        WerewolfRule.initGame(self)

    def nexeTurn_2day(self):
        logging.info("2��°�� ����!")

        #�Ϲ� �α׸� ���� ���� ����� üũ�Ѵ�.
        self.game.entry.checkNoCommentPlayer()

        #����� NPC ����
        victim =self.game.entry.getVictim()
        victim.toDeathByWerewolf()
        
        #�ܽ���
        hamsterPlayer = self.game.entry.getPlayersByTruecharacter(Truecharacter.WEREHAMSTER)[0] 
        
        #�� ��!
        self.assaultByForecast(hamsterPlayer)

        #������ ��Ŵ 
        noMannerPlayers = self.game.entry.getNoMannerPlayers()
        for noMannerPlayer in noMannerPlayers:
            noMannerPlayer.toDeath("���� ")       
        
        #�ڸ��� �ʱ�ȭ
        self.game.entry.initComment()

        #3. ���� ���� ������Ʈ
        self.game.setGameState("state", "������")
        self.game.setGameState("day", self.game.day+1)
      
    def nextTurn_Xday(self):
        logging.info("���� ���� ����!")

        #�Ϲ� �α׸� ���� ���� ����� üũ�Ѵ�.
        self.game.entry.checkNoCommentPlayer()
        
        #��ǥ -��� �ִ� �����ڰ� ��ǥ�� �ߴ��� üũ, ���ߴٸ� ���� ��ǥ
        victim = self.decideByMajority()
        if victim:
            victim.toDeath("����") 
        
        #������ ��Ŵ 
        noMannerPlayers = self.game.entry.getNoMannerPlayers()
        for noMannerPlayer in noMannerPlayers:
            noMannerPlayer.toDeath("���� ")       
        
        #�ڸ��� �ʱ�ȭ
        self.game.entry.initComment()

        #�ܽ���
        hamsterPlayer = self.game.entry.getPlayersByTruecharacter(Truecharacter.WEREHAMSTER)[0] 
        
        #�� ��!
        self.assaultByForecast(hamsterPlayer)

        #����!
        assaultVictim = self.decideByWerewolf()
        if assaultVictim:
            logging.debug("assaultVictim: %s", assaultVictim)
            self.assaultByWerewolfAndHamster(assaultVictim, victim, hamsterPlayer)

        #���� ���� Ȯ��
        #���!
        humanRace = self.game.entry.getEntryByRace(Race.HUMAN)
        #for human in humanRace :
        #    print human
        
        #������!
        werewolfRace = self.game.entry.getEntryByRace(Race.WEREWOLF)
        #for werewolf in werewolfRace :
        #    print werewolf
        
        if (len(humanRace) <= len(werewolfRace)) or not humanRace:
            if self.game.termOfDay == 60:
                self.game.setGameState("state", GAME_STATE.TESTOVER)
            else:
                self.game.setGameState("state", GAME_STATE.GAMEOVER)

            if hamsterPlayer.alive == "����":
                logging.info("�ܽ��� �¸�")
                self.game.setGameState("win", "2")
            else:
                logging.info("�ζ� �¸�")
                self.game.setGameState("win", "1")
            
        elif not werewolfRace:
            if self.game.termOfDay == 60:
                self.game.setGameState("state", GAME_STATE.TESTOVER)
            else:
                self.game.setGameState("state", GAME_STATE.GAMEOVER)

            if hamsterPlayer.alive == "����":
                logging.info("�ܽ��� �¸�")
                self.game.setGameState("win", "2")
            else:
                logging.info("�ΰ� �¸�")
                self.game.setGameState("win", "0")
        else:
            logging.info("��� ����")
            #self.game.setGameState("state","������")
        
        self.game.setGameState("day",self.game.day+1)
        
    def assaultByForecast(self, hamsterPlayer):
        logging.debug("�ܺ�!!")
        forecastTarget = {}
        seerPlayer = self.game.entry.getPlayersByTruecharacter(Truecharacter.SEER)[0]    

        if seerPlayer.alive == "����":
            logging.debug("seerPlayer: %s", seerPlayer)
            forecastTarget = seerPlayer.openEye()
            logging.debug("forecastTarget: %s", forecastTarget)

            if forecastTarget is not None:
                forecastTarget = self.game.entry.getCharacter(forecastTarget['mystery'])

        logging.debug("hamsterPlayer: ", hamsterPlayer)

        if forecastTarget and hamsterPlayer.alive == "����" and hamsterPlayer.id == forecastTarget.id:
            logging.debug("�ܺ� ����: %s", hamsterPlayer)
            hamsterPlayer.toDeath("����")                        
        else:
            logging.debug("�ܺ� ����")
            
    def assaultByWerewolfAndHamster(self, assaultVictim, victim, hamsterPlayer):
        self.game.entry.recordAssaultResult(assaultVictim)

        guard = {}
        hunterPlayer = self.game.entry.getPlayersByTruecharacter(Truecharacter.BODYGUARD)[0]

        if(hunterPlayer.alive == "����"):
            logging.debug("hunterPlayer: %s", hunterPlayer)
            guard = hunterPlayer.guard()
            if guard is not None:
                guard = self.game.entry.getCharacter(guard['purpose'])
                logging.debug("guard: %s", guard)
                
        if assaultVictim.id == victim.id:
            logging.debug("���� ����: ������")
        elif guard and assaultVictim.id == guard.id:
            logging.debug("���� ����: ����")
        elif assaultVictim.id == hamsterPlayer.id:
            logging.debug("���� ����: ����")
        else:
            logging.debug("���� ����: %s", assaultVictim)
            assaultVictim.toDeath("����")