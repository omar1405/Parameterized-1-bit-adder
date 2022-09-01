# this is a user-library to ease the process of creating
# Verilog modules automatically using python
# By: Omar Amgad

# NORMAL INITIATION SECTION///////////////////////////////////////////////////////////

def init_v_module_unparam(filename, modulename):
    # this fn clears and/or creates <tb_file_name> and writes
    # the declaration of <module_name> without parameterization.
    # this also
    given_file = open(filename, "w")
    given_file.seek(0, 0)
    given_file.write("module " + modulename + "(")
    given_file.close()


def init_v_module_param(filename, modulename, parameter_name, n):
    # this fn clears and/or creates <tb_file_name> and writes
    # the declaration of <module_name> parameterized to <N>.
    # this also
    given_file = open(filename, "w")
    given_file.seek(0, 0)
    given_file.writelines("module " + modulename + " #(parameter " + parameter_name + " = " + str(n) + " ) " + "( \n")
    given_file.close()


def end_v_module(filename):
    # this fn appends to <tb_file_name> that is .v file "endmodule"
    # at the end of the file
    given_file = open(filename, "a")
    given_file.seek(0, 2)
    given_file.writelines("\nendmodule\n")
    given_file.close()


# NORMAL TB INITIATION SECTION///////////////////////////////////////////////////////////


def init_v_tb_section(tb_filename, comment_here):
    given_file = open(tb_filename, "a")
    # given_file.seek(0, 2)
    given_file.write("//" + comment_here)
    given_file.write("//////////////////////////////////////////////////////////////////////////////////\n")
    given_file.close()


def init_v_timescale(tb_filename, timestep, timestep_timeunit, precision, precision_timeunit):
    given_file = open(tb_filename, "a")
    given_file.seek(0, 0)
    given_file.writelines("`timescale " + str(timestep) + timestep_timeunit + "/" + str(precision) + precision_timeunit)
    given_file.writelines("\n")
    given_file.close()


def init_v_tb_module_unparam(tb_filename, tb_modulename):
    # this fn clears and/or creates testbench of <tb_file_name> and writes
    # the declaration of <module_name> without parameterization.
    given_file = open(tb_filename, "a")
    given_file.write("module " + tb_modulename + "();\n")
    given_file.close()


def init_v_tb_read_parameter_val(filename):
    given_file = open(filename, "r")
    declaration = given_file.readline()
    given_file.close()
    return declaration.partition("= ")[2].partition(" )")[0]


def init_v_tb_module_param(tb_filename, tb_modulename, parameter_name, n):
    # this fn clears and/or creates testbench of <tb_file_name> and writes
    # the declaration of <module_name> without parameterization.
    given_file = open(tb_filename, "a")
    given_file.writelines("module " + tb_modulename + "();\n")
    given_file.writelines("parameter " + parameter_name + " = " + str(n) + ";\n")
    given_file.close()


def import_v_tb_io(module_filename, number_of_lines, tb_filename):
    # this function reads the module_file's i/o list and generates its tb's reg/wire list.
    verilog_file = open(module_filename, "r")
    tb_verilog_file = open(tb_filename, "a")
    # skip first line (the 'module ...(' line)
    verilog_file.readline()
    # populate io_list with sum of lines of i and o in the module,
    # then replace 'input' with 'reg' and 'output' with 'reg'
    io_list = []
    tb_list = []
    index = 0
    for line in range(number_of_lines):
        io_list.append(verilog_file.readline())
        index += 1
    for string in io_list:
        new_string = string.replace('input', 'reg')
        new_string = new_string.replace('output', 'wire')
        new_string = new_string.replace(',', ';')
        new_string = new_string.replace(');', ';')
        tb_list.append(new_string)
    tb_verilog_file.writelines(tb_list)
    # close
    verilog_file.close()
    tb_verilog_file.close()


def init_v_tb_clock(tb_filename, period):
    given_file = open(tb_filename, "a")
    given_file.write("reg clock;\nparameter T = " + str(period) + ";")
    given_file.write("\ninitial begin \n\tclock=0;\n\tforever #T" + " clock=~clock;\nend\n")
    given_file.close()


def init_v_tb_test_val_auto(tb_filename, testfile):
    # this copies a file prepared by the user directly to the tb file
    # the file has to contain everything inside the initial-block
    test_file = open(testfile, "r")
    tb_verilog_file = open(tb_filename, "a")
    tb_verilog_file.write("initial begin\n")
    tb_verilog_file.writelines(test_file.readlines())
    tb_verilog_file.write("end\n")
    tb_verilog_file.close()


'''
def init_v_tb_test_val_manu(tb_filename, testfile):
    test_file = open(testfile, "r")
    tb_verilog_file = open(tb_filename, "a")
############do later
'''
