from final_example.callables import function_1, function_2, function_3
from random import randrange
from concurrent.futures import ThreadPoolExecutor

CALLABLES = [function_1, function_2, function_3]


class User:
    def __init__(self, n):
        self.n = n
        self.actions = self.set_callables()

    def set_callables(self):
        callables = []
        params = []
        for _ in range(self.n):
            idx = randrange(0, len(CALLABLES))
            params.append(randrange(1, 5))
            callables.append(CALLABLES[idx])
        return callables, params

    def call_all(self):
        for f, param in zip(self.actions[0], self.actions[1]):
            f(param)


def activate_user(n):
    user = User(n)
    user.call_all()
    return True


if __name__ == '__main__':
    users = 20
    users_actions = [randrange(1, 10) for _ in range(users)]

    e = ThreadPoolExecutor()
    result = all(list(e.map(activate_user, users_actions)))
