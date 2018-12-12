import configparser
vAR_Config = configparser.ConfigParser(allow_no_value=True)
vAR_Config.read('C:/AI_POC/Lease_Formulation/DS_LEASE_ACCOUNTING_MODEL_CONS_INI_FILE1.INI')
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Session ID Inputs

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_Session_ID_Preview_Model1_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL1_OD']
#print(vAR_Session_ID_Preview_Model1_OD)

vAR_Session_ID_Preview_Model2_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL2_OD']
#print(vAR_Session_ID_Preview_Model2_OD)

vAR_Session_ID_Preview_Model3_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL3_OD']
#print(vAR_Session_ID_Preview_Model3_OD)

vAR_Session_ID_Preview_Model4_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL4_OD']
#print(vAR_Session_ID_Preview_Model4_OD)

vAR_Session_ID_Preview_Model5_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL5_OD']
#print(vAR_Session_ID_Preview_Model5_OD)

vAR_Session_ID_Preview_AllModel_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_ALL_MODEL_OD']
#print(vAR_Session_ID_Preview_AllModel_OD)


vAR_Session_ID_Run_Model1_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL1_OD']
#print(vAR_Session_ID_Run_Model1_OD)

vAR_Session_ID_Run_Model2_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL2_OD']
#print(vAR_Session_ID_Run_Model2_OD)

vAR_Session_ID_Run_Model3_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL3_OD']
#print(vAR_Session_ID_Run_Model3_OD)

vAR_Session_ID_Run_Model4_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL4_OD']
#print(vAR_Session_ID_Run_Model4_OD)

vAR_Session_ID_Run_Model5_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL5_OD']
#print(vAR_Session_ID_Run_Model5_OD)

vAR_Session_ID_Run_AllModel_OD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_ALL_MODEL_OD']
#print(vAR_Session_ID_Run_AllModel_OD)


vAR_Session_ID_Preview_Model1_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL1_YD']
#print(vAR_Session_ID_Preview_Model1_YD)

vAR_Session_ID_Preview_Model2_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL2_YD']
#print(vAR_Session_ID_Preview_Model2_YD)

vAR_Session_ID_Preview_Model3_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL3_YD']
#print(vAR_Session_ID_Preview_Model3_YD)

vAR_Session_ID_Preview_Model4_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL4_YD']
#print(vAR_Session_ID_Preview_Model4_YD)

vAR_Session_ID_Preview_Model5_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_MODEL5_YD']
#print(vAR_Session_ID_Preview_Model5_YD)

vAR_Session_ID_Preview_AllModel_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_PREVIEW_ALL_MODEL_YD']
#print(vAR_Session_ID_Preview_AllModel_YD)


vAR_Session_ID_Run_Model1_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL1_YD']
print(vAR_Session_ID_Run_Model1_YD)

vAR_Session_ID_Run_Model2_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL2_YD']
#print(vAR_Session_ID_Run_Model2_YD)

vAR_Session_ID_Run_Model3_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL3_YD']
#print(vAR_Session_ID_Run_Model3_YD)

vAR_Session_ID_Run_Model4_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL4_YD']
#print(vAR_Session_ID_Run_Model4_YD)

vAR_Session_ID_Run_Model5_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_MODEL5_YD']
#print(vAR_Session_ID_Run_Model5_YD)

vAR_Session_ID_Run_AllModel_YD = vAR_Config['PROBLEM1 CONFIGURATION']['SESSION_ID_RUN_ALL_MODEL_YD']
#print(vAR_Session_ID_Run_AllModel_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## File Name Inputs

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_File_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['FILE_NAME_PREVIEW_YOUR_DATA']
#print(vAR_File_Name_Preview_Your_Data)

vAR_File_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['FILE_NAME_RUN_YOUR_DATA']
print(vAR_File_Name_Run_Your_Data)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Model Name Inputs

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_Model1_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_PREVIEW_OUR_DATA']
#print(vAR_Model1_Name_Preview_Our_Data)

vAR_Model2_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_PREVIEW_OUR_DATA']
#print(vAR_Model2_Name_Preview_Our_Data)

vAR_Model3_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_PREVIEW_OUR_DATA']
#print(vAR_Model3_Name_Preview_Our_Data)

vAR_Model4_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_PREVIEW_OUR_DATA']
#print(vAR_Model4_Name_Preview_Our_Data)

vAR_Model5_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_PREVIEW_OUR_DATA']
#print(vAR_Model5_Name_Preview_Our_Data)

vAR_AllModel_Name_Preview_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_NAME_PREVIEW_OUR_DATA']
#print(vAR_AllModel_Name_Preview_Our_Data)


vAR_Model1_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_RUN_OUR_DATA']
#print(vAR_Model1_Name_Run_Our_Data)

