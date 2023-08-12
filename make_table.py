import numpy as np
import pprint
from FT2Signal import get_passing_table
import os
from matplotlib import pyplot as plt

cwd = os.getcwd()
tab_dir = os.path.join(cwd, os.path.normpath('tables'))
T = np.arange(100, 3010, 10)
foils = ['be_100um.txt', 'be_200um.txt', 'be_300um.txt', 'be_400um.txt', 'be_500um.txt', 'be_700um.txt']

energy_c8h8, passing_c8h8 = get_passing_table(os.path.join(tab_dir, 'c8h8_5000um.txt'))
# energy_be100, passing_be100 = get_passing_table(os.path.join(tab_dir, 'be_100um.txt'))
# energy_be200, passing_be200 = get_passing_table(os.path.join(tab_dir, 'be_200um.txt'))
for foil in foils:
    _, passing_be_main = get_passing_table(os.path.join(tab_dir, foil))
    table_file = os.path.join(tab_dir, 'table_' + foil)
    data = [str(x).rjust(4, ' ') + '   ' for x in T]
    for foil_secondary in foils:
        _, passing_be_secondary = get_passing_table(os.path.join(tab_dir, foil_secondary))
        for ind, t in enumerate(T):
            int1 = np.trapz(np.exp(-energy_c8h8/t) * (1-passing_c8h8) * passing_be_main, energy_c8h8)
            int2 = np.trapz(np.exp(-energy_c8h8/t) * (1-passing_c8h8) * passing_be_secondary, energy_c8h8)
            rel = int1 / int2
            data[ind] = data[ind] + ' ' + str(rel)
    for i in range(len(data)):
        data[i] = data[i] + '\n'
    with open(table_file, 'w') as f:
        f.writelines(data)
# pprint.pprint(rel_100_200)
# plt.plot(energy_c8h8, np.exp(-energy_c8h8/T) * (1-passing_c8h8) * passing_be100)
# print(np.trapz(np.exp(-energy_c8h8/T) * (1-passing_c8h8) * passing_be100, energy_c8h8))
# plt.grid(visible=True)
# plt.show()
