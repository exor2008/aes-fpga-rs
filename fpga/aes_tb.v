`default_nettype none
`define DUMPSTR(x) `"x.vcd`"
`timescale 100 ns / 10 ns

module main_tb();
    
    parameter DURATION = 20;
    
    reg rst;
    reg clk;
    reg [127:0] key;
    reg [127:0] plaintext;
    
    always #1 clk = ~clk;
    
    main uut(
    .clk(clk),
    .rst(rst),
    .key(key),
    .plaintext(plaintext)
    );
    
    initial begin
        $dumpfile(`DUMPSTR(`VCD_OUTPUT));
        $dumpvars(0, main_tb);
        clk = 0;
        rst = 0;
        
        #1 rst = 1;
        #1 rst = 0;
        
        key       = 'h1111_1111_1111_1111_1111_1111_1111_1111;
        plaintext = 'h0000_0000_0000_0000_1111_1111_1111_1111;
        
        #2
        key       = 'h1000_0200_0000_0000_0003_0002_0001_0001;
        plaintext = 'h0000_0000_0000_0000_0000_0000_0000_0000;
        
        #2
        key       = 'h0000_0000_0000_0000_0000_0000_0000_0000;
        plaintext = 'h0000_0000_0000_0000_0000_0000_0000_0000;
        
        #2
        key       = 'h0000_FFFF_0000_FFFF_0000_FFFF_0000_FFFF;
        plaintext = 'hFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF;
        
        #2
        key       = 'h00FF_00FF_00FF_00FF_00FF_00FF_00FF_00FF;
        plaintext = 'h0000_0000_FFFF_FFFF_0000_0000_FFFF_FFFF;
        
        #2
        key       = 'hFF00_FF00_FF00_FF00_FF00_FF00_FF00_FF00;
        plaintext = 'hFFFF_0000_FFFF_FFFF_0000_0000_FFFF_0000;
        
        
        #(DURATION) $display("End of simulation");
        $finish;
    end
    
    
endmodule