vAR_Model2_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_RUN_OUR_DATA']
#print(vAR_Model2_Name_Run_Our_Data)

vAR_Model3_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_RUN_OUR_DATA']
#print(vAR_Model3_Name_Run_Our_Data)

vAR_Model4_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_RUN_OUR_DATA']
#print(vAR_Model4_Name_Run_Our_Data)

vAR_Model5_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_RUN_OUR_DATA']
#print(vAR_Model5_Name_Run_Our_Data)

vAR_AllModel_Name_Run_Our_Data = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_NAME_RUN_OUR_DATA']
#print(vAR_AllModel_Name_Run_Our_Data)


vAR_Model1_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_PREVIEW_YOUR_DATA']
#print(vAR_Model1_Name_Preview_Your_Data)

vAR_Model2_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_PREVIEW_YOUR_DATA']
#print(vAR_Model2_Name_Preview_Your_Data)

vAR_Model3_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_PREVIEW_YOUR_DATA']
#print(vAR_Model3_Name_Preview_Your_Data)

vAR_Model4_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_PREVIEW_YOUR_DATA']
#print(vAR_Model4_Name_Preview_Your_Data)

vAR_Model5_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_PREVIEW_YOUR_DATA']
#print(vAR_Model5_Name_Preview_Your_Data)

vAR_AllModel_Name_Preview_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_NAME_PREVIEW_YOUR_DATA']
#print(vAR_AllModel_Name_Preview_Your_Data)


vAR_Model1_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_NAME_RUN_YOUR_DATA']
print(vAR_Model1_Name_Run_Our_Data)

vAR_Model2_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_NAME_RUN_YOUR_DATA']
#print(vAR_Model2_Name_Run_Our_Data)

vAR_Model3_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_NAME_RUN_YOUR_DATA']
#print(vAR_Model3_Name_Run_Our_Data)

vAR_Model4_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_NAME_RUN_YOUR_DATA']
#print(vAR_Model4_Name_Run_Our_Data)

vAR_Model5_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_NAME_RUN_YOUR_DATA']
#print(vAR_Model5_Name_Run_Our_Data)

vAR_AllModel_Name_Run_Your_Data = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_NAME_RUN_YOUR_DATA']
#print(vAR_AllModel_Name_Run_Your_Data)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## User Action Inputs

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_Model1_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_FLAG_PREVIEW_OD']
#print(vAR_Model1_Preview_Flag_OD)

vAR_Model2_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_FLAG_PREVIEW_OD']
#print(vAR_Model2_Preview_Flag_OD)

vAR_Model3_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_FLAG_PREVIEW_OD']
#print(vAR_Model3_Preview_Flag_OD)

vAR_Model4_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_FLAG_PREVIEW_OD']
#print(vAR_Model4_Preview_Flag_OD)

vAR_Model5_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_FLAG_PREVIEW_OD']
#print(vAR_Model5_Flag_OD)

vAR_AllModel_Preview_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_FLAG_PREVIEW_OD']
#print(vAR_AllModel_Preview_Flag_OD)


vAR_Model1_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_FLAG_RUN_OD']
#print(vAR_Model1_Run_Flag_OD)

vAR_Model2_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_FLAG_RUN_OD']
#print(vAR_Model2_Run_Flag_OD)

vAR_Model3_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_FLAG_RUN_OD']
#print(vAR_Model3_Run_Flag_OD)

vAR_Model4_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_FLAG_RUN_OD']
#print(vAR_Model4_Run_Flag_OD)

vAR_Model5_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_FLAG_RUN_OD']
#print(vAR_Model5_Run_Flag_OD)

vAR_AllModel_Run_Flag_OD = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_FLAG_RUN_OD']
#print(vAR_AllModel_Run_Flag_OD)


vAR_Model1_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_FLAG_PREVIEW_YD']
#print(vAR_Model1_Preview_Flag_YD)

vAR_Model2_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_FLAG_PREVIEW_YD']
#print(vAR_Model2_Preview_Flag_YD)

vAR_Model3_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_FLAG_PREVIEW_YD']
#print(vAR_Model3_Preview_Flag_YD)

vAR_Model4_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_FLAG_PREVIEW_YD']
#print(vAR_Model4_Preview_Flag_YD)

vAR_Model5_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_FLAG_PREVIEW_YD']
#print(vAR_Model5_Flag_YD)

vAR_AllModel_Preview_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_FLAG_PREVIEW_YD']
#print(vAR_AllModel_Preview_Flag_YD)


vAR_Model1_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL1_FLAG_RUN_YD']
print(vAR_Model1_Run_Flag_YD)

