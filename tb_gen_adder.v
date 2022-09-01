`timescale 1ns/1ns
module tb_gen_adder();
parameter unit_size = 14;
parameter output_size = 3;
parameter number_of_tests = 14;
//I/O LIST//////////////////////////////////////////////////////////////////////////////////
		reg  a0; 
		reg  a1; 
		reg  a2; 
		reg  a3; 
		reg  a4; 
		reg  a5; 
		reg  a6; 
		reg  a7; 
		reg  a8; 
		reg  a9; 
		reg  a10; 
		reg  a11; 
		reg  a12; 
		reg  a13; 
		wire [3:0] b ; 
//CLOCK//////////////////////////////////////////////////////////////////////////////////
reg clock;
parameter T = 16;
initial begin 
	clock=0;
	forever #T clock=~clock;
end

gen_adder #(unit_size) dut (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, b);

integer testno = 0;
reg [unit_size-1:0] mem [0:number_of_tests-1];
initial begin 
$readmemb("./tb_file",mem);
$display("%p",mem);
end
reg [output_size:0] rowsum;integer col;
task summer();
	begin
		rowsum=0;
		for (col=0;col<unit_size;col=col+1)
		begin
			$display("For mem[col%d]=%p; mem[testno%d][col%d]=%b",col,mem[col],testno,col,mem[testno][col]);
			rowsum = rowsum + mem[testno][col];
		end
	end
endtask
wire eq;	assign eq = (b==rowsum)?1:0;
////////////////////////////////////////////////////////////
initial begin 
	for (testno=0; testno< number_of_tests; testno=testno+1)
	begin
		if(testno==0)   #0;  else    #T;
{a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13}=mem[testno];summer();
end
		#T $stop;
end

endmodule
