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
#plot_rotate_complex()

from image import file2image

def plot_image():
    data = file2image("img01.png")
    plot({ x + ((len(data) - y) * 1j) for x in range(len(data[0])) for y in range(len(data)) if sum(data[y][x]) / 3 < 120 }, 200)

#plot_image()

def f(z):
    return { (s - z) for s in S }

def f_2(z):
    data = file2image("img01.png")
    data_set = { x + ((len(data) - y) * 1j) for x in range(len(data[0])) for y in range(len(data)) if sum(data[y][x]) / 3 < 120 }
    return { (s - z) for s in data_set }

#mean_x = sum({ z.real for z in S }) / len(S)
#mean_y = sum({ z.imag for z in S }) / len(S)
#plot(f(mean_x + mean_y * 1j))

#plot(f_2(90 + 80j), 200)

from math import e, pi

n_total = 20

#points = { (e**((2 * pi * 1j) / n_total)) ** n for n in range(n_total) }

#plot(points)


#plot({ z * e ** (r * 1j) for z in S for r in { 0, pi / 4, pi / 2, 3 * pi / 4, pi, 5 * pi / 4, 3 * pi / 2, 7 * pi / 4, 2 * pi } })

data = file2image("img01.png")
data_set = { x + ((len(data) - y) * 1j) for x in range(len(data[0])) for y in range(len(data)) if sum(data[y][x]) / 3 < 120 }
data_set = { z * e ** (r * 1j) for z in data_set for r in { 0, pi / 4, pi / 2, 3 * pi / 4, pi, 5 * pi / 4, 3 * pi / 2, 7 * pi / 4, 2 * pi } }

#plot(data_set, 200)

data_set = { ((x + ((len(data) - y) * 1j)) - 80 - 80j) * e ** (r * 1j) for x in range(len(data[0])) for y in range(len(data)) for r in { pi / 4 } if sum(data[y][x]) / 3 < 120 }
#plot(data_set, 200)


def one_time_pad(binary):
    pad = []
    
    for val in range(32):
        binary_key, _ = integer_to_binary(val)
        binary_key = binary_key.zfill(5)
        
        pad_item = ["", ""]

        for i in range(len(binary)):
            bin_val = int(binary[i])
            bin_key = int(binary_key[i])
            
            if bin_val == 1 and bin_key == 1:
                pad_item[0] += "1"
            else:
                pad_item[0] += "0"
                
            if bin_val != bin_key:
                pad_item[1] += "1"
            else:
                pad_item[1] += "0"
                
        pad.append(pad_item)
            
    print(pad)
    
    return pad
        
def integer_to_binary(integer, exp = 0):
    binary = ""    
    
    if (2 ** (exp + 1) <= integer):
        binary, integer = integer_to_binary(integer, exp + 1)
        
    calc_exp = 2 ** exp
    val = integer // calc_exp
    
    if val > 0:
        integer = integer - calc_exp
        binary = binary + "1"        
    else:
        binary = binary + "0"

    return binary, integer
    
def binary_to_integer(binary):
    total = 0

    for i in range(len(binary)):
        bit = binary[len(binary) - i - 1]
        total += int(bit) * (2 ** i)
            
    return total

def crack():
    code = [ "10101", "00100", "10101", "01011", "11001", "00011", "01011", "10101", "00100", "11001", "11010" ]
    
    all_answers = []
    
    for arr in code:
        answers = [""] * 64
        potential_combos = one_time_pad(arr)
        
#        print(len(potential_combos))
#        print(len(potential_combos[0]))

        count = 0
        
        for combo in potential_combos:
            for alg in combo:
#                print("count", count)
                answers[count] = alg
                count += 1
                
#        print(potential_combos)
        
        t = binary_to_integer(arr)

        all_answers.append(answers)        
#        print(t, t + 65, chr(t + 65))
        
    all_answers = list(zip(*all_answers))
    print(all_answers)
    print(len(all_answers))
    
    
    return all_answers


my_ans = crack()
#one_time_pad("10111")
#binary, _ = integer_to_binary(23)
#print(binary)





















