from python2verilog import *
import random
f = open("tb_file", "w")
test_times = int(input("number of tests: ") or "10")
module_name = "gen_adder.v"
input_bits = int(init_v_tb_read_parameter_val(module_name))

for line in range(test_times):
    f.seek(0, 2)
    string = ""
    # generate a random 8-bits string of 0 and 1
    for index in range(input_bits):
        random_number = random.randint(0, 1)
        string = string + str(random_number)
        index += 1
    f.write(string + "\n")
    line += 1
f.close()
