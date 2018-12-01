import configparser
vAR_Config = configparser.ConfigParser(allow_no_value=True)
vAR_Config.read('/opt/conda/bin/Lease_Formulation/Lease_Formulation/Lease_Formulation/DS_LEASE_ACCOUNTING_MODEL_CONS_INI_FILE1.INI')
#vAR_Config.read(vAR_Fetched_Data_INI_File_Path)
vAR_Data = vAR_Config.sections()
vAR_Config.sections()

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

vAR_Fetched_Path_Data_Provider = vAR_Config['PROBLEM1 CONFIGURATION']['DATA_PROVIDER_PATH']
#print(vAR_Fetched_Path_Data_Provider)

vAR_Fetched_Path_Preview_Outcome_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)

vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_JSON_DATA_URL_OD']
#print(vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD)

vAR_Fetched_Path_Preview_Outcome_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_JSON_DATA_URL_YD']
#print(vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD)

vAR_File_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['FILE_NAME_OUR_DATA']
#print(vAR_File_Name_Our_Data)

vAR_File_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['FILE_NAME_YOUR_DATA']
#print(vAR_File_Name_Your_Data)

vAR_Model1_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_OUR_DATA']
#print(vAR_Model1_Name_Our_Data)

vAR_Model2_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_OUR_DATA']
#print(vAR_Model2_Name_Our_Data)

vAR_Model3_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_OUR_DATA']
#print(vAR_Model3_Name_Our_Data)

vAR_Model4_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_OUR_DATA']
#print(vAR_Model4_Name_Our_Data)

vAR_Model5_Name_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_OUR_DATA']
#print(vAR_Model5_Name_Our_Data)

vAR_Model1_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_YOUR_DATA']
#print(vAR_Model1_Name_Your_Data)

vAR_Model2_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_YOUR_DATA']
#print(vAR_Model2_Name_Your_Data)

vAR_Model3_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_YOUR_DATA']
#print(vAR_Model3_Name_Your_Data)

vAR_Model4_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_YOUR_DATA']
#print(vAR_Model4_Name_Your_Data)

vAR_Model5_Name_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_YOUR_DATA']
#print(vAR_Model5_Name_Your_Data)

vAR_Session_ID_Run_Model1_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL1_OD']
print(vAR_Session_ID_Run_Model1_OD)

vAR_Session_ID_Run_Model2_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL2_OD']
print(vAR_Session_ID_Run_Model2_OD)

vAR_Session_ID_Run_Model3_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL3_OD']
print(vAR_Session_ID_Run_Model3_OD)

vAR_Session_ID_Run_Model4_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL4_OD']
print(vAR_Session_ID_Run_Model4_OD)

vAR_Session_ID_Run_Model5_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL5_OD']
print(vAR_Session_ID_Run_Model5_OD)

vAR_Session_ID_Run_Model1_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL1_YD']
print(vAR_Session_ID_Run_Model1_YD)

vAR_Session_ID_Run_Model2_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL2_YD']
print(vAR_Session_ID_Run_Model2_YD)

vAR_Session_ID_Run_Model3_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL3_YD']
print(vAR_Session_ID_Run_Model3_YD)

vAR_Session_ID_Run_Model4_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL4_YD']
print(vAR_Session_ID_Run_Model4_YD)

vAR_Session_ID_Run_Model5_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL5_YD']
print(vAR_Session_ID_Run_Model5_YD)

vAR_Session_ID_Run_AllModel_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_ALLMODEL_OD']
#print(vAR_Session_ID_Run_AllModel_OD)

vAR_Session_ID_Run_AllModel_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_ALLMODEL_YD']
#print(vAR_Session_ID_Run_AllModel_YD)

vAR_Model1_Flag = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_FLAG']
#print(vAR_Model1_Flag)

vAR_Model2_Flag = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_FLAG']
#print(vAR_Model2_Flag)

vAR_Model3_Flag = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_FLAG']
#print(vAR_Model3_Flag)

vAR_Model4_Flag = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_FLAG']
#print(vAR_Model4_Flag)

vAR_Model5_Flag = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_FLAG']
#print(vAR_Model5_Flag)

import Data_Provider2
import pandas as vAR_pd
from Data_Provider2 import vAR_df
from Data_Provider2 import vAR_df1
from Data_Provider2 import vAR_df3
from Data_Provider2 import vAR_df4
from Data_Provider2 import vAR_df5
from Data_Provider2 import vAR_df6
from Data_Provider2 import vAR_df7
from Data_Provider2 import vAR_df8
from Data_Provider2 import vAR_df9
from Data_Provider2 import vAR_df10
from Data_Provider2 import vAR_df11
from Data_Provider2 import vAR_df12

from Data_Provider2 import vAR_model
from Data_Provider2 import vAR_model1
from Data_Provider2 import vAR_model2
from Data_Provider2 import vAR_model3
from Data_Provider2 import vAR_model4

