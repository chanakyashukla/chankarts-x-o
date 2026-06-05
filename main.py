import os
from pathlib import Path
from dataclasses import dataclass, field


def configure_tk_runtime() -> None:
    # Some Windows Python bundles need an explicit Tcl/Tk path for Tkinter.
    python_home = Path(os.__file__).resolve().parent.parent
    os.environ.setdefault("TCL_LIBRARY", str(python_home / "tcl" / "tcl8.6"))
    os.environ.setdefault("TK_LIBRARY", str(python_home / "tcl" / "tk8.6"))


configure_tk_runtime()

import tkinter as tk


BOARD_SIZE = 3
WIN_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


@dataclass
class TicTacToeState:
    board: list[str] = field(default_factory=lambda: [""] * 9)
    current_player: str = "X"
    winner: str | None = None
    winning_combo: tuple[int, int, int] | None = None
    is_draw: bool = False
    scores: dict[str, int] = field(
        default_factory=lambda: {"X": 0, "O": 0, "Draws": 0}
    )

    def make_move(self, index: int) -> bool:
        if self.winner or self.is_draw or self.board[index]:
            return False

        self.board[index] = self.current_player

        for combo in WIN_COMBINATIONS:
            a, b, c = combo
            marker = self.board[a]
            if marker and marker == self.board[b] == self.board[c]:
                self.winner = marker
                self.winning_combo = combo
                self.scores[marker] += 1
                return True

        if all(self.board):
            self.is_draw = True
            self.scores["Draws"] += 1
            return True

        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def reset_board(self) -> None:
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None
        self.winning_combo = None
        self.is_draw = False

    def reset_scores(self) -> None:
        self.scores = {"X": 0, "O": 0, "Draws": 0}

    @property
    def status_text(self) -> str:
        if self.winner:
            return f"Player {self.winner} Wins!"
        if self.is_draw:
            return "It's a Draw!"
        return f"Player {self.current_player}'s Turn"


