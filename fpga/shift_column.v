module shift_column (input clk,
                     input rst,
                     input [31:0] plaincolumn,
                     input [31:0] ciphercolumn);
    
    shift_byte b1(
    .clk(clk),
    .rst(rst),
    .plainbyte(plaincolumn[7:0]),
    .cipherbyte(ciphercolumn[7:0])
    );
    
    shift_byte b2(
    .clk(clk),
    .rst(rst),
    .plainbyte(plaincolumn[15:8]),
    .cipherbyte(ciphercolumn[15:8])
    );
    
    shift_byte b3(
    .clk(clk),
    .rst(rst),
    .plainbyte(plaincolumn[23:16]),
    .cipherbyte(ciphercolumn[23:16])
    );
    
    shift_byte b4(
    .clk(clk),
    .rst(rst),
    .plainbyte(plaincolumn[31:24]),
    .cipherbyte(ciphercolumn[31:24])
    );
    
endmodule
