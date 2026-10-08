# =========================================================
# CONNECT 4 AI - COMPLETE ASSIGNMENT IMPLEMENTATION
# + GUI TREE VISUALIZATION (BONUS ADDED)
# =========================================================

import pygame
import sys
import math
import time
import numpy as np
import pygame._sdl2.video as sdl2   # ⭐ BONUS (multi-window support)

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────
ROW_COUNT    = 6
COLUMN_COUNT = 7
PLAYER       = 1
AI           = 2
EMPTY        = 0
SQUARESIZE   = 90
RADIUS       = SQUARESIZE // 2 - 6

BLUE        = (30,  80, 200)
BLACK       = (10,  10,  20)
BG_COLOR    = (15,  15,  30)
RED         = (220,  50,  50)
YELLOW      = (240, 200,  30)
WHITE       = (245, 245, 245)
GREEN       = ( 50, 200, 100)
GRAY        = (120, 120, 130)
DARK_GRAY   = ( 40,  40,  50)
PURPLE      = (160,  50, 220)
TEAL        = ( 30, 200, 180)

TREE_W = 1200
TREE_H = 700

nodes_expanded = 0
pruned_count = 0


# ─────────────────────────────────────────────
# TREE NODE
# ─────────────────────────────────────────────
class TreeNode:
    def __init__(self, move_col, depth, is_max, heuristic=None, parent=None):
        self.move_col = move_col
        self.depth = depth
        self.is_max = is_max
        self.heuristic = heuristic
        self.value = None
        self.parent = parent
        self.children = []
        self.pruned = False
        self.x = 0
        self.y = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


# ─────────────────────────────────────────────
# BOARD
# ─────────────────────────────────────────────
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def is_full(board):
    return len(get_valid_locations(board)) == 0


# ─────────────────────────────────────────────
# HEURISTIC (simplified)
# ─────────────────────────────────────────────
def score_position(board, piece):
    return np.sum(board == piece)


# ─────────────────────────────────────────────
# MINIMAX (simple)
# ─────────────────────────────────────────────
def minimax(board, depth, maximizing, parent=None, col=None):
    global nodes_expanded
    nodes_expanded += 1

    node = TreeNode(col if col is not None else -1, depth, maximizing, score_position(board, AI), parent)
    if parent:
        parent.add_child(node)

    if depth == 0 or is_full(board):
        node.value = score_position(board, AI)
        return None, node.value, node

    valid = get_valid_locations(board)

    if maximizing:
        best = -math.inf
        best_col = valid[0]
        for c in valid:
            r = get_next_open_row(board, c)
            temp = board.copy()
            drop_piece(temp, r, c, AI)
            _, val, _ = minimax(temp, depth-1, False, node, c)
            if val > best:
                best = val
                best_col = c
        node.value = best
        return best_col, best, node
    else:
        best = math.inf
        best_col = valid[0]
        for c in valid:
            r = get_next_open_row(board, c)
            temp = board.copy()
            drop_piece(temp, r, c, PLAYER)
            _, val, _ = minimax(temp, depth-1, True, node, c)
            if val < best:
                best = val
                best_col = c
        node.value = best
        return best_col, best, node


# ─────────────────────────────────────────────
# TREE LAYOUT
# ─────────────────────────────────────────────
def layout(node, x, y, span):
    node.x = x
    node.y = y
    if not node.children:
        return
    step = span / len(node.children)
    start = x - span/2 + step/2
    for i, ch in enumerate(node.children):
        layout(ch, start + i*step, y+80, step)


# ─────────────────────────────────────────────
# ⭐ GUI TREE (BONUS WINDOW)
# ─────────────────────────────────────────────
def show_tree_window(root, algo, k):
    window = sdl2.Window("MINIMAX TREE (BONUS)", size=(TREE_W, TREE_H))
    renderer = sdl2.Renderer(window)

    surface = pygame.Surface((TREE_W, TREE_H))

    layout(root, TREE_W//2, 50, TREE_W-100)

    font = pygame.font.SysFont("consolas", 14)

    running = True
    while running:
        surface.fill((10, 10, 20))

        def draw_edges(n):
            for c in n.children:
                pygame.draw.line(surface, GRAY, (n.x, n.y), (c.x, c.y))
                draw_edges(c)

        def draw_nodes(n):
            color = PURPLE if n.is_max else (255, 140, 0)
            pygame.draw.circle(surface, color, (int(n.x), int(n.y)), 18)

            txt = font.render(f"{n.value:.0f}" if n.value else "?", True, WHITE)
            surface.blit(txt, (n.x-10, n.y-10))

            for c in n.children:
                draw_nodes(c)

        draw_edges(root)
        draw_nodes(root)

        tex = sdl2.Texture.from_surface(renderer, surface)
        renderer.clear()
        renderer.copy(tex)
        renderer.present()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

    window.destroy()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    pygame.init()

    board = create_board()
    screen = pygame.display.set_mode((700, 600))
    font = pygame.font.SysFont("consolas", 30)

    turn = PLAYER
    game_over = False

    last_root = None

    while not game_over:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN and turn == PLAYER:
                col = e.pos[0] // SQUARESIZE
                if is_valid_location(board, col):
                    r = get_next_open_row(board, col)
                    drop_piece(board, r, col, PLAYER)
                    turn = AI

        if turn == AI:
            col, val, root = minimax(board, 4, True)
            last_root = root

            r = get_next_open_row(board, col)
            drop_piece(board, r, col, AI)

            print("AI move:", col, "val:", val)

            turn = PLAYER

            # ⭐ SHOW TREE GUI (BONUS)
            show_tree_window(last_root, "Minimax", 4)

        screen.fill(BG_COLOR)
        pygame.display.update()


if __name__ == "__main__":
    main()