from Data_Provider2 import vAR_df_UC
from Data_Provider2 import vAR_df_UC1
#from Data_Provider2 import vAR_df_UC2
from Data_Provider2 import vAR_df_UC3
from Data_Provider2 import vAR_df_UC4
from Data_Provider2 import vAR_df_LE
from Data_Provider2 import vAR_df_LE1
from Data_Provider2 import vAR_df_LE2
from Data_Provider2 import vAR_df_LE3
from Data_Provider2 import vAR_df_ET
from Data_Provider2 import vAR_df_ET1
from Data_Provider2 import vAR_df_ET2
from Data_Provider2 import vAR_df_ET3
from Data_Provider2 import vAR_df_IBR
from Data_Provider2 import vAR_df_IBR1
from Data_Provider2 import vAR_df_IBR2
from Data_Provider2 import vAR_df_IBR3
from Data_Provider2 import vAR_df_LA
from Data_Provider2 import vAR_df_LA1
from Data_Provider2 import vAR_df_LA2
from Data_Provider2 import vAR_df_LA3

from Data_Provider2 import vAR_Features_Train
from Data_Provider2 import vAR_Label_Train
from Data_Provider2 import vAR_Features_Train1
from Data_Provider2 import vAR_Label_Train1
from Data_Provider2 import vAR_Features_Train2
from Data_Provider2 import vAR_Label_Train2
from Data_Provider2 import vAR_Features_Train3
from Data_Provider2 import vAR_Label_Train3
from Data_Provider2 import vAR_Features_Train4
from Data_Provider2 import vAR_Label_Train4
from Data_Provider2 import vAR_Features_Train5
from Data_Provider2 import vAR_Label_Train5

from Data_Provider2 import vAR_Features_Train_UC_BF
from Data_Provider2 import vAR_Label_Train_UC_BF
from Data_Provider2 import vAR_Features_Train_UC_UF
from Data_Provider2 import vAR_Label_Train_UC_UF
from Data_Provider2 import vAR_Features_Train_UC_OF
from Data_Provider2 import vAR_Label_Train_UC_OF

from Data_Provider2 import vAR_Features_Test1
from Data_Provider2 import vAR_Features_Test2
from Data_Provider2 import vAR_Features_Test3
from Data_Provider2 import vAR_Features_Test4
from Data_Provider2 import vAR_Features_Test5

from Data_Provider2 import vAR_Labels_Pred
from Data_Provider2 import vAR_Labels_Pred1
from Data_Provider2 import vAR_Labels_Pred2
from Data_Provider2 import vAR_Labels_Pred3
from Data_Provider2 import vAR_Labels_Pred4

from Data_Provider2 import vAR_df_UC_BF
from Data_Provider2 import vAR_df_UC_UF
from Data_Provider2 import vAR_df_UC_OF

from Data_Provider2 import vAR_Labels_Pred_UC_BF
from Data_Provider2 import vAR_Labels_Pred_UC_UF
from Data_Provider2 import vAR_Labels_Pred_UC_OF

from Data_Provider2 import vAR_Model_Train_Unplanned_Charges
from Data_Provider2 import vAR_Model_Validation_Unplanned_Charges
from Data_Provider2 import vAR_Model_Testing_Unplanned_Charges
from Data_Provider2 import vAR_Model_Running_Unplanned_Charges
from Data_Provider2 import vAR_Model_Outcome_Unplanned_Charges
from Data_Provider2 import vAR_Model_Best_Fit_Unplanned_Charges
from Data_Provider2 import vAR_Model_Under_Fit_Unplanned_Charges
from Data_Provider2 import vAR_Model_Over_Fit_Unplanned_Charges
from Data_Provider2 import vAR_Model_Before_Hyperparameter_Tuning_Unplanned_Charges
from Data_Provider2 import vAR_Model_After_Hyperparameter_Tuning_Unplanned_Charges

from Data_Provider2 import vAR_Model_Train_Lease_Extension
from Data_Provider2 import vAR_Model_Cross_Validation_Lease_Extension
from Data_Provider2 import vAR_Model_Test_Lease_Extension
from Data_Provider2 import vAR_Model_Run_Lease_Extension
from Data_Provider2 import vAR_Model_Outcome_Lease_Extension

from Data_Provider2 import vAR_Model_Train_Extension_Terms
from Data_Provider2 import vAR_Model_Cross_Validation_Extension_Terms
from Data_Provider2 import vAR_Model_Test_Extension_Terms
from Data_Provider2 import vAR_Model_Run_Extension_Terms
from Data_Provider2 import vAR_Model_Outcome_Extension_Terms

from Data_Provider2 import vAR_Model_Train_IBR
from Data_Provider2 import vAR_Model_Cross_Validation_IBR
from Data_Provider2 import vAR_Model_Test_IBR
from Data_Provider2 import vAR_Model_Run_IBR
from Data_Provider2 import vAR_Model_Outcome_IBR

