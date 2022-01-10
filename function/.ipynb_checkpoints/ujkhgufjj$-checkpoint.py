# -*- coding: utf-8 -*-
"""some helper functions."""

import pandas as pd 
import numpy as np
from datetime import *
import scipy.signal as ss
import matplotlib.pyplot as plt

def test_stat(df_merge,df_withsubject,FILE):
    '''
    INPUT : df merge with the BP_result and the initial 
    OUTPUT : df with all the stat for each test
    '''
    
    ## Survey 1 (T qu1) -----------------------------------------------------------
    timestamp_qu1 = str(df_merge['t_qu1_end_UC'][0])
    date_format_str = '%Y-%m-%d %H:%M:%S'
    end_time_qu1 = datetime.strptime(timestamp_qu1, date_format_str)

    t_qu1_start_REAL = end_time_qu1 - timedelta(minutes=3)
    delta_t1 = df_merge['t_qu1_end_UC'][0] - t_qu1_start_REAL

    # getting the rows for the first test
    mask = (df_withsubject['time'] >= t_qu1_start_REAL) & (df_withsubject['time'] <= df_merge['t_qu1_end_UC'][0])
    tqu1 = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time'] >= t_qu1_start_REAL) & (df_merge['time'] <= df_merge['t_qu1_end_UC'][0])
    tqu1_ = df_merge.loc[mask_]

    ## Cognitive test 1 (Cog1 Stroop) ----------------------------------------------
    start_cog1=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog1_STROOP_start'][0].hour,
                 minute=df_merge['cog1_STROOP_start'][0].minute,
                 second=df_merge['cog1_STROOP_start'][0].second)
    end_cog1=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog1_STROOP_end'][0].hour,
                 minute=df_merge['cog1_STROOP_end'][0].minute,
                 second=df_merge['cog1_STROOP_end'][0].second)
    delta_t2= end_cog1-start_cog1

    # getting the rows for the second test cog1
    mask = (df_withsubject['time']>=start_cog1) & (df_withsubject['time']<=end_cog1)
    cog1 = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time']>=start_cog1) & (df_merge['time']<=end_cog1)
    cog1_ = df_merge.loc[mask_]
    
    ## Cognitive test 2 ----------------------------------------------------------
    start_cog2=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog2_SART_start'][0].hour,
                 minute=df_merge['cog2_SART_start'][0].minute,
                 second=df_merge['cog2_SART_start'][0].second)
    end_cog2=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog2_SART_end'][0].hour,
                 minute=df_merge['cog2_SART_end'][0].minute,
                 second=df_merge['cog2_SART_end'][0].second)
    delta_t3=end_cog2-start_cog2

    # getting the rows for the third test cog2_SART_start
    mask = (df_withsubject['time']>=start_cog2) & (df_withsubject['time']<=end_cog2)
    cog2 = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time']>=start_cog2) & (df_merge['time']<=end_cog2)
    cog2_ = df_merge.loc[mask_]
    
    ##  Cog 3 NBACK -------------------------------------------------------------
    start_cog3=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog3_NBACK_start'][0].hour,
                 minute=df_merge['cog3_NBACK_start'][0].minute,
                 second=df_merge['cog3_NBACK_start'][0].second)
    end_cog3=pd.Timestamp(year=df_merge['date'][0].year,
                 month=df_merge['date'][0].month,
                 day=df_merge['date'][0].day,
                 hour=df_merge['cog3_NBACK_end'][0].hour,
                 minute=df_merge['cog3_NBACK_end'][0].minute,
                 second=df_merge['cog3_NBACK_end'][0].second)
    delta_t4=end_cog3-start_cog3

    # getting the rows for the third test cog3_NBACK_start
    mask = (df_withsubject['time']>=start_cog3) & (df_withsubject['time']<=end_cog3)
    cog3 = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time']>=start_cog3) & (df_merge['time']<=end_cog3)
    cog3_ = df_merge.loc[mask_]
    
    ## Creativity test (t creativity) -------------------------------------------
    start_creativity = df_merge['t_creativity_start_BH'][0]
    end_creativity = df_merge['t_creativity_end_UC'][0]
    delta_t5 = end_creativity-start_creativity

    # getting the rows for the creativity test
    mask = (df_withsubject['time']>df_merge['t_creativity_start_BH'][0]) & (df_withsubject['time']<df_merge['t_creativity_end_UC'][0])
    creativity = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time']>df_merge['t_creativity_start_BH'][0]) & (df_merge['time']<df_merge['t_creativity_end_UC'][0])
    creativity_ = df_merge.loc[mask_]
       
    ## Survey 2 (T qu2) ---------------------------------------------------------------
    timestamp_crea = str(end_creativity)
    end_time_crea = datetime.strptime(timestamp_crea, date_format_str)
    t_qu2_start_REAL = end_time_crea + timedelta(seconds=20)

    end_tqu2 = df_merge['t_qu2_end_UC'][0]
    delta_t6 = end_tqu2-t_qu2_start_REAL

    # getting the rows for the first test
    mask = (df_withsubject['time']>t_qu2_start_REAL) & (df_withsubject['time']<df_merge['t_qu2_end_UC'][0])
    tqu2 = df_withsubject.loc[mask]
    
    mask_ = (df_merge['time']>t_qu2_start_REAL) & (df_merge['time']<df_merge['t_qu2_end_UC'][0])
    tqu2_ = df_merge.loc[mask_]
    
    ##---------------------------------------------------------------------------------
    # printing the stat
    
    # Dmean pupil ---------------------------------------------------------------------        
