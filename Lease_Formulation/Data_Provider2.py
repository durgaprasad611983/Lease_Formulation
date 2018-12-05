#!/opt/conda/bin/python

import configparser
vAR_Config = configparser.ConfigParser(allow_no_value=True)
vAR_Config.read('/opt/conda/bin/Lease_Formulation/Lease_Formulation/DS_LEASE_ACCOUNTING_MODEL_CONS_INI_FILE1.INI')
vAR_Data = vAR_Config.sections()
vAR_Config.sections()

import pandas as vAR_pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

vAR_Fetched_Path_Train_Unplanned_Expenses_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TRAINING_DATA_UNPLANNED_EXPENSES_OD']
#print(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)

vAR_Fetched_Path_Test_Unplanned_Expenses_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_UNPLANNED_EXPENSES_OD']
#print(vAR_Fetched_Path_Test_Unplanned_Expenses_OD)

vAR_Fetched_Path_Test_Lease_Extension_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_LEASE_EXTENSION_OD']
#print(vAR_Fetched_Path_Test_Lease_Extension_OD)

vAR_Fetched_Path_Test_Extension_Terms_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_EXTENSION_TERMS_OD']
#print(vAR_Fetched_Path_Test_Lease_Extension_OD)

vAR_Fetched_Path_Test_IBR_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_IBR_OD']
#print(vAR_Fetched_Path_Test_IBR_OD)

vAR_Fetched_Path_Test_Lease_Amount_OD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_LEASE_AMOUNT_OD']
#print(vAR_Fetched_Path_Test_Lease_Amount_OD)

vAR_Fetched_Path_Predicted_Lease_Amount_OD = vAR_Config['PROBLEM1 CONFIGURATION']['LEASE_AMOUNT_PREDICTION_OD']
#print(vAR_Fetched_Path_Predicted_Lease_Amount_OD)

vAR_Fetched_Path_Best_Fit_OD = vAR_Config['PROBLEM1 CONFIGURATION']['BEST_FIT_DATA_PATH_OD']
#print(vAR_Fetched_Path_Best_Fit_OD)

vAR_Fetched_Path_Under_Fit_OD = vAR_Config['PROBLEM1 CONFIGURATION']['UNDER_FIT_DATA_PATH_OD']
#print(vAR_Fetched_Path_Under_Fit_OD)

vAR_Fetched_Path_Over_Fit_OD = vAR_Config['PROBLEM1 CONFIGURATION']['OVER_FIT_DATA_PATH_OD']
#print(vAR_Fetched_Path_Over_Fit_OD)

vAR_Fetched_Path_Train_Unplanned_Expenses_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TRAINING_DATA_UNPLANNED_EXPENSES_YD']
#print(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)

vAR_Fetched_Path_Train_Lease_Extension_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TRAINING_DATA_LEASE_EXTENSION_YD']
#print(vAR_Fetched_Path_Train_Lease_Extension_YD)

vAR_Fetched_Path_Test_Unplanned_Expenses_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_UNPLANNED_EXPENSES_YD']
#print(vAR_Fetched_Path_Test_Unplanned_Expenses_YD)

vAR_Fetched_Path_Test_Lease_Extension_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_LEASE_EXTENSION_YD']
#print(vAR_Fetched_Path_Test_Lease_Extension_YD)

vAR_Fetched_Path_Test_Extension_Terms_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_EXTENSION_TERMS_YD']
#print(vAR_Fetched_Path_Test_Lease_Extension_YD)

vAR_Fetched_Path_Test_IBR_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_IBR_YD']
#print(vAR_Fetched_Path_Test_IBR_YD)

vAR_Fetched_Path_Test_Lease_Amount_YD = vAR_Config['PROBLEM1 CONFIGURATION']['TEST_DATA_LEASE_AMOUNT_YD']
#print(vAR_Fetched_Path_Test_Lease_Amount_YD)

vAR_Fetched_Path_Predicted_Lease_Amount_YD = vAR_Config['PROBLEM1 CONFIGURATION']['LEASE_AMOUNT_PREDICTION_YD']
#print(vAR_Fetched_Path_Predicted_Lease_Amount_YD)

vAR_Fetched_Path_Best_Fit_YD = vAR_Config['PROBLEM1 CONFIGURATION']['BEST_FIT_DATA_PATH_YD']
#print(vAR_Fetched_Path_Best_Fit_YD)

vAR_Fetched_Path_Under_Fit_YD = vAR_Config['PROBLEM1 CONFIGURATION']['UNDER_FIT_DATA_PATH_YD']
#print(vAR_Fetched_Path_Under_Fit_YD)

vAR_Fetched_Path_Over_Fit_YD = vAR_Config['PROBLEM1 CONFIGURATION']['OVER_FIT_DATA_PATH_YD']
#print(vAR_Fetched_Path_Over_Fit_YD)

vAR_Fetched_Feature1 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE1']
#print(vAR_Fetched_Feature1)

vAR_Fetched_Feature2 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE2']
#print(vAR_Fetched_Feature2)

vAR_Fetched_Feature3 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE3']
#print(vAR_Fetched_Feature3)

vAR_Fetched_Feature4 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE4']
#print(vAR_Fetched_Feature4)

vAR_Fetched_Feature5 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE5']
#print(vAR_Fetched_Feature5)

vAR_Fetched_Feature6 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE6']
#print(vAR_Fetched_Feature6)

vAR_Fetched_Feature7 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE7']
#print(vAR_Fetched_Feature7)

vAR_Fetched_Feature8 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE8']
#print(vAR_Fetched_Feature8)

vAR_Fetched_Feature9 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE9']
#print(vAR_Fetched_Feature9)

vAR_Fetched_Feature10 = vAR_Config['PROBLEM1 CONFIGURATION']['FEATURE10']
#print(vAR_Fetched_Feature10)

vAR_Fetched_Label1 = vAR_Config['PROBLEM1 CONFIGURATION']['LABEL1']
#print(vAR_Fetched_Label1)

vAR_Fetched_Label2 = vAR_Config['PROBLEM1 CONFIGURATION']['LABEL2']
#print(vAR_Fetched_Label2)

vAR_Fetched_Label3 = vAR_Config['PROBLEM1 CONFIGURATION']['LABEL3']
#print(vAR_Fetched_Label3)

vAR_Fetched_Label4 = vAR_Config['PROBLEM1 CONFIGURATION']['LABEL4']
#print(vAR_Fetched_Label4)