from Data_Provider2 import vAR_Model_Train_Lease_Amount
from Data_Provider2 import vAR_Model_Cross_Validation_Lease_Amount
from Data_Provider2 import vAR_Model_Test_Lease_Amount
from Data_Provider2 import vAR_Model_Run_Lease_Amount
from Data_Provider2 import vAR_Model_Outcome_Lease_Amount

from Data_Provider2 import vAR_DF
from Data_Provider2 import vAR_DF1
from Data_Provider2 import vAR_DF3
from Data_Provider2 import vAR_DF4
from Data_Provider2 import vAR_DF5
from Data_Provider2 import vAR_DF6
from Data_Provider2 import vAR_DF7
from Data_Provider2 import vAR_DF8
from Data_Provider2 import vAR_DF9
from Data_Provider2 import vAR_DF10
from Data_Provider2 import vAR_DF11
from Data_Provider2 import vAR_DF12

from Data_Provider2 import vAR_model
from Data_Provider2 import vAR_model1
from Data_Provider2 import vAR_model2
from Data_Provider2 import vAR_model3
from Data_Provider2 import vAR_model4

from Data_Provider2 import vAR_DF_UC
from Data_Provider2 import vAR_DF_UC1
from Data_Provider2 import vAR_DF_UC2
from Data_Provider2 import vAR_DF_UC3
from Data_Provider2 import vAR_DF_UC4
from Data_Provider2 import vAR_DF_LE
from Data_Provider2 import vAR_DF_LE1
from Data_Provider2 import vAR_DF_LE2
from Data_Provider2 import vAR_DF_LE3
from Data_Provider2 import vAR_DF_ET
from Data_Provider2 import vAR_DF_ET1
from Data_Provider2 import vAR_DF_ET2
from Data_Provider2 import vAR_DF_ET3
from Data_Provider2 import vAR_DF_IBR
from Data_Provider2 import vAR_DF_IBR1
from Data_Provider2 import vAR_DF_IBR2
from Data_Provider2 import vAR_DF_IBR3
from Data_Provider2 import vAR_DF_LA
from Data_Provider2 import vAR_DF_LA1
from Data_Provider2 import vAR_DF_LA2
from Data_Provider2 import vAR_DF_LA3

from Data_Provider2 import vAR_Features_Train_YD
from Data_Provider2 import vAR_Label_Train_YD
from Data_Provider2 import vAR_Features_Train1_YD
from Data_Provider2 import vAR_Label_Train1_YD
from Data_Provider2 import vAR_Features_Train2_YD
from Data_Provider2 import vAR_Label_Train2_YD
from Data_Provider2 import vAR_Features_Train3_YD
from Data_Provider2 import vAR_Label_Train3_YD
from Data_Provider2 import vAR_Features_Train4_YD
from Data_Provider2 import vAR_Label_Train4_YD
from Data_Provider2 import vAR_Features_Train5_YD
from Data_Provider2 import vAR_Label_Train5_YD

from Data_Provider2 import vAR_Features_Train_YD_UC_BF
from Data_Provider2 import vAR_Label_Train_YD_UC_BF
from Data_Provider2 import vAR_Features_Train_YD_UC_UF
from Data_Provider2 import vAR_Label_Train_YD_UC_UF
from Data_Provider2 import vAR_Features_Train_YD_UC_OF
from Data_Provider2 import vAR_Label_Train_YD_UC_OF

from Data_Provider2 import vAR_Features_Test1_YD
from Data_Provider2 import vAR_Features_Test2_YD
from Data_Provider2 import vAR_Features_Test3_YD
from Data_Provider2 import vAR_Features_Test4_YD
from Data_Provider2 import vAR_Features_Test5_YD

from Data_Provider2 import vAR_Labels_Pred_YD
from Data_Provider2 import vAR_Labels_Pred1_YD
from Data_Provider2 import vAR_Labels_Pred2_YD
from Data_Provider2 import vAR_Labels_Pred3_YD
from Data_Provider2 import vAR_Labels_Pred4_YD

from Data_Provider2 import vAR_DF_UC_BF
from Data_Provider2 import vAR_DF_UC_UF
from Data_Provider2 import vAR_DF_UC_OF

from Data_Provider2 import vAR_Labels_Pred_YD_UC_BF
from Data_Provider2 import vAR_Labels_Pred_YD_UC_UF
from Data_Provider2 import vAR_Labels_Pred_YD_UC_OF

from Data_Provider2 import vAR_Model_Train_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Validation_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Testing_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Running_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Outcome_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Best_Fit_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Under_Fit_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Over_Fit_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_Before_Hyperparameter_Tuning_Unplanned_Charges_YD
from Data_Provider2 import vAR_Model_After_Hyperparameter_Tuning_Unplanned_Charges_YD

from Data_Provider2 import vAR_Model_Train_Lease_Extension_YD
from Data_Provider2 import vAR_Model_Cross_Validation_Lease_Extension_YD
from Data_Provider2 import vAR_Model_Test_Lease_Extension_YD
from Data_Provider2 import vAR_Model_Run_Lease_Extension_YD
from Data_Provider2 import vAR_Model_Outcome_Lease_Extension_YD

