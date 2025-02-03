import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg='#fafafa')
        
        self.window.minsize(500, 600)
        self.window.geometry("500x600")
        self.window.eval('tk::PlaceWindow . center')
        
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        
        self.status_frame = tk.Frame(
            self.window,
            bg='#fafafa',
            pady=30
        )
        self.status_frame.grid(row=0, column=0, sticky="ew")
        
        self.title_label = tk.Label(
            self.status_frame,
            text="tic tac toe",
            font=('SF Pro Display', 32, 'normal'),
            bg='#fafafa',
            fg='#1d1d1f',
        )
        self.title_label.pack()
        
        self.turn_label = tk.Label(
            self.status_frame,
            text="player X's turn",
            font=('SF Pro Text', 16, 'normal'),
            bg='#fafafa',
            fg='#86868b',
            pady=10
        )
        self.turn_label.pack()
        
        self.board_frame = tk.Frame(
            self.window,
            bg='#ffffff',
            padx=30,
            pady=30,
            relief='solid',
            borderwidth=0
        )
        self.board_frame.grid(row=1, column=0, padx=40, pady=(0, 40), sticky="nsew")
        
        for i in range(3):
            self.board_frame.grid_rowconfigure(i, weight=1)
            self.board_frame.grid_columnconfigure(i, weight=1)
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=('SF Pro Display', 48, 'normal'),
                    width=2,
                    height=1,
                    bg='#ffffff',
                    fg='#000000',
                    relief='flat',
                    borderwidth=0,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=4, pady=4, sticky="nsew")
                
                if j < 2:  
                    separator = tk.Frame(self.board_frame, width=1, bg='#e5e5e5')
                    separator.grid(row=i, column=j, sticky='nse', pady=20)
                if i < 2:  
                    separator = tk.Frame(self.board_frame, height=1, bg='#e5e5e5')
                    separator.grid(row=i, column=j, sticky='sew', padx=20)
                
                self.buttons.append(button)
                
                button.bind('<Enter>', lambda e, btn=button: self.on_hover(btn, True))
                button.bind('<Leave>', lambda e, btn=button: self.on_hover(btn, False))
        
        self.reset_button = tk.Button(
            self.window,
            text="new game",
            font=('SF Pro Text', 16),
            bg='#000000',
            fg='#ffffff',
            relief='flat',
            command=self.reset_game,
            padx=30,
            pady=12,
            cursor='hand2'
        )
        self.reset_button.grid(row=2, column=0, pady=(0, 40))
        
        self.reset_button.bind('<Enter>', lambda e: self.reset_button.configure(bg='#1d1d1f'))
        self.reset_button.bind('<Leave>', lambda e: self.reset_button.configure(bg='#000000'))

    def on_hover(self, button, entering):
        if button['text'] == "" and self.game_active:
            button.configure(bg='#f5f5f7' if entering else '#ffffff')

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "" and self.game_active:
            self.board[index] = self.current_player
            
            color = '#007AFF' if self.current_player == 'X' else '#FF2D55'
            self.buttons[index].configure(
                text=self.current_player,
                fg=color,
                bg='#ffffff'
            )
            
            if self.check_winner():
                self.turn_label.configure(text=f"player {self.current_player} wins")
                self.game_active = False
            elif "" not in self.board:
                self.turn_label.configure(text="it's a tie")
                self.game_active = False
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.configure(text=f"player {self.current_player}'s turn")

    def check_winner(self):
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]  
        ]
        
        for line in lines:
            if (self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ""):
                for i in line:
                    self.buttons[i].configure(bg='#f5f5f7')
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.game_active = True
        self.turn_label.configure(text="player X's turn")
        
        for button in self.buttons:
            button.configure(
                text="",
                bg='#ffffff',
                fg='#000000'
            )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
