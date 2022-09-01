all: clean test_all
gen_adder: 	AdderGenerator.py
	python3 AdderGenerator.py

tb_file:	 	gen_adder.v tb_file_gen.py
	python3 tb_file_gen.py

tb_gen_adder: gen_adder.v tb_file tb_AdderGenerator.py
	python3 tb_AdderGenerator.py

vsim:= /home/omarvm/intelFPGA/19.1/modelsim_ase/bin/vsim

create: gen_adder tb_file tb_gen_adder

dofile: 
	$(vsim) -do all.do

wave:
	$(vsim) -do waverecover.do

test_all: create dofile

clean:
	rm -rf *.v
	rm -rf tb_file
	# $(clear)
