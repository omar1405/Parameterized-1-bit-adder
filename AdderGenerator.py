# Task 1 | Python Module
# By: Omar Amgad
# This py script auto generates a parameterized verilog code
# in order to create a general adder.



# importing
from python2verilog import *
from math import log2

# script
file_name = "gen_adder.v"
module_name = " gen_adder"
parameter_name = "unit_size"
input_bits = int(input("Enter number of input bits of addends: ") or "10")

# calculating
output_bits = int(log2(input_bits))

# opening file and writing
verilog_file = open(file_name, "a")
init_v_module_param(file_name, module_name, parameter_name, input_bits)

# I/O list
in_index = 0
verilog_file.seek(0, 1)
for in_index in range(input_bits):
    verilog_file.writelines("\t\tinput  a" + str(in_index) + ", " + "\n")

verilog_file.writelines("\t\toutput [" + str(output_bits) + ":0] b ); " + "\n")

# dataflow
assign_index = 0
verilog_file.seek(0, 1)
verilog_file.writelines("\tassign b = ")
for assign_index in range(input_bits):
    if assign_index < input_bits-1:
        verilog_file.writelines("a" + str(assign_index) + " + ")
    else:
        verilog_file.writelines("a" + str(assign_index) + ";\n\t")

# ending file and closing
verilog_file.seek(0, 2)
end_v_module(file_name)
verilog_file.close()
