

from sys import stderr, stdin, stdout
from GameState import GameState


class Bot(object):

    '''
    settings [type] [value] given only at the start of the game. General settings of the game are given here.
    action [type] [time] indicates a request for an action.
    update [player] [type] [value] this is an update of the game state. [player] indicates what bot the update is about, but could also be 'game' to indicate a general update.


    Output from engine	Description
    settings timebank t	 -> Maximum time in milliseconds that your bot can have in its time bank
    settings time_per_move t -> Time in milliseconds that is added to your bot's time bank each move
    settings player_names [b,...] -> A list of all player names in this match, including your bot's name
    settings your_bot b	-> The name of your bot for this match
    settings field_width i	-> The width of the field, i.e. number of row-cells
    settings field_height i	-> The height of the field, i.e. number of column-cells
    update game round i	-> The number of the current round
    update game this_piece_type s	-> The type of the piece that has just spawned on the field
    update game next_piece_type s	-> The type of the piece that will spawn the next round
    update game this_piece_position i,i	-> The starting position in the field for the current piece (top left corner of the piece bounding box)
    update b row_points i	-> The amount of row points the given player has scored so far
    update b combo i	-> The height of the current combo for the given player
    update b field [[c,...];...]	-> The complete playing field of the given player
    action moves t	->Request for the whole set of moves for this round

    Output from bot	Description
    [m,...]	A list of moves separated by comma's

    '''
    def __init__(self):
        '''
        Bot constructor

        Add data that needs to be persisted between rounds here.
        '''
        self.game_state = GameState()



    def run(self):
        '''
        Main loop

        Keeps running while begin fed data from stdin.
        Writes output to stdout, remember to flush.
        '''
        while not stdin.closed:
            try:
                rawline = stdin.readline()

                # End of file check
                if len(rawline) == 0:
                    break

                line = rawline.strip()

                # Empty lines can be ignored
                if len(line) == 0:
                    continue

                parts = line.split()
                command = parts[0].lower()

                if command == 'settings':
                    self.game_state.parseSettingsMessage(parts[1:])
                    pass
                elif command == 'update':
                    self.game_state.parseGameMessage(parts[1:])
                    pass

                elif command == 'action':
                    stdout.write('drop \n')
                    stdout.flush()
                    pass
                else:
                    stderr.write('Unknown command: %s\n' % (command))
                    stderr.flush()
            except EOFError:
                return


if __name__ == '__main__':
    '''
    Not used as module, so run
    '''
    Bot().run()