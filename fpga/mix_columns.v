module mix_columns (input clk,
                    input rst,
                    input [127:0] plaintext,
                    input [127:0] ciphertext);
    
    wire [127:0] shifted;
    reg [127:0] copy_plain;
    
    shift_column sc1(
    .clk(clk),
    .rst(rst),
    .plaincolumn(plaintext[31:0]),
    .ciphercolumn(shifted[31:0]));
    
    mix_column mc1(
    .clk(clk),
    .rst(rst),
    .plaincolumn(copy_plain[31:0]),
    .shiftcolumn(shifted[31:0]),
    .ciphercolumn(ciphertext[31:0]));
    
    shift_column sc2(
    .clk(clk),
    .rst(rst),
    .plaincolumn(plaintext[63:32]),
    .ciphercolumn(shifted[63:32]));
    
    mix_column mc2(
    .clk(clk),
    .rst(rst),
    .plaincolumn(copy_plain[63:32]),
    .shiftcolumn(shifted[63:32]),
    .ciphercolumn(ciphertext[63:32]));
    
    shift_column sc3(
    .clk(clk),
    .rst(rst),
    .plaincolumn(plaintext[95:64]),
    .ciphercolumn(shifted[95:64]));
    
    mix_column mc3(
    .clk(clk),
    .rst(rst),
    .plaincolumn(copy_plain[95:64]),
    .shiftcolumn(shifted[95:64]),
    .ciphercolumn(ciphertext[95:64]));
    
    shift_column sc4(
    .clk(clk),
    .rst(rst),
    .plaincolumn(plaintext[127:96]),
    .ciphercolumn(shifted[127:96]));
    
    mix_column mc4(
    .clk(clk),
    .rst(rst),
    .plaincolumn(copy_plain[127:96]),
    .shiftcolumn(shifted[127:96]),
    .ciphercolumn(ciphertext[127:96]));
    
    always @(posedge clk) begin
        if (rst) begin
            copy_plain <= 0;
        end
        else begin
            copy_plain <= plaintext;
        end
    end
    
endmodule
