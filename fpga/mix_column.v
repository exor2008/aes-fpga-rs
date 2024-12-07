module mix_column (input clk,
                   input rst,
                   input [31:0] plaincolumn,
                   input [31:0] shiftcolumn,
                   output reg [31:0] ciphercolumn);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            ciphercolumn <= 0;
        end
        else begin
            ciphercolumn[7:0]   <= shiftcolumn[7:0]   ^ plaincolumn[31:24] ^ plaincolumn[23:16] ^ shiftcolumn[15:8]  ^ plaincolumn[15:8];
            ciphercolumn[15:8]  <= shiftcolumn[15:8]  ^ plaincolumn[7:0]   ^ plaincolumn[31:24] ^ shiftcolumn[23:16] ^ plaincolumn[23:16];
            ciphercolumn[23:16] <= shiftcolumn[23:16] ^ plaincolumn[15:8]  ^ plaincolumn[7:0]   ^ shiftcolumn[31:24] ^ plaincolumn[31:24];
            ciphercolumn[31:24] <= shiftcolumn[31:24] ^ plaincolumn[23:16] ^ plaincolumn[15:8]  ^ shiftcolumn[7:0]   ^ plaincolumn[7:0];
        end
    end
    
endmodule
