module aes (input clk,
            input rst,
            input [127:0] key0,
            input [127:0] key1,
            input [127:0] key2,
            input [127:0] key3,
            input [127:0] plaintext,
            inout [127:0] ciphertext);
    
    wire [127: 0] cipher_add_key;
    add_key initial_round(
    .clk(clk),
    .rst(rst),
    .key(key0),
    .plaintext(plaintext),
    .ciphertext(cipher_add_key)
    );
    
    wire [127: 0] cipher_round1;
    round round1(
    .clk(clk),
    .rst(rst),
    .key(key1),
    .plaintext(cipher_add_key),
    .ciphertext(cipher_round1)
    );
    
    wire [127: 0] cipher_round2;
    round round2(
    .clk(clk),
    .rst(rst),
    .key(key2),
    .plaintext(cipher_round1),
    .ciphertext(cipher_round2)
    );
    
    wire [127: 0] cipher_round3;
    round round3(
    .clk(clk),
    .rst(rst),
    .key(key3),
    .plaintext(cipher_round2),
    .ciphertext(ciphertext)
    );
    
    
endmodule
