module shift_byte (input clk,
                   input rst,
                   input [7:0] plainbyte,
                   output reg [7:0] cipherbyte);
    
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            cipherbyte <= 0;
        end
        else begin
            cipherbyte = plainbyte << 1;
            if (plainbyte[7] == 1) begin
                cipherbyte <= cipherbyte ^ 'h1B;
            end
        end
        
        
    end
    
endmodule
