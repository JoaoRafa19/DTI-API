# API JOGO DA VELHA


*API para processo seletivo*

Api de jogo-da-velha escrita em python utilizando o framework Flask
com permanência de dados paseada em arquivos.

## Endpoints

 - ```[POST] - /game```

    - ### Método:  POST
    #
    - ### Body:  Vazio
    #
    - ### Descrição: 
      
      Cria um Jogo e salva em um arquivo. Retorna o id do jogo criado e o primeiro jogador que deve jogar (O ou X), sorteado aleatoriamente 
    #
    - ### Retorno : 
      ```
      {
        "first_player": "X",
        "id": "1a3d0805d7d9465a89d4d1311aa2e3d2"
      }
      ```
  

  - ```[POST] - /game/<id>/movement``` 
    - ### Método:  POST
    #
    - ### Body:  
        - "id" : id da partida
        - "player": Jogador (X ou O )
         *Deve ser a vez do jogador*
        - "position" : deve conter as coordenadas da posição que o jogador deseja jogar (coordenadas dever ser entre 0 e 2 inclusive)
        ```
        {
          "id": "1a3d0805d7d9465a89d4d1311aa2e3d2",
          "player": "x",
          "position": {
            "x": 2,
            "y": 0
          }
        }
        ```

    #
    - ### Descrição: 
      
      Altera o proximo jogador, verifica o status do jogo e grava a jogada se for válida
    #
    - ### Retorno : 
        - caso a jogada seja bem sucedida 
            ```
              {
                "msg": "Movimento Concluido"
              }
            ```
        - caso não seja a vez do jogador
            ```
            {
              "msg": "Não é turno do jogador"
            }
            ```
        - caso o movimento seja inválido
            ```
            {
              "msg": "Movimento inválido"
            }
            ```
        - caso o jogo não seja encontrado

            ```
            {
              "msg": "Partida não encontrada"
            }
            ```
        - caso o jogo solicitado ja tenha chegado ao fim
          ```
          {
            "status": "Partida finalizada",
            "winner": "Draw"
          }
          ```
## Build

Instruções de Build

### Windows
- Requisitos
  - Python 3.8 
- Certifique-se de ter o python instalado no doretório do projeto ou adicionado as variáveis de ambiente
- Clona ou faça download do repositório
- Abra o terminal na pasta que foi clonada/baixada
- Digite  : 
  
  para instalar as dependencias
 
  ```{r cars, class.source='klippy'} klippy::klippy()
  pip install -r requirements.txt 
  ```
  para rodar o projeto

  ```
  python main.py
  ```
