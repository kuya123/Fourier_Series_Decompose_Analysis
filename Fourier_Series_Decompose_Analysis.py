"""
Purpose,

I want to get a first hand feeling about digitized fft and how cos sin domain element can conbine out any target waveform,
let me try here

several variables:
    
target_wf_length : the length of the waveform
target_wf[]: target_wf

coeff_number : define how many cos , sin we use to combine output
cos_coeff[] : use 10 cos and sin to combine out the target
sin_coeff[]


several functions:
    
1. target_func_gen() : define the shape of the waveform
2. cal_ff_serial_coeff(): calculate the coefficient of each cos and sin sub wave
2.1 cal_ff_serial_coeff_i()
3. plot_original_wf() : plot out original waveform
4. plot_ff_sum(): plot out cos and sin waveform and combined result
"""
import matplotlib.pyplot as plt
import math


# Initialise the figure and axes.
fig,[subplot1,subplot2,subplot3,subplot4] = plt.subplots(4, figsize=(12, 15))
fig.suptitle('display Fourier Serial Decompose an Arbitary Waveform', fontsize=15)
subplot1.set_ylabel("original_wf");
subplot2.set_ylabel("cos and sin components");
subplot3.set_ylabel("cos and sin combined phases");
subplot4.set_ylabel("fourier serier combined wf ");


#set the initial func plot
target_step=0.01
target_wf_half_length = 100;
target_wf=[0]*target_wf_half_length*2;
target_step_pnt=[0]*target_wf_half_length*2;
half_period=target_wf_half_length*target_step;

# set the order of cos sin waves to implement Fouriers Seriers Combination
coeff_number=50;
cos_coeff=[0]*coeff_number;
sin_coeff=[0]*coeff_number;
total_sin_cos_a0_result=[0]*target_wf_half_length*2   
AZERO=0




# here we can config out the target arbitary waveform
def target_func_gen():
        
    for i in range(target_wf_half_length*2):
        target_step_pnt[i]=target_step*i
        # cos wave
        # target_wf[i]= math.cos(i*target_step);
        
        
        # triangle wave
        target_wf[i]= ((i*target_step)*100%50)/100;
        
        
        '''
        #square wave
        if (i%50)>15:
            target_wf[i] =10
        else:
            target_wf[i]=-10
        '''
        
        '''
        # arbitary waveform
        if (i<target_wf_half_length/3):
            target_wf[i]=-10
        elif (i<target_wf_half_length*2/3):
            target_wf[i]=-10 + i*target_step*10
        elif (i<target_wf_half_length*4/3):
            target_wf[i]= 10 - i*target_step*10
        else:
            target_wf[i]=0        
        '''
        
    plot_original_wf();
    
    
def plot_original_wf():
        subplot1.set_ylabel("original_wf");
        subplot1.plot(target_step_pnt,target_wf);
    

# calculate Fourier Transform Coefficient for each order tri func
def cal_ff_serial_coeff():
    cal_a0()
    for i in range(coeff_number):
        [cos_coeff[i],sin_coeff[i]]=cal_ff_serial_coeff_i(i)
        plot_cos_sin_components(i)
    
    subplot4.plot(target_step_pnt,total_sin_cos_a0_result)


def cal_ff_serial_coeff_i(i):
    An=0
    Bn=0
    for n in range(target_wf_half_length*2):
        An += target_wf[n]*math.cos(math.pi*i*(n)/target_wf_half_length)
        Bn += target_wf[n]*math.sin(math.pi*i*(n)/target_wf_half_length)
        
            
    return [An/target_wf_half_length,Bn/target_wf_half_length]

# compose out each cos and sin sub wave according to corresponding coeff
def plot_cos_sin_components(n):
    cos_single_result=[0]*target_wf_half_length*2    
    sin_single_result=[0]*target_wf_half_length*2
    for i in range(target_wf_half_length*2):
        if (n!=0):
            cos_single_result[i]=cos_coeff[n]*math.cos(math.pi*n*i/target_wf_half_length)
            sin_single_result[i]=sin_coeff[n]*math.sin(math.pi*n*i/target_wf_half_length)
        else:
            cos_single_result[i]=AZERO/2
            sin_single_result[i]=AZERO/2
            
        total_sin_cos_a0_result[i]+=cos_single_result[i]+sin_single_result[i]
        
    subplot2.plot(target_step_pnt,cos_single_result)
    subplot2.plot(target_step_pnt,sin_single_result)    
    subplot3.plot(target_step_pnt,total_sin_cos_a0_result)
 
    
    
def cal_a0():   
    global AZERO;
    for n in range(target_wf_half_length*2):
        AZERO += target_wf[n]
    
    AZERO=AZERO/target_wf_half_length






#### main func ####    


target_func_gen()  #defin target func shape
cal_ff_serial_coeff() # cal culate fourier serial

#print(cos_coeff)  # cos coeff
#print(sin_coeff)  # sin coeff

plt.show()