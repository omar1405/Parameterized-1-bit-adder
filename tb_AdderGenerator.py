# Task 1 | Python Module
# By: Omar Amgad
# This py script auto generates a parameterized tb verilog code
# in order to create a tb of the general adder.

# importing
from python2verilog import *
from math import log2

# script
module_filename = "gen_adder.v"
dut_name = "gen_adder"

tb_filename = "tb_" + module_filename
tb_modulename = "tb_" + dut_name
parameter_name = "unit_size"

# user specifications
input_bits = int(init_v_tb_read_parameter_val(module_filename))
input_period = int(input("Enter of period for timescale 1ns/1ns: ") or "100")

# calculating
output_bits = int(log2(input_bits))
timestep = 1
timestep_timeunit = "ns"
precision = 1
precision_timeunit = "ns"

# opening file and writing
tb_verilog_file = open(tb_filename, "w")
init_v_timescale(tb_filename, timestep, timestep_timeunit, precision, precision_timeunit)
init_v_tb_module_param(tb_filename, tb_modulename, parameter_name, input_bits)

# this section adds the additional parameters required
tb_verilog_file.seek(0, 2)
tb_verilog_file.write("parameter output_size = " + str(output_bits) + ";\n")
tfile = open("tb_file", "r")
total_tests = len(tfile.readlines())
tfile.close()
tb_verilog_file.write("parameter number_of_tests = " + str(total_tests) + ";\n")

# io list
number_of_i = input_bits
number_of_o = 1
sum_of_io = number_of_o + number_of_i
tb_verilog_file.seek(0, 2)
init_v_tb_section(tb_filename, "I/O LIST")
import_v_tb_io(module_filename, sum_of_io, tb_filename)
init_v_tb_section(tb_filename, "CLOCK")
init_v_tb_clock(tb_filename, input_period)

# DUT
tb_verilog_file.seek(0, 2)
tb_verilog_file.write("\n")
init_v_tb_section(tb_filename, "DUT")
tb_verilog_file.write(dut_name + " #(" + parameter_name + ") " + "dut (")
for index in range(input_bits):
    tb_verilog_file.write("a" + str(index) + ", ")
tb_verilog_file.write("b);\n\n")

# memory reading
tb_verilog_file.seek(0, 2)
init_v_tb_section(tb_filename, "MEMORY READING")
tb_verilog_file.write("integer testno = 0;\n")
tb_verilog_file.write("reg [unit_size-1:0] mem [0:number_of_tests-1];\n")
tb_verilog_file.write("initial begin \n")
tb_verilog_file.write("$readmemb(\"./tb_file\",""mem);\n")
tb_verilog_file.write("$display(\"%p\",mem);\nend\n")

# task for adding bits
tb_verilog_file.seek(0, 2)
init_v_tb_section(tb_filename, "SUMMER TASK")
tb_verilog_file.write("reg [output_size:0] rowsum;integer col;\n")
tb_verilog_file.write("task summer();\n\tbegin\n")
tb_verilog_file.write("\t\trowsum=0;\n")
tb_verilog_file.write("\t\tfor (col=0;col<unit_size;col=col+1)\n")
tb_verilog_file.write("\t\tbegin\n")
tb_verilog_file.write("\t\t\t$display(\"For mem[col%d]=%p; mem[testno%d][col%d]=%b\"")
tb_verilog_file.write(",col,mem[col],testno,col,mem[testno][col]);\n")
tb_verilog_file.write("\t\t\trowsum = rowsum + mem[testno][col];\n")
tb_verilog_file.write("\t\tend\n\tend\nendtask\n")

# error check(comparing)
tb_verilog_file.seek(0, 2)
init_v_tb_section(tb_filename, "ERROR CHECKING")
tb_verilog_file.write("wire eq;\tassign eq = (b==rowsum)?1:0;\n")

# actual test
tb_verilog_file.seek(0, 2)
init_v_tb_section(tb_filename, "TEST")
tb_verilog_file.write("initial begin \n")
tb_verilog_file.write("\tfor (testno=0; testno< number_of_tests; testno=testno+1)\n")
tb_verilog_file.write("\tbegin\n")
tb_verilog_file.write("\t\tif(testno==0)   #0;  else    #T;\n{")
for bit in range(input_bits):
    if bit < input_bits - 1:
        tb_verilog_file.write("a" + str(bit) + ",")
    else:
        tb_verilog_file.write("a" + str(bit) + "}")
tb_verilog_file.write("=mem[testno];summer();\n")
tb_verilog_file.write("end\n")
tb_verilog_file.write("\t\t#T $stop;\nend\n")

# ending file
tb_verilog_file.seek(0, 2)
end_v_module(tb_filename)

# closing
tb_verilog_file.close()
