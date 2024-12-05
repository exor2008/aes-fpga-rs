module aes (input clk,
            input rst,
            input [127:0] key,
            input [127:0] ciphertext);
    
    wire [127: 0] cipher_add_key;
    
    add_key initial_round(
    .clk(clk),
    .rst(rst),
    .key(key),
    .ciphertext(ciphertext),
    .cipher_add_key(cipher_add_key)
    );
endmodule
