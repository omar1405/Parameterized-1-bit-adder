//01 Sept   : py files uploaded + Makefile
//31 Aug    : I will upload all the files tomorrow due to no current access to workplace.
//
//
# Parameterized-1-bit-adder
these are a group of python scripts that generate an adder's module, test-values, and testbench, in Verilog-2001 language.
These files were created as a part of my internship. I am still new to python, 
so the source code probably has a better way of implementation, but it should be fast.

# Content
this repository contains the following:

- 4 * python scripts + main.py, that are user-interactive, but also could be run automatically (each have default values):
  - python2verilog.py    :   contains personally-created functions in an attempt to create a library .
    - input: n/a
  - AdderGenerator.py    :   creates the parametrized module ---> gen_adder.v .
    - input: number of input bits.
  - tb_file_gen.py       :   reads number of input bits in gen_adder.v and generates accordingly the data file accordingly ---> tb_file
    - input: number of test cases.
  - tb_AdderGenerator.py :   reads the previously generated files and creates the tb verilog module ---> tb_gen_adder.v
    - input: period of testbench, for a timescale of 1ns/1ns.
  - main.py              :   runs python scripts b-d.

- 1xMakefile:
  - has several targets.
  - including ones that run ModelSim (v19.1). 
    This could be edited via editing the definition of Enviro. Vari. 'vsim' inside the Makefile: vsim:= /home/omarvm/intelFPGA/<version>/modelsim_ase/bin/vsim

    
- 2x.do file:
  - all.do           :   
    - creates a work library
    - deletes previous simulations and data
    - compiles tb_gen_adder.v and gen_adder.v
    - simulates/runs tb_gen_adder.v
    - saves all datasets and waveforms in the form of vsim.wlf and wave.do (ModelSim's defaults)
  - waverecover.do   :   
    - opens last simulated wave (vsim.wlf and wave.do)
