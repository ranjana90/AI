import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
    def centralTendency(descriptive,dataset, columns):
        for column in columns:
            descriptive[column]["Mean"]= dataset[column].mean()
            descriptive[column]["Median"]= dataset[column].median()
            descriptive[column]["Mode"]= dataset[column].mode()[0]
        return descriptive

    def measureOfLocation(dataset, columns):
        descriptive = pd.DataFrame(index=["Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max",
                                          "Kurtosis","Skew","Variance","StandeardDeviation"], columns=columns)
        for column in columns:
            descriptive[column]["Q1:25%"]= dataset.describe()[column]["25%"]  #np.percentile(dataset[column],25)
            descriptive[column]["Q2:50%"]= dataset.describe()[column]["50%"]  #np.percentile(dataset[column],50)
            descriptive[column]["Q3:75%"]= dataset.describe()[column]["75%"]  #np.percentile(dataset[column],75)
            descriptive[column]["Q4:100%"]= dataset.describe()[column]["max"]
            descriptive[column]["IQR"]= descriptive[column]["Q3:75%"] - descriptive[column]["Q1:25%"]
            descriptive[column]["1.5Rule"]= 1.5*descriptive[column]["IQR"]
            descriptive[column]["Lesser"]= descriptive[column]["Q1:25%"]-descriptive[column]["1.5Rule"]
            descriptive[column]["Greater"]= descriptive[column]["Q3:75%"]+descriptive[column]["1.5Rule"]
            descriptive[column]["Min"]= dataset[column].min()
            descriptive[column]["Max"]= dataset[column].max()   
            descriptive[column]["Kurtosis"]= dataset[column].kurtosis()   
            descriptive[column]["Skew"]= dataset[column].skew()
            descriptive[column]["Variance"]= dataset[column].var()
            descriptive[column]["StandeardDeviation"]= dataset[column].std()
        return descriptive
    def findingOutlier(descriptive, columns):
        #Finding outlier
        lesser = list()
        greater = list()
        for column in columns:
            if descriptive[column]["Min"] < descriptive[column]["Lesser"]:
                lesser.append(column)
            if descriptive[column]["Max"] > descriptive[column]["Greater"]:
                greater.append(column)
        return lesser, greater

    def replaceTheOutlier(descriptive, dataset, lesser, greater):
        # Replace the outliner
        for columnName in lesser:            
            dataset[columnName][dataset[columnName] < descriptive[columnName]["Lesser"]] = descriptive[columnName]["Lesser"]                    
        for columnName in greater:
            dataset[columnName][dataset[columnName] > descriptive[columnName]["Greater"]] = descriptive[columnName]["Greater"]
        return dataset 
        
    def frequencyTable(dataset, column_name):
        freq_table = pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","Cusum"])
        freq_table["Unique_values"] = dataset[column_name].value_counts().index
        freq_table["Frequency"] = dataset[column_name].value_counts().values
        freq_table["Relative_Frequency"] = (freq_table["Frequency"]/103)
        freq_table["Cusum"] = freq_table["Relative_Frequency"].cumsum()
        return freq_table

    def CreateImputerForReplaceNan(dataset_type, dataset, column_list):
        
        if "Quantitative" in dataset_type:
            strategy='mean'
            print("Quantitative")
        else:
            strategy='most_frequent'
            print(False)

        # Create an imputer to replace NaN values with the mean of each column
        imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
        
        # Fit the imputer and transform the data
        imputer.fit(dataset[column_list])
        ds = imputer.transform(dataset[column_list])
        processed_df = pd.DataFrame(ds, columns= column_list)
        return processed_df
        
        
    def replaceQualitativeColumn(dataset, column_names):
        for column in column_names:
            most_frequent = dataset[column].mode()[0]
            dataset[column] = dataset[column].fillna(most_frequent)
        return dataset