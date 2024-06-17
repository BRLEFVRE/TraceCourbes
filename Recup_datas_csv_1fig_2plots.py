# -*- coding: utf-8 -*-
"""
Created on 12/06/2024

@author: B.Lefebvre
"""

# %% Imports the necessary libraries
from csv import reader
from datetime import datetime
import matplotlib.pyplot as plt
import math

# %% Variables globales
path_data = 'c:/users/b.lefebvre/OneDrive - Supergrid Institute/Documents/Work/Python/TraceCourbes/Donnees/'
path_figure = 'c:/users/b.lefebvre/OneDrive - Supergrid Institute/Documents/Work/Python/TraceCourbes/Figures/'
file1 = path_data + 'NIDEC_V1_TI_GT04_Transfo2_MesuresFibre.csv'
file2 = path_data + 'NIDEC_V1_TI_GT04_Transfo2_MesuresCameraThermique.csv'

# %%
# -------------------------EXTRACT DATA FROM CSV--------------------------
# open file in read mode
with open(file1, 'r') as read_obj:
    line_count1 = 0
    time1 = []
    ch1_1 = []          # voie1 du 1er fichier
    ch1_2 = []
    ch1_3 = []
    ch1_4 = []         
    ch1_5 = []         # -/!\- à rajouter/diminuer, en fonction du nombre de courbes
    
    csv_reader = reader(read_obj, delimiter=';')  # pass the file object to reader() to get the reader object

    # --------Stockage dans des listes de toutes les colonnes de l'objet "csv-reader"
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # on élimine les valeurs non numériques
        if (not math.isinf(float(row[1])) or not math.isnan(float(row[1]))
                or not math.isinf(float(row[2])) or not math.isnan(float(row[2]))
                or not math.isinf(float(row[3])) or not math.isnan(float(row[3]))
                or not math.isinf(float(row[4])) or not math.isnan(float(row[4]))
                or not math.isinf(float(row[5])) or not math.isnan(float(row[5]))):
            dt1 = datetime.strptime(row[0], '%d.%m.%Y %H:%M:%S.%f')      # format de la date dans le fichier de mesure
            time1.append(dt1.timestamp()-7181-1718189155)                           # on récupère la date exprimée en secondes et on recale par rapport à la 2ème courbe
            ch1_1.append(float(row[1]))
            ch1_2.append(float(row[2]))
            ch1_3.append(float(row[3]))
            ch1_4.append(float(row[4]))  
            ch1_5.append(float(row[5]))  # -/!\- à rajouter/diminuer, en fonction du nombre de courbes
            line_count1 += 1
    print(f'Processed {line_count1} lines.')  # on affiche le nombre de lignes scrutées


# %%
# -------------------------EXTRACT DATA FROM CSV--------------------------
# open file in read mode
with open(file2, 'r') as read_obj:
    line_count2 = 0
    time2 = []
    ch2_1 = []          # voie1 du 2ème fichier
    ch2_2 = []
    ch2_3 = []
    ch2_4 = []         # -/!\- à rajouter/diminuer, en fonction du nombre de courbes
    
    csv_reader = reader(read_obj, delimiter=',')  # pass the file object to reader() to get the reader object

    # --------Stockage dans des listes de toutes les colonnes de l'objet "csv-reader"
    for row in csv_reader:
        # row variable is a list that represents a row in csv   
        # on élimine les valeurs non numériques
        if (not math.isinf(float(row[2])) or not math.isnan(float(row[2]))
               or not math.isinf(float(row[3])) or not math.isnan(float(row[3]))
               or not math.isinf(float(row[4])) or not math.isnan(float(row[4]))
               or not math.isinf(float(row[5])) or not math.isnan(float(row[5]))): 
            dt2 = datetime.strptime(row[1],'%Y-%m-%d %H:%M:%S.%f')      # format de la date dans le fichier de mesure
            time2.append(dt2.timestamp()-1718189155)                                 # on récupère la date exprimée en secondes
            ch2_1.append(float(row[3]))
            ch2_2.append(float(row[4]))
            ch2_3.append(float(row[5]))
            ch2_4.append(float(row[6]))  # -/!\- à rajouter/diminuer, en fonction du nombre de courbes
        line_count2 += 1
    print(f'Processed {line_count2} lines.')  # on affiche le nombre de lignes scrutées


# %%
# -------------------------PLOT ON SCREEN UNE SEULE COURBE voie CH1 --------------------------
# plt.subplots() is a function that returns a tuple containing a figure and axes object(s), 
# Thus when using : fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax,
# Having "fig" is useful if you want to change figure-level attributes or save the figure as an
# image file later (e.g. with fig.savefig('yourfilename.png'))

# On bloque le mode interactif (plt.ion()), de manière à ce que toutes les figures puissent être affichées en même temps
# En effet, la commande : plt.show() affiche la courbe, mais bloque le code jusqu'à ce qu'on ferme la fenêtre
plt.ioff()

