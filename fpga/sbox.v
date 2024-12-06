module sbox (input clk,
             input rst,
             input [127: 0] plaintext,
             output reg [127: 0] ciphertext);
    
    reg [7: 0] mem [0: 255];
    
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            ciphertext <= 0;
        end
        else begin
            ciphertext <= {
            mem[plaintext[127:120]],
            mem[plaintext[119:112]],
            mem[plaintext[111:104]],
            mem[plaintext[103:96]],
            mem[plaintext[95:88]],
            mem[plaintext[87:80]],
            mem[plaintext[79:72]],
            mem[plaintext[71:64]],
            
            mem[plaintext[63:56]],
            mem[plaintext[55:48]],
            mem[plaintext[47:40]],
            mem[plaintext[39:32]],
            mem[plaintext[31:24]],
            mem[plaintext[23:16]],
            mem[plaintext[15:8]],
            mem[plaintext[7:0]]
            
            };
        end
        
    end
    
    initial begin
        $readmemh("sbox.txt", mem);
    end
endmodule
