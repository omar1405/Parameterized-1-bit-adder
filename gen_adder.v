module  gen_adder #(parameter unit_size = 14 ) ( 
		input  a0, 
		input  a1, 
		input  a2, 
		input  a3, 
		input  a4, 
		input  a5, 
		input  a6, 
		input  a7, 
		input  a8, 
		input  a9, 
		input  a10, 
		input  a11, 
		input  a12, 
		input  a13, 
		output [3:0] b ); 
	assign b = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13;
	
endmodule
