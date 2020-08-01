import matplotlib.pyplot as plt
import numpy as np
import random

def sampleTaus():
    # Mean lives in years
    tau1 = np.random.normal(15.7, 0.4)/np.log(2)
    tau2 = np.random.normal(15.6, 0.5)/np.log(2)
    
    return tau1, tau2

def main():
    random.seed()
    
    nn = 1e7
    nn = int(nn)
    
    # Distribution probabilities
    p1, p2, p3 = 34.1, 47.7, 49.8
    
    abs_tau_eq = []; tau_eq = []
    for ii in range(nn):
        # Sample Teq
        tau1, tau2 = sampleTaus()
        tau_eq.append((tau2*tau1)/(tau2 - tau1))
        abs_tau_eq.append(abs(tau_eq[-1]))
    
    mean = np.mean(abs_tau_eq)
    median = np.median(abs_tau_eq)
    
    sig1_1 = np.percentile(abs_tau_eq, 50 - p1)
    sig1_2 = np.percentile(abs_tau_eq, 50 + p1)
    
    sig2_1 = np.percentile(abs_tau_eq, 50 - p2)
    sig2_2 = np.percentile(abs_tau_eq, 50 + p2)
    
    sig3_1 = np.percentile(abs_tau_eq, 50 - p3)
    sig3_2 = np.percentile(abs_tau_eq, 50 + p3)
    
    print("Values for |tau_eq|")
    print("Mean = {:.2f}, median = {:.2f}".format(mean, median))
    print("{}% = {:.2f} - {:.2f}".format(p1*2, sig1_1, sig1_2))
    print("{}% = {:.2f} - {:.2f}".format(p2*2, sig2_1, sig2_2))
    print("{}% = {:.2f} - {:.2f}".format(p3*2, sig3_1, sig3_2))
    plt.hist(abs_tau_eq, bins = int(1e3), range = [0, 4e3])
    plt.xlabel("$|\\tau_{{eq}}|$ in Myr")
    plt.savefig("abs_Tau_eq_distribution.pdf")
    plt.show()
    
    # if you want to forward-decay an initial value in init_val, make fDecay = True
    fDecay = False
    if not fDecay:
        return
    
    # Decay distributions for initial values
    init_val = 406.5
    decays = [150., 200.]
    
    # Calculate the decayed value distribution
    val_dist = []
    for decay in decays:
        val_dist.append([])
    for t_eq in tau_eq:
        for ii in range(len(decays)):
            decay = decays[ii]
            val_dist[ii].append(init_val*np.exp(-decay/t_eq))
    
    print("-----------")
    print("Distribution for an initial ratio of {}".format(init_val))
    for ii in range(len(decays)):
        decay = decays[ii]
        
        # Calculate values
        median = np.median(val_dist[ii])
        sig1_1 = np.percentile(val_dist[ii], 50 - p1)
        sig1_2 = np.percentile(val_dist[ii], 50 + p1)
        sig2_1 = np.percentile(val_dist[ii], 50 - p2)
        sig2_2 = np.percentile(val_dist[ii], 50 + p2)
        sig3_1 = np.percentile(val_dist[ii], 50 - p3)
        sig3_2 = np.percentile(val_dist[ii], 50 + p3)
        
        # Print them
        print("--------")
        print("Decay of {} Myr".format(decay))
        print("Median = {:.2f}".format(median))
        print("{}% = {:.2f} - {:.2f}".format(p1*2, sig1_1, sig1_2))
        print("{}% = {:.2f} - {:.2f}".format(p2*2, sig2_1, sig2_2))
        print("{}% = {:.2f} - {:.2f}".format(p3*2, sig3_1, sig3_2))
        
        plt.hist(val_dist[ii], bins = int(1e3))
        plt.title("Decay of {} Myr".format(decay))
        plt.xlabel("Final ratio")
        plt.show()

if __name__ == "__main__":
    main()
