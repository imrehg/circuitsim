#!/usr/bin/env python2
"""
Plotting the nmLaser shutter simulation results
"""
import numpy as np
import pylab as pl

if __name__ == "__main__":
    slow = np.loadtxt('simslow.data')
    fast = np.loadtxt('simfast.data')

    tslow = slow[:, 0]
    v3slow = slow[:, 3]
    v4slow = slow[:, 5]
    tfast = fast[:, 0]
    v3fast = fast[:, 3]
    v4fast = fast[:, 5]

    f = pl.figure(figsize=(8.69, 11.27))
    pl.subplot(2,1,1)
    pl.plot(tslow*1e3, (v3slow-v4slow), 'k-', linewidth=2)
    pl.xlabel('Time (ms)', fontsize=14)
    pl.ylabel('Inductor voltage (V)', fontsize=14)
    pl.title('Shutter field collapse: Original flywheel diode setup')
    pl.grid()

    pl.subplot(2,1,2)
    pl.plot(tfast*1e9, (v3fast-v4fast)/1e3, 'k-', linewidth=2)
    pl.xlabel('Time (ns)', fontsize=14)
    pl.ylabel('Inductor voltage (kV)', fontsize=14)
    pl.title('Adding series Zener diode')
    pl.grid()

    pl.savefig('Shutter01.pdf')

    pl.show()