vAR_Fetched_Label5 = vAR_Config['PROBLEM1 CONFIGURATION']['LABEL5']
#print(vAR_Fetched_Label5)

vAR_df = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)

vAR_Feature1 = vAR_df[vAR_Fetched_Feature1]
vAR_Feature2 = vAR_df[vAR_Fetched_Feature2]
vAR_Feature3 = vAR_df[vAR_Fetched_Feature3]
vAR_Feature4 = vAR_df[vAR_Fetched_Feature4]
vAR_Feature5 = vAR_df[vAR_Fetched_Feature5]
vAR_Feature6 = vAR_df[vAR_Fetched_Feature6]
vAR_Feature7 = vAR_df[vAR_Fetched_Feature7]
vAR_Feature8 = vAR_df[vAR_Fetched_Feature8]
vAR_Feature9 = vAR_df[vAR_Fetched_Feature9]
vAR_Feature10 = vAR_df[vAR_Fetched_Feature10]

vAR_Label1 = vAR_df[vAR_Fetched_Label1]
vAR_Label2 = vAR_df[vAR_Fetched_Label2]
vAR_Label3 = vAR_df[vAR_Fetched_Label3]
vAR_Label4 = vAR_df[vAR_Fetched_Label4]
vAR_Label5 = vAR_df[vAR_Fetched_Label5]

vAR_model = LinearRegression()
vAR_model1 = LogisticRegression()
vAR_model2 = LinearRegression()
vAR_model3 = LinearRegression()
vAR_model4 = LinearRegression()

vAR_df = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df = vAR_df[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df1 = vAR_df.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
#vAR_df2 = vAR_df1.merge(vAR_Asset_Location_Conversion_df,left_index=True, right_index=True)

## Fetching Train Data Features & Labels

vAR_Features_Train = vAR_df1[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train = vAR_df1[vAR_Fetched_Label1]

vAR_df3 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df3 = vAR_df3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df3.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df4 = vAR_df3.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)

vAR_df_UC_BF = vAR_pd.read_excel(vAR_Fetched_Path_Best_Fit_OD)
vAR_df_UC_BF = vAR_df_UC_BF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_UC_BF = vAR_df_UC_BF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_UC_BF = vAR_df_UC_BF[vAR_Fetched_Label1]

vAR_df_UC_UF = vAR_pd.read_excel(vAR_Fetched_Path_Under_Fit_OD)
vAR_df_UC_UF = vAR_df_UC_BF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_UC_UF = vAR_df_UC_BF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_UC_UF = vAR_df_UC_BF[vAR_Fetched_Label1]

vAR_df_UC_OF = vAR_pd.read_excel(vAR_Fetched_Path_Over_Fit_OD)
vAR_df_UC_OF = vAR_df_UC_OF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_UC_OF = vAR_df_UC_OF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_UC_OF = vAR_df_UC_OF[vAR_Fetched_Label1]

vAR_Features_Train2 = vAR_df3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_Label_Train2 = vAR_df3[vAR_Fetched_Label2]

vAR_df5 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df5 = vAR_df5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df5.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df6 = vAR_df5.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)

vAR_Features_Train3 = vAR_df5[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_Label_Train3 = vAR_df5[vAR_Fetched_Label3]

vAR_df7 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df7 = vAR_df7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df7.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df8 = vAR_df7.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)

vAR_Features_Train4 = vAR_df7[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_Label_Train4 = vAR_df7[vAR_Fetched_Label4]

vAR_df9 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df9 = vAR_df9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4,vAR_Fetched_Label5]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df9.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df10 = vAR_df9.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)

vAR_Features_Train5 = vAR_df9[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_Label_Train5 = vAR_df9[vAR_Fetched_Label5]

#vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
#vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
#vAR_le = LabelEncoder()
#vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df11.iloc[:,0])
#vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
#vAR_df12 = vAR_df11.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)

## Fetching Test Data Features

vAR_df3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_OD)
vAR_df3 = vAR_df3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df3.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df4 = vAR_df3.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test1 = vAR_df4[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]

vAR_model = LinearRegression()
vAR_model.fit(vAR_Features_Train,vAR_Label_Train)    
vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)
vAR_Labels_Pred = vAR_Labels_Pred.astype(int)
vAR_Labels_Pred = vAR_pd.DataFrame(vAR_Labels_Pred,columns={'Predicted_Unplanned_Charges'})
vAR_df_UC = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_OD)
vAR_df_UC1 = vAR_df_UC.merge(vAR_Labels_Pred,left_index=True, right_index=True)
vAR_df_UC2 = vAR_df_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)    
vAR_df_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
vAR_df_UC4 = vAR_df_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

vAR_df5 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
vAR_df5 = vAR_df5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df5.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df6 = vAR_df5.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test2 = vAR_df6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]



vAR_model1 = LogisticRegression()
vAR_model1.fit(vAR_Features_Train2,vAR_Label_Train2)               
vAR_Labels_Pred1 = vAR_model1.predict(vAR_Features_Test2)
vAR_Labels_Pred1 = vAR_Labels_Pred1.astype(int)
vAR_Labels_Pred1 = vAR_pd.DataFrame(vAR_Labels_Pred1,columns={'Predicted_Lease_Extension'})
vAR_df_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
vAR_df_LE1 = vAR_df_LE.merge(vAR_Labels_Pred1,left_index=True, right_index=True)
vAR_df_LE2 = vAR_df_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
vAR_df_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)

vAR_df7 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
vAR_df7 = vAR_df7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df7.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df8 = vAR_df7.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test3 = vAR_df8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_Features_Test3 = vAR_Features_Test3.loc[vAR_Features_Test3['Predicted_Lease_Extension'] == 1]

vAR_model2 = LinearRegression()
vAR_model2.fit(vAR_Features_Train3,vAR_Label_Train3)
vAR_Labels_Pred2 = vAR_model2.predict(vAR_Features_Test3)
vAR_Labels_Pred2 = vAR_Labels_Pred2.astype(int)
vAR_Labels_Pred2 = vAR_pd.DataFrame(vAR_Labels_Pred2,columns={'Predicted_Extension_Terms'})
vAR_df_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
vAR_df_ET = vAR_df_ET.loc[vAR_df_ET['Predicted_Lease_Extension'] == 1]
vAR_df_ET1 = vAR_df_ET.merge(vAR_Labels_Pred2,left_index=True, right_index=True)
vAR_df_ET2 = vAR_df_ET1.to_excel(vAR_Fetched_Path_Test_IBR_OD)
vAR_df_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)


