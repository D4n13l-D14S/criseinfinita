from player.main import Player
from npc.main import Npc
from random import randint
from helpers import printWSleep, print1by1
class Turn:
  def __init__(self,player:Player,npc:Npc):
    self.player = player
    self.npc = npc
    self.action()

  def action(self):
    playerAction = 0
    npcAction = int(randint(1,3))
    
    while int(playerAction) not in [1, 2] :
      print('Player HP: ',self.player.hp)
      print('Enemy HP: ',self.npc.hp)

      

      print('''Erga sua arma contra essa vil criatura ou defenda-se!
      [  1  ] Para atacar
      [  2  ] Para defender ''')
      playerAction = (str(input('Escolha uma opção: ')))

    if int(playerAction) == 2:
      self.player.defend = True
    if self.npc.name in ['Goblin', 'Ogro']:
      if npcAction == 3:
        self.npc.defend = True
    if self.npc.name in ['Vampiro']:
      if npcAction == 3:
        self.npc.healAtk(self.npc.atk)
        self.npc.defend = False
    if self.npc.name in ['Succubus']:
      if npcAction == 3:
        self.player.tomoucc = True
        self.player.defend = False

    if int(playerAction) == 0:
      self.npc.calculateDamage(0)
    if self.player.tomoucc == True:
      playerAction = 0
      print1by1('O Succubus te lança um charme irresistível, você não consegue se mover!\n')
    if self.npc.defend and self.player.defend:
      self.player.turnHeal()
    if playerAction == 0:
      self.npc.calculateDamage(0)
    elif not self.player.defend:
      self.npc.calculateDamage(self.player.atk)
    if not(self.npc.defend) and self.npc.alive:
      self.player.calculateDamage(self.npc.atk)
    
    self.player.tomoucc = False
    self.player.defend = False
    self.npc.defend = False
    printWSleep()
    
