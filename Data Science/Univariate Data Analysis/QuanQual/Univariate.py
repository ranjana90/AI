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

    def measureOfLocation(descriptive,dataset, columns):
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
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]] = descriptive[columnName]["Lesser"]
        
        for columnName in greater:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Greater"]] = descriptive[columnName]["Greater"]
        return dataset 
            