vAR_df9 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
vAR_df9 = vAR_df9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df9.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df10 = vAR_df9.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)    
vAR_Features_Test4 = vAR_df10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_Features_Test4 = vAR_Features_Test4.loc[vAR_Features_Test4['Predicted_Lease_Extension'] == 1]

vAR_model3 = LinearRegression()
vAR_model3.fit(vAR_Features_Train4,vAR_Label_Train4)
vAR_Labels_Pred3 = vAR_model3.predict(vAR_Features_Test4)
vAR_Labels_Pred3 = vAR_Labels_Pred3.astype(int)
vAR_Labels_Pred3 = vAR_pd.DataFrame(vAR_Labels_Pred3,columns={'Predicted_IBR'})
vAR_df_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
vAR_df_IBR = vAR_df_IBR.loc[vAR_df_IBR['Predicted_Lease_Extension'] == 1]
vAR_df_IBR1 = vAR_df_IBR.merge(vAR_Labels_Pred3,left_index=True, right_index=True)
vAR_df_IBR2 = vAR_df_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
vAR_df_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)

vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df11.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df12 = vAR_df11.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test5 = vAR_df12[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_Features_Test5 = vAR_Features_Test5.loc[vAR_Features_Test5['Predicted_Lease_Extension'] == 1]

vAR_model4 = LinearRegression()
vAR_model4.fit(vAR_Features_Train5,vAR_Label_Train5)
vAR_Labels_Pred4 = vAR_model4.predict(vAR_Features_Test5)
vAR_Labels_Pred4 = vAR_Labels_Pred4.astype(int)
vAR_Labels_Pred4 = vAR_pd.DataFrame(vAR_Labels_Pred4,columns={'Predicted_Lease_Amount'})
vAR_df_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
vAR_df_LA = vAR_df_LA.loc[vAR_df_LA['Predicted_Lease_Extension'] == 1]
vAR_df_LA1 = vAR_df_LA.merge(vAR_Labels_Pred4,left_index=True, right_index=True)
vAR_df_LA2 = vAR_df_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD) 
vAR_df_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)

###############################################################################################################################################################################################################################################################################################################################################


### Features & Labels for Model Performance (Unplanned Expenses)

vAR_Features_Train1 = vAR_df_UC3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]] 
vAR_Label_Train1 = vAR_df_UC3.iloc[:,12]
vAR_model.fit(vAR_Features_Train_UC_BF,vAR_Label_Train_UC_BF)    
vAR_Labels_Pred_UC_BF = vAR_model.predict(vAR_Features_Train_UC_BF)
vAR_Labels_Pred_UC_BF = vAR_Labels_Pred_UC_BF.astype(int)
vAR_Labels_Pred_UC_BF = vAR_pd.DataFrame(vAR_Labels_Pred_UC_BF,columns={'Predicted_Unplanned_Charges'})
vAR_model.fit(vAR_Features_Train_UC_UF,vAR_Label_Train_UC_UF)    
vAR_Labels_Pred_UC_UF = vAR_model.predict(vAR_Features_Train_UC_UF)
vAR_Labels_Pred_UC_UF = vAR_Labels_Pred_UC_UF.astype(int)
vAR_Labels_Pred_UC_UF = vAR_pd.DataFrame(vAR_Labels_Pred_UC_UF,columns={'Predicted_Unplanned_Charges'})
vAR_model.fit(vAR_Features_Train_UC_OF,vAR_Label_Train_UC_OF)    
vAR_Labels_Pred_UC_OF = vAR_model.predict(vAR_Features_Train_UC_OF)
vAR_Labels_Pred_UC_OF = vAR_Labels_Pred_UC_OF.astype(int)
vAR_Labels_Pred_UC_OF = vAR_pd.DataFrame(vAR_Labels_Pred_UC_OF,columns={'Predicted_Unplanned_Charges'})


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - File

vAR_df = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df = vAR_df[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df1 = vAR_df.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
#vAR_df2 = vAR_df1.merge(vAR_Asset_Location_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train = vAR_df1[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train = vAR_df1[vAR_Fetched_Label1]

vAR_Features_Train1 = vAR_df_UC3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]] 
vAR_Label_Train1 = vAR_df_UC3.iloc[:,12]

vAR_df3 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df3 = vAR_df3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df3.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df4 = vAR_df3.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train2 = vAR_df3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_Label_Train2 = vAR_df3[vAR_Fetched_Label2]

