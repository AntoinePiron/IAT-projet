from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.qagent import QAgent

def main():

    game = SpaceInvaders(display=True)
    #controller = KeyboardController()
    #controller = RandomAgent(game.na)
    controller = QAgent(game, 800, 800, alpha=1)
    controller.learn(game, n_episodes=25, max_steps=5000)
    
    print("Learning done !")
 
    state = game.reset()
    while True:
        action = controller.select_action(state)
        state, reward, is_done = game.step(action)
        if(is_done):
            break
        sleep(0.0001)
    print("Game over !")
    print("Score : ", game.score_val)

if __name__ == '__main__' :
    main()
