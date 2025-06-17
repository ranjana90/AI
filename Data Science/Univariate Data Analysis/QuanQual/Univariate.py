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
         
            