from Data_Provider2 import vAR_Model_Train_Extension_Terms_YD
from Data_Provider2 import vAR_Model_Cross_Validation_Extension_Terms_YD
from Data_Provider2 import vAR_Model_Test_Extension_Terms_YD
from Data_Provider2 import vAR_Model_Run_Extension_Terms_YD
from Data_Provider2 import vAR_Model_Outcome_Extension_Terms_YD

from Data_Provider2 import vAR_Model_Train_IBR_YD
from Data_Provider2 import vAR_Model_Cross_Validation_IBR_YD
from Data_Provider2 import vAR_Model_Test_IBR_YD
from Data_Provider2 import vAR_Model_Run_IBR_YD
from Data_Provider2 import vAR_Model_Outcome_IBR_YD

from Data_Provider2 import vAR_Model_Train_Lease_Amount_YD
from Data_Provider2 import vAR_Model_Cross_Validation_Lease_Amount_YD
from Data_Provider2 import vAR_Model_Test_Lease_Amount_YD
from Data_Provider2 import vAR_Model_Run_Lease_Amount_YD
from Data_Provider2 import vAR_Model_Outcome_Lease_Amount_YD

from flask import Flask, request
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as vAR_plt

app = Flask(__name__)

@app.route('/run_model')

def run_model():
    
    if vAR_Session_ID_Run_AllModel_OD == '1001' :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        from Data_Provider2 import vAR_model
        vAR_model.fit(vAR_Features_Train,vAR_Label_Train)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Validation

        #from sklearn.model_selection import cross_val_predict
        #from sklearn.linear_model import LinearRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train, vAR_Label_Train , cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train.min(), vAR_Label_Train.max()], [vAR_Label_Train.min(), vAR_Label_Train.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual Unplanned Expenses')
        #vAR_ax.set_ylabel('Predicted Unplanned Expenses')
        ##vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

    # Function for Testing the Model

        vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)

        vAR_Labels_Pred = vAR_Labels_Pred.astype(int)

        vAR_Labels_Pred = vAR_pd.DataFrame(vAR_Labels_Pred,columns={'Predicted_Unplanned_Charges'})

        #vAR_Labels_Pred = print(vAR_Labels_Pred)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_UC1 = vAR_df_UC.merge(vAR_Labels_Pred,left_index=True, right_index=True)

        vAR_df_UC2 = vAR_df_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)

        vAR_df_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)

        vAR_df_UC4 = vAR_df_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Best Fit

        #import matplotlib.pyplot as vAR_plt
        #from sklearn.linear_model import LinearRegression
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train_UC_BF, vAR_Labels_Pred_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
        #vAR_ax.plot([vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Under Fit

        #import matplotlib.pyplot as vAR_plt
        #from sklearn.linear_model import LinearRegression
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train_UC_UF, vAR_Labels_Pred_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
        #vAR_ax.plot([vAR_Labels_Pred_UC_UF.min(), vAR_Labels_Pred_UC_UF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Over Fit

        #import matplotlib.pyplot as vAR_plt
        #from sklearn.linear_model import LinearRegression
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train_UC_OF, vAR_Labels_Pred_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
        #vAR_ax.plot([vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()], [vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Hyperparameter Tuning (Before)

        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LinearRegression()
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
        #vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    # Function for Model Hyperparameter Tuning (After)

        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
        #vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
        #vAR_ax.plot()
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
            
    # Function for Training the Model

        vAR_model1.fit(vAR_Features_Train2,vAR_Label_Train2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

        from sklearn.model_selection import cross_val_predict
        from sklearn.linear_model import LogisticRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LogisticRegression()
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2, cv=2)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=2)
        #vAR_ax.set_xlabel('Actual Lease Extension')
        #vAR_ax.set_ylabel('Planned Lease Extension')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2 , cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual Lease Extension')
        #vAR_ax.set_ylabel('Planned Lease Extension')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2, vAR_Label_Train2 , cv=10)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train2, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train2.min(), vAR_Label_Train2.max()], [vAR_Label_Train2.min(), vAR_Label_Train2.max()], 'k--', lw=6)
        #vAR_ax.set_xlabel('Actual Lease Extension')
        #vAR_ax.set_ylabel('Planned Lease Extension')
        ##plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test2 = vAR_df6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome            

        vAR_df_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
        vAR_df_LE1 = vAR_df_LE.merge(vAR_Labels_Pred1,left_index=True, right_index=True)
        vAR_df_LE2 = vAR_df_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
        vAR_df_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model2.fit(vAR_Features_Train3,vAR_Label_Train3)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

        #from sklearn.model_selection import cross_val_predict
        #from sklearn.linear_model import LinearRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LinearRegression()
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=2)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=2)
        #vAR_ax.set_xlabel('Actual Extension Term')
        #vAR_ax.set_ylabel('Predicted Extension Term')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual Extension Term')
        #vAR_ax.set_ylabel('Predicted Extension Term')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train3, vAR_Label_Train3, cv=10)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train3, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train3.min(), vAR_Label_Train3.max()], [vAR_Label_Train3.min(), vAR_Label_Train3.max()], 'k--', lw=6)
        #vAR_ax.set_xlabel('Actual Extension Term')
        #vAR_ax.set_ylabel('Predicted Extension Term')
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test3 = vAR_df8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
        vAR_Features_Test3 = vAR_Features_Test3.loc[vAR_Features_Test3['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
        vAR_df_ET = vAR_df_ET.loc[vAR_df_ET['Predicted_Lease_Extension'] == 1]
        vAR_df_ET1 = vAR_df_ET.merge(vAR_Labels_Pred2,left_index=True, right_index=True)
        vAR_df_ET2 = vAR_df_ET1.to_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_df_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model3.fit(vAR_Features_Train4,vAR_Label_Train4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

        #from sklearn.model_selection import cross_val_predict
        #from sklearn.linear_model import LinearRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LinearRegression()
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=2)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=2)
        #vAR_ax.set_xlabel('Actual IBR')
        #vAR_ax.set_ylabel('Predicted IBR')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual IBR')
        #vAR_ax.set_ylabel('Predicted IBR')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train4, vAR_Label_Train4, cv=10)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train4, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train4.min(), vAR_Label_Train4.max()], [vAR_Label_Train4.min(), vAR_Label_Train4.max()], 'k--', lw=6)
        #vAR_ax.set_xlabel('Actual IBR')
        #vAR_ax.set_ylabel('Predicted IBR')
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test4 = vAR_df10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
        vAR_Features_Test4 = vAR_Features_Test4.loc[vAR_Features_Test4['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_df_IBR = vAR_df_IBR.loc[vAR_df_IBR['Predicted_Lease_Extension'] == 1]
        vAR_df_IBR1 = vAR_df_IBR.merge(vAR_Labels_Pred3,left_index=True, right_index=True)
        vAR_df_IBR2 = vAR_df_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        #vAR_df_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)##

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model4.fit(vAR_Features_Train5,vAR_Label_Train5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

        #from sklearn.model_selection import cross_val_predict
        #from sklearn.linear_model import LinearRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_model = LinearRegression()
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=2)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=2)
        #vAR_ax.set_xlabel('Actual Lease Amount')
        #vAR_ax.set_ylabel('Predicted Lease Amount')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual Lease Amount')
        #vAR_ax.set_ylabel('Predicted Lease Amount')
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train5, vAR_Label_Train5, cv=10)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train5, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train5.min(), vAR_Label_Train5.max()], [vAR_Label_Train5.min(), vAR_Label_Train5.max()], 'k--', lw=6)
        #vAR_ax.set_xlabel('Actual Lease Amount')
        #vAR_ax.set_ylabel('Predicted Lease Amount')
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred4

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_df_LA = vAR_df_LA.loc[vAR_df_LA['Predicted_Lease_Extension'] == 1]
        vAR_df_LA1 = vAR_df_LA.merge(vAR_Labels_Pred4,left_index=True, right_index=True)
        vAR_df_LA2 = vAR_df_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
        vAR_df_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)   
               
        vAR_data = pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_AllModel_YD == '2001':
        
    # Function for Training the Model

        from Data_Provider2 import vAR_model
        vAR_model.fit(vAR_Features_Train_YD,vAR_Label_Train_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Validation

        #from sklearn.model_selection import cross_val_predict
        #from sklearn.linear_model import LinearRegression
        #import matplotlib.pyplot as vAR_plt
        #vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train_YD, vAR_Label_Train_YD , cv=5)
        #vAR_fig, vAR_ax = vAR_plt.subplots()
        #vAR_ax.scatter(vAR_Label_Train_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        #vAR_ax.plot([vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], [vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], 'k--', lw=4)
        #vAR_ax.set_xlabel('Actual Unplanned Expenses')
        #vAR_ax.set_ylabel('Predicted Unplanned Expenses')
        ##vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

    # Function for Testing the Model

        vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)

        vAR_Labels_Pred_YD = vAR_Labels_Pred_YD.astype(int)

        vAR_Labels_Pred_YD = vAR_pd.DataFrame(vAR_Labels_Pred_YD,columns={'Predicted_Unplanned_Charges'})

        #vAR_Labels_Pred = print(vAR_Labels_Pred)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_UC1 = vAR_DF_UC.merge(vAR_Labels_Pred_YD,left_index=True, right_index=True)

        vAR_DF_UC2 = vAR_DF_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)

        vAR_DF_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)

        vAR_DF_UC4 = vAR_DF_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Best Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_BF, vAR_Labels_Pred_YD_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Under Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_UF, vAR_Labels_Pred_YD_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_UF.min(), vAR_Labels_Pred_YD_UC_UF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Over Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_OF, vAR_Labels_Pred_YD_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()], [vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Hyperparameter Tuning (Before)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression()
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1_YD, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    # Function for Model Hyperparameter Tuning (After)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1_YD, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

    # Function for Training the Model
    
        vAR_model1.fit(vAR_Features_Train2_YD,vAR_Label_Train2_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD, cv=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=4)
        vAR_ax.set_xlabel('Actual Lease Extension')
        vAR_ax.set_ylabel('Planned Lease Extension')
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD, cv=10)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=6)
        vAR_ax.set_xlabel('Actual Lease Extension')
        vAR_ax.set_ylabel('Planned Lease Extension')
        ##plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test2_YD = vAR_DF6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred1_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome            

        vAR_DF_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        vAR_DF_LE1 = vAR_DF_LE.merge(vAR_Labels_Pred1_YD,left_index=True, right_index=True)
        vAR_DF_LE2 = vAR_DF_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_DF_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model2.fit(vAR_Features_Train3_YD,vAR_Label_Train3_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test3_YD = vAR_DF8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
        vAR_Features_Test3_YD = vAR_Features_Test3_YD.loc[vAR_Features_Test3_YD['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred2_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_DF_ET = vAR_DF_ET.loc[vAR_DF_ET['Predicted_Lease_Extension'] == 1]
        vAR_DF_ET1 = vAR_DF_ET.merge(vAR_Labels_Pred2_YD,left_index=True, right_index=True)
        vAR_DF_ET2 = vAR_DF_ET1.to_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_DF_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model3.fit(vAR_Features_Train4_YD,vAR_Label_Train4_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test4_YD = vAR_DF10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
        vAR_Features_Test4_YD = vAR_Features_Test4_YD.loc[vAR_Features_Test4_YD['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred3_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_DF_IBR = vAR_DF_IBR.loc[vAR_DF_IBR['Predicted_Lease_Extension'] == 1]
        vAR_DF_IBR1 = vAR_DF_IBR.merge(vAR_Labels_Pred3_YD,left_index=True, right_index=True)
        vAR_DF_IBR2 = vAR_DF_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model4.fit(vAR_Features_Train5_YD,vAR_Label_Train5_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred4_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF_LA = vAR_DF_LA.loc[vAR_DF_LA['Predicted_Lease_Extension'] == 1]
        vAR_DF_LA1 = vAR_DF_LA.merge(vAR_Labels_Pred4_YD,left_index=True, right_index=True)
        vAR_DF_LA2 = vAR_DF_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)
        vAR_DF_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())
  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model1_OD == '100' :

# Function for Training the Model

        from Data_Provider2 import vAR_model
        vAR_model.fit(vAR_Features_Train,vAR_Label_Train)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Validation

        from sklearn.model_selection import cross_val_predict
        from sklearn.linear_model import LinearRegression
        import matplotlib.pyplot as vAR_plt
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train, vAR_Label_Train , cv=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train.min(), vAR_Label_Train.max()], [vAR_Label_Train.min(), vAR_Label_Train.max()], 'k--', lw=4)
        vAR_ax.set_xlabel('Actual Unplanned Expenses')
        vAR_ax.set_ylabel('Predicted Unplanned Expenses')
        ##vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

    # Function for Testing the Model

        vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred = vAR_model.predict(vAR_Features_Test1)

        vAR_Labels_Pred = vAR_Labels_Pred.astype(int)

        vAR_Labels_Pred = vAR_pd.DataFrame(vAR_Labels_Pred,columns={'Predicted_Unplanned_Charges'})

        #vAR_Labels_Pred = print(vAR_Labels_Pred)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_UC1 = vAR_df_UC.merge(vAR_Labels_Pred,left_index=True, right_index=True)

        vAR_df_UC2 = vAR_df_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)

        vAR_df_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)

        vAR_df_UC4 = vAR_df_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    


        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Best Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_UC_BF, vAR_Labels_Pred_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Under Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_UC_UF, vAR_Labels_Pred_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_UC_UF.min(), vAR_Labels_Pred_UC_UF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Over Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_UC_OF, vAR_Labels_Pred_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()], [vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Hyperparameter Tuning (Before)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression()
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    # Function for Model Hyperparameter Tuning (After)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    if vAR_Session_ID_Run_Model2_OD == '111':

    # Function for Training the Model

       vAR_model1.fit(vAR_Features_Train2,vAR_Label_Train2)   

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

    # Function for Validating the Model

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

       vAR_Features_Test2 = vAR_df6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

       vAR_Labels_Pred1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome            

       vAR_df_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_OD)
       vAR_df_LE1 = vAR_df_LE.merge(vAR_Labels_Pred1,left_index=True, right_index=True)
       vAR_df_LE2 = vAR_df_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
       vAR_df_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)

       vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
       vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
       vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
       vAR_response = urllib.request.urlopen(vAR_url)
       vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                          

    if vAR_Session_ID_Run_Model3_OD == '121':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model2.fit(vAR_Features_Train3,vAR_Label_Train3)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test3 = vAR_df8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
        vAR_Features_Test3 = vAR_Features_Test3.loc[vAR_Features_Test3['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_OD)
        vAR_df_ET = vAR_df_ET.loc[vAR_df_ET['Predicted_Lease_Extension'] == 1]
        vAR_df_ET1 = vAR_df_ET.merge(vAR_Labels_Pred2,left_index=True, right_index=True)
        vAR_df_ET2 = vAR_df_ET1.to_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_df_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model4_OD == '131':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model3.fit(vAR_Features_Train4,vAR_Label_Train4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test4 = vAR_df10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
        vAR_Features_Test4 = vAR_Features_Test4.loc[vAR_Features_Test4['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_OD)
        vAR_df_IBR = vAR_df_IBR.loc[vAR_df_IBR['Predicted_Lease_Extension'] == 1]
        vAR_df_IBR1 = vAR_df_IBR.merge(vAR_Labels_Pred3,left_index=True, right_index=True)
        vAR_df_IBR2 = vAR_df_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_df_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model5_OD == '141':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model4.fit(vAR_Features_Train5,vAR_Label_Train5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_df11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_df11 = vAR_df11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred4

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_df_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_OD)
        vAR_df_LA = vAR_df_LA.loc[vAR_df_LA['Predicted_Lease_Extension'] == 1]
        vAR_df_LA1 = vAR_df_LA.merge(vAR_Labels_Pred4,left_index=True, right_index=True)
        vAR_df_LA2 = vAR_df_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
        vAR_df_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_OD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_OD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           

    if vAR_Session_ID_Run_Model1_YD == '151':


    # Function for Training the Model

        from Data_Provider2 import vAR_model
        vAR_model.fit(vAR_Features_Train_YD,vAR_Label_Train_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Validation

        from sklearn.model_selection import cross_val_predict
        from sklearn.linear_model import LinearRegression
        import matplotlib.pyplot as vAR_plt
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train_YD, vAR_Label_Train_YD , cv=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], [vAR_Label_Train_YD.min(), vAR_Label_Train_YD.max()], 'k--', lw=4)
        vAR_ax.set_xlabel('Actual Unplanned Expenses')
        vAR_ax.set_ylabel('Predicted Unplanned Expenses')
        ##vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

    # Function for Testing the Model

        vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred_YD = vAR_model.predict(vAR_Features_Test1_YD)

        vAR_Labels_Pred_YD = vAR_Labels_Pred_YD.astype(int)

        vAR_Labels_Pred_YD = vAR_pd.DataFrame(vAR_Labels_Pred_YD,columns={'Predicted_Unplanned_Charges'})

        #vAR_Labels_Pred = print(vAR_Labels_Pred)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_UC1 = vAR_DF_UC.merge(vAR_Labels_Pred_YD,left_index=True, right_index=True)

        vAR_DF_UC2 = vAR_DF_UC1.to_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)

        vAR_DF_UC3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)

        vAR_DF_UC4 = vAR_DF_UC3[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]    

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Best Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_BF, vAR_Labels_Pred_YD_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Under Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_UF, vAR_Labels_Pred_YD_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_UF.min(), vAR_Labels_Pred_YD_UC_UF.max()], [vAR_Labels_Pred_YD_UC_BF.min(), vAR_Labels_Pred_YD_UC_BF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Over Fit

        import matplotlib.pyplot as vAR_plt
        from sklearn.linear_model import LinearRegression
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train_YD_UC_OF, vAR_Labels_Pred_YD_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
        vAR_ax.plot([vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()], [vAR_Labels_Pred_YD_UC_OF.min(), vAR_Labels_Pred_YD_UC_OF.max()])
        #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Hyperparameter Tuning (Before)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression()
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1_YD, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    # Function for Model Hyperparameter Tuning (After)

        import matplotlib.pyplot as vAR_plt
        vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train1_YD, vAR_Labels_Pred_YD, edgecolors=(0, 0, 0), s=50, c='gbc')
        vAR_ax.plot([vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()], [vAR_Labels_Pred_YD.min(), vAR_Labels_Pred_YD.max()])
        vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

    if vAR_Session_ID_Run_Model2_YD == '161':

    # Function for Training the Model
    
        vAR_model1.fit(vAR_Features_Train2_YD,vAR_Label_Train2_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD, cv=5)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=4)
        vAR_ax.set_xlabel('Actual Lease Extension')
        vAR_ax.set_ylabel('Planned Lease Extension')
        vAR_Predicted = cross_val_predict(vAR_model, vAR_Features_Train2_YD, vAR_Label_Train2_YD, cv=10)
        vAR_fig, vAR_ax = vAR_plt.subplots()
        vAR_ax.scatter(vAR_Label_Train2_YD, vAR_Predicted, edgecolors=(0, 0, 0))
        vAR_ax.plot([vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], [vAR_Label_Train2_YD.min(), vAR_Label_Train2_YD.max()], 'k--', lw=6)
        vAR_ax.set_xlabel('Actual Lease Extension')
        vAR_ax.set_ylabel('Planned Lease Extension')
        ##plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test2_YD = vAR_DF6[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred1_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome            

        vAR_DF_LE = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        vAR_DF_LE1 = vAR_DF_LE.merge(vAR_Labels_Pred1_YD,left_index=True, right_index=True)
        vAR_DF_LE2 = vAR_DF_LE1.to_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_DF_LE3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model3_YD == '171':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model2.fit(vAR_Features_Train3_YD,vAR_Label_Train3_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test3_YD = vAR_DF8[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension']]
        vAR_Features_Test3_YD = vAR_Features_Test3_YD.loc[vAR_Features_Test3_YD['Predicted_Lease_Extension'] == 1]  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred2_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_ET = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
        vAR_DF_ET = vAR_DF_ET.loc[vAR_DF_ET['Predicted_Lease_Extension'] == 1]
        vAR_DF_ET1 = vAR_DF_ET.merge(vAR_Labels_Pred2_YD,left_index=True, right_index=True)
        vAR_DF_ET2 = vAR_DF_ET1.to_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_DF_ET3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model4_YD == '181':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model3.fit(vAR_Features_Train4_YD,vAR_Label_Train4_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_Features_Test4_YD = vAR_DF10[[vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms']]
        vAR_Features_Test4_YD = vAR_Features_Test4_YD.loc[vAR_Features_Test4_YD['Predicted_Lease_Extension'] == 1]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred3_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_IBR = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        vAR_DF_IBR = vAR_DF_IBR.loc[vAR_DF_IBR['Predicted_Lease_Extension'] == 1]
        vAR_DF_IBR1 = vAR_DF_IBR.merge(vAR_Labels_Pred3_YD,left_index=True, right_index=True)
        vAR_DF_IBR2 = vAR_DF_IBR1.to_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF_IBR3 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if vAR_Session_ID_Run_Model5_YD == '191':

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Training the Model

        vAR_model4.fit(vAR_Features_Train5_YD,vAR_Label_Train5_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Validating the Model

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
        #vAR_plt.show()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Testing the Model

        vAR_DF11 = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF11 = vAR_DF11[[vAR_Fetched_Feature1,vAR_Fetched_Feature2,vAR_Fetched_Feature3,vAR_Fetched_Feature4,vAR_Fetched_Feature5,vAR_Fetched_Feature6,vAR_Fetched_Feature7,vAR_Fetched_Feature8,vAR_Fetched_Feature9,vAR_Fetched_Feature10,'Predicted_Unplanned_Charges','Predicted_Lease_Extension','Predicted_Extension_Terms','Predicted_IBR']]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Running the Model

        vAR_Labels_Pred4_YD

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Outcome

        vAR_DF_LA = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_DF_LA = vAR_DF_LA.loc[vAR_DF_LA['Predicted_Lease_Extension'] == 1]
        vAR_DF_LA1 = vAR_DF_LA.merge(vAR_Labels_Pred4_YD,left_index=True, right_index=True)
        vAR_DF_LA2 = vAR_DF_LA1.to_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)
        vAR_DF_LA3 = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_OD)

        vAR_data = pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
        vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_json_Data_YD)
        vAR_url = vAR_Fetched_Path_Preview_Outcome_json_Data_URL_YD
        vAR_response = urllib.request.urlopen(vAR_url)
        vAR_data = json.loads(vAR_response.read())

    else:
         print("Model not Run")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #if vAR_Session_ID_Run_Model1_OD == '101' :
    
        #return "Model-Unplanned Expenses for our Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model2_OD == '111' :

        #return "Model-Lease Extension for our Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model3_OD == '120' :

        #return "Model-Extension Terms for our Data Ran Sucessfully"
    
    #elif vAR_Session_ID_Run_Model4_OD == '130' :

        #return "Model-IBR for our Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model5_OD == '140' :

        #return "Model-Lease Amount for our Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_AllModel_YD == '1000' :

        #return "All Models for our Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model1_YD == '150' :
    
        #return "Model-Unplanned Expenses for Your Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model2_YD == '160' :

        #return "Model-Lease Extension for Your Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model3_YD == '170' :

        #return "Model-Extension Terms for Your Data Ran Sucessfully"
    
    #elif vAR_Session_ID_Run_Model4_YD == '180' :

        #return "Model-IBR for Your Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_Model5_YD == '190' :

        #return "Model-Lease Amount for Your Data Ran Sucessfully"

    #elif vAR_Session_ID_Run_AllModel_YD == '2000' :

        #return "All Models for Your Data Ran Sucessfully"  

    return "Model Run Sucessfully"  
  
if __name__ == '__main__':
    print("Model Run Sucessfully")
    
# Run Server

app.run(host='0.0.0.0',port=9000,use_reloader=True)
