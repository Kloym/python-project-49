#!/usr/bin/env python3


import brain_games.games.even
import brain_games.engine


def main():
    game = brain_games.games.even
    brain_games.engine.run_game(game)


if __name__ == "__main__":
    main()
