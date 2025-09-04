# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path

'''
1. temperature and ph # normal
2. Ammonia (with avg line) # require changes
3. nitrate
4. phosphate
5. Chlorine
6. DO

Maybe make as a pannel
Graphs per annunum 

Could we make it live. 
'''



def graphsForCitizenScience(dataLocation, site, dateStart, dateEnd, outputLocation, save=False):
    
    
    #### if wanting saveed then this will create a folder by sitename and date
    
    if save:
        output = make_folder(outputLocation, site)
    else:
        output = 'nothing'
    
    ## read in data
    df = pd.read_csv(dataLocation)    
    

    ## headings weren't aligned for some of the data
    # fix headings:
    df_cols_8_13 = df.iloc[0, 7:13].values  # index 7 to 12 inclusive

    # replace column names for these columns
    df.columns.values[7:13] = df_cols_8_13


    ### get to just site in question
    df = df[df['Site']==site]
    
    
    ### get to just wanted dates
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')        

    mask = (df['Date'] >= pd.to_datetime(dateStart)) & (df['Date'] <= pd.to_datetime(dateEnd))
    maindf = df.loc[mask]
    
    
    ## make the individual graphs
    # temperature 
    PhTempGraph(maindf, site, save, output)
    
    ### all other graphs this loops through the titles and makes a graph
    for i in ['Chlorine Free (mg/L)',
        'Chlorine Total (mg/L)',
        'Ammonia + Nitrogen(mg/L)',
        'Nitrate (mg/L)',
        'Phosphate (mg/L)',
        'D.O. (mg/L)']:
        plotSimple(i, maindf, site, save, output)
    
    # Make a panel of all of these:
    panel(maindf, site, save, output)
    
    
    print('Done')






#%%
def PhTempGraph(df, sitename, save, output):
    fig, ax1 = plt.subplots() 
    
    # get temperature 
    df['Temp (°C)'] = pd.to_numeric(df['Temp (°C)'], errors='coerce')
    Tdf = df[['Date','Temp (°C)']].dropna().sort_values('Date')
    
    # get ph
    df['pH'] = pd.to_numeric(df['pH'], errors='coerce')
    Pdf = df[['Date','pH']].dropna().sort_values('Date')
    
    
    ax1.plot(Tdf['Date'], Tdf['Temp (°C)'], label='Temp (°C)', color='tab:blue')
    ax1.set_ylabel('Temperature (°C)', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.plot(Pdf['Date'], Pdf['pH'], label='pH', color='tab:red')
    ax2.set_ylabel('Ph', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    plt.xlabel('Date')
    plt.title(f"Water Quality at {sitename}")

    fig.legend(loc='upper center', ncol=2)
    plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")

    if save:
        save_path = output / f"phTemperature.png"
        fig.savefig(save_path, dpi=600, bbox_inches="tight")



#%%
def plotSimple(item, df, sitename, save, output):
    """
    items: list of simplified column names (e.g. ['Ph', 'Nitrate'])
    df: your pandas DataFrame
    """
    plt.figure(figsize=(10,6))
    df[item] = pd.to_numeric(df[item], errors='coerce')
    ndf = df[['Date',item]].dropna().sort_values('Date')
    plt.plot(ndf['Date'], ndf[item], label=item)

 

    plt.xlabel("Date")
    if item == 'Temp':
        plt.ylabel("Degrees °C")
    elif item == 'Ph':
        plt.ylabel("Ph")
    else:
        plt.ylabel("Mg/L")

    plt.title(f"Water Quality at {sitename}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        save_path = output / f"{item.replace('/', '').replace('\\', '')}.png"
        plt.savefig(save_path, dpi=600, bbox_inches="tight")
    
#%%
   
def panel(df, sitename, save, output):
    
    # create plot to fit items
    fig, ax = plt.subplots(4,2, sharex=True, figsize=(10,20))
    axes = ax.flatten()
    
    # get them all as options
    itemsList =     ['Temp (°C)', 'pH', 
                     'Chlorine Free (mg/L)',
                     'Chlorine Total (mg/L)',
                     'Ammonia + Nitrogen(mg/L)',
                     'Nitrate (mg/L)',
                     'Phosphate (mg/L)',
                    'D.O. (mg/L)']



    for i in range(8):
        item = itemsList[i]
        
        df[item] = pd.to_numeric(df[item], errors='coerce')
        ndf = df[['Date',item]].dropna().sort_values('Date')
        
        axes[i].plot(ndf['Date'], ndf[item], label=item)
        axes[i].legend()



    plt.setp(axes[-1].get_xticklabels(), rotation=45, ha="right")
    plt.setp(axes[-2].get_xticklabels(), rotation=45, ha="right")

    fig.suptitle(f"Water Quality at {sitename}", fontsize=14)
    
    if save:
        save_path = output / f"Pannel.png"
        fig.savefig(save_path, dpi=600, bbox_inches="tight")

    plt.tight_layout()
    plt.show()
    
#%% generic function

def make_folder(location_var, varName):
    folder_path = Path(location_var) / varName
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


    
#%% run this 
# plt.close('all')
# dataLocation = r"C:\Users\Svalm\OneDrive - East Mercia Rivers Trust\GeneralEMRT\pythonForDominika\Horncastle Citizen Science Data Sheet_03Sep2025.csv"
# site = 'Site 30'
# graphsForCitizenScience(dataLocation, site, dateStart=('12/12/2000'), dateEnd=('12/12/2030'), outputLocation=r"C:\Users\Svalm\Downloads", save=True)



    
    
    
    
    