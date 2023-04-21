# paths
train_data_path = '/Users/raj2.gaurav/Desktop/Git/Causal_Model/05. Training Data/Pre_Processed_Causl_Data.pickle'
data_hygeine_path= f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/Data/Hygeine_Report'
data_hygeibe_report_file= data_hygeine_path + '/Model_Reports.xlsx'
model_hygeine_path="f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_name}/Data/Hygeine_Report'"
model_hygeine_report_file="f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_name}/Data/Hygeine_Report/{model_name}_Reports.xlsx'"
plot_path="f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_name}/Model_Results/Accuarcy'"
plot_soruce_path='/Users/raj2.gaurav/Desktop/Git/Causal_Model/08. SRC'
save_model_path="f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_name}/Model_Results/Model_Objects'"


### Data Hyegine Report Sheet Name
data_hygeibe_report_file_sheet1='Data Summary'
data_hygeibe_report_file_sheet2= 'Model Comparasion'


### Model Hyegine Report Sheet Name
model_hygeibe_report_file_sheet1='Model Results'
model_hygeibe_report_file_sheet2= 'Model Tuned Results'
model_hygeibe_report_file_sheet3= 'Model Hyperparameters'








# transformation
Target = 'Target_Variable'
Train_size = 0.7 # between 0.0 to 1.0
Ignore_features = ['context_environment_Mobile','entity_cell_id','entity_geohash','data_date',\
                'last_rrc_measurement_earfcn_bucketed','p95_pucch_sinr','context_environment_Indoor','qci_9_tp']
Preprocess = True
Imputation_type = 'simple'
numeric_imputation = 'mean' # can be drop, mean, median, mode, knn, int
categorical_imputation = 'mode' # can be drop, mode, str
remove_outliers = True
outliers_method = 'iforest' # can be iforest, ee, lof
outliers_threshold = 0.5
fix_imbalance = True
fix_imbalance_method = 'SMOTE'
normalize = True
normalize_method = 'minmax' # can be minmax, zscore, maxbs, robust


# model building

'''
lr  ---  Logistic Regression
knn ---  K Neighbors Classifier
nb  ---  Naive Bayes
dt	Decision Tree Classifie
svm	SVM - Linear Kernel
rbfsvm	SVM - Radial Kernel
gpc	Gaussian Process Classifier
mlp	MLP Classifier
ridge	Ridge Classifier
rf	Random Forest Classifier
qda	Quadratic Discriminant Analysis
ada	Ada Boost Classifier
gbc	Gradient Boosting Classifier
lda	Linear Discriminant Analysis
et	Extra Trees Classifier
lightgbm	Light Gradient Boosting Machine
dummy	Dummy Classifier'''

# Comapre Models
models = ['lr','dt','svm','rf','ada','gbc','lightgbm']

#Create Model
fold_n=5

#Tuned Model
fold_tuned_n=5








### Accuracy plots
plot_lst=['feature','auc','confusion_matrix']
plot_format=(".png",".jpg",".jpeg")

## Model Sve Path

model_save_path= f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{models[0]}'

# scoring data path
scoring_data_path = '/Users/raj2.gaurav/Desktop/Git/Causal_Model/06. Inference Data/Scoring_dataset.pickle'


## Model Object Path
model_obj= 'Light Gradient Boosting Machine'
model_object_path= f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_obj}/Model_Results/Model_Objects/lightgbm'

##Prediction Result
prediction_path=f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_obj}/Prediction_Results/'
prediction_path_file = f'/Users/raj2.gaurav/Desktop/Git/Causal_Model/07. Model/{model_obj}/Prediction_Results/{model_obj}_Prediction.csv'



# columns to be drop Inference
Ignore_features_inference = ['context_environment_Mobile','entity_cell_id','entity_geohash','data_date',
                'last_rrc_measurement_earfcn_bucketed','p95_pucch_sinr','context_environment_Indoor','qci_9_tp','Target_Variable']