vAR_Model2_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL2_FLAG_RUN_YD']
#print(vAR_Model2_Run_Flag_YD)

vAR_Model3_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL3_FLAG_RUN_YD']
#print(vAR_Model3_Run_Flag_YD)

vAR_Model4_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL4_FLAG_RUN_YD']
#print(vAR_Model4_Run_Flag_YD)

vAR_Model5_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['MODEL5_FLAG_RUN_YD']
#print(vAR_Model5_Run_Flag_YD)

vAR_AllModel_Run_Flag_YD = vAR_Config['PROBLEM1 CONFIGURATION']['ALL_MODEL_FLAG_RUN_YD']
#print(vAR_AllModel_Run_Flag_YD)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vAR_Fetched_Path_Preview_Outcome_UC_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_UNPLANNED_CHARGES_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_OD)                                

vAR_Fetched_Path_Preview_Outcome_LE_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_LEASE_EXTENSION_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_OD)

vAR_Fetched_Path_Preview_Outcome_ET_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_EXTENSION_TERMS_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_OD)

vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_IBR_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_OD)

vAR_Fetched_Path_Preview_Outcome_LA_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_LEASE_AMOUNT_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_LA_json_Data_OD)

vAR_Fetched_Path_Preview_Outcome_All_json_Data_OD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_ALL_JSON_DATA_PATH_OD']
#print(vAR_Fetched_Path_Preview_Outcome_All_json_Data_OD)


vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_UNPLANNED_CHARGES_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_LEASE_EXTENSION_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_EXTENSION_TERMS_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_IBR_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_LEASE_AMOUNT_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD)

vAR_Fetched_Path_Preview_Outcome_All_json_Data_YD = vAR_Config['PROBLEM1 CONFIGURATION']['PREVIEW_OUTCOME_ALL_JSON_DATA_PATH_YD']
#print(vAR_Fetched_Path_Preview_Outcome_All_json_Data_YD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
import urllib, json
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as vAR_plt
import os
import paramiko
import requests

app = Flask(__name__)

@app.route('/run_model')