#    for i,j in zip([tqu1, cog1, cog2, cog3, creativity, tqu2],
#              ['Survey 1','Cognitive test 1','Cognitive test 2',
#               'Cognitive test 3','Creative test','Survey 2']):
#        stat = i[[' AU45_r', 'pupil_diam_mean']].describe()
        
    
    df_stat= pd.DataFrame(index={FILE},data={
            'Survey 1 Dmean pupil' : tqu1['pupil_diam_mean'].describe()['mean']})

#    df_stat= pd.DataFrame(index={FILE},data={
#            'Survey 1 Dmean pupil' : tqu1['pupil_diam_mean'].describe()['mean'],
#            'Cognitive test 1 Dmean pupil' : cog1['pupil_diam_mean'].describe()['mean'], 
#            'Cognitive test 2 Dmean pupil' : cog2['pupil_diam_mean'].describe()['mean'],
#            'Cognitive test 3 Dmean pupil' : cog3['pupil_diam_mean'].describe()['mean'], 
#            'Creative test Dmean pupil' : creativity['pupil_diam_mean'].describe()['mean'],
#            'Survey 2 Dmean pupil' : tqu2['pupil_diam_mean'].describe()['mean']})
    
    
    
    # Blink rate ---------------------------------------------------------------------- 
    for i,j in zip([(tqu1,delta_t1,tqu1_), (cog1,delta_t2,cog1_), (cog2,delta_t3,cog2_), (cog3,delta_t4,cog3_), (creativity,delta_t5,creativity_), (tqu2,delta_t6,tqu2_)],
               ['Survey 1','Cognitive test 1','Cognitive test 2','Cognitive test 3','Creative test','Survey 2']):
        for k in [1]:
            # query the one over 1 or 0.5
            mask = i[0][' AU45_r'] > k
            filtered = i[0][mask]

            # to numpy in order to use findpeak function
            AU45_r_array = filtered[' AU45_r'].to_numpy()
            filtered = filtered.reset_index()

            # finding peaks
            peaks, _ = ss.find_peaks(AU45_r_array,prominence=0.1)
            peaks_as_time = filtered.loc[peaks]
            stat_blink=peaks_as_time.set_index("time").groupby(pd.Grouper(freq="1    min")).count()[' AU45_c']
            df_stat['Blink mean '+str(j)+' ['+ str(k) +']']=(60*len(peaks)/i[1].seconds) # mean by minute by test
            df_stat['Second blink mean '+str(j)+' ['+ str(k) +']']=(60*len(peaks)/i[1].seconds)/(i[0].shape[0]/i[2].shape[0]) # mean by minute by test
            
        df_stat['Total time of '+str(j)] = str(np.short(np.floor(i[1].seconds/60)))+" min "+str(np.short(i[1].seconds-np.floor(i[1].seconds/60)*60))+" sec"
        
        df_stat['Ratio kept '+str(j)] = str((i[0].shape[0]/i[2].shape[0])*100)
      
    
    # printing the dataframe -----------------------------------------------------------
    df_stat['exposure_nr']=df_merge['exposure_nr'][0]
    df_stat['session_ID']=df_merge['session_ID'][0]
    return df_stat.T
          
    
          



