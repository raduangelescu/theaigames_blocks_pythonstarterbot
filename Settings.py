from sys import stderr, stdin, stdout

class Settings:

    def __init__(self):
        self.timebank = 0       #Maximum time in milliseconds that your bot can have in its time bank
        self.time_per_move = 0  #Time in milliseconds that is added to your bot's time bank each move
        self.bots = {
            'me': {},
            'opponent': {}
        }
        self.field_width = 0 #The width of the field, i.e. number of row-cells
        self.field_height = 0 #The height of the field, i.e. number of column-cells

    def parseSetting(self, parts):
        setting = parts[0].lower()

        if setting== 'timebank':
            #settings timebank t	(miliseconds)
            self.timebank = int(parts[1])
            pass
        elif setting == 'time_per_move':
            #settings time_per_move t (miliseconds)
            self.time_per_move = int(parts[1])
            pass
        elif setting == 'player_names':
            #settings player_names [b,...]
            players = parts[1].split(',')
            self.bots["me"] = players[0]
            self.bots["opponent"] = players[1]
            pass
        elif setting == 'your_bot':
            #settings your_bot b
            if self.bots["me"] == parts[1]:
                return
            else:
                self.bots["opponent"] = self.bots["me"]
                self.bots["me"] = parts[1]
            pass
        elif setting =='field_width':
            # settings field_width i
            self.field_width = int(parts[1])
            pass
        elif setting == 'field_height':
            # settings field_height i
            self.field_height = int(parts[1])
            pass
        else:
            stderr.write('Unknown setting: %s\n' % (setting))
            stderr.flush()