vAR_df5 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df5 = vAR_df5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df5.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df6 = vAR_df5.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train3 = vAR_df5[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_Label_Train3 = vAR_df5[vAR_Fetched_Label3]

vAR_df7 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df7 = vAR_df7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df7.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df8 = vAR_df7.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train4 = vAR_df7[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_Label_Train4 = vAR_df7[vAR_Fetched_Label4]

vAR_df9 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_OD)
vAR_df9 = vAR_df9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4,vAR_Fetched_Label5]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df9.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df10 = vAR_df9.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train5 = vAR_df9[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_Label_Train5 = vAR_df9[vAR_Fetched_Label5]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect(''DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TRAINING_DATA'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - SAP HANA

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - Oracle

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - MSSQL

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Unplanned Charges (Model 1) - File 

vAR_df3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_OD)
vAR_df3 = vAR_df3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df3.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df4 = vAR_df3.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test1 = vAR_df4[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Unplanned Charges (Model 1) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_UNPLANNED_EXPENSES'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - File 

vAR_df5 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
vAR_df5 = vAR_df5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df5.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df6 = vAR_df5.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test2 = vAR_df6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - File 

vAR_df7 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
vAR_df7 = vAR_df7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df7.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df8 = vAR_df7.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test3 = vAR_df8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_Features_Test3 = vAR_Features_Test3.loc[vAR_Features_Test3['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - File 

vAR_df9 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
vAR_df9 = vAR_df9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df9.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df10 = vAR_df9.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)    
vAR_Features_Test4 = vAR_df10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_Features_Test4 = vAR_Features_Test4.loc[vAR_Features_Test4['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease AMount (Model 5) - File 

vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_df9.iloc[:,0])
vAR_Asset_Type_Conversion_df = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_df12 = vAR_df11.merge(vAR_Asset_Type_Conversion_df,left_index=True, right_index=True)
vAR_Features_Test5 = vAR_df12[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_Features_Test5 = vAR_Features_Test5.loc[vAR_Features_Test5['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Training the Model

def vAR_Model_Train_Unplanned_Charges():
        
    from Data_Provider1 import vAR_model
    vAR_model.fit(vAR_Features_Train,vAR_Label_Train)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Model Validation
        
def vAR_Model_Validation_Unplanned_Charges():
    
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train, vAR_Label_Train , cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train.min(), vAR_Label_Train.max()], [vAR_Label_Train.min(), vAR_Label_Train.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Unplanned Expenses')
    vAR_ax.set_ylabel('Predicted Unplanned Expenses')
    #vAR_plt.show()
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

# Function for Testing the Model
            
def vAR_Model_Testing_Unplanned_Charges():
            
    vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Running_Unplanned_Charges():

    vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)
            
    vAR_Labels_Pred = vAR_Labels_Pred.astype(int)

    vAR_Labels_Pred = vAR_pd.DataFrame(vAR_Labels_Pred,columns={'Predicted_Unplanned_Charges'})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_Unplanned_Charges():
            
    vAR_df_UC1 = vAR_df_UC.merge(vAR_Labels_Pred,left_index=True, right_index=True)

    vAR_df_UC2 = vAR_df_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
    
    vAR_df_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
        
    vAR_df_UC4 = vAR_df_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Best Fit
                        
def vAR_Model_Best_Fit_Unplanned_Charges():
    
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_UC_BF, vAR_Labels_Pred_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Under Fit

def vAR_Model_Under_Fit_Unplanned_Charges():
        
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_UC_UF, vAR_Labels_Pred_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_UC_UF.min(), vAR_Labels_Pred_UC_UF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Over Fit

def vAR_Model_Over_Fit_Unplanned_Charges():
        
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_UC_OF, vAR_Labels_Pred_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()], [vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Hyperparameter Tuning (Before)

def vAR_Model_Before_Hyperparameter_Tuning_Unplanned_Charges():
    
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
    vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
    vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

# Function for Model Hyperparameter Tuning (After)
                
def vAR_Model_After_Hyperparameter_Tuning_Unplanned_Charges():
            
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
    vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
    vAR_ax.plot()                                  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Training the Model

def vAR_Model_Train_Lease_Extension():
    print(vAR_model1.fit(vAR_Features_Train2,vAR_Label_Train2))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Validating the Model

def vAR_Model_Cross_Validation_Lease_Extension():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LogisticRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2 , cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2 , cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    ##plt.show()
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Testing the Model

def vAR_Model_Test_Lease_Extension():
    vAR_Features_Test2 = vAR_df6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Running the Model

def vAR_Model_Run_Lease_Extension():
    vAR_Labels_Pred1
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Model Outcome            
                
def vAR_Model_Outcome_Lease_Extension():
   vAR_df_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
   vAR_df_LE1 = vAR_df_LE.merge(vAR_Labels_Pred1,left_index=True, right_index=True)
   vAR_df_LE2 = vAR_df_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
   vAR_df_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
                    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_Extension_Terms():
    print(vAR_model2.fit(vAR_Features_Train3,vAR_Label_Train3))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model

def vAR_Model_Cross_Validation_Extension_Terms():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_Extension_Terms():
    vAR_Features_Test3 = vAR_df8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
    vAR_Features_Test3 = vAR_Features_Test3.loc[vAR_Features_Test3['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Run_Extension_Terms():
    vAR_Labels_Pred2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
        
def vAR_Model_Outcome_Extension_Terms():
    vAR_df_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
    vAR_df_ET = vAR_df_ET.loc[vAR_df_ET['Predicted_Lease_Extension'] == 1]
    vAR_df_ET1 = vAR_df_ET.merge(vAR_Labels_Pred2,left_index=True, right_index=True)
    vAR_df_ET2 = vAR_df_ET1.to_excel(vAR_Fetched_Path_Test_IBR_OD)
    vAR_df_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_IBR():
    print(vAR_model4.fit(vAR_Features_Train4,vAR_Label_Train4))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model
    
def vAR_Model_Cross_Validation_IBR():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_plt.show()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_IBR():
    vAR_Features_Test4 = vAR_df10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
    vAR_Features_Test4 = vAR_Features_Test4.loc[vAR_Features_Test4['Predicted_Lease_Extension'] == 1]
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Run_IBR():
    vAR_Labels_Pred3
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_IBR():
    vAR_df_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
    vAR_df_IBR = vAR_df_IBR.loc[vAR_df_IBR['Predicted_Lease_Extension'] == 1]
    vAR_df_IBR1 = vAR_df_IBR.merge(vAR_Labels_Pred3,left_index=True, right_index=True)
    vAR_df_IBR2 = vAR_df_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
    vAR_df_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_Lease_Amount():
    print(vAR_model.fit(vAR_Features_Train5,vAR_Label_Train5))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model
    
def vAR_Model_Cross_Validation_Lease_Amount():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_plt.show()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_Lease_Amount():
    vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
    vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model

def vAR_Model_Run_Lease_Amount():
    vAR_Labels_Pred4
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_Lease_Amount():
    vAR_df_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
    vAR_df_LA = vAR_df_LA.loc[vAR_df_LA['Predicted_Lease_Extension'] == 1]
    vAR_df_LA1 = vAR_df_LA.merge(vAR_Labels_Pred4,left_index=True, right_index=True)
    vAR_df_LA2 = vAR_df_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
    vAR_df_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Train_Data():
	print(vAR_Features_Train)
	print(vAR_Label_Train)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def vAR_Collect_Test_Data_Unplanned_Charges():
	print(vAR_Features_Test1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Lease_Extension():
	print(vAR_Features_Test2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Extension_Terms():
	print(vAR_Features_Test3)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_IBR():
	print(vAR_Features_Test4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Lease_Amount():
	print(vAR_Features_Test5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_df_Train_All = vAR_df1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Train_Data_Unplanned_Charges():
     print(vAR_df_Train_All)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_df_Test_UC = vAR_df4

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Unplanned_Charges():
     print(vAR_df_Test_UC)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_df_Test_LE = vAR_df6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Lease_Extension():
     print(vAR_df_Test_LE)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_df_Test_ET = vAR_df8

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Extension_Terms():
     print(vAR_df_Test_ET)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#vAR_df_Test_IBR = vAR_df10

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#def vAR_Integrate_Test_Data_IBR():
     #print(vAR_df_Test_IBR)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#vAR_df_Test_LA = vAR_df12

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#def vAR_Integrate_Test_Data_Lease_Amount():
     #print(vAR_df_Test_LA)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


vAR_DF = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)

vAR_Feature1 = vAR_DF[vAR_Fetched_Feature1]
vAR_Feature2 = vAR_DF[vAR_Fetched_Feature2]
vAR_Feature3 = vAR_DF[vAR_Fetched_Feature3]
vAR_Feature4 = vAR_DF[vAR_Fetched_Feature4]
vAR_Feature5 = vAR_DF[vAR_Fetched_Feature5]
vAR_Feature6 = vAR_DF[vAR_Fetched_Feature6]
vAR_Feature7 = vAR_DF[vAR_Fetched_Feature7]
vAR_Feature8 = vAR_DF[vAR_Fetched_Feature8]
vAR_Feature9 = vAR_DF[vAR_Fetched_Feature9]
vAR_Feature10 = vAR_DF[vAR_Fetched_Feature10]

vAR_Label1 = vAR_DF[vAR_Fetched_Label1]
vAR_Label2 = vAR_DF[vAR_Fetched_Label2]
vAR_Label3 = vAR_DF[vAR_Fetched_Label3]
vAR_Label4 = vAR_DF[vAR_Fetched_Label4]
vAR_Label5 = vAR_DF[vAR_Fetched_Label5]

vAR_model = LinearRegression()
vAR_model1 = LogisticRegression()
vAR_model2 = LinearRegression()
vAR_model3 = LinearRegression()
vAR_model4 = LinearRegression()

vAR_DF = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF = vAR_DF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF1 = vAR_DF.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
#vAR_DF2 = vAR_DF1.merge(vAR_Asset_Location_Conversion_df,left_index=True, right_index=True)

vAR_Features_Train_YD = vAR_DF1[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_YD = vAR_DF1[vAR_Fetched_Label1]

vAR_DF3 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF3 = vAR_DF3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF3.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF4 = vAR_DF3.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)

vAR_DF_UC_BF = vAR_pd.read_excel(vAR_Fetched_Path_Best_Fit_YD)
vAR_DF_UC_BF = vAR_DF_UC_BF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_YD_UC_BF = vAR_DF_UC_BF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_YD_UC_BF = vAR_DF_UC_BF[vAR_Fetched_Label1]

vAR_DF_UC_UF = vAR_pd.read_excel(vAR_Fetched_Path_Under_Fit_YD)
vAR_DF_UC_UF = vAR_DF_UC_BF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_YD_UC_UF = vAR_DF_UC_BF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_YD_UC_UF = vAR_DF_UC_BF[vAR_Fetched_Label1]

vAR_DF_UC_OF = vAR_pd.read_excel(vAR_Fetched_Path_Over_Fit_YD)
vAR_DF_UC_OF = vAR_DF_UC_OF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]

vAR_Features_Train_YD_UC_OF = vAR_DF_UC_OF[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_YD_UC_OF = vAR_DF_UC_OF[vAR_Fetched_Label1]

vAR_Features_Train2_YD = vAR_DF3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_Label_Train2_YD = vAR_DF3[vAR_Fetched_Label2]

vAR_DF5 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF5 = vAR_DF5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF5.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF6 = vAR_DF5.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)

vAR_Features_Train3_YD = vAR_DF5[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_Label_Train3_YD = vAR_DF5[vAR_Fetched_Label3]

vAR_DF7 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF7 = vAR_DF7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF7.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF8 = vAR_DF7.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)

vAR_Features_Train4_YD = vAR_DF7[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_Label_Train4_YD = vAR_DF7[vAR_Fetched_Label4]

vAR_DF9 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF9 = vAR_DF9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4,vAR_Fetched_Label5]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF9.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF10 = vAR_DF9.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)

vAR_Features_Train5_YD = vAR_DF9[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_Label_Train5_YD = vAR_DF9[vAR_Fetched_Label5]

#vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
#vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
#vAR_le = LabelEncoder()
#vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF11.iloc[:,0])
#vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
#vAR_DF12 = vAR_DF11.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)

vAR_DF3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_YD)
vAR_DF3 = vAR_DF3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF3.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF4 = vAR_DF3.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test1_YD = vAR_DF4[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]

vAR_model = LinearRegression()
vAR_model.fit(vAR_Features_Train_YD,vAR_Label_Train_YD)    
vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)
vAR_Labels_Pred_YD = vAR_Labels_Pred_YD.astype(int)
vAR_Labels_Pred_YD = vAR_pd.DataFrame(vAR_Labels_Pred_YD,columns={'Predicted_Unplanned_Charges'})
vAR_DF_UC = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_YD)
vAR_DF_UC1 = vAR_DF_UC.merge(vAR_Labels_Pred_YD,left_index=True, right_index=True)
vAR_DF_UC2 = vAR_DF_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)    
vAR_DF_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
vAR_DF_UC4 = vAR_DF_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]
vAR_Features_Train1_YD = vAR_DF_UC3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]] 
vAR_Label_Train1_YD = vAR_DF_UC3.iloc[:,12]

vAR_DF5 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
vAR_DF5 = vAR_DF5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF5.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF6 = vAR_DF5.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test2_YD = vAR_DF6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

vAR_model1 = LogisticRegression()
vAR_model1.fit(vAR_Features_Train2_YD,vAR_Label_Train2_YD)               
vAR_Labels_Pred1_YD = vAR_model1.predict(vAR_Features_Test2_YD)
vAR_Labels_Pred1_YD = vAR_Labels_Pred1_YD.astype(int)
vAR_Labels_Pred1_YD = vAR_pd.DataFrame(vAR_Labels_Pred1_YD,columns={'Predicted_Lease_Extension'})
vAR_DF_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
vAR_DF_LE1 = vAR_DF_LE.merge(vAR_Labels_Pred1_YD,left_index=True, right_index=True)
vAR_DF_LE2 = vAR_DF_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
vAR_DF_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)


vAR_DF7 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
vAR_DF7 = vAR_DF7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF7.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF8 = vAR_DF7.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test3_YD = vAR_DF8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_Features_Test3_YD = vAR_Features_Test3_YD.loc[vAR_Features_Test3_YD['Predicted_Lease_Extension'] == 1]


vAR_model2 = LinearRegression()
vAR_model2.fit(vAR_Features_Train3_YD,vAR_Label_Train3_YD)
vAR_Labels_Pred2_YD = vAR_model2.predict(vAR_Features_Test3_YD)
vAR_Labels_Pred2_YD = vAR_Labels_Pred2_YD.astype(int)
vAR_Labels_Pred2_YD = vAR_pd.DataFrame(vAR_Labels_Pred2_YD,columns={'Predicted_Extension_Terms'})
vAR_DF_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
vAR_DF_ET = vAR_DF_ET.loc[vAR_DF_ET['Predicted_Lease_Extension'] == 1]
vAR_DF_ET1 = vAR_DF_ET.merge(vAR_Labels_Pred2_YD,left_index=True, right_index=True)
vAR_DF_ET2 = vAR_DF_ET1.to_excel(vAR_Fetched_Path_Test_IBR_YD)
vAR_DF_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)

vAR_DF9 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
vAR_DF9 = vAR_DF9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF9.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF10 = vAR_DF9.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)    
vAR_Features_Test4_YD = vAR_DF10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_Features_Test4_YD = vAR_Features_Test4_YD.loc[vAR_Features_Test4_YD['Predicted_Lease_Extension'] == 1]

vAR_model3 = LinearRegression()
vAR_model3.fit(vAR_Features_Train4_YD,vAR_Label_Train4_YD)
vAR_Labels_Pred3_YD = vAR_model3.predict(vAR_Features_Test4_YD)
vAR_Labels_Pred3_YD = vAR_Labels_Pred3_YD.astype(int)
vAR_Labels_Pred3_YD = vAR_pd.DataFrame(vAR_Labels_Pred3_YD,columns={'Predicted_IBR'})
vAR_DF_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
vAR_DF_IBR = vAR_DF_IBR.loc[vAR_DF_IBR['Predicted_Lease_Extension'] == 1]
vAR_DF_IBR1 = vAR_DF_IBR.merge(vAR_Labels_Pred3_YD,left_index=True, right_index=True)
vAR_DF_IBR2 = vAR_DF_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
vAR_DF_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)

vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF11.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF12 = vAR_DF11.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test5_YD = vAR_DF12[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_Features_Test5_YD = vAR_Features_Test5_YD.loc[vAR_Features_Test5_YD['Predicted_Lease_Extension'] == 1]

vAR_model4 = LinearRegression()
vAR_model4.fit(vAR_Features_Train5_YD,vAR_Label_Train5_YD)
vAR_Labels_Pred4_YD = vAR_model4.predict(vAR_Features_Test5_YD)
vAR_Labels_Pred4_YD = vAR_Labels_Pred4_YD.astype(int)
vAR_Labels_Pred4_YD = vAR_pd.DataFrame(vAR_Labels_Pred4_YD,columns={'Predicted_Lease_Amount'})
vAR_DF_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
vAR_DF_LA = vAR_DF_LA.loc[vAR_DF_LA['Predicted_Lease_Extension'] == 1]
vAR_DF_LA1 = vAR_DF_LA.merge(vAR_Labels_Pred4_YD,left_index=True, right_index=True)
vAR_DF_LA2 = vAR_DF_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD) 
vAR_DF_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)

vAR_model.fit(vAR_Features_Train_YD_UC_BF,vAR_Label_Train_YD_UC_BF)    
vAR_Labels_Pred_YD_UC_BF = vAR_model.predict(vAR_Features_Train_YD_UC_BF)
vAR_Labels_Pred_YD_UC_BF = vAR_Labels_Pred_YD_UC_BF.astype(int)
vAR_Labels_Pred_YD_UC_BF = vAR_pd.DataFrame(vAR_Labels_Pred_YD_UC_BF,columns={'Predicted_Unplanned_Charges'})
vAR_model.fit(vAR_Features_Train_YD_UC_UF,vAR_Label_Train_YD_UC_UF)    
vAR_Labels_Pred_YD_UC_UF = vAR_model.predict(vAR_Features_Train_YD_UC_UF)
vAR_Labels_Pred_YD_UC_UF = vAR_Labels_Pred_YD_UC_UF.astype(int)
vAR_Labels_Pred_YD_UC_UF = vAR_pd.DataFrame(vAR_Labels_Pred_YD_UC_UF,columns={'Predicted_Unplanned_Charges'})
vAR_model.fit(vAR_Features_Train_YD_UC_OF,vAR_Label_Train_YD_UC_OF)    
vAR_Labels_Pred_YD_UC_OF = vAR_model.predict(vAR_Features_Train_YD_UC_OF)
vAR_Labels_Pred_YD_UC_OF = vAR_Labels_Pred_YD_UC_OF.astype(int)
vAR_Labels_Pred_YD_UC_OF = vAR_pd.DataFrame(vAR_Labels_Pred_YD_UC_OF,columns={'Predicted_Unplanned_Charges'})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - File

vAR_DF = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF = vAR_DF[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF1 = vAR_DF.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
#vAR_DF2 = vAR_DF1.merge(vAR_Asset_Location_Conversion_df,left_index=True, right_index=True)
vAR_Features_Train_YD = vAR_DF1[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_Label_Train_YD = vAR_DF1[vAR_Fetched_Label1]

vAR_Features_Train1_YD = vAR_DF_UC3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]] 
vAR_Label_Train1_YD = vAR_DF_UC3.iloc[:,12]

vAR_DF3 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF3 = vAR_DF3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF3.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF4 = vAR_DF3.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Train2_YD = vAR_DF3[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1]]
vAR_Label_Train2_YD = vAR_DF3[vAR_Fetched_Label2]

vAR_DF5 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF5 = vAR_DF5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF5.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF6 = vAR_DF5.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Train3_YD = vAR_DF5[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2]]
vAR_Label_Train3_YD = vAR_DF5[vAR_Fetched_Label3]

vAR_DF7 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF7 = vAR_DF7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF7.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF8 = vAR_DF7.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Train4_YD = vAR_DF7[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3]]
vAR_Label_Train4_YD = vAR_DF7[vAR_Fetched_Label4]

