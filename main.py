class Game:
    def __init__(self):
        self.width = 7
        self.height = 6
        self.field = []
        self.num_players = 2
        for i in range(self.height):
            self.field.append([0] * self.width)
        self.conditions = [
            {"h_start": 0, "h_end": self.height, "w_start": 0, "w_end": self.width - 3,
             "stepper": lambda i, j, k: (i, j + k)},
            {"h_start": 0, "h_end": self.height - 3, "w_start": 0, "w_end": self.width,
             "stepper": lambda i, j, k: (i + k, j)},
            {"h_start": 0, "h_end": self.height - 3, "w_start": 0, "w_end": self.width - 3,
             "stepper": lambda i, j, k: (i + k, j + k)},
            {"h_start": 0, "h_end": self.height, "w_start": 0, "w_end": self.width - 3,
             "stepper": lambda i, j, k: (i - k, j + k)},
            {"h_start": 3, "h_end": self.height, "w_start": 3, "w_end": self.width,
             "stepper": lambda i, j, k: (i - k, j - k)},
            {"h_start": 0, "h_end": self.height - 3, "w_start": 3, "w_end": self.width,
             "stepper": lambda i, j, k: (i + k, j - k)},
        ]

    def _check_one_direction(self, conditions, player):
        for i in range(conditions["h_start"], conditions["h_end"]):
            for j in range(conditions["w_start"], conditions["w_end"]):
                if self.field[i][j] == player:
                    count = 1
                    for k in range(1, 4):
                        step_h, step_w = conditions["stepper"](i, j, k)
                        if self.field[step_h][step_w] != player:
                            break
                        else:
                            count += 1
                    if count == 4:
                        return True

    def player_won(self, player):
        for cond in self.conditions:
            res = self._check_one_direction(cond, player)
            if res:
                return res
        return False

    def make_move(self, player, column):
        made_move = False
        for i in range(self.height - 1, -1, -1):
            if self.field[i][column] == 0:
                self.field[i][column] = player
                made_move = True
                break
        return made_move

    def print_field(self):
        for i in range(self.height):
            print(" ".join([str(val) for val in self.field[i]]))


if __name__ == "__main__":
    game = Game()
    has_winner = False
    while not has_winner:
        for i in range(1, game.num_players + 1):
            game.print_field()
            print("Player {}, make your move - print number from 1 to {} - column number.".format(i, game.width))
            success = False
            while not success:
                try:
                    col_num = int(input()) - 1
                except ValueError:
                    print("Player {}, please provide correct number".format(i))
                else:
                    if col_num < 0 or col_num >= game.width:
                        print("Player {}, please provide correct number".format(i))
                    else:
                        success = True
            success = game.make_move(i, col_num)
            while not success:
                print("Player {}, please make another step - the column i filled")
                col_num = int(input()) - 1
                success = game.make_move(i, col_num)
            if game.player_won(i):
                has_winner = True
                print("Player {}, you won!".format(i))
                game.print_field()
                exit(0)
