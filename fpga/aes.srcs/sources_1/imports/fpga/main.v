module main (input clk,
             input rst,
             input key_w_clk,
             input [15:0] in,
             input [127:0] plaintext,
             inout [127:0] ciphertext);
    
    wire [127:0] key0;
    wire [127:0] key1;
    wire [127:0] key2;
    wire [127:0] key3;
    
    aes aes(
    .clk(clk),
    .rst(rst),
    .key0(key0),
    .key1(key1),
    .key2(key2),
    .key3(key3),
    .plaintext(plaintext),
    .ciphertext(ciphertext));
    
    key key(
    .clk(clk),
    .rst(rst),
    .w_clk(key_w_clk),
    .r_data(in),
    .key0(key0),
    .key1(key1),
    .key2(key2),
    .key3(key3)
    );
    
endmodule
