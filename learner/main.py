import agent
import environment as env

if __name__ == '__main__':
    state = (1, 1, 1, 1)
    print(state)
    player = agent.Agent()
    player.train()
    while player.transitions[env.sanitize(*state)]:
        print("My turn:")
        new_state = player.best_action(state)
        print(new_state)
        print("Your turn:")
        state = tuple(map(int, input().split(',')))
    print(state)