def run_model():

    vAR_Payload="""{"vAR_Wrapper": {
    "vAR_Session_ID_Preview_Model1_OD": "200",
    "vAR_Session_ID_Preview_Model2_OD": "210",
    "vAR_Session_ID_Preview_Model3_OD": "220",
    "vAR_Session_ID_Preview_Model4_OD": "230",
    "vAR_Session_ID_Preview_Model5_OD": "240",    
    "vAR_Session_ID_Preview_AllModel_OD": "3000",
    "vAR_Session_ID_Preview_Model1_YD": "250",
    "vAR_Session_ID_Preview_Model2_YD": "260",
    "vAR_Session_ID_Preview_Model3_YD": "270",
    "vAR_Session_ID_Preview_Model4_YD": "280",
    "vAR_Session_ID_Preview_Model5_YD": "290" ,   
    "vAR_Session_ID_Preview_AllModel_YD": "4000",
    "vAR_Session_ID_Run_Model1_OD": "100",
    "vAR_Session_ID_Run_Model2_OD": "110",
    "vAR_Session_ID_Run_Model3_OD": "120",
    "vAR_Session_ID_Run_Model4_OD": "130",
    "vAR_Session_ID_Run_Model5_OD": "140",
    "vAR_Session_ID_Run_All_Model_OD": "1000",
    "vAR_Session_ID_Run_Model1_YD": "150",
    "vAR_Session_ID_Run_Model2_YD": "160",
    "vAR_Session_ID_Run_Model3_YD": "170",
    "vAR_Session_ID_Run_Model4_YD": "180",
    "vAR_Session_ID_Run_Model5_YD": "190",
    "vAR_Session_ID_Run_All_Model_YD": "2000",
    "vAR_File_Name_Preview_Your_Data": "Test_Data_Unplanned_Expenses.xlsx",
    "vAR_File_Name_Run_Your_Data": "Test_Data_Unplanned_Expenses.xlsx",
    "vAR_Model1_Name_Preview_Our_Data": "Model1_PREVIEW_OD",
    "vAR_Model2_Name_Preview_Our_Data": "Model2_PREVIEW_OD",
    "vAR_Model3_Name_Preview_Our_Data": "Model2_PREVIEW_OD",
    "vAR_Model4_Name_Preview_Our_Data": "Model4_PREVIEW_OD",
    "vAR_Model5_Name_Preview_Our_Data": "Model5_PREVIEW_OD",
    "vAR_All_Model_Name_Preview_Our_Data": "ALL_MODEL_PREVIEW_OD",
    "vAR_Model1_Name_Run_Our_Data": "Model1_RUN_OD",
    "vAR_Model2_Name_Run_Our_Data": "Model2_RUN_OD",
    "vAR_Model3_Name_Run_Our_Data": "Model3_RUN_OD",
    "vAR_Model4_Name_Run_Our_Data": "Model4_RUN_OD",
    "vAR_Model5_Name_Run_Our_Data": "Model5_RUN_OD",
    "vAR_All_Model_Name_Run_Our_Data": "ALL_MODEL_RUN_OD",
    "vAR_Model1_Name_Preview_Your_Data": "Model1_PREVIEW_YD",
    "vAR_Model2_Name_Preview_Your_Data": "Model2_PREVIEW_YD",
    "vAR_Model3_Name_Preview_Your_Data": "Model2_PREVIEW_YD",
    "vAR_Model4_Name_Preview_Your_Data": "Model4_PREVIEW_YD",
    "vAR_Model5_Name_Preview_Your_Data": "Model5_PREVIEW_YD",
    "vAR_All_Model_Name_Preview_Your_Data": "ALL_MODEL_PREVIEW_YD",
    "vAR_Model1_Name_Run_Your_Data": "Model1_RUN_YD",
    "vAR_Model2_Name_Run_Your_Data": "Model2_RUN_YD",
    "vAR_Model3_Name_Run_Your_Data": "Model3_RUN_YD",
    "vAR_Model4_Name_Run_Your_Data": "Model4_RUN_YD",
    "vAR_Model5_Name_Run_Your_Data": "Model5_RUN_YD",
    "vAR_All_Model_Name_Run_Your_Data": "ALL_MODEL_RUN_YD",
    "vAR_Model1_Flag_Preview_OD": "N",
    "vAR_Model2_Flag_Preview_OD": "N",
    "vAR_Model3_Flag_Preview_OD": "N",
    "vAR_Model4_Flag_Preview_OD": "N",
    "vAR_Model5_Flag_Preview_OD": "N",
    "vAR_All_Model_Flag_Preview_OD": "N",
    "vAR_Model1_Flag_Run_OD": "Y",
    "vAR_Model2_Flag_Run_OD": "N",
    "vAR_Model3_Flag_Run_OD": "N",
    "vAR_Model4_Flag_Run_OD": "N",
    "vAR_Model5_Flag_Run_OD": "N",
    "vAR_All_Model_Flag_Run_OD": "N",
    "vAR_Model1_Flag_Preview_YD": "N",
    "vAR_Model2_Flag_Preview_YD": "N",
    "vAR_Model3_Flag_Preview_YD": "N",
    "vAR_Model4_Flag_Preview_YD": "N",
    "vAR_Model5_Flag_Preview_YD": "N",
    "vAR_All_Model_Flag_Preview_YD": "N",
    "vAR_Model1_Flag_Run_YD": "N",
    "vAR_Model2_Flag_Run_YD": "N",
    "vAR_Model3_Flag_Run_YD": "N",
    "vAR_Model4_Flag_Run_YD": "N",
    "vAR_Model5_Flag_Run_YD": "N",
    "vAR_All_Model_Flag_Run_YD": "N"
    }}
    """

    vARdata = json.loads(vAR_Payload)
    #print(vARdata)

    SESSION_ID_PREVIEW_MODEL1_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model1_OD']
 
    SESSION_ID_PREVIEW_MODEL2_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model2_OD']

    SESSION_ID_PREVIEW_MODEL3_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model3_OD']

    SESSION_ID_PREVIEW_MODEL4_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model4_OD']

    SESSION_ID_PREVIEW_MODEL5_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model5_OD']

    SESSION_ID_PREVIEW_ALL_MODEL_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_AllModel_OD']

    SESSION_ID_PREVIEW_MODEL1_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model1_YD']
 
    SESSION_ID_PREVIEW_MODEL2_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model2_YD']

    SESSION_ID_PREVIEW_MODEL3_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model3_YD']

    SESSION_ID_PREVIEW_MODEL4_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model4_YD']

    SESSION_ID_PREVIEW_MODEL5_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_Model5_YD']

    SESSION_ID_PREVIEW_ALL_MODEL_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Preview_AllModel_YD']

    SESSION_ID_RUN_MODEL1_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model1_OD']
 
    SESSION_ID_RUN_MODEL2_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model2_OD']

    SESSION_ID_RUN_MODEL3_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model3_OD']

    SESSION_ID_RUN_MODEL4_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model4_OD']

    SESSION_ID_RUN_MODEL5_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model5_OD']

    SESSION_ID_RUN_ALL_MODEL_OD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_All_Model_OD']

    SESSION_ID_RUN_MODEL1_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model1_YD']
 
    SESSION_ID_RUN_MODEL2_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model2_YD']

    SESSION_ID_RUN_MODEL3_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model3_YD']

    SESSION_ID_RUN_MODEL4_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model4_YD']

    SESSION_ID_RUN_MODEL5_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_Model5_YD']

    SESSION_ID_RUN_ALL_MODEL_YD = vARdata['vAR_Wrapper']['vAR_Session_ID_Run_All_Model_YD']

    FILE_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_File_Name_Preview_Your_Data']

    FILE_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_File_Name_Run_Your_Data']

    MODEL1_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model1_Name_Preview_Our_Data']

    MODEL2_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model2_Name_Preview_Our_Data']

    MODEL3_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model3_Name_Preview_Our_Data']

    MODEL4_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model4_Name_Preview_Our_Data']

    MODEL5_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model5_Name_Preview_Our_Data']

    ALL_MODEL_NAME_PREVIEW_OUR_DATA = vARdata['vAR_Wrapper']['vAR_All_Model_Name_Preview_Our_Data']

    MODEL1_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model1_Name_Run_Our_Data']

    MODEL2_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model2_Name_Run_Our_Data']

    MODEL3_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model3_Name_Run_Our_Data']

    MODEL4_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model4_Name_Run_Our_Data']

    MODEL5_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_Model5_Name_Run_Our_Data']

    ALL_MODEL_NAME_RUN_OUR_DATA = vARdata['vAR_Wrapper']['vAR_All_Model_Name_Run_Our_Data']

    MODEL1_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model1_Name_Preview_Your_Data']

    MODEL2_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model2_Name_Preview_Your_Data']

    MODEL3_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model3_Name_Preview_Your_Data']

    MODEL4_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model4_Name_Preview_Your_Data']

    MODEL5_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model5_Name_Preview_Your_Data']

    ALL_MODEL_NAME_PREVIEW_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_All_Model_Name_Preview_Your_Data']

    MODEL1_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model1_Name_Run_Your_Data']

    MODEL2_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model2_Name_Run_Your_Data']

    MODEL3_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model3_Name_Run_Your_Data']

    MODEL4_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model4_Name_Run_Your_Data']

    MODEL5_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_Model5_Name_Run_Your_Data']

    ALL_MODEL_NAME_RUN_YOUR_DATA = vARdata['vAR_Wrapper']['vAR_All_Model_Name_Run_Your_Data']

    MODEL1_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_Model1_Flag_Preview_OD']

    MODEL2_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_Model2_Flag_Preview_OD']

    MODEL3_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_Model3_Flag_Preview_OD']

    MODEL4_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_Model4_Flag_Preview_OD']

    MODEL5_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_Model5_Flag_Preview_OD']

    ALL_MODEL_FLAG_PREVIEW_OD = vARdata['vAR_Wrapper']['vAR_All_Model_Name_Preview_Our_Data']

    MODEL1_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_Model1_Flag_Run_OD']

    MODEL2_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_Model2_Flag_Run_OD']

    MODEL3_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_Model3_Flag_Run_OD']

    MODEL4_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_Model4_Flag_Run_OD']

    MODEL5_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_Model5_Flag_Run_OD']

    ALL_MODEL_FLAG_RUN_OD = vARdata['vAR_Wrapper']['vAR_All_Model_Flag_Run_OD']

    MODEL1_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_Model1_Flag_Preview_YD']

    MODEL2_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_Model2_Flag_Preview_YD']

    MODEL3_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_Model3_Flag_Preview_YD']

    MODEL4_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_Model4_Flag_Preview_YD']

    MODEL5_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_Model5_Flag_Preview_YD']

    ALL_MODEL_FLAG_PREVIEW_YD = vARdata['vAR_Wrapper']['vAR_All_Model_Flag_Preview_YD']

    MODEL1_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_Model1_Flag_Run_YD']

    MODEL2_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_Model2_Flag_Run_YD']

    MODEL3_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_Model3_Flag_Run_YD']

    MODEL4_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_Model4_Flag_Run_YD']

    MODEL5_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_Model5_Flag_Run_YD']

    ALL_MODEL_FLAG_RUN_YD = vARdata['vAR_Wrapper']['vAR_All_Model_Flag_Run_YD']

    #print(SESSION_ID_RUN_MODEL1_OD)

    #print(MODEL1_NAME_RUN_OUR_DATA)

    #print(MODEL1_FLAG_RUN_OD)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## User Action -  "Preview Outcome"  Without their own data

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    if SESSION_ID_PREVIEW_MODEL1_OD == SESSION_ID_PREVIEW_MODEL2_OD and MODEL1_NAME_PREVIEW_OUR_DATA == MODEL1_NAME_PREVIEW_OUR_DATA :
       
        if MODEL1_FLAG_PREVIEW_OD == MODEL1_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Unplanned_Charges_YD.json.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL2_OD == SESSION_ID_PREVIEW_MODEL3_OD and MODEL2_NAME_PREVIEW_OUR_DATA == MODEL2_NAME_PREVIEW_OUR_DATA :
       
        if MODEL2_FLAG_PREVIEW_OD == MODEL2_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Extension_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL3_OD == SESSION_ID_PREVIEW_MODEL4_OD and MODEL3_NAME_PREVIEW_OUR_DATA == MODEL3_NAME_PREVIEW_OUR_DATA :
       
        if MODEL3_FLAG_PREVIEW_OD == MODEL3_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_IBR_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL4_OD == SESSION_ID_PREVIEW_MODEL5_OD and MODEL4_NAME_PREVIEW_OUR_DATA == MODEL4_NAME_PREVIEW_OUR_DATA :
       
        if MODEL4_FLAG_PREVIEW_OD == MODEL4_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_IBR_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL5_OD == SESSION_ID_PREVIEW_MODEL4_OD and MODEL5_NAME_PREVIEW_OUR_DATA == MODEL5_NAME_PREVIEW_OUR_DATA :
       
        if MODEL5_FLAG_PREVIEW_OD == MODEL5_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Amount_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_ALL_MODEL_OD == SESSION_ID_PREVIEW_MODEL5_OD and ALL_MODEL_NAME_PREVIEW_OUR_DATA == ALL_MODEL_NAME_PREVIEW_OUR_DATA :
       
        if ALL_MODEL_FLAG_PREVIEW_OD == ALL_MODEL_FLAG_PREVIEW_OD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Amount_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## User Action -  "Preview Outcome"  With their own data

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    if SESSION_ID_PREVIEW_MODEL1_YD == SESSION_ID_PREVIEW_MODEL2_YD and MODEL1_NAME_PREVIEW_YOUR_DATA == MODEL1_NAME_PREVIEW_YOUR_DATA :
       
        if MODEL1_FLAG_PREVIEW_YD == MODEL1_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Unplanned_Charges_YD.json.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL2_YD == SESSION_ID_PREVIEW_MODEL3_YD and MODEL2_NAME_PREVIEW_YOUR_DATA == MODEL2_NAME_PREVIEW_YOUR_DATA :
       
        if MODEL2_FLAG_PREVIEW_YD == MODEL2_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Extension_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL3_YD == SESSION_ID_PREVIEW_MODEL4_YD and MODEL3_NAME_PREVIEW_YOUR_DATA == MODEL3_NAME_PREVIEW_YOUR_DATA :
       
        if MODEL3_FLAG_PREVIEW_YD == MODEL3_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_IBR_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL4_YD == SESSION_ID_PREVIEW_MODEL5_YD and MODEL4_NAME_PREVIEW_YOUR_DATA == MODEL4_NAME_PREVIEW_YOUR_DATA :
       
        if MODEL4_FLAG_PREVIEW_YD == MODEL4_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_IBR_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_MODEL5_YD == SESSION_ID_PREVIEW_MODEL4_YD and MODEL5_NAME_PREVIEW_YOUR_DATA == MODEL5_NAME_PREVIEW_YOUR_DATA :
       
        if MODEL5_FLAG_PREVIEW_YD == MODEL5_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Amount_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_PREVIEW_ALL_MODEL_YD == SESSION_ID_PREVIEW_MODEL5_YD and ALL_MODEL_NAME_PREVIEW_YOUR_DATA == ALL_MODEL_NAME_PREVIEW_YOUR_DATA :
       
        if ALL_MODEL_FLAG_PREVIEW_YD == ALL_MODEL_FLAG_PREVIEW_YD :           

           uri = "http://www.deep-sphere.com/knowledge-sharing/Content/Predicted_Lease_Amount_YD.json"
        
           uResponse = requests.get(uri)
                  
           Jresponse = uResponse.text
    
           return Jresponse

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## User Action -  "Run Model"  Without their own data

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif SESSION_ID_RUN_MODEL1_OD == SESSION_ID_RUN_MODEL2_OD and MODEL1_NAME_RUN_OUR_DATA == MODEL1_NAME_RUN_OUR_DATA :
       
        if MODEL1_FLAG_RUN_OD == MODEL1_FLAG_RUN_OD :           

