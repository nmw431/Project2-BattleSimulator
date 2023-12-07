from PyQt6.QtWidgets import *
from gui import *
from main import *
import sys
import random



class Logic(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.C_ONE.setChecked(True)
        
        self.characters()
        self.Stats_Label.setText(f"Hp: {self.c_1[1]}\nAttack: {self.c_1[2]}\nElement: {self.c_1[4]}")
        self.Stats_Label_2.setText(f"Hp: {self.c_2[1]}\nAttack: {self.c_2[2]}\nElement: {self.c_2[4]}")
        self.Stats_Label_3.setText(f"Hp: {self.c_3[1]}\nAttack: {self.c_3[2]}\nElement: {self.c_3[4]}")
        
        self.turn = 1
        self.START.clicked.connect(lambda: self.start())
        self.QUIT.clicked.connect(lambda: self.Quit())
        self.ATTACK.clicked.connect(lambda: self.attack())
        self.BACK.clicked.connect(lambda: self.back())
        self.MOVE.clicked.connect(lambda: self.move_one())
        self.MOVE_2.clicked.connect(lambda: self.move_two())
        self.MOVE_3.clicked.connect(lambda: self.move_three())
        self.BACK.clicked.connect(lambda: self.back())
        
        
        
    
    def characters(self):
        self.character_set = []
        with open('CharacterStats.csv', 'r') as stat_contents:
            for character in stat_contents:        
                self.character_set.append(character)

        #print(self.characters)
        self.c_1 = self.character_set[1].split(",")
        self.c_2 = self.character_set[2].split(",")
        self.c_3 = self.character_set[3].split(",")
    def start(self):
        self.concluded = False
        self.enemy_defeated = False
        self.player_defeated = False
        self.player_mid_health = False
        self.player_low_health = False
        self.enemy_mid_health = False
        self.enemy_low_health = False
        self.characters()
        self.HPBAR_ONE.setProperty("value", 100)
        self.HPBAR_ONE.setStyleSheet("""
            QProgressBar {
                border: 2px solid rgba(0, 0, 0, 1); 
                border-radius: 5px;
                text-align: center;
                font-size: 12px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.35);
                color: black;
            }
            QProgressBar::chunk {
                background-color: ##30B700;
            }
        """)
        
        
        
        self.HPBAR_ONE_2.setProperty("value", 100)
        
        self.HPBAR_ONE_2.setStyleSheet("""
            QProgressBar {
                border: 2px solid rgba(0, 0, 0, 1);
                border-radius: 5px;
                text-align: center;
                font-size: 12px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.35);
                color: black;
            }
            QProgressBar::chunk {
                background-color: ##30B700;
            }
        """)
        
        self.Screens.setCurrentWidget(self.Battle)
        print(self.characters)
        option_one = self.character_set[1].split(",")
        option_two = self.character_set[2].split(",")
        option_three = self.character_set[3].split(",")
        
        option_one[1] = int(option_one[1])
        option_one[2] = int(option_one[2])
        
        option_two[1] = int(option_two[1])
        option_two[2] = int(option_two[2])
        
        option_three[1] = int(option_three[1])
        option_three[2] = int(option_three[2])
        
        print(option_one)
        print(option_two)
        print(option_three)


        option_one2 = self.character_set[1].split(",")
        option_two2 = self.character_set[2].split(",")
        option_three2 = self.character_set[3].split(",")
        
        option_one2[1] = int(option_one[1])
        option_one2[2] = int(option_one[2])
        
        option_two2[1] = int(option_two[1])
        option_two2[2] = int(option_two[2])
        
        option_three2[1] = int(option_three[1])
        option_three2[2] = int(option_three[2])
        
        
        print(option_one2)
        print(option_two2)
        print(option_three2)
        
        
        option = random.randint(1, 3)
        
        
        
        if option == 1:
            self.enemy_stats = option_one
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]}")
            self.ENEMY_IMAGE.setPixmap(QtGui.QPixmap(f"{self.enemy_stats[3]}"))
            self.max_hp = option_one[1]
        elif option == 2:
            self.enemy_stats = option_two
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]}")
            self.ENEMY_IMAGE.setPixmap(QtGui.QPixmap(f"{self.enemy_stats[3]}"))
            self.max_hp = option_two[1]
        elif option == 3:
            self.enemy_stats = option_three
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]}")
            self.ENEMY_IMAGE.setPixmap(QtGui.QPixmap(f"{self.enemy_stats[3]}"))
            self.max_hp = option_three[1]
        if self.C_ONE.isChecked():
            self.player_stats = option_one2
            self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]}")
            self.PLAYER_IMAGE.setPixmap(QtGui.QPixmap(f"{self.player_stats[3]}"))
            self.MOVE.setText(f"{self.player_stats[5]}")
            self.MOVE_2.setText(f"{self.player_stats[9]}")
            self.MOVE_3.setText(f"{self.player_stats[13]}")
            self.max_hp2 = option_one2[1]
            self.MOVE_2.setStyleSheet("background-color: rgb(252, 76, 2);")
            self.MOVE_3.setStyleSheet("background-color: rgb(252, 76, 2);")
            print("C_ONE")

        elif self.C_TWO.isChecked():
            self.player_stats = option_two2
            self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]}")
            self.PLAYER_IMAGE.setPixmap(QtGui.QPixmap(f"{self.player_stats[3]}"))
            self.MOVE.setText(f"{self.player_stats[5]}")
            self.MOVE_2.setText(f"{self.player_stats[9]}")
            self.MOVE_3.setText(f"{self.player_stats[13]}")
            self.max_hp2 = option_two2[1]
            self.MOVE_2.setStyleSheet("background-color: rgb(5, 194, 221);")
            self.MOVE_3.setStyleSheet("background-color: rgb(5, 194, 221);")
            print("C_TWO")

        elif self.C_THREE.isChecked():
            self.player_stats = option_three2
            self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]}") 
            self.PLAYER_IMAGE.setPixmap(QtGui.QPixmap(f"{self.player_stats[3]}"))
            self.MOVE.setText(f"{self.player_stats[5]}")
            self.MOVE_2.setText(f"{self.player_stats[9]}")
            self.MOVE_3.setText(f"{self.player_stats[13]}")
            self.max_hp2 = option_three2[1]
            self.MOVE_2.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.MOVE_3.setStyleSheet("background-color: rgb(0, 255, 0);")
            print("C_THREE")
    
        print(f'Player :{self.player_stats}')
        print(f'Enemy :{self.enemy_stats}')
        
        
        
    def attack(self):
        if self.concluded == True:
            self.Screens.setCurrentWidget(self.Pick)
            self.turn = 1
            self.CURRENT_EVENT.setText("")
            self.CURRENT_EVENT_2.setText("")
            self.Turn_Tracker.setText(f"Turn: {self.turn}")
            self.Conclusion.setText("")

        
        self.PLAYERO.setCurrentWidget(self.MOVES)
    def back(self):
        self.PLAYERO.setCurrentWidget(self.BOPTIONS)

    def enemy_turn(self):
        if self.enemy_stats[1] > 0 and self.player_stats[1] > 0:
            opposing_move = random.randint(1, 3)
            if opposing_move == 1:
                move_one = self.enemy_stats[6]
                self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[6])) + (int(self.enemy_stats[2])))
                self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[6])) + (int(self.enemy_stats[2])))} damage from {self.enemy_stats[5]}.\n Effective.")
                #self.HPBAR_ONE.setProperty("value", float((self.player_stats[1]) / (self.max_hp2) * 100))
                
            elif opposing_move == 2:
                #Effective
                move_two = self.enemy_stats[10]
                if self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) * 2)} damage from {self.enemy_stats[9]}. \nVery Effective!")
                    
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) * 2)} damage from {self.enemy_stats[9]}. \nVery Effective!")
                    
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) * 2)} damage from {self.enemy_stats[9]}. \nVery Effective!")
                #Not Very Effective
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) - 1)} damage from {self.enemy_stats[9]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) - 1)} damage from {self.enemy_stats[9]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) * 2)} damage from {self.enemy_stats[9]}. \n Not very effective.")    
                
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) - 1)} damage from {self.enemy_stats[9]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) - 1)} damage from {self.enemy_stats[9]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[10])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[10])) - 1)} damage from {self.enemy_stats[9]}. \n Not very effective.")                
                else:
                    self.player_stats[1] = self.player_stats[1] - int(self.enemy_stats[10])
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {self.enemy_stats[10]} damage from {self.enemy_stats[9]}. \n Effective.")
                    
            elif opposing_move == 3:
                #Very Effective
                move_three = self.enemy_stats[14]
                if self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) * 2)} damage from {self.enemy_stats[13]}. \nVery Effective!")
                    
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) * 2)} damage from {self.enemy_stats[13]}. \nVery Effective!")
                    
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) * 2)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) * 2)} damage from {self.enemy_stats[13]}. \nVery Effective!")
                #Not Very Effective
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective.")
                
                elif self.enemy_stats[0] == 'Blitzadile' and self.player_stats[0] == 'Blitzadile':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective.")
                    
                elif self.enemy_stats[0] == 'Jormangandr' and self.player_stats[0] == 'Jormangandr':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective")
                    
                elif self.enemy_stats[0] == 'Totogaia' and self.player_stats[0] == 'Totogaia':
                    self.player_stats[1] = self.player_stats[1] - ((int(self.enemy_stats[14])) - 1)
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {((int(self.enemy_stats[14])) - 1)} damage from {self.enemy_stats[13]}. \n Not very effective.")               
           
                else: 
                    self.player_stats[1] = self.player_stats[1] - int(self.enemy_stats[14])
                    self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                    self.CURRENT_EVENT.setText(f"Player took {self.enemy_stats[14]} damage from {self.enemy_stats[13]}. \nEffective.")
                    
            if float(((self.player_stats[1]) / (self.max_hp2)) * 100) < 50:
                self.player_mid_health = True
                
            if float(((self.player_stats[1]) / (self.max_hp2)) * 100) < 30:
                self.player_low_health = True
            
            if int(self.player_stats[1]) <= 0:
                self.Conclusion.setText(f"Enemy Wins !!!")
                #self.CURRENT_EVENT.setText(f"Enemy Wins")
                self.player_defeated = True
                self.player_stats[1] = 0
                self.PLAYER_STATS.setText(f"PLAYER\nName: {self.player_stats[0]} \nHP: {self.player_stats[1]} / {self.max_hp2}")
                
    def move_one(self):
        self.Turn_Tracker.setText(f"Turn: {self.turn}")
        if self.enemy_stats[1] > 0 and self.player_stats[1] > 0:            
            #damage = (int(self.player_stats[6]) + int(self.player_stats[2]))
            self.enemy_stats[1] = self.enemy_stats[1] - (int(self.player_stats[6]) + int(self.player_stats[2]))
            

        self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
        self.CURRENT_EVENT_2.setText(f"Enemy took {(int(self.player_stats[6]) + int(self.player_stats[2]))} damage from {self.player_stats[5]}. \nEffective.")
        
        
        self.PLAYERO.setCurrentWidget(self.BOPTIONS)
        
        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 50:
            self.enemy_mid_health = True
        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 30:
            self.enemy_low_health = True   
            
        if int(self.enemy_stats[1]) <= 0:
            self.Conclusion.setText(f"Player Wins !!!")
            #self.CURRENT_EVENT.setText(f"Player Wins")
            self.enemy_defeated = True
            self.enemy_stats[1] = 0
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
            self.PLAYERO.setCurrentWidget(self.BOPTIONS)

            self.HPBAR_ONE.setProperty("value", float(((self.player_stats[1]) / (self.max_hp)) * 100))
        self.battle_loop()
    def move_two(self):
        self.Turn_Tracker.setText(f"Turn: {self.turn}")
        #Very Effective
        
        if self.enemy_stats[1] > 0 and self.player_stats[1] > 0:
            if self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) * 2} damage from {self.player_stats[9]}. \nVery Effective!")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) * 2} damage from {self.player_stats[9]}.\nVery Effective!")
                
            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) * 2} damage from {self.player_stats[9]}. \nVery Effective!")
            
            #Not Very Effective
            
            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}. \n Not very effective.")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}.\n Not very effective.")
                
            elif self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}. \n Not very effective.")
            
            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}. \n Not very effective.")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}.\n Not very effective.")
                
            elif self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[10])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10]) - 1} damage from {self.player_stats[9]}. \n Not very effective.")
            
            else:        
            
                self.enemy_stats[1] = self.enemy_stats[1] - int(self.player_stats[10])

                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[10])} damage from {self.player_stats[9]}. \nEffective.")
                

        self.PLAYERO.setCurrentWidget(self.BOPTIONS)

        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 50:
            self.enemy_mid_health = True
        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 30:
            self.enemy_low_health = True
            
        if int(self.enemy_stats[1]) <= 0:
            self.Conclusion.setText(f"Player Wins !!!")
            self.enemy_defeated = True
            self.enemy_stats[1] = 0
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
            
            self.PLAYERO.setCurrentWidget(self.BOPTIONS)
        
        self.battle_loop()
    def move_three(self):
        self.Turn_Tracker.setText(f"Turn: {self.turn}")
        #Very Effective
        if self.enemy_stats[1] > 0 and self.player_stats[1] > 0:
            if self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) * 2} damage from {self.player_stats[13]}. \nVery Effective!")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) * 2} damage from {self.player_stats[13]}.\nVery Effective!")
                
            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) * 2)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) * 2} damage from {self.player_stats[13]}. \nVery Effective!")
            #Not Very Effective

            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}. \n Not very effective.")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}.\n Not very effective.")
                
            elif self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}. \n Not very effective.")     
            
            elif self.player_stats[0] == 'Totogaia' and self.enemy_stats[0] == 'Totogaia':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}. \n Not very effective.")
                
            elif self.player_stats[0] == 'Jormangandr' and self.enemy_stats[0] == 'Jormangandr':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}.\n Not very effective.")
                
            elif self.player_stats[0] == 'Blitzadile' and self.enemy_stats[0] == 'Blitzadile':
                self.enemy_stats[1] = self.enemy_stats[1] - ((int(self.player_stats[14])) - 1)
                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14]) - 1} damage from {self.player_stats[13]}. \n Not very effective.")
            
            else:        
            
                self.enemy_stats[1] = self.enemy_stats[1] - int(self.player_stats[14])

                self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
                self.CURRENT_EVENT_2.setText(f"Enemy took {int(self.player_stats[14])} damage from {self.player_stats[13]}. \nEffective.")
                

        self.PLAYERO.setCurrentWidget(self.BOPTIONS)

        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 50:
            self.enemy_mid_health = True
        if float((self.enemy_stats[1]) / (self.max_hp) * 100) < 30:
            self.enemy_low_health = True   
            
        if int(self.enemy_stats[1]) <= 0:
            #self.CURRENT_EVENT.setText(f"Player Wins")
            self.Conclusion.setText(f"Player Wins")
            self.enemy_defeated = True
            self.enemy_stats[1] = 0
            self.ENEMY_STATS.setText(f"ENEMY\nName: {self.enemy_stats[0]} \nHP: {self.enemy_stats[1]} / {self.max_hp}")
            
            self.PLAYERO.setCurrentWidget(self.BOPTIONS)
        
        self.battle_loop()
    def battle_loop(self):
        self.concluded = False
        
        
        if self.enemy_defeated == True:
            self.concluded = True
        
        if self.enemy_defeated == False:
            self.enemy_turn()
        
        if self.player_defeated == True:
            self.concluded = True
        
        self.turn = self.turn + 1
        
        self.HPBAR_ONE.setProperty("value", float(((self.player_stats[1]) / (self.max_hp2)) * 100))
        self.HPBAR_ONE_2.setProperty("value", float((self.enemy_stats[1]) / (self.max_hp) * 100))
        
        if self.player_mid_health == True:
            self.HPBAR_ONE.setStyleSheet("""
                QProgressBar {
                    border: 2px solid rgba(0, 0, 0, 1); 
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0.35);
                    color: black;
                }
                QProgressBar::chunk {
                    background-color: #FFB81C;
                }
            """)
        if self.player_low_health == True:
            self.HPBAR_ONE.setStyleSheet("""
                QProgressBar {
                    border: 2px solid rgba(0, 0, 0, 1); 
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0.35);
                    color: black;
                }
                QProgressBar::chunk {
                    background-color: #ff0000;
                }
            """)

        if self.enemy_mid_health == True:
            self.HPBAR_ONE_2.setStyleSheet("""
                QProgressBar {
                    border: 2px solid rgba(0, 0, 0, 1); 
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0.35);
                    color: black;
                }
                QProgressBar::chunk {
                    background-color: #FFB81C;
                }
            """)
        if self.enemy_low_health == True:
            self.HPBAR_ONE_2.setStyleSheet("""
                QProgressBar {
                    border: 2px solid rgba(0, 0, 0, 1); 
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0.35);
                    color: black;
                }
                QProgressBar::chunk {
                    background-color: #ff0000;
                }
            """)

    def Quit(self):
        self.Screens.setCurrentWidget(self.Pick)
        self.turn = 1
        self.CURRENT_EVENT.setText("")
        self.CURRENT_EVENT_2.setText("")
        self.HPBAR_ONE.setProperty("value", 100)
        self.HPBAR_ONE_2.setProperty("value", 100)
        self.Turn_Tracker.setText(f"Turn: {self.turn}")
        self.Conclusion.setText("")

