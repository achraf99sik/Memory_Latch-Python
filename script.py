class Register8Bit:
    def __init__(self):
        self.latch_states = [0] * 8
        self.R8in = [0] * 8
        self.enable = False

    def and_or_latch(self, set: bool, reset: bool, index: int) -> int:
        self.latch_states[index] = (set or self.latch_states[index]) and not reset
        return int(self.latch_states[index])

    def gated_latch(self, data_input: bool, write_enable: bool, index: int) -> int:
        return self.and_or_latch(data_input and write_enable, not data_input and write_enable, index)

    def recalculate(self) -> list:
        return [self.gated_latch(self.R8in[i], self.enable, i) for i in range(8)]

    def update_input(self, new_input: list, enable: bool):
        self.R8in = new_input
        self.enable = enable
        return self.recalculate()

# Testing
register = Register8Bit()

R8out = register.update_input([0,1,0,0,0,0,0,0], True)
print(R8out)

R8out = register.update_input([0,1,0,1,0,0,0,0], False)
print(R8out)

R8out = register.update_input([1,1,0,1,0,1,1,1], True)
print(R8out)