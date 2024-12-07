module aes (input clk,
            input rst,
            input [127:0] key,
            input [127:0] plaintext);
    
    wire [127: 0] cipher_add_key;
    
    add_key initial_round(
    .clk(clk),
    .rst(rst),
    .key(key),
    .plaintext(plaintext),
    .cipher_add_key(cipher_add_key)
    );
    
    wire [127: 0] cipher_sbox;
    sbox sbox(
    .clk(clk),
    .rst(rst),
    .plaintext(cipher_add_key),
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
    
endmodule
