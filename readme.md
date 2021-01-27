### Decompose arbitary function into fourier series components 
generate decomposed waveform and fourier series coefficiens for any target waveform.

### Background
I have some wave generator in my lab which can generate sin and cos wave.  I want to link them up with PC and use them to generate arbitary waveform.  I will config out target waveform from PC end, decompose it out into fourier serial form, and then config my lab equipments through GPIB. thus, I need write out a code to verify my idea and try out my flow of getting correct Fourier Series Coefficients.

Here I have this python prototype code.  It works well.  

#### License: Any user can modify it without any limit. 

### Here are some key parameters
1. target_step            ## step length for each sampling points
2. target_wf_half_length  ## number of points for half period
3. coeff_number           ## the target order for your Fourier Series sin/cos components

### Here are some function explanation. 
1. target_func_gen()      ## mannualy set up how your target waveform looks like.  example of cos / triangle /square /arbitary are included.

### Here are output explanation
1. plot1: original target waveform
2. plot2: sin and cos components
3. plot3: overlay of component waveforms
4. plot4: overall Foureir Serie result waveform

### Final Words
with this discrete calculation method,  you can implement it into your labview or C++, then sent it out through GPIB to dicrete instruments or PCIe to NI PXI system, then,  em, you can config out any waveform for your testing. If you want to use it as a voltage source, then, the combined output is better to connect to an power amplifier. 

of course, this is for fun.  if you got an FPGA card in your PXI system, just use that, it is much more easier. 

anyway, have fun!

Chen jian
