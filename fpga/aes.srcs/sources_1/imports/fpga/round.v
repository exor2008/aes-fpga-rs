module round (input clk,
              input rst,
              input [127:0] key,
              input [127:0] plaintext,
              inout [127:0] ciphertext);
    
    wire [127: 0] cipher_sbox;
    
    sbox sbox(
    .clk(clk),
    .rst(rst),
    .plaintext(plaintext),
    .ciphertext(cipher_sbox)
    );
    
    wire [127: 0] cipher_shift_rows;
    shift_rows shift_rows(
    .clk(clk),
    .rst(rst),
    .plaintext(cipher_sbox),
    .ciphertext(cipher_shift_rows)
    );
    
    wire [127: 0] cipher_mix_columns;
    mix_columns mix_columns(
    .clk(clk),
    .rst(rst),
    .plaintext(cipher_shift_rows),
    .ciphertext(cipher_mix_columns)
    );
    
    add_key add_key(
    .clk(clk),
    .rst(rst),
    .key(key),
    .plaintext(cipher_mix_columns),
    .ciphertext(ciphertext)
    );
    
endmodule
