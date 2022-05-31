# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 23:42:40 2022

@author: js
"""
import torch

def checkGPU(): 
    if torch.cuda.is_available(): 
        print("CUDA available!")
    
        print(f'GPU quantity: {torch.cuda.device_count()}') # GPU quantity
    
        print(f'GPU current device index: {torch.cuda.current_device()}') # GPU index
        
        # print(torch.cuda.get_device_name(0)) # GPU name
        
        # get all devices name
        for i in range(torch.cuda.device_count()): 
            print(f'{torch.cuda.get_device_name(i)}')
        
    else: 
        print("CUDA_NOT_AVAILABEL")

if __name__ == '__main__': 
    checkGPU()
