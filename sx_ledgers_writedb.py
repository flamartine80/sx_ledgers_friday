#%%

import pandas as pd
import xlwings as xw
import numpy as np
pd.set_option('display.max_columns', 1000, 'display.max_rows',1000, 'display.max_colwidth', None)
import psycopg2
import psycopg2.extras as extras
from sqlalchemy import create_engine


# z: 2018,a :2019, b:2020; c:2021; d:2022

# locations
d_location = r"C:\Users\fernando.lamartine\Box\0 - Personal Working Folders (F Lamartine)\SX Chile General Ledgers\20221231_SX Chile_General Ledger Dic22 (Acum).xlsx"
c_location = r"C:\Users\fernando.lamartine\Box\0 - Personal Working Folders (F Lamartine)\SX Chile General Ledgers\20211231_SX Chile_General Ledger Dic21 (Acum).xlsx"
b_location = r"C:\Users\fernando.lamartine\Box\0 - Personal Working Folders (F Lamartine)\SX Chile General Ledgers\20201231_SX Chile_General Ledger Dec20 (Acum).xlsx"
a_location = r"C:\Users\fernando.lamartine\Box\0 - Personal Working Folders (F Lamartine)\SX Chile General Ledgers\20191231_SX Chile_General Ledger December 2019 (Acum).xlsx"

d_fileName = "20221231_SX Chile_General Ledger Dic22 (Acum).xlsx"
c_fileName = "20211231_SX Chile_General Ledger Dic21 (Acum).xlsx"
b_fileName = "20201231_SX Chile_General Ledger Dec20 (Acum).xlsx"
a_fileName = "20191231_SX Chile_General Ledger December 2019 (Acum).xlsx"
z_fileName = '2018_mayor_SXChile.xlsx'


dump_fileName = "sxLedgers_dumpFile.xlsx"

d_rangeData = 'a1:o40000'
c_rangeData = 'a1:o40000'
b_rangeData = 'a1:o40000'
a_rangeData = 'a1:o40000'
z_rangeData = 'a1:o40000'

dump_rangeData = 'a1'
dump_rangeData_delete = 'a1:z30000'

d_sheet = 'CW202301265BEB'
c_sheet = 'CW20220126B561'
b_sheet = 'USD'
a_sheet = 'CW202001218740'
z_sheet = '2018'


dump_sheet = 'Sheet1'
dump_sheet_2 = 'Sheet2'


d_book = xw.Book(d_fileName)
c_book = xw.Book(c_fileName)
b_book = xw.Book(b_fileName)
a_book = xw.Book(a_fileName)
z_book = xw.Book(z_fileName)

x_book = xw.Book(a_fileName)
#---------D : 2022-------------------------------------------------------------------------------------------------------------

# Make DataFrame from spreadsheet
d_data = d_book.sheets(d_sheet).range(d_rangeData).value
df_d = pd.DataFrame(d_data)

#drop unnecesary columns
df_d_2 = df_d.drop([5,6,7,10], axis=1)
df_d_3 = df_d_2[df_d_2[0].str.contains('SALDO ANTERIOR')==False]
df_d_4 = df_d_3.dropna(thresh=2)

# ACCOUNT NAMES
df_d_accounts = df_d_2[df_d_2[0].str.contains('SALDO ANTERIOR')==True]

#MAKING ROW ONE THE HEADER
df_d_4.columns = df_d_4.iloc[0]
df_d_4 = df_d_4[1:]

#DATE PARSING
df_d_4['FECHA']=pd.to_datetime(df_d_4['FECHA'], dayfirst=True)

#--------------C : 2021--------------------------------------------------------------------------------------------------------

#MAKE DATAFRAME FROM SPREADSHEET
c_data = c_book.sheets(c_sheet).range(c_rangeData).value
df_c = pd.DataFrame(c_data)

