module main (input clk,
             input rst,
             input key_w_clk,
             input [15:0] in,
             input [127:0] plaintext);
    
    /*     aes aes(
     .clk(clk),
     .rst(rst),
     .key(key),
     .plaintext(plaintext));
     */
    
    key key(
    .clk(clk),
    .rst(rst),
    .w_clk(key_w_clk),
    .r_data(in)
    );
    
endmodule
