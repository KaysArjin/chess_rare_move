import chess.pgn
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import os


def main():
    pgn_file_path = 'data/lichess_games.pgn'  # Update with your actual file path

    # Open the PGN file
    pgn = open(pgn_file_path, encoding='utf-8')


    # Extract moves
    moves_list = []
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break  # End of file
        node = game
        while node.variations:
            next_node = node.variation(0)
            move_san = node.board().san(next_node.move)
            moves_list.append(move_san)
            node = next_node

    # Analyze the data
    move_counts = Counter(moves_list)
    rare_moves = move_counts.most_common()[::-1]

    # Prepare data for visualization
    df_moves = pd.DataFrame(rare_moves, columns=['Move', 'Frequency'])

    # Visualize the data
    df_moves.head(20).plot(kind='barh', x='Move', y='Frequency', legend=False)
    plt.xlabel('Frequency')
    plt.ylabel('Move')
    plt.title('Top 20 Rarest Chess Moves')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
