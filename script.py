latch_states = [False] * 8

def AndOrLatch(set: bool, reset: bool, index: int) -> int:
    global latch_states
    latch_states[index] = (set or latch_states[index]) and not reset
    return int(latch_states[index])

def GatedLatch(data_input: bool, write_enable: bool, index: int) -> int:
    return AndOrLatch(data_input and write_enable, not data_input and write_enable, index)
def Recalculate():
    return [GatedLatch(R8in[i], enable, i) for i in range(8)]

# Tests
R8in = [0,1,0,0,0,0,0,0]
enable = True

R8out = Recalculate()

print(R8out)
R8in = [0,1,0,1,0,0,0,0]
enable = False
R8out = Recalculate()
print(R8out)
R8in = [1,1,0,1,0,1,1,1]
enable = True
R8out = Recalculate()
print(R8out)
