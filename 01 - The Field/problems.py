from plotting import plot

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

def plot_imaginary():    
    plot(S, 4)

def plot_addition(add):
    plot({ add + z for z in S }, 4)
    
def plot_half():
    plot({ 0.5 * z for z in S }, 4)
    
def plot_rotate():
    plot({ 0.5 * 1j * z for z in S }, 4)
    
def plot_rotate_complex():
    plot({ 0.5 * 1j * z + (2 - 1j) for z in S }, 4)

    

#plot_imaginary()
#plot_addition(1 + 2j)
#plot_half()
#plot_rotate()
plot_rotate_complex()









