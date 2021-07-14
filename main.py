from services.game import Game
from flask import Flask
import json
from flask import request, make_response, jsonify
from utils.status import *

app = Flask(__name__)


@app.route('/game', methods=['POST'])
def game():
    game = Game()
    game.create()
    return {"id": game.id, "first_player": game.initialPlayer}

@app.route('/game/<id>/movement', methods=['POST'])
def movement(id):
  game = Game().load(id)
  if isinstance(game, GameNotFound) :
    message = jsonify(msg="Partida não encontrada")
    response = make_response(message, 404)
    return response
  else:
    verify = game.verify()
    if(verify==''):
      data = json.loads(request.data)
      print(data)
      if data['player'].upper() != game.currentPlayer:
        message = jsonify(msg="Não é turno do jogador")
        response = make_response(message, 400)
        return response
      valid = game.movement(data['player'].upper(), data['position']['x'], data['position']['y'])
      if(valid):
        message = jsonify(msg="Movimento Concluido")
        response = make_response(message, 400)
        return response
      else:
        message = jsonify(msg="Movimento inválido")
        response = make_response(message, 400)
        return response
    elif verify == 'Draw':
      message = jsonify(status="Partida finalizada", winner=verify)
      response = make_response(message, 400)
      return response
    else:
      message = jsonify(status="Partida finalizada", winner=game.winner)
      response = make_response(message, 400)
      return response

if __name__ == '__main__':
    app.run(debug=False)
