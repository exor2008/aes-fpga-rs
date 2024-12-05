module main (input clk,
             input rst,
             input [127:0] key,
             input [127:0] ciphertext);
    
    aes aes(
    .clk(clk),
    .rst(rst),
    .key(key),
    .ciphertext(ciphertext));
    
endmodule