#DROP UNNECESARY COLUMNS
df_c_2 = df_c.drop([5,6,7,10], axis=1)
df_c_3 = df_c_2[df_c_2[0].str.contains('SALDO ANTERIOR')==False]
df_c_4 = df_c_3.dropna(thresh=2)

# ACCOUNT NAMES
df_c_accounts = df_c_2[df_c_2[0].str.contains('SALDO ANTERIOR')==True]

#MAKING ROW ONE THE HEADER
df_c_4.columns = df_c_4.iloc[0]
df_c_4 = df_c_4[1:]

#PARSE DATE
df_c_4['FECHA']=pd.to_datetime(df_c_4['FECHA'],dayfirst=True)
#
#--------------B : 2020--------------------------------------------------------------------------------------------------------

#MAKE DATAFRAME FROM SPREADSHEET
b_data = b_book.sheets(b_sheet).range(b_rangeData).value
df_b = pd.DataFrame(b_data)

#DROP UNNECESARY COLUMNS
df_b_2 = df_b.drop([5,6,7,10], axis=1)
df_b_3 = df_b_2[df_b_2[0].str.contains('SALDO ANTERIOR')==False]
df_b_4 = df_b_3.dropna(thresh=2)

# ACCOUNT NAMES
df_b_accounts = df_b_2[df_b_2[0].str.contains('SALDO ANTERIOR')==True]

#MAKING ROW ONE THE HEADER
df_b_4.columns = df_b_4.iloc[0]
df_b_4 = df_b_4[1:]

#PARSE DATE
df_b_4['FECHA']=pd.to_datetime(df_b_4['FECHA'],dayfirst=True)
#
#--------------A : 2019--------------------------------------------------------------------------------------------------------


#MAKE DATAFRAME FROM SPREADSHEET
a_data = a_book.sheets(a_sheet).range(a_rangeData).value
df_a = pd.DataFrame(a_data)

#DROP UNNECESARY COLUMNS
df_a_2 = df_a.drop([5,6,7,10], axis=1)
df_a_3 = df_a_2[df_a_2[0].str.contains('SALDO ANTERIOR')==False]
df_a_4 = df_a_3.dropna(thresh=2)

# ACCOUNT NAMES
df_a_accounts = df_a_2[df_a_2[0].str.contains('SALDO ANTERIOR')==True]

#MAKING ROW ONE THE HEADER
df_a_4.columns = df_a_4.iloc[1]
df_a_4 = df_a_4[2:]

#PARSE DATE
df_a_4['FECHA']=pd.to_datetime(df_a_4['FECHA'],dayfirst=True)

# --------------Z : 2018--------------------------------------------------------------------------------------------------------

# MAKE DATAFRAME FROM SPREADSHEET
z_data = z_book.sheets(z_sheet).range(z_rangeData).value
df_z = pd.DataFrame(z_data)

#DROP UNNECESARY COLUMNS
df_z_2 = df_z.drop([5,6,7,10], axis=1)
df_z_3 = df_z_2[df_z_2[0].str.contains('SALDO ANTERIOR')==False]
df_z_4 = df_z_3.dropna(thresh=2)

# ACCOUNT NAMES76
df_z_accounts = df_z_2[df_z_2[0].str.contains('SALDO ANTERIOR')==True]

#MAKING ROW ONE THE HEADER
df_z_4.columns = df_z_4.iloc[0]
df_z_4 = df_z_4[1:]

#PARSE DATE
df_z_4['FECHA']=pd.to_datetime(df_z_4['FECHA'],dayfirst=True)

# #-----------------------------------------------------------------------------------------------------------------------

joined_years = pd.concat([df_z_4,df_a_4,df_b_4,df_c_4,df_d_4])

acct_uniques = joined_years['CUENTA'].unique()

ACCOUNT = joined_years['CUENTA'].str.split(n=1, expand=True)
joined_years['NRO CUENTA'] = ACCOUNT[0]
joined_years['NOMBRE CUENTA'] = ACCOUNT[1]

