from Settings import Settings
from sys import stderr, stdin, stdout

class PlayerState:
    def __init__(self):
        self.row_points = 0;
        self.combo = 0;
        self.field = ""

    def parsePlayerState(self, parts):
        playerStateMessage = parts[0].lower()

        if playerStateMessage == 'row_points':
            #update b row_points i	-> The amount of row points the given player has scored so far
            self.row_points = int(parts[1].lower());

            pass
        elif playerStateMessage == 'combo':
            #update b combo i	-> The height of the current combo for the given player
            self.combo = int(parts[1].lower())

            pass
        elif playerStateMessage == 'field':
             #update b field [[c,...];...]	-> The complete playing field of the given player
            self.field = parts[1].lower()
            pass
        else:
            stderr.write('Unknown player state: %s\n' % (playerStateMessage))
            stderr.flush()



class GameState:

    #update game round i	-> The number of the current round
    #update game this_piece_type s	-> The type of the piece that has just spawned on the field
    #update game next_piece_type s	-> The type of the piece that will spawn the next round
    #update game this_piece_position i,i	-> The starting position in the field for the current piece (top left corner of the piece bounding box)

    def __init__(self):
        self.round = 0
        self.this_piece_type = 'n'
        self.next_piece_type = 'n'
        self.this_piece_position = {"x":1 , "y":2}
        self.players = {"me":PlayerState(), "opponent":PlayerState()}
        self.settings = Settings()

    def parseSettingsMessage(self, parts):
        self.settings.parseSetting(parts)

    def parseGameMessage(self, parts):
        if parts[0] == "game":
            gameStateMessage = parts[1]

            if gameStateMessage== 'round':
                #update game round i
                self.round = int(parts[2])
                pass
            elif gameStateMessage == 'this_piece_type':
                #update game this_piece_type s
                self.this_piece_type = parts[2]
                pass
            elif gameStateMessage == 'next_piece_type':
                #update game next_piece_type s
                self.next_piece_type = parts[2]
                pass
            elif gameStateMessage == 'this_piece_position':
                #update game this_piece_position i,i
                position = parts[2].split(',')
                self.this_piece_position["x"] = int(position[0])
                self.this_piece_position["y"] = int(position[1])
                pass
            else:
                stderr.write('Unknown gameStateMessage: %s\n' % (parts[1]))
                stderr.flush()

        elif parts[0] == self.settings.bots["me"]:
            self.players["me"].parsePlayerState(parts[1:])
            pass
        elif parts[0] == self.settings.bots["opponent"]:
            self.players["opponent"].parsePlayerState(parts[1:])
            pass
        else:
            stderr.write('Unknown gameStateMessage: %s\n' % (parts[0]))
            stderr.flush()