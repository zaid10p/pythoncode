
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
        try:
            return self.elem.pop(0)
        except IndexError:
            print("List already empty")

    def getList(self):
        return self.elem