# Affichage de toutes les courbes sur la même figure
# affichage pleine page(constrained_layout), on partage l'axe des x(sharex) et l'axe des Y (sharey)
plt.rc('lines', linewidth=2.5)
#fig, ax = plt.subplots(layout="constrained")
fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=False, sharex=True, sharey=False)
fig.suptitle('Evolution of the temperatures of the Mosfets - Flyback circuit V2', fontsize=24, fontstyle='normal', weight='bold', x=0.5, y=0.94)
#fig.suptitle("\n".join(["Evolution of the temperatures of the Mosfets and the main transformer"]*2), y=0.95)

line1_1, = ax1.plot(time1, ch1_1, label='Higher Mosfet', color='r', linestyle='-')                     
#line1.set_dashes([2, 2, 10, 2])                                                                        # 2pt line, 2pt break, 10pt line, 2pt break.
#line1.set_dash_capstyle('round')
line1_2, = ax1.plot(time1, ch1_2, label='Lower Mosfet', color='b', linestyle='-')     
#line1_3, = ax1.plot(time1, ch1_3, label='Transformer Copper', color='g', linestyle='-')
#line1_4, = ax1.plot(time1, ch1_4, label='TRansformer Ferrite', color='y', linestyle='-')
line1_5, = ax1.plot(time1, ch1_5, dashes=[6, 2], label='Ambient', color='g')
#line1_4.set_dashes([2, 2, 10, 2])                                                                        # 2pt line, 2pt break, 10pt line, 2pt break.
#line1_4.set_dash_capstyle('round')

#line2, = ax.plot(time2, ch2_1, dashes=[6, 2], label='camera', color='r', linewidth=2, linestyle='-')             # using the dashes parameter
##line2, = ax.plot(time2, ch2_1, label='camera', color='r', linestyle='-')  

line2_1, = ax2.plot(time2, ch2_1, dashes=[5, 8], label='Higher Mosfet', color='r')   
line2_2, = ax2.plot(time2, ch2_2, dashes=[5, 8], label='Lower Mosfet', color='b')   
#line2_3, = ax2.plot(time2, ch2_3, dashes=[1, 8], label='Transformer (Box camera)', color='g')
#line2_4, = ax2.plot(time2, ch2_4, dashes=[1, 8], label='Ambient', color='g')              

ax1.set_xlabel('Time (s)', fontsize=16, fontstyle='normal', weight='bold')
ax1.set_ylabel('Temperatures Fiber Optic (°C)', fontsize=16, fontstyle='normal', weight='bold')
#ax1.set_xlim(min(time1[0],time2[0]), max(time1[line_count1-1], time2[line_count2-1]))
ax1.set_ylim(0, 120)
ax1.set_xlim(1000, 8000)
ax1.yaxis.set_tick_params(labelsize=16)             # taille de la police de graduation en y
#ax1.set_xlim(time1[0], time1[line_count1-1])
#ax1.set_xlim(34800, 44200)
ax1.legend(handlelength=4, loc = 'center right', fontsize=16)

ax2.set_xlabel('Time (s)', fontsize=16, fontstyle='normal', weight='bold')
ax2.set_ylabel('Temperatures Camera (°C)', fontsize=16, fontstyle='normal', weight='bold')
#ax1.set_xlim(min(time1[0],time2[0]), max(time1[line_count1-1], time2[line_count2-1]))
ax2.yaxis.set_tick_params(labelsize=16)             # taille de la police de graduation en y
ax2.xaxis.set_tick_params(labelsize=16)             # taille de la police de graduation en x
ax2.set_ylim(0, 120)
ax2.set_xlim(1000, 8000)
#ax2.set_xlim(time2[0], time2[line_count2-1])
#ax2.set_xlim(34800, 44200)
ax2.legend(handlelength=4, loc = 'center right', fontsize=16)

# %%
# -------------------------AFFICHAGE DES COURBES--------------------------
# Affichage des courbes à la suite, grâce à la commande "plt.ioff()" du début
plt.show()
plt.close()

# %%
# -------------------------ENREGISTREMENT FICHIERS--------------------------
fig.savefig(path_figure + 'Plot.png', transparent='None', dpi=200, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)
# Attention : il faut fermer manuellement les figures pour que les commandes soient prises en compte
#def save_fig(f1, f2, f3):
def save_fig(f1):
    fig.savefig(f1, dpi=200, pad_inches=0.1, format='pdf')
    #fig2.savefig(f2, dpi=600, format='pdf')
    #fig3.savefig(f3, dpi=600, format='pdf')
    print('Files saved !!')


#save_fig('Figures\\Plot1.pdf', 'Figures\\Plot2.pdf', 'Figures\\Plot3.pdf')
save_fig(path_figure + 'Plot1.pdf')