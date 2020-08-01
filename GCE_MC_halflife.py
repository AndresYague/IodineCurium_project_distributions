import numpy as np
import matplotlib.pyplot as plt
import random
 
random.seed()
 
cycles = int(1e7)
binnum = 80
xmax = 2000
 
tle = 200         # Time since last event, Myr
figname = 'new2_{:.0f}Myr_{:.0e}run.pdf'.format(tle, cycles)
s = "Producing figure {}".format(figname)
print(s)
 
Cm_T       = 15.6 # Myr, halflife
Cm_err     = 0.5  # Myr, 1 sigma of halflife error
II_T       = 15.7 # Myr
II_err     = 0.4  # Myr
muess      = 438  # Cm/I
muess_err  = 92 # 1 sigma of Cm/I at ESS
 
 
def muinitcalc(tauCm, tauI, muess, tlaste):
    # the variables are randomly generated (Cm, I mean lives; muess; time from last event)
    # If taking the recommended half-life, tau_eq is negative for this ratio
    taueq = (tauCm * tauI) / (tauCm - tauI)
    muinit = muess * np.exp(tlaste / taueq)
    return muinit
 
 
# Sample and calculate
muinits = []
for cyc in range(cycles):
    tauCm_rand = np.random.normal(Cm_T, Cm_err)/np.log(2)
    tauI_rand  = np.random.normal(II_T, II_err)/np.log(2)
    muess_rand = np.random.normal(muess, muess_err)
    muinit_rand = muinitcalc(tauCm_rand, tauI_rand, muess_rand, tle)
    muinits.append(muinit_rand)

# Get stats
p1 = 34.1; p2 = 47.7
muinit_mid = np.median(muinits)
muinit_min_1sig = np.percentile(muinits, 50 - p1)
muinit_max_1sig = np.percentile(muinits, 50 + p1)
muinit_min_2sig = np.percentile(muinits, 50 - p2)
muinit_max_2sig = np.percentile(muinits, 50 + p2)
 
 
 
muinit_minus = muinit_mid - muinit_min_2sig
muinit_plus = muinit_max_2sig - muinit_mid
 
print('Initial ratio middle: {:.1f}'.format(muinit_mid))
print('Plus: {:.1f}'.format(muinit_plus))
print(muinit_max_2sig)
print('Minus: {:.1f}'.format(muinit_minus))
print(muinit_min_2sig)
 
 
plt.hist(muinits, bins=binnum)
plt.xlim(0, xmax)
plt.xlabel('Initial ratio')
plt.ylabel('Number')
ymin, ymax = plt.ylim() # ymin is always 0
 
txt_xstart = xmax - 900
tle_txt = 'Time since last event: {:.0f} Myr'.format(tle)
plt.text(txt_xstart, ymax * 0.94, tle_txt)
runs_txt = 'Number of runs: {:.1e}'.format(cycles)
plt.text(txt_xstart, ymax * 0.9, runs_txt, horizontalalignment='left')
mean_txt = 'Median of initial ratio: {:.1f}'.format(muinit_mid)
plt.text(txt_xstart, ymax * 0.8, mean_txt, horizontalalignment='left')
 
plt.text(txt_xstart, ymax * 0.73, '1 sigma:')
std_txt = 'Minimum:  {:.1f} (-{:.1f})'.format(muinit_min_1sig, (muinit_mid - muinit_min_1sig))
plt.text(txt_xstart, ymax * 0.69, std_txt, horizontalalignment='left')
std_txt = 'Maximum: {:.1f} (+{:.1f})'.format(muinit_max_1sig, (muinit_max_1sig - muinit_mid))
plt.text(txt_xstart, ymax * 0.65, std_txt, horizontalalignment='left')
 
plt.text(txt_xstart, ymax * 0.58, '2 sigma:')
std_txt = 'Minimum:  {:.1f} (-{:.1f})'.format(muinit_min_2sig, (muinit_mid - muinit_min_2sig))
plt.text(txt_xstart, ymax * 0.54, std_txt, horizontalalignment='left')
std_txt = 'Maximum: {:.1f} (+{:.1f})'.format(muinit_max_2sig, (muinit_max_2sig - muinit_mid))
plt.text(txt_xstart, ymax * 0.50, std_txt, horizontalalignment='left')
 
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
 
plt.savefig(figname)
plt.show()
