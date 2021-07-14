import json
import uuid
import random
import os
from utils.status import *
from utils.function import coordinateToMatrixPosition


class Game:

    def __init__(self):
        super().__init__()
        self.id = ''
        self.currentPlayer = ''
        self.initialPlayer = ''
        self.table = [['','',''], ['','',''], ['','','']]
        self.movements = []
        self.winner = ''

    def create(self):
        self.id = uuid.uuid4().hex
        self.initialPlayer = 'X' if random.randint(0, 100) % 2 == 0 else 'O'
        self.currentPlayer = self.initialPlayer
        self.save()

    def _toJson(self) -> dict:
        data = {

            "currentPlayer": self.currentPlayer,
            "initialPlayer": self.initialPlayer,
            "table": self.table,
            "movements": self.movements,
            "winner":self.winner
        }
        return data
    
    def _fromJson(self, json):
        self.currentPlayer = json['currentPlayer']
        self.initialPlayer = json['initialPlayer']
        self.movements = json['movements']
        self.table = json['table']
        self.winner = json['winner']
        

    def load(self, id):
        if os.path.isfile(os.path.join('data', f"{id}.json")):
            self.id = id
            with open(os.path.join('data', f"{id}.json")) as file:
                data = json.load(file)
                print(data)
                self._fromJson(data)
                return self

        else:
            return GameNotFound()

    def save(self):
        if not os.path.isfile(f"./data/{self.id}.json"):
            newFile = open(f"./data/{self.id}.json","x")
            newFile.write("")
            newFile.close()
        with open(f"./data/{self.id}.json","r+b") as f:
            f.truncate(0)
            f.seek(0)
            newData = self._toJson()
            jsonToWrite = str.encode(json.dumps(newData))
            f.write(jsonToWrite)
            f.close()

    def verify(self):
        if self.winner == '':
            winner = ''
            #linha 1
            if self.table[0][0] == self.table[0][1] == self.table[0][2]:
                winner = self.table[0][0]
            #linha 2
            elif self.table[1][0] == self.table[1][1] == self.table[1][2]:
                winner = self.table[1][0]
            #linha 3
            elif self.table[2][0] == self.table[2][1] == self.table[2][2]:
                winner = self.table[2][0]
            #coluna 1
            elif self.table[0][0] == self.table[1][0] == self.table[2][0]:
                winner = self.table[0][0]
            #coluna 2
            elif self.table[0][1] == self.table[1][1] == self.table[2][1]:
                winner = self.table[0][1]
            #coluna 3
            elif self.table[0][2] == self.table[1][2] == self.table[2][2]:
                winner = self.table[0][2]
            #Diagonal 1
            elif self.table[0][0] == self.table[1][1] == self.table[2][2]:
                winner = self.table[0][0]
            #Diagonal 2
            elif self.table[0][2] == self.table[1][1] == self.table[2][0]:
                winner = self.table[0][2]
            else:
                blank = 0
                for i in self.table:
                    for j in i: 
                        if j == '': blank+=1
                if blank == 0: 
                    winner = 'Draw'
            self.winner = winner
            self.save()
            return winner
        else: return self.winner

    def changePlayer(self):
        self.currentPlayer = 'O' if self.currentPlayer == 'X' else 'X'

    def movement(self, player:str, x:int, y:int) -> bool:
        linha, coluna = coordinateToMatrixPosition(x,y)
        print(linha, coluna)
        if self.table[linha][coluna] != "":
            return False
        self.table[linha][coluna] = player 
        self.changePlayer()
        self.save()
        return True