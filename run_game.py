from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.qagent import QAgent

def main():

    game = SpaceInvaders(display=False)
    #controller = KeyboardController()
    #controller = RandomAgent(game.na)
    controller = QAgent(game, alpha=0.75)
    controller.learn(game, n_episodes=500, max_steps=5000)
    
    newGame = SpaceInvaders(display=True)
    state = newGame.reset()
    while True:
        action = controller.select_action(state)
        state, reward, is_done = newGame.step(action)
        if(is_done):
            break
        sleep(0.0001)
    print("Game over !")
    print("Score : ", newGame.score_val)

if __name__ == '__main__' :
    main()