#SECOND SPLIT

NOMBRE_CUENTA = joined_years['NOMBRE CUENTA'].str.split("/", n=1, expand=True)
joined_years['Account Name - English'] =NOMBRE_CUENTA[0]
joined_years['Account Name - Spanish'] = NOMBRE_CUENTA[1]

# acct_uniques= pd.Series(acct_uniques)


# acct_uniques.str.split(n=1, expand=True)

tagua_tagua = joined_years[joined_years['DESCRIPCION'].str.contains( 'TAGUA TAGUA|taguatagua', case=False ) == True]
tres_cruces = joined_years[joined_years['DESCRIPCION'].str.contains( 'tres cruces', case=False ) == True]
andino = joined_years[joined_years['DESCRIPCION'].str.contains( 'ANDINO', case=False ) == True]
storage = joined_years[joined_years['DESCRIPCION'].str.contains( 'storage', case=False ) == True]
pelequen = joined_years[joined_years['DESCRIPCION'].str.contains( 'pelequen', case=False ) == True]
quebradaTalca = joined_years[joined_years['DESCRIPCION'].str.contains( 'talca', case=False ) == True]
greenfield = joined_years[joined_years['DESCRIPCION'].str.contains( 'greenfield', case=False ) == True]
domeyko = joined_years[joined_years['DESCRIPCION'].str.contains( 'domeyko', case=False ) == True]
corso = joined_years[joined_years['DESCRIPCION'].str.contains( 'santa lucia', case=False ) == True]
angamos = joined_years[joined_years['DESCRIPCION'].str.contains( 'angamos', case=False ) == True]
santaLucia = joined_years[joined_years['DESCRIPCION'].str.contains( 'santa lucia', case=False ) == True]
donDario = joined_years[joined_years['DESCRIPCION'].str.contains( 'don dario', case=False ) == True]



joined_years['tagua_tagua'  ]   =joined_years['DESCRIPCION'].str.contains('TAGUA TAGUA|taguatagua', case=False)
joined_years['tres_cruces'  ]   =joined_years['DESCRIPCION'].str.contains('tres cruces', case=False)
joined_years['andino'  ]        =joined_years['DESCRIPCION'].str.contains('ANDINO', case=False)
joined_years['storage'  ]       =joined_years['DESCRIPCION'].str.contains('storage', case=False)
joined_years['pelequen'  ]      =joined_years['DESCRIPCION'].str.contains('pelequen', case=False)
joined_years['quebrada_Talca' ]  =joined_years['DESCRIPCION'].str.contains('talca', case=False)
joined_years['greenfield'  ]    =joined_years['DESCRIPCION'].str.contains('greenfield', case=False)
joined_years['domeyko'  ]       =joined_years['DESCRIPCION'].str.contains('domeyko', case=False)
joined_years['corso'  ]         =joined_years['DESCRIPCION'].str.contains('santa lucia', case=False)
joined_years['angamos'  ]       =joined_years['DESCRIPCION'].str.contains('angamos', case=False)
joined_years['santa_Lucia'  ]    =joined_years['DESCRIPCION'].str.contains('santa lucia', case=False)
joined_years['don_Dario'  ]    =joined_years['DESCRIPCION'].str.contains('don dario', case=False)


def check_false(*args):
    base = list(args)
    condition = all(i == False for i in base)
    if condition == True:
        return True
    else:
        return False


joined_years['Non Projects'] = joined_years.apply(lambda x: check_false(
    x['tagua_tagua'],
    x['tres_cruces'],
    x['andino'],
    x['storage'],
    x['pelequen'],
    x['quebrada_Talca'],
    x['greenfield' ],
    x['domeyko' ],
    x['corso'],
    x['angamos'],
    x['santa_Lucia'],
    x['don_Dario'],
), axis=1)

