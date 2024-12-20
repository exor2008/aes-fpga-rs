module add_key (input clk,
                input rst,
                input [127:0] key,
                input [127:0] plaintext,
                output reg [127:0] ciphertext);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            ciphertext <= 0;
        end
        else begin
            ciphertext <= plaintext ^ key;
        end
    end
endmodule