# Function for Training the Model

           from Data_Provider2 import vAR_model
           from Data_Provider2 import vAR_model
           vAR_model.fit(vAR_Features_Train,vAR_Label_Train)

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
           #vAR_plt.show()

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Best Fit

           import matplotlib.pyplot as vAR_plt
           from sklearn.linear_model import LinearRegression
           vAR_fig, vAR_ax = vAR_plt.subplots()
           #vAR_ax.scatter(vAR_Label_Train_UC_BF, vAR_Labels_Pred_UC_BF, edgecolors=(0, 0, 0), s=50, c='g')
           #vAR_ax.plot([vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
           #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Under Fit

           import matplotlib.pyplot as vAR_plt
           from sklearn.linear_model import LinearRegression
           vAR_fig, vAR_ax = vAR_plt.subplots()
           #vAR_ax.scatter(vAR_Label_Train_UC_UF, vAR_Labels_Pred_UC_UF, edgecolors=(0, 0, 0), s=50, c='g')
           #vAR_ax.plot([vAR_Labels_Pred_UC_UF.min(), vAR_Labels_Pred_UC_UF.max()], [vAR_Labels_Pred_UC_BF.min(), vAR_Labels_Pred_UC_BF.max()])
           #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Over Fit

           import matplotlib.pyplot as vAR_plt
           from sklearn.linear_model import LinearRegression
           #vAR_fig, vAR_ax = vAR_plt.subplots()
           #vAR_ax.scatter(vAR_Label_Train_UC_OF, vAR_Labels_Pred_UC_OF, edgecolors=(0, 0, 0), s=50, c='g')
           #vAR_ax.plot([vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()], [vAR_Labels_Pred_UC_OF.min(), vAR_Labels_Pred_UC_OF.max()])
           #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Function for Model Hyperparameter Tuning (Before)

           import matplotlib.pyplot as vAR_plt
           vAR_model = LinearRegression()
           vAR_fig, vAR_ax = vAR_plt.subplots()
           #vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
           #vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
           #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                            

    # Function for Model Hyperparameter Tuning (After)

           import matplotlib.pyplot as vAR_plt
           vAR_model = LinearRegression(fit_intercept=False, normalize=True, copy_X=False, n_jobs=5)
           #vAR_fig, vAR_ax = vAR_plt.subplots()
           #vAR_ax.scatter(vAR_Label_Train1, vAR_Labels_Pred, edgecolors=(0, 0, 0), s=50, c='gbc')
           #vAR_ax.plot([vAR_Labels_Pred.min(), vAR_Labels_Pred.max()], [vAR_Labels_Pred.min(), vAR_Labels_Pred.max()])
           #vAR_ax.plot()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL2_OD == SESSION_ID_RUN_MODEL3_OD and MODEL2_NAME_RUN_OUR_DATA == MODEL2_NAME_RUN_OUR_DATA :
       
        if MODEL2_FLAG_RUN_OD == MODEL2_FLAG_RUN_OD:           

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL3_OD == SESSION_ID_RUN_MODEL4_OD and MODEL3_NAME_RUN_OUR_DATA == MODEL3_NAME_RUN_OUR_DATA :
       
        if MODEL3_FLAG_RUN_OD == MODEL3_FLAG_RUN_OD:           

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL4_OD == SESSION_ID_RUN_MODEL5_OD and MODEL4_NAME_RUN_OUR_DATA == MODEL4_NAME_RUN_OUR_DATA :
       
        if MODEL4_FLAG_RUN_OD == MODEL4_FLAG_RUN_OD :           

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL5_OD == SESSION_ID_RUN_MODEL1_OD and MODEL5_NAME_RUN_OUR_DATA == MODEL5_NAME_RUN_OUR_DATA :
       
        if MODEL5_FLAG_RUN_OD == MODEL5_FLAG_RUN_OD :    

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_ALL_MODEL_OD == SESSION_ID_RUN_MODEL5_OD and ALL_MODEL_NAME_RUN_OUR_DATA == ALL_MODEL_NAME_RUN_OUR_DATA :
       
        if ALL_MODEL_FLAG_RUN_OD == ALL_MODEL_FLAG_RUN_OD :    

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## User Action -  "Run Model"  With their own data

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL1_YD == SESSION_ID_RUN_MODEL2_YD and MODEL1_NAME_RUN_YOUR_DATA == MODEL1_NAME_RUN_YOUR_DATA :
       
        if MODEL1_FLAG_RUN_YD == MODEL1_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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
        
    elif SESSION_ID_RUN_MODEL2_YD == SESSION_ID_RUN_MODEL3_YD and MODEL2_NAME_RUN_YOUR_DATA == MODEL2_NAME_RUN_YOUR_DATA :
       
        if MODEL2_FLAG_RUN_YD == MODEL2_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)
           vAR_ssh = paramiko.SSHClient()
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
           #vAR_sftp = vAR_ssh.open_sftp()
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD
           #vAR_remotepath = 'Content/Predicted_Lease_Extension_YD.json'
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
           ##vAR_sftp.close()
           #vAR_ssh.close()	

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        
    elif SESSION_ID_RUN_MODEL3_YD == SESSION_ID_RUN_MODEL4_YD and MODEL3_NAME_RUN_YOUR_DATA == MODEL3_NAME_RUN_YOUR_DATA :
       
        if MODEL3_FLAG_RUN_YD == MODEL3_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)
           vAR_ssh = paramiko.SSHClient()
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
           #vAR_sftp = vAR_ssh.open_sftp()
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD
           #vAR_remotepath = 'Content/Predicted_Lease_Extension_YD.json'
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
           ##vAR_sftp.close()
           #vAR_ssh.close()	

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Extension_Terms_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL4_YD == SESSION_ID_RUN_MODEL5_YD and MODEL4_NAME_RUN_YOUR_DATA == MODEL4_NAME_RUN_YOUR_DATA :
       
        if MODEL4_FLAG_RUN_YD == MODEL4_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)
           vAR_ssh = paramiko.SSHClient()
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
           #vAR_sftp = vAR_ssh.open_sftp()
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD
           #vAR_remotepath = 'Content/Predicted_Lease_Extension_YD.json'
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
           ##vAR_sftp.close()
           #vAR_ssh.close()	

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Extension_Terms_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
       
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_IBR_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_MODEL5_YD == SESSION_ID_RUN_MODEL4_YD and MODEL5_NAME_RUN_YOUR_DATA == MODEL5_NAME_RUN_YOUR_DATA :
       
        if MODEL5_FLAG_RUN_YD == MODEL5_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)
           vAR_ssh = paramiko.SSHClient()
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
           #vAR_sftp = vAR_ssh.open_sftp()
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD
           #vAR_remotepath = 'Content/Predicted_Lease_Extension_YD.json'
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
           ##vAR_sftp.close()
           #vAR_ssh.close()	

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Extension_Terms_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
       
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_IBR_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)

           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD)

           vAR_ssh = paramiko.SSHClient()

           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")

           #vAR_sftp = vAR_ssh.open_sftp()

           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD

           #vAR_remotepath = 'Content/Predicted_Lease_Amount_YD.json'

           #vAR_sftp.put(vAR_localpath, vAR_remotepath)

           ##vAR_sftp.close()

           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    elif SESSION_ID_RUN_ALL_MODEL_YD == SESSION_ID_RUN_MODEL5_YD and ALL_MODEL_NAME_RUN_YOUR_DATA == ALL_MODEL_NAME_RUN_YOUR_DATA :
       
        if ALL_MODEL_FLAG_RUN_YD == ALL_MODEL_FLAG_RUN_YD :

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Extension_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_UC_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Unplanned_Charges_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()	
 
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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Extension_Terms_YD)
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD)
           vAR_ssh = paramiko.SSHClient()
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
           #vAR_sftp = vAR_ssh.open_sftp()
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LE_json_Data_YD
           #vAR_remotepath = 'Content/Predicted_Lease_Extension_YD.json'
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
           ##vAR_sftp.close()
           #vAR_ssh.close()	

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_IBR_YD)
        
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_ET_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_Extension_Terms_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Test_Lease_Amount_YD)
       
           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD)
        
           vAR_ssh = paramiko.SSHClient()
        
           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")
        
           #vAR_sftp = vAR_ssh.open_sftp()
        
           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_IBR_json_Data_YD
        
           #vAR_remotepath = 'Content/Predicted_IBR_YD.json'
        
           #vAR_sftp.put(vAR_localpath, vAR_remotepath)
        
           ##vAR_sftp.close()
        
           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

           vAR_data = vAR_pd.read_excel(vAR_Fetched_Path_Predicted_Lease_Amount_YD)

           vAR_data_json = vAR_data.to_json(vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD)

           vAR_ssh = paramiko.SSHClient()

           vAR_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

           #vAR_ssh.connect('ftp3.ftptoyoursite.com', username="0ztek", password="aY6fuwX%RALhkx")

           #vAR_sftp = vAR_ssh.open_sftp()

           #vAR_localpath = vAR_Fetched_Path_Preview_Outcome_LA_json_Data_YD

           #vAR_remotepath = 'Content/Predicted_Lease_Amount_YD.json'

           #vAR_sftp.put(vAR_localpath, vAR_remotepath)

           ##vAR_sftp.close()

           #vAR_ssh.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        else:
            print ("Invalid User Action")
            return "Invalid User Action"   

    else:
         print('Session ID and Model name are mandatory fields')
         return "Session ID and Model name are mandatory fields"
    
    #return "Invalid User Action"

    return "Model Run Sucessfully"
       
if __name__ == '__main__':
    #print("Model Run Sucessfully")
	    
# Run Server

    app.run(host='0.0.0.0',port=9085,use_reloader=True)