import numpy as np

N=8

xn1 = [1,2,1,0,0,0,0,0]
xn2 = [-1,1,1,1,2,-2,0,0]

Xk1 = np.fft.fft(xn1, N)
Xk2 = np.fft.fft(xn2, N)
conv = np.convolve(Xk1 , Xk2)
print("Convolution : \n" , conv , "\n")

conv1 = np.fft.fft(xn1, N)
print("Convolution lineaire de Xk1 : \n" , conv1 , "\n")

conv2 = np.fft.fft(xn2, N)
print("Convolution lineaire de Xk2 : \n" , conv2 , "\n")

