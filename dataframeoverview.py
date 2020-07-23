"""This Utility Script provides functions that will provide an overview of a pandas dataframe
Objectives :
- Understand the Dataset and it's features better
- Perform tasks like automated removal of missing values based on a threshold
- Identifying the types of features
"""

# Library Imports
import pandas as pd


def feature_info(df):
    """Function returns dataframe with the necessary information about features of the dataset"""
    f_type = [df[f].dtype for f in df.columns]
    f_size = [len(df[f]) for f in df.columns]
    f_miss_percent = [round(((max(f_size)-val)/max(f_size))*100,2) for val in f_size]
    
    # Construct the dataframe
    feature_df = pd.DataFrame({"Feature_Name":df.columns, "Feature_Type":f_type, "Missing_Val_%":f_miss_percent})
    
    return feature_df

def remove_features(df, threshold=0.50):
    """Function returns dataframe after removing those features with a missing value percentage above a given threshold"""
    f_dataframe = feature_info(df)
    above_thresh = list(f_dataframe[(f_dataframe["Missing_Val_%"]>threshold)]["Feature_Name"])
    post_removal_df = df.drop(above_thresh, axis=1)
    
    return post_removal_df

def clean_feature_names(df):
    """Function returns dataframe with spaces and newlines replaced by underscores in feature names"""
    clean_feat = []
    for f in df.columns:
        clean_feat.append(((f.casefold()).replace("\n","_")).replace(" ","_"))
    df=df.rename(columns=dict(zip(df.columns,clean_feat)))
    
    return df

"""Future Versions will include further modules"""