#
# # #INFORMATION WRITE TO EXCEL
# xw.Book(dump_fileName).sheets(dump_sheet).range(dump_rangeData_delete).value = ""
# xw.Book(dump_fileName).sheets(dump_sheet).range(dump_rangeData).value = joined_years
# # xw.Book(dump_fileName).sheets(dump_sheet_2).range(dump_rangeData_delete).value = ""
# # xw.Book(dump_fileName).sheets(dump_sheet_2).range("a1:a1000").value = acct_uniques
#




original_columns = ['CUENTA',
                    'FECHA',
                    'N° COMPROBANTE',
                    'TIPO',
                    'N° INTERNO',
                    'TIPO DOC.',
                    'NUMERO DOC',
                    ' DEBE',
                    'HABER',
                    'SALDO',
                    'DESCRIPCION',
                    'NRO CUENTA',
                    'NOMBRE CUENTA',
                    'Account Name - English',
                    'Account Name - Spanish',
                    'tagua_tagua',
                    'tres_cruces',
                    'andino',
                    'storage',
                    'pelequen',
                    'quebrada_Talca',
                    'greenfield',
                    'domeyko',
                    'corso',
                    'angamos',
                    'santa_Lucia',
                    'don_Dario',
                    'Non Projects']

changed_columns = {
                    'N° COMPROBANTE':'nro_comprobante',
                    'N° INTERNO':'nro_interno',
                    'TIPO DOC.':'tipo_doc',
                    'NUMERO DOC':'nro_doc',
                    'NRO CUENTA':'nro_cuenta',
                    'NOMBRE CUENTA':'nombre_cuenta',
                    'Account Name - English':'acct_name_eng',
                    'Account Name - Spanish':'acct_name_spa',
                    'Non Projects':'non_projects',
}



joined_years[joined_years['Non Projects']==False]
joined_years.rename(columns = changed_columns,inplace=True)
df = joined_years


relevant_cols = [ 'FECHA',
       ' DEBE', 'HABER', 'SALDO', 'DESCRIPCION', 'nro_cuenta',
       'nombre_cuenta', 'acct_name_eng', 'acct_name_spa', 'tagua_tagua',
       'tres_cruces', 'andino', 'storage', 'pelequen', 'quebrada_Talca',
       'greenfield', 'domeyko', 'corso', 'angamos', 'santa_Lucia', 'don_Dario',
       'non_projects']



relevant_cols_subset = [ 'FECHA',
       ' DEBE', 'HABER', 'SALDO', 'DESCRIPCION', 'nro_cuenta',
       'nombre_cuenta']


#project cols missing
joined_years_relevant = joined_years[relevant_cols_subset]


data = joined_years_relevant.iloc[5:7,]
table = 'consolidated_info_2'

def execute_values(conn, df, table):
    tuples = [tuple( x ) for x in df.to_numpy()]
    cols = ','.join( list( df.columns ) )
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values( cursor, query, tuples )
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print( "Error: %s" % error )
        conn.rollback()
        cursor.close()
        return query
    print( "the dataframe is inserted" )
    cursor.close()
    # return query
# conn_string = create_engine('postgresql+psycopg2://postgres:Rondamon_1988@database-2.culhcfcdryty.us-east-2.rds.amazonaws.com/sonnedix_chile')

# conn = psycopg2.connect( database='sonnedix_chile', user='postgres', password='Rondamon_1988', host='database-2.culhcfcdryty.us-east-2.rds.amazonaws.com',
#     port='5432' )

conn = psycopg2.connect( database='sx_chile_local', user='postgres', password='Zenon_1917',
                         host='localhost',port='5432' )


df = joined_years_relevant

execute_values( conn, df, 'consolidated_info_2' )

# xw.Book('sxLedgers_dumpFile.xlsx').sheets('Sheet1').range('a1:ao80000').value = ""
# xw.Book('sxLedgers_dumpFile.xlsx').sheets('Sheet1').range('a1').value = joined_years_relevant





