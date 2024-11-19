import numpy as np
#from scipy.fft import fft
def autocorr(x):
    X=np.real(np.fft.ifft(np.conj(np.fft.fft(x))*np.fft.fft(x)))
    return(X)