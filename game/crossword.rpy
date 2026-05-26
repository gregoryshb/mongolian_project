init python:

    import random
    import time
    from operator import itemgetter
    from collections import defaultdict

    class Crossword_words:
        
        def __init__ (self, rows, cols, empty = ' ', available_words = []):

            self.rows = rows
            self.cols = cols
            self.empty = empty
            self.available_words = available_words
            self.let_coords = defaultdict(list)
            self.original_words = available_words.copy()

        def grid_words(self):

            self.current_wordlist = []
            self.let_coords.clear()
            self.grid = [[self.empty]*self.cols for i in range(self.rows)]
            if self.available_words:
                self.first_word(self.available_words[0])

        def compute_crossword(self, time_permitted = 5.0):

            self.best_wordlist = []
            wordlist_length = len(self.available_words)
            time_permitted = float(time_permitted)
            start_full = float(time.time())

            while (float(time.time()) - start_full) < time_permitted:

                self.grid_words()
                for word in self.available_words:
                    
                    if word[0] not in [w[0] for w in self.current_wordlist]:
                        
                        self.add_everything(word)

                if len(self.current_wordlist) > len(self.best_wordlist):

                    self.best_wordlist = list(self.current_wordlist)
                    self.best_grid = [row[:] for row in self.grid]

                if len(self.best_wordlist) == wordlist_length:
                    break
            
            return self.best_grid, self.best_wordlist

        def get_coords(self, word):

            word_text = word[0]
            word_length = len(word_text)
            coords = []

            for let, letter in enumerate(word_text):
                if letter in self.let_coords:
                    for row_c, col_c, vert_c in self.let_coords[letter]:
                        if vert_c:
                            if col_c - let >= 0 and (col_c - let) + word_length <= self.cols:
                                row, col = row_c, col_c - let
                                score = self.check_hor(word, row, col, word_length)

                                if score:
                                    coords.append([row, col, 0, score])
                        else:
                            if row_c - let >= 0 and (row_c - let) + word_length <= self.rows:
                                row, col = row_c - let, col_c
                                score = self.check_vert(word, row, col, word_length)

                                if score:
                                    coords.append([row, col, 1, score])
            
            if coords:
                return max(coords, key = itemgetter(3))
            
            return None
        
        def first_word(self, word):

            v = random.choice([True, False])

            if v:
                row = random.randrange(0, self.rows - len(word[0]))
                col = random.randrange(0, self.cols)

            else:
                row = random.randrange(0, self.rows)
                col = random.randrange(0, self.cols - len(word[0]))

            # word_obj = [word, None]
            self.place_word(word, row, col, v)
            #self.set_word(word_obj, row, col, v)

        def add_everything(self, word):

            coords = self.get_coords(word)
            if not coords:
                return False

            row, col, vert, score = coords
            self.place_word(word, row, col, vert)
            return True

        def check_hor(self, word, row, col, word_length, score = 1):
            word_text = word[0]

            if col > 0 and self.cell_occupied(row, col - 1):
                return 0

            for i, l in enumerate(word_text):
                current_col = col + i
                active_cell = self.grid[row][current_col]

                if active_cell == self.empty:
                    if row + 1 < self.rows and self.cell_occupied(row + 1, current_col):
                        return 0

                elif active_cell == l:
                    score += 1

                else:
                    return 0

            return score

        def check_vert(self, word, row, col, word_length, score=1):
            word_text = word[0]

            if row > 0 and self.cell_occupied(row - 1, col):
                return 0

            for i, l in enumerate(word_text):
                current_row = row + i
                active_cell = self.grid[current_row][col]

                if active_cell == self.empty:
                    if col + 1 < self.cols and self.cell_occupied(current_row, col + 1):
                        return 0
                
                    if col - 1 >= 0 and self.cell_occupied(current_row, col - 1):
                        return 0

                elif active_cell == l:
                    score += 1

                else:
                    return 0

            return score

        def place_word(self, word, row, col, vert):
            word_text = word[0]
            # word.append(row)  # Добавляем координаты в список слова
            # word.append(col)
            # word.append(vert)
            self.current_wordlist.append([word[0], word[1], row, col, vert])

            for i, let in enumerate(word_text):
                if vert:
                    fin_row = row + i
                    fin_col = col
                else:
                    fin_row = row
                    fin_col = col + i

                self.grid[fin_row][fin_col] = let

                self.let_coords[let].append((fin_row, fin_col, not vert))
        
        def cell_occupied(self, row, col):
            
            if 0 <= row < self.rows and 0 <= col < self.cols:
                return self.grid[row][col] != self.empty
            
            return False

    

    class Crossword_shape:

        def __init__(self, rows = 20, cols = 20):
            self.rows = rows
            self.cols = cols
            self.gen = None
            self.correct_grid = None
            self.player_grid = None
            self.words = []

            self.selected_row = 0
            self.selected_col = 0
            self.direction = 0

            self.find_first_letter()

        def find_first_letter(self):

            if not self.correct_grid: 
                return
            #found False

            for i in range(self.rows):
                for q in range(self.cols):
                    if self.correct_grid[i][q] != ' ':
                        self.selected_row = i
                        self.selected_col = q
                        return
                        #found = True
                        #break
                
                #if found:
                    #break

        def create_new(self, wordlist, time_permitted = 5.0):

            self.gen = Crossword_words(self.rows, self.cols, ' ', wordlist)
            self.correct_grid, self.words = self.gen.compute_crossword(time_permitted)
            self.player_grid = [['' if cell != '' else None for cell in row] for row in self.correct_grid]
            self.find_first_letter()

        def moves(self, d_row, d_col):

            new_row = self.selected_row + d_row
            new_col = self.selected_col + d_col

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.correct_grid[new_row][new_col] != ' ':
                    self.selected_row = new_row
                    self.selected_col = new_col
                    return True

            return False

        def backspace(self):

            row, col = self.selected_row, self.selected_col
            
            if not self.player_grid[row][col]:
                if self.direction == 0:
                    self.moves(0, -1)
                else:
                    self.moves(-1, 0) 

                row, col = self.selected_row, self.selected_col

            if self.player_grid[row][col]:

                self.player_grid[row][col] = ' '

        def input_letter(self, let):

            if self.place_letter(self.selected_row, self.selected_col, let):
                if self.direction == 0:
                    self.moves(0, 1)
                else:
                    self.moves(1, 0)
                return True
            
            return False

        def change_direction(self):

            self.direction = 1 - self.direction

        def place_letter(self, row, col, let):

            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.correct_grid[row][col] != ' ':
                    self.correct_grid[row][col] = let.upper()
                    return True

                return False
            
        def check_cell(self, row, col):

            if self.player_grid[row][col] and self.correct_grid[row][col] != ' ':
                self.player_grid[row][col] == self.correct_grid[row][col]
            
            return False

        def check_word(self, text):

            for data in self.words:
                if data[0] == text:
                    if len(data) > 5:
                        row, col, vert = data[2], data[3], data[4]
                        for i, let in enumerate(text):
                            r = row + (i if vert else 0)
                            c = col + (i if not vert else 0)
                            if self.player_grid[r][c] != let:
                                return False
                    
                    return True
                
            return False

        def active_word_info(self): #это должно проверять к какому слову относится клеточка и направление и понимать собственно само слово и его объянение

            for i, data in enumerate(self.words):
                text, clue, w_row, w_col, w_vert = data
                length = len(text)

                if w_vert == (self.direction == 1):

                    if w_vert:
                        
                        if self.selected_col == w_col and w_row <= self.selected_row < w_row + length:
                            return i + 1, text, clue
                    else:

                        if self.selected_row == w_row and w_col <= self.selected_col < w_col + length:
                            return i + 1, text, clue
                    
            return None, '', ''

        def is_in_active_word(self, row, col): #а это должно подсвечивать какие клеточки относятся к тому-то слову
            
            idx, text, clue = self.active_word_info()
            if not idx:
                return False

            data = self.words[idx - 1]
            w_row, w_col, w_vert = data[2], data[3], data[4]
            length = len(text)

            if w_vert:
                return col == w_col and w_row <= row <= w_row + length
            
            else:
                return row == w_row and w_col <= col <= w_row + length



            