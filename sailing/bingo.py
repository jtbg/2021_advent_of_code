import logging


class Board:
    def __init__(self, rows, board_id=0):
        self.board_id = board_id
        self.moves_to_win = 0
        self.playing_card = []
        self.parse_rows(rows)
        self.tracking = {
            "cols": [0, 0, 0, 0, 0],
            "rows": [0, 0, 0, 0, 0],
            "diags": [0, 0]
        }
        self.winning_score = 0

    def parse_rows(self, rows):
        for row in rows:
            for square in row.split():
                self.playing_card.append(int(square.strip()))
        logging.debug(f'''new board imported: {self.playing_card}''')

    def eval_number(self, called_number):
        self.moves_to_win += 1
        if called_number in self.playing_card:
            for pos, num in enumerate(self.playing_card):
                if num == called_number:
                    self.playing_card[pos] = 0
                    row, col = pos // 5, pos % 5
                    logging.debug(f'''board {self.board_id} matched {called_number} at r:{row} c:{col}''')
                    self.tracking['rows'][col] += 1
                    self.tracking['cols'][row] += 1
                    if row == col:
                        self.tracking["diags"][0] += 1
                    if row + col == 4:
                        self.tracking["diags"][1] += 1
        if 5 in self.tracking['cols'] or 5 in self.tracking['rows'] or 5 in self.tracking['diags']:
            self.winning_score = called_number * sum(self.playing_card)
            logging.info(f'''
                  Card {self.board_id} wins when {called_number} is called.
                  {self.playing_card}
                  ''')
            return self


class Game:
    def __init__(self):
        self.boards = []
        self.calls = []
        self.completed_calls = []
        self.boards_in_play = 0

    def bulk_import(self, bingo_loc="./assets/squid_bingo", bingo_calls_line=1):
        current_line = 1
        with open(bingo_loc, 'r') as f:
            rows = []
            for ln, line in enumerate(f):
                if ln == bingo_calls_line - 1:
                    self.calls = list(map(int, line.split(",")))
                    logging.debug(f'''bingo answer key imported from line {bingo_calls_line}''')
                elif line.strip():
                    rows.append(line.strip())
                if len(rows) == 5:
                    self.boards.append(Board(rows, board_id=self.boards_in_play))
                    self.boards_in_play += 1
                    rows = []
            logging.info(f'''bulk import complete, {self.boards_in_play} total boards in play''')

    def cheat(self):
        logging.warning(f'''A cheater is you''')
        for called_num in self.calls:
            self.completed_calls.append(called_num)
            for potential in self.boards:
                if potential.eval_number(called_num):
                    return potential
            logging.debug(f'''{called_num} called out, but no board wins''')
