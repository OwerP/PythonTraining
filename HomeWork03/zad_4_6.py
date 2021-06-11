"""
Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.

Ma ona mieć metody:
`dodaj_element(x: int, y: int, rodzaj_elementu)`
W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"o"`. Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.

`stan_gry()`
Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).

`czyj_ruch()`
Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).

Wyświetlenie obiektu tej klasy ma wypisać planszę.

Użyj tej klasy do zrobienia gry w kółko i krzyżyk.
"""


class PlanszaXO:
    def __init__(self):
        self.x_o_status_board = [[None, None, None], [None, None, None], [None, None, None]]
        self.last_active = 'O'

    def state(self, mark):
        if self.x_o_status_board[0][0] == self.x_o_status_board[0][1] == self.x_o_status_board[0][
            2] == mark:  # horizontal 0
            return True
        elif self.x_o_status_board[1][0] == self.x_o_status_board[1][1] == self.x_o_status_board[1][
            2] == mark:  # horizontal 1
            return True
        elif self.x_o_status_board[2][0] == self.x_o_status_board[2][1] == self.x_o_status_board[2][
            2] == mark:  # horizontal 2
            return True
        elif self.x_o_status_board[0][0] == self.x_o_status_board[1][0] == self.x_o_status_board[2][
            0] == mark:  # vertical 0
            return True
        elif self.x_o_status_board[0][1] == self.x_o_status_board[1][1] == self.x_o_status_board[2][
            1] == mark:  # vertical 1
            return True
        elif self.x_o_status_board[0][2] == self.x_o_status_board[1][2] == self.x_o_status_board[2][
            2] == mark:  # vertical 2
            return True
        elif self.x_o_status_board[0][0] == self.x_o_status_board[1][1] == self.x_o_status_board[2][
            2] == mark:  # diagonal 0
            return True
        elif self.x_o_status_board[0][2] == self.x_o_status_board[1][1] == self.x_o_status_board[2][
            0] == mark:  # diagonal 1
            return True
        return False

    def stan_gry(self):
        if self.state('X'):
            print("wygrana 'X'")
            return 1  # win X
        elif self.state('O'):
            print("wygrana 'O'")
            return 1  # win O
        elif self.is_full():
            print("Koniec gry ale gra nie rozstrzygnięta ")
            return 1  # end of game - pat
        else:
            return 0  # game continues

    def czyj_ruch(self):
        if self.last_active == 'X':
            return 'O'
        else:
            return 'X'

    def dodaj_element(self, x: int, y: int, rodzaj_elementu):
        if rodzaj_elementu in ('X', 'O'):
            if x - 1 in range(0, 3) and y - 1 in range(0, 3) and self.item_is_empty(y - 1, x - 1):
                self.x_o_status_board[y - 1][x - 1] = str(rodzaj_elementu)
                self.last_active = str(rodzaj_elementu)
                return True
        return False

    def item_is_empty(self, x: int, y: int):
        if (self.x_o_status_board[x][y] is None):
            return True
        else:
            return False

    def is_empty(self):
        for row in self.x_o_status_board:
            if any(row):
                return False
        return True

    def is_full(self):
        for row in self.x_o_status_board:
            if not all(row):
                return False
        return True

    def make_a_move(self):
        tmp_marker = self.czyj_ruch()
        x, y = input(f" '{tmp_marker}' wybiera współrzędne x,y oddzielone przecinkiem np 1,2 ").split(',')
        while not self.dodaj_element(int(x), int(y), tmp_marker):
            x, y = input(
                f" '{tmp_marker}' wybiera poprawne współrzędne x,y oddzielone przecinkiem z przedziału 1-3 i wolnego obszaru ").split(',')


    def __str__(self):
        x_and_o_display_board = """
        ___________________
        :     :     :     :
        : 1,3 : 2,3 : 3,3 :
        :     :     :     :
        :-----------------:
        :     :     :     :
        : 1,2 : 2,2 : 3,2 :
        :     :     :     :
        :-----------------:
        :     :     :     :
        : 1,1 : 2,1 : 3,1 :
        :     :     :     :
        :-----------------:
        """
        if (not self.is_empty()):
            for y in range(0, 3):
                for x in range(0, 3):
                    str_tmp = str(x + 1) + ',' + str(y + 1)
                    if self.item_is_empty(y, x):
                        x_and_o_display_board = x_and_o_display_board.replace(str_tmp, '   ')
                    else:
                        x_and_o_display_board = x_and_o_display_board.replace(str_tmp,
                                                                              ' ' + self.x_o_status_board[y][x] + ' ')
        return (x_and_o_display_board)


print("witam w grze kółko i krzyżyk \nniżej sposób adresowania planszy")
x_o = PlanszaXO()
print(x_o)
while not x_o.stan_gry():
    x_o.make_a_move()
    print(x_o)
