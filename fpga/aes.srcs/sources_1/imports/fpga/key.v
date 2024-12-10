module key (input clk,
            input rst,
            input w_clk,
            input [15:0] r_data);
    reg [127:0] mem [0:16];
    reg [3:0] offset;
    reg [3:0] counter;
    reg [1:0] state;
    
    localparam READ  = 2'b1;
    localparam WRITE = 2'b10;
    localparam IDLE  = 2'b0;
    
    always @(posedge w_clk or posedge rst) begin
        if (rst) begin
            offset  <= 0;
            counter <= 0;
            state   <= WRITE;
        end
        else begin
            case (state)
                WRITE: begin
                    case (offset)
                        0: begin
                            mem[counter][15:0] <= r_data;
                        end
                        1: begin
                            mem[counter][31:16] <= r_data;
                        end
                        2: begin
                            mem[counter][47:32] <= r_data;
                        end
                        3: begin
                            mem[counter][63:48] <= r_data;
                        end
                        4: begin
                            mem[counter][79:64] <= r_data;
                        end
                        5: begin
                            mem[counter][95:80] <= r_data;
                        end
                        6: begin
                            mem[counter][111:96] <= r_data;
                        end
                        7: begin
                            mem[counter][127:112] <= r_data;
                        end
                    endcase
                    
                    offset <= offset + 1;
                    
                    if (offset == 7) begin
                        offset  <= 0;
                        counter <= counter + 1;
                    end
                end
                
                READ: begin
                    
                end
                
                IDLE: begin
                    
                end
            endcase
        end
    end
    
endmodule