vAR_DF9 = vAR_pd.read_excel(vAR_Fetched_Path_Train_Unplanned_Expenses_YD)
vAR_DF9 = vAR_DF9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4,vAR_Fetched_Label5]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF9.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF10 = vAR_DF9.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Train5_YD = vAR_DF9[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,vAR_Fetched_Label1,vAR_Fetched_Label2,vAR_Fetched_Label3,vAR_Fetched_Label4]]
vAR_Label_Train5_YD = vAR_DF9[vAR_Fetched_Label5]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect(''DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TRAINING_DATA'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - SAP HANA

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - Oracle

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Train Data for all the Models - MSSQL

import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#CSLAB_STMNT = 'SELECT * FROM DURGA.TRAINING_DATA'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Unplanned Charges (Model 1) - File 

vAR_DF3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Unplanned_Expenses_YD)
vAR_DF3 = vAR_DF3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF3.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF4 = vAR_DF3.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test1_YD = vAR_DF4[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10]]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Unplanned Charges (Model 1) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_UNPLANNED_EXPENSES'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - File 

vAR_DF5 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
vAR_DF5 = vAR_DF5[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF5.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF6 = vAR_DF5.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test2_YD = vAR_DF6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Extension (Model 2) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_EXTENSION'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - File 

vAR_DF7 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
vAR_DF7 = vAR_DF7[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF7.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF8 = vAR_DF7.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test3_YD = vAR_DF8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
vAR_Features_Test3_YD = vAR_Features_Test3_YD.loc[vAR_Features_Test3_YD['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Extension Terms (Model 3) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_EXTENSION_TERMS'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - File 

vAR_DF9 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
vAR_DF9 = vAR_DF9[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF9.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF10 = vAR_DF9.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)    
vAR_Features_Test4_YD = vAR_DF10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
vAR_Features_Test4_YD = vAR_Features_Test4_YD.loc[vAR_Features_Test4_YD['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for IBR (Model 4) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_IBR'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease AMount (Model 5) - File 

vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_le = LabelEncoder()
vAR_Asset_Type_Conversion = vAR_le.fit_transform(vAR_DF9.iloc[:,0])
vAR_Asset_Type_Conversion_DF = vAR_pd.DataFrame(vAR_Asset_Type_Conversion,columns={'Asset_Type_Converted'})
vAR_DF12 = vAR_DF11.merge(vAR_Asset_Type_Conversion_DF,left_index=True, right_index=True)
vAR_Features_Test5_YD = vAR_DF12[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
vAR_Features_Test5_YD = vAR_Features_Test5_YD.loc[vAR_Features_Test5_YD['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - Hadoop

import pypyodbc as pyodbc

#vAR_CSLAB_CONN = pyodbc.connect('DSN=vAR_HADOOP;UID=vAR_USER;PWD=vAR_PW',autocommit=True)

#vAR_CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#vAR_CSLAB_CURSOR.execute(CSLAB_STMNT)

#vAR_CSLAB_RESULT = CSLAB_CURSOR.fetchall() 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - SAP HANA
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_SAPHANA;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - Oracle
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_Oracle;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Test Data for Lease Amount (Model 5) - MSSQL
    
import pypyodbc as pyodbc 

#CSLAB_CONN = pyodbc.connect('DSN=vAR_MSSQL;UID=vAR_USER;PWD=vAR_PW'')

#CSLAB_CURSOR = CSLAB_CONN.cursor()

#vAR_CSLAB_STMNT = 'SELECT * FROM TEST_DATA_LEASE_AMOUNT'

#CSLAB_CURSOR.execute(CSLAB_STMNT)

#CSLAB_RESULT = CSLAB_CURSOR.fetchall()

#print (CSLAB_RESULT)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Training the Model

def vAR_Model_Train_Unplanned_Charges_YD():
        
    from Data_Provider2 import vAR_model
    vAR_model.fit(vAR_Features_Train_YD,vAR_Label_Train_YD)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Model Validation
        
def vAR_Model_Validation_Unplanned_Charges_YD():
    
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train_YD, vAR_Label_Train_YD , cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], [vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Unplanned Expenses')
    vAR_ax.set_ylabel('Predicted Unplanned Expenses')
    #vAR_plt.show()
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

# Function for Testing the Model
            
def vAR_Model_Testing_Unplanned_Charges_YD():
            
    vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Running_Unplanned_Charges_YD():

    vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)
            
    vAR_Labels_Pred_YD = vAR_Labels_Pred_YD.astype(int)

    vAR_Labels_Pred_YD = vAR_pd.DataFrame(vAR_Labels_Pred_YD,columns={'Predicted_Unplanned_Charges'})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_Unplanned_Charges_YD():
            
    vAR_DF_UC1 = vAR_DF_UC.merge(vAR_Labels_Pred_YD,left_index=True, right_index=True)

    vAR_DF_UC2 = vAR_DF_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
    
    vAR_DF_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
    vAR_DF_UC4 = vAR_DF_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Best Fit
                        
def vAR_Model_Best_Fit_Unplanned_Charges_YD():
    
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD_UC_BF, vAR_Labels_Pred_YD_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Under Fit

def vAR_Model_Under_Fit_Unplanned_Charges_YD():
        
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD_UC_UF, vAR_Labels_Pred_YD_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_YD_UC_UF.min(), vAR_Labels_Pred_YD_UC_UF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Over Fit

def vAR_Model_Over_Fit_Unplanned_Charges_YD():
        
    import matplotlib.pyplot as vAR_plt
    from sklearn.linear_model import LinearRegression
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD_UC_OF, vAR_Labels_Pred_YD_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
    vAR_ax.plot([vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()], [vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()])
    #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Hyperparameter Tuning (Before)

def vAR_Model_Before_Hyperparameter_Tuning_Unplanned_Charges_YD():
    
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD1, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
    vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
    vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

# Function for Model Hyperparameter Tuning (After)
                
def vAR_Model_After_Hyperparameter_Tuning_Unplanned_Charges_YD():
            
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train_YD1, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
    vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
    vAR_ax.plot()                                  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Training the Model

def vAR_Model_Train_Lease_Extension_YD():
    print(vAR_model1.fit(vAR_Features_Train2_YD,vAR_Label_Train2_YD))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Validating the Model

def vAR_Model_Cross_Validation_Lease_Extension_YD():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LogisticRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD , cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD , cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Lease Extension')
    vAR_ax.set_ylabel('Planned Lease Extension')
    ##plt.show()
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Testing the Model

def vAR_Model_Test_Lease_Extension_YD():
    vAR_Features_Test2_YD = vAR_DF6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Running the Model

def vAR_Model_Run_Lease_Extension_YD():
    vAR_Labels_Pred1_YD
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# Function for Model Outcome            
                
def vAR_Model_Outcome_Lease_Extension_YD():
   vAR_DF_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
   vAR_DF_LE1 = vAR_DF_LE.merge(vAR_Labels_Pred1_YD,left_index=True, right_index=True)
   vAR_DF_LE2 = vAR_DF_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
   vAR_DF_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
                    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_Extension_Terms_YD():
    print(vAR_model2.fit(vAR_Features_Train3_YD,vAR_Label_Train3_YD))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model

def vAR_Model_Cross_Validation_Extension_Terms_YD():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3_YD, vAR_Label_Train3_YD, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], [vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3_YD, vAR_Label_Train3_YD, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], [vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3_YD, vAR_Label_Train3_YD, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train3_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], [vAR_Label_Train3_YD.min(), vAR_Label_Train3_YD.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Extension Term')
    vAR_ax.set_ylabel('Predicted Extension Term')
    vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_Extension_Terms_YD():
    vAR_Features_Test3_YD = vAR_DF8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
    vAR_Features_Test3_YD = vAR_Features_Test3_YD.loc[vAR_Features_Test3_YD['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Run_Extension_Terms_YD():
    vAR_Labels_Pred2_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
        
def vAR_Model_Outcome_Extension_Terms_YD():
    vAR_DF_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
    vAR_DF_ET = vAR_DF_ET.loc[vAR_DF_ET['Predicted_Lease_Extension'] == 1]
    vAR_DF_ET1 = vAR_DF_ET.merge(vAR_Labels_Pred2_YD,left_index=True, right_index=True)
    vAR_DF_ET2 = vAR_DF_ET1.to_excel(vAR_Fetched_Path_Test_IBR_YD)
    vAR_DF_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_IBR_YD():
    print(vAR_model4.fit(vAR_Features_Train4_YD,vAR_Label_Train4_YD))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model
    
def vAR_Model_Cross_Validation_IBR_YD():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4_YD, vAR_Label_Train4_YD, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], [vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4_YD, vAR_Label_Train4_YD, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], [vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4_YD, vAR_Label_Train4_YD, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train4_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], [vAR_Label_Train4_YD.min(), vAR_Label_Train4_YD.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual IBR')
    vAR_ax.set_ylabel('Predicted IBR')
    vAR_plt.show()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_IBR_YD():
    vAR_Features_Test4_YD = vAR_DF10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
    vAR_Features_Test4_YD = vAR_Features_Test4_YD.loc[vAR_Features_Test4_YD['Predicted_Lease_Extension'] == 1]
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model
    
def vAR_Model_Run_IBR_YD():
    vAR_Labels_Pred3_YD
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_IBR_YD():
    vAR_DF_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
    vAR_DF_IBR = vAR_DF_IBR.loc[vAR_DF_IBR['Predicted_Lease_Extension'] == 1]
    vAR_DF_IBR1 = vAR_DF_IBR.merge(vAR_Labels_Pred3_YD,left_index=True, right_index=True)
    vAR_DF_IBR2 = vAR_DF_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
    vAR_DF_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Training the Model

def vAR_Model_Train_Lease_Amount_YD():
    print(vAR_model.fit(vAR_Features_Train5_YD,vAR_Label_Train5_YD))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Validating the Model
    
def vAR_Model_Cross_Validation_Lease_Amount_YD():
    from sklearn.model_selection import cross_val_predict
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as vAR_plt
    vAR_model = LinearRegression()
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5_YD, vAR_Label_Train5_YD, cv=2)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], [vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], 'k--', lw=2)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5_YD, vAR_Label_Train5_YD, cv=5)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], [vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], 'k--', lw=4)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5_YD, vAR_Label_Train5_YD, cv=10)
    vAR_fig, vAR_ax = vAR_plt.subplots()
    vAR_ax.scatter(vAR_Label_Train5_YD, vAR_Predicted, edgecolors=(0, 0, 0))
    vAR_ax.plot([vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], [vAR_Label_Train5_YD.min(), vAR_Label_Train5_YD.max()], 'k--', lw=6)
    vAR_ax.set_xlabel('Actual Lease Amount')
    vAR_ax.set_ylabel('Predicted Lease Amount')
    vAR_plt.show()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Testing the Model
    
def vAR_Model_Test_Lease_Amount_YD():
    vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
    vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]
   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Running the Model

def vAR_Model_Run_Lease_Amount_YD():
    vAR_Labels_Pred4_YD
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function for Model Outcome
    
def vAR_Model_Outcome_Lease_Amount_YD():
    vAR_DF_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
    vAR_DF_LA = vAR_DF_LA.loc[vAR_DF_LA['Predicted_Lease_Extension'] == 1]
    vAR_DF_LA1 = vAR_DF_LA.merge(vAR_Labels_Pred4_YD,left_index=True, right_index=True)
    vAR_DF_LA2 = vAR_DF_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)
    vAR_DF_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Unplanned_Charges_YD():
	print(vAR_Features_Test1_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Lease_Extension_YD():
	print(vAR_Features_Test2_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Extension_Terms_YD():
	print(vAR_Features_Test3_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_IBR_YD():
	print(vAR_Features_Test4_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Collect_Test_Data_Lease_Amount_YD():
	print(vAR_Features_Test5_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_DF_Train_All = vAR_DF1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Train_Data_Unplanned_Charges_YD():
     print(vAR_DF_Train_All)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_DF_Test_UC = vAR_DF4

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Unplanned_Charges_YD():
     print(vAR_DF_Test_UC)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_DF_Test_LE = vAR_DF6

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Lease_Extension_YD():
     print(vAR_DF_Test_LE)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_DF_Test_ET = vAR_DF8

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def vAR_Integrate_Test_Data_Extension_Terms_YD():
     print(vAR_DF_Test_ET)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#vAR_DF_Test_IBR = vAR_DF10

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#def vAR_Integrate_Test_Data_IBR_YD():
     #print(vAR_DF_Test_IBR)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#vAR_DF_Test_LA = vAR_DF12

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#def vAR_Integrate_Test_Data_Lease_Amount_YD():
     #print(vAR_DF_Test_LA)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>