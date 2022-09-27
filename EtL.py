def EtL(file):
    # input file: xlsx file
    import warnings
    import pandas as pd
    warnings.simplefilter("ignore")
    name = pd.read_excel(file)
    name = name[10:].reset_index(drop = True)
    name.columns = name.iloc[0]
    name = name[1:].reset_index(drop = True)

    name = name.melt(id_vars=["Year"], 
            var_name="month", 
            value_name="PPI")


    name['month'].replace({'Jan': 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9,
           'Oct':10, 'Nov':11, 'Dec':12}, inplace = True)
    name['date'] = pd.to_datetime(name[['Year', 'month']].assign(DAY=1))

    name.drop(columns = ['month', 'Year'], inplace = True)

    name = name.dropna()

    name.PPI = name.PPI.astype(float).round(2)
    
    return name

freight = EtL('FREIGHT.xlsx')
diesel = EtL('DIESEL.xlsx')

diesel.rename(columns = {'PPI': 'DIESEL_PPI'}, inplace = True)

distribution_data = diesel
distribution_data['FREIGHT_PPI'] = freight['PPI']

distribution_data