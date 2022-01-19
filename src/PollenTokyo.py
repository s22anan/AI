import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
url = 'https://www.fukushihoken.metro.tokyo.lg.jp/allergy/pollen/data/herbaceous.html'
dfs = pd.read_html(url)

#print(len(dfs))

#print(dfs[1].head())

tiyo = dfs[1].set_index('観測期間')
sugi = dfs[2].set_index('観測期間')
oum = dfs[3].set_index('観測期間')
hatio= dfs[4].set_index('観測期間')
tam = dfs[5].set_index('観測期間')
mati= dfs[6].set_index('観測期間')
tachi = dfs[7].set_index('観測期間')
fuc = dfs[8].set_index('観測期間')
koda = dfs[9].set_index('観測期間')

tiki_list =["tiyoda","suginami","oumi","hatioji","tama","matida","tachikawa","fuchu","kodaira"]



if len(sys.argv)==2:
    if sys.argv[1] in tiki_list:
        if 'tiyoda'==str(sys.argv[1]):
            tiyo.plot()
            plt.savefig("kafun.png")
            plt.show()
            
        elif 'suginami'==str(sys.argv[1]):
            sugi.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'oumi'==str(sys.argv[1]):
            oum.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'hatioji'==str(sys.argv[1]):
            hatio.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'tama'==str(sys.argv[1]):
            tam.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'matida'==str(sys.argv[1]):
            mati.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'tachikawa'==str(sys.argv[1]):
            tachi.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'fuchu'==str(sys.argv[1]):
            fuc.plot()
            plt.savefig("kafun.png")
            plt.show()
        elif 'kodaira'==str(sys.argv[1]):
            koda.plot()
            plt.savefig("kafun.png")
            plt.show()
    else:
        print('その地域はありません。順次更新予定です')


