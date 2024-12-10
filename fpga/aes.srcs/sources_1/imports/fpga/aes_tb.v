`timescale 100 ns / 10 ns

module main_tb();
    reg rst;
    reg clk;
    reg w_clk;
    reg [15:0] key;
    reg [127:0] plaintext;
    
    always #1 clk = ~clk;
    
    main uut(
    .clk(clk),
    .rst(rst),
    .key_w_clk(w_clk),
    .in(key),
    .plaintext(plaintext)
    );
    
    initial begin
        clk   = 0;
        rst   = 0;
        w_clk = 0;
        
        #1 rst = 1;
        #1 rst = 0;
        
        #0.7
        key        = 'h1111_1111;
        w_clk      = 1;
        #0.1 w_clk = 0;
        
        #1.1
        key        = 'h2222_2222;
        w_clk      = 1;
        #0.3 w_clk = 0;
        
        #0.7
        key        = 'h3333_3333;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #0.9
        key        = 'h4444_4444;
        w_clk      = 1;
        #0.3 w_clk = 0;
        
        #1
        key        = 'h5555_5555;
        w_clk      = 1;
        #0.3 w_clk = 0;
        
        #0.8
        key        = 'h6666_6666;
        w_clk      = 1;
        #0.4 w_clk = 0;
        
        #1.1
        key        = 'h7777_7777;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h8888_8888;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #0.9
        key        = 'h1111_1111;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h2222_2222;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h3333_3333;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h4444_4444;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h5555_5555;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h6666_6666;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h7777_7777;
        w_clk      = 1;
        #0.2 w_clk = 0;
        
        #1
        key        = 'h8888_8888;
        w_clk      = 1;
        #0.2 w_clk = 0;

        $finish;
    end
    
    
endmodule
