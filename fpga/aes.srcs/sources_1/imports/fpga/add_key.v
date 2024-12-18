module add_key (input clk,
                input rst,
                input [127:0] key,
                input [127:0] plaintext,
                output reg [127:0] cipher_add_key);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            cipher_add_key <= 0;
        end
        else begin
            cipher_add_key <= plaintext ^ key;
        end
    end
endmodule
