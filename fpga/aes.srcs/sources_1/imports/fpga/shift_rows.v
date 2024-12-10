module shift_rows (input clk,
                   input rst,
                   input [127:0] plaintext,
                   output reg [127:0] ciphertext);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            ciphertext <= 0;
        end
        else begin
            ciphertext <= {
            plaintext[95:88],   // 11
            plaintext[55:48],   // 6
            plaintext[15:8],    // 1
            plaintext[103:96],  // 12
            
            plaintext[63:56],   // 7
            plaintext[23:16],   // 2
            plaintext[111:104], // 13
            plaintext[71:64],   // 8
            
            plaintext[31:24],   // 3
            plaintext[119:112], // 14
            plaintext[79:72],   // 9
            plaintext[39:32],   // 4
            
            plaintext[127:120], // 15
            plaintext[87:80],   // 10
            plaintext[47:40],   // 5
            plaintext[7:0]      // 0
            };
        end
    end
endmodule