class ChankArtsXOApp:
    BG = "#101418"
    SURFACE = "#171d24"
    PANEL = "#1d2630"
    CELL_BG = "#212c38"
    CELL_HOVER = "#2a3746"
    TEXT = "#edf2f7"
    MUTED = "#93a1b2"
    ACCENT = "#f2c94c"
    X_COLOR = "#ff6b6b"
    O_COLOR = "#59c3ff"
    WIN_BG = "#334a2f"
    WIN_BORDER = "#9be564"
    BUTTON_BG = "#273240"
    BUTTON_HOVER = "#344355"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.state = TicTacToeState()
        self.cells: list[tk.Button] = []
        self.score_labels: dict[str, tk.Label] = {}

        self.root.title("ChankArts X & O")
        self.root.geometry("500x650")
        self.root.minsize(420, 560)
        self.root.configure(bg=self.BG)

        self._build_ui()
        self._refresh_ui()
        self.root.after(10, self._center_window)

    def _build_ui(self) -> None:
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        container = tk.Frame(self.root, bg=self.BG, padx=28, pady=24)
        container.grid(sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(3, weight=1)

        title = tk.Label(
            container,
            text="ChankArts X & O",
            bg=self.BG,
            fg=self.TEXT,
            font=("Segoe UI Semibold", 24),
        )
        title.grid(row=0, column=0, sticky="n", pady=(0, 12))

        self.status_label = tk.Label(
            container,
            text="",
            bg=self.BG,
            fg=self.MUTED,
            font=("Segoe UI", 14),
        )
        self.status_label.grid(row=1, column=0, pady=(0, 18))

        score_frame = tk.Frame(
            container,
            bg=self.SURFACE,
            highlightthickness=1,
            highlightbackground="#25313d",
            padx=14,
            pady=14,
        )
        score_frame.grid(row=2, column=0, sticky="ew", pady=(0, 18))
        for column in range(3):
            score_frame.grid_columnconfigure(column, weight=1)

        self._create_score_card(score_frame, 0, "X Wins", "X", self.X_COLOR)
        self._create_score_card(score_frame, 1, "O Wins", "O", self.O_COLOR)
        self._create_score_card(score_frame, 2, "Draws", "Draws", self.ACCENT)

        board_frame = tk.Frame(
            container,
            bg=self.SURFACE,
            highlightthickness=1,
            highlightbackground="#25313d",
            padx=14,
            pady=14,
        )
        board_frame.grid(row=3, column=0, sticky="nsew")
        for row in range(BOARD_SIZE):
            board_frame.grid_rowconfigure(row, weight=1, uniform="board")
            board_frame.grid_columnconfigure(row, weight=1, uniform="board")

        for index in range(9):
            row, col = divmod(index, BOARD_SIZE)
            button = tk.Button(
                board_frame,
                text="",
                font=("Segoe UI Black", 34),
                bg=self.CELL_BG,
                fg=self.TEXT,
                activebackground=self.CELL_HOVER,
                activeforeground=self.TEXT,
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda idx=index: self._handle_move(idx),
            )
            button.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            button.bind("<Enter>", lambda event, idx=index: self._on_cell_hover(idx, True))
            button.bind("<Leave>", lambda event, idx=index: self._on_cell_hover(idx, False))
            self.cells.append(button)

        controls = tk.Frame(container, bg=self.BG)
        controls.grid(row=4, column=0, sticky="ew", pady=(18, 0))
        controls.grid_columnconfigure(0, weight=1)
        controls.grid_columnconfigure(1, weight=1)

        self.new_game_button = self._create_action_button(
            controls, "New Game", self._new_game
        )
        self.new_game_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        self.reset_score_button = self._create_action_button(
            controls, "Reset Score", self._reset_score
        )
        self.reset_score_button.grid(row=0, column=1, sticky="ew", padx=(8, 0))

    def _create_score_card(
        self, parent: tk.Frame, column: int, title: str, key: str, color: str
    ) -> None:
        card = tk.Frame(parent, bg=self.PANEL, padx=10, pady=10)
        card.grid(row=0, column=column, sticky="ew", padx=6)
        label = tk.Label(
            card,
            text=title,
            bg=self.PANEL,
            fg=self.MUTED,
            font=("Segoe UI Semibold", 11),
        )
        label.pack()
        value = tk.Label(
            card,
            text="0",
            bg=self.PANEL,
            fg=color,
            font=("Segoe UI Black", 22),
        )
        value.pack(pady=(6, 0))
        self.score_labels[key] = value

    def _create_action_button(
        self, parent: tk.Frame, text: str, command
    ) -> tk.Button:
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI Semibold", 12),
            bg=self.BUTTON_BG,
            fg=self.TEXT,
            activebackground=self.BUTTON_HOVER,
            activeforeground=self.TEXT,
            relief="flat",
            bd=0,
            padx=12,
            pady=14,
            cursor="hand2",
        )
        button.bind(
            "<Enter>", lambda event, widget=button: widget.configure(bg=self.BUTTON_HOVER)
        )
        button.bind(
            "<Leave>", lambda event, widget=button: widget.configure(bg=self.BUTTON_BG)
        )
        return button

    def _handle_move(self, index: int) -> None:
        if self.state.make_move(index):
            self._refresh_ui()

    def _new_game(self) -> None:
        self.state.reset_board()
        self._refresh_ui()

    def _reset_score(self) -> None:
        self.state.reset_scores()
        self.state.reset_board()
        self._refresh_ui()

    def _on_cell_hover(self, index: int, is_hovered: bool) -> None:
        if self.state.board[index] or self.state.winner or self.state.is_draw:
            return
        color = self.CELL_HOVER if is_hovered else self.CELL_BG
        self.cells[index].configure(bg=color)

    def _refresh_ui(self) -> None:
        self.status_label.configure(text=self.state.status_text)
        if self.state.winner:
            self.status_label.configure(fg=self.ACCENT)
        elif self.state.is_draw:
            self.status_label.configure(fg="#f7b267")
        else:
            self.status_label.configure(fg=self.MUTED)

        for key, label in self.score_labels.items():
            label.configure(text=str(self.state.scores[key]))

        game_over = self.state.winner is not None or self.state.is_draw
        winning_cells = set(self.state.winning_combo or ())

        for index, button in enumerate(self.cells):
            marker = self.state.board[index]
            is_winner = index in winning_cells

            background = self.WIN_BG if is_winner else self.CELL_BG
            foreground = self.TEXT
            if marker == "X":
                foreground = self.X_COLOR
            elif marker == "O":
                foreground = self.O_COLOR

            button.configure(
                text=marker,
                fg=foreground,
                bg=background,
                activebackground=background if marker else self.CELL_HOVER,
                state="disabled" if game_over or marker else "normal",
                disabledforeground=foreground,
                highlightthickness=2 if is_winner else 0,
                highlightbackground=self.WIN_BORDER if is_winner else background,
                highlightcolor=self.WIN_BORDER if is_winner else background,
            )

    def _center_window(self) -> None:
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() - width) // 2
        y = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f"{width}x{height}+{max(0, x)}+{max(0, y)}")

def main() -> None:
    root = tk.Tk()
    app = ChankArtsXOApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
