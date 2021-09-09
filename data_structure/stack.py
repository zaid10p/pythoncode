
class Stack:
    def __init__(self, initVal=[]) -> None:
        self.elem = initVal

    def __len__(self):
        return len(self.elem)

    def __getitem__(self, i):
        return self.elem[i]

    def push(self, e) -> None:
        self.elem.insert(0, e)

    def pop(self):
        val = self.elem[0]
        self.elem = self.elem[1:]
        return val

    def getList(self):
        return self.elem
