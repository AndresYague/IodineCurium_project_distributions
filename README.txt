# IodineCurium_project_distributions
ESS and tau_eq distributions for the Iodine and Curium project

This code was developed by:
Blanka Világos (https://github.com/vblanka24)
Andrés Yagüe López (https://github.com/AndresYague)

==========How to use=========

Simply run the relevant script for each distribution:

-python3 GCE_MC_halflife.py
This script calculates the distribution for the backwards-decayed ESS
I-129/Cm-247 ratio for "tle" Myrs until the time of the last event. By default
this value is 200 Myr. After the script finishes, it creates a figure with the
calculated distribution.

-python3 montecarloTEq.py
This script calculates the distribution of the absolute tau_eq for the
I-129/Cm-247 ratio. After the script finishes, it creates a figure with the
calculated distribution.
