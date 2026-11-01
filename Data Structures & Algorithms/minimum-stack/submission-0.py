class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)          # empilha o novo valor normalmente
        if not self.min_stack:          # se ainda não existe mínimo, o val é o primeiro mínimo
            self.min_stack.append(val)
        else:
            atual_min = self.min_stack[-1]             # último mínimo conhecido
            self.min_stack.append(min(val, atual_min)) # salva o menor entre val e o mínimo anterior


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
