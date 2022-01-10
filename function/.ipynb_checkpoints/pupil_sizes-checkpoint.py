# -*- coding: utf-8 -*-
"""Automatisation of the calcul of the diameter of the pupil"""

import pandas as pd 
import numpy as np


# adding the size of the pupil 
def pupil_size(df):
    
    '''
    This function are cleaning the columns and calcul the diameter of the pupil using Openface software
    Input : df with the timeline added
    Output : df with a new column with the diameter 
    '''

    # Rename columns to make it lighter
    left20= df[[" eye_lmk_X_20", " eye_lmk_Y_20", " eye_lmk_Z_20"]].rename(columns={' eye_lmk_X_20': 'x', ' eye_lmk_Y_20': 'y', ' eye_lmk_Z_20': 'z'})
    left21= df[[" eye_lmk_X_21", " eye_lmk_Y_21", " eye_lmk_Z_21"]].rename(columns={' eye_lmk_X_21': 'x', ' eye_lmk_Y_21': 'y', ' eye_lmk_Z_21': 'z'})
    left22= df[[" eye_lmk_X_22", " eye_lmk_Y_22", " eye_lmk_Z_22"]].rename(columns={' eye_lmk_X_22': 'x', ' eye_lmk_Y_22': 'y', ' eye_lmk_Z_22': 'z'})
    left23= df[[" eye_lmk_X_23", " eye_lmk_Y_23", " eye_lmk_Z_23"]].rename(columns={' eye_lmk_X_23': 'x', ' eye_lmk_Y_23': 'y', ' eye_lmk_Z_23': 'z'})
    left24= df[[" eye_lmk_X_24", " eye_lmk_Y_24", " eye_lmk_Z_24"]].rename(columns={' eye_lmk_X_24': 'x', ' eye_lmk_Y_24': 'y', ' eye_lmk_Z_24': 'z'})
    left25= df[[" eye_lmk_X_25", " eye_lmk_Y_25", " eye_lmk_Z_25"]].rename(columns={' eye_lmk_X_25': 'x', ' eye_lmk_Y_25': 'y', ' eye_lmk_Z_25': 'z'})
    left26= df[[" eye_lmk_X_26", " eye_lmk_Y_26", " eye_lmk_Z_26"]].rename(columns={' eye_lmk_X_26': 'x', ' eye_lmk_Y_26': 'y', ' eye_lmk_Z_26': 'z'})
    left27= df[[" eye_lmk_X_27", " eye_lmk_Y_27", " eye_lmk_Z_27"]].rename(columns={' eye_lmk_X_27': 'x', ' eye_lmk_Y_27': 'y', ' eye_lmk_Z_27': 'z'})

    # Pythagore formula to get the diameter
    def pythagore_dist_3D(p,q):
        return np.sqrt((p.x-q.x)**2+(p.y-q.y)**2+(p.z-q.z)**2)

    # Getting 4 diameters of opposed points
    diam1=pythagore_dist_3D(left24,left20)
    diam2=pythagore_dist_3D(left25,left21)
    diam3=pythagore_dist_3D(left26,left22)
    diam4=pythagore_dist_3D(left27,left23)

    # Mean calculation
    pupil_diam_mean = (diam1 + diam2 + diam3 + diam4)/4

    # Add pupil diameter to dataset
    df['pupil_diam_mean']=pupil_diam_mean
    # Cleaning the dataset with dropping culumns used for pupil size
    return df.drop([" face_id"," eye_lmk_X_20", " eye_lmk_Y_20", " eye_lmk_Z_20"
                    ," eye_lmk_X_21", " eye_lmk_Y_21", " eye_lmk_Z_21"
                    ," eye_lmk_X_22", " eye_lmk_Y_22", " eye_lmk_Z_22"
                    ," eye_lmk_X_23", " eye_lmk_Y_23", " eye_lmk_Z_23"
                    ," eye_lmk_X_24", " eye_lmk_Y_24", " eye_lmk_Z_24"
                    ," eye_lmk_X_25", " eye_lmk_Y_25", " eye_lmk_Z_25"
                    ," eye_lmk_X_26", " eye_lmk_Y_26", " eye_lmk_Z_26"
                    ," eye_lmk_X_27", " eye_lmk_Y_27", " eye_lmk_Z_27"," eye_lmk_X_48", " eye_lmk_Y_48", " eye_lmk_Z_48"
                    ," eye_lmk_X_49", " eye_lmk_Y_49", " eye_lmk_Z_49"
                    ," eye_lmk_X_50", " eye_lmk_Y_50", " eye_lmk_Z_50"
                    ," eye_lmk_X_51", " eye_lmk_Y_51", " eye_lmk_Z_51"
                    ," eye_lmk_X_52", " eye_lmk_Y_52", " eye_lmk_Z_52"
                    ," eye_lmk_X_53", " eye_lmk_Y_53", " eye_lmk_Z_53"
                    ," eye_lmk_X_54", " eye_lmk_Y_54", " eye_lmk_Z_54"
                    ," eye_lmk_X_55", " eye_lmk_Y_55", " eye_lmk_Z_55"],axis=1)