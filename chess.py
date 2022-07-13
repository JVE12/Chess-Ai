from stockfish import Stockfish
stockfish = Stockfish(path="C:\\Users\\jvane\\Downloads\\stockfish_15_win_x64_avx2\\stockfish_15_win_x64_avx2\\stockfish_15_x64_avx2.exe", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
def find_best_fen_move(fen):
    stockfish.set_fen_position(fen)
    print(stockfish.get_best_move())
    stockfish.set_position([stockfish.get_best_move()])


def find_best_move(move):
    stockfish.make_moves_from_current_position([move])
    print(stockfish.get_best_move())
    stockfish.make_moves_from_current_position([stockfish.get_best_move()])
    print(stockfish.get_board_visual(False))

stockfish.make_moves_from_current_position([stockfish.get_best_move()])
print(stockfish.get_board_visual(False))

while True:
    mov = input("Enter your move: ")
    find_best_move(mov)