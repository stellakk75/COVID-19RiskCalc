# Import dependencies
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from datetime import date

# from pgsql import savePredictedResults

# Main Function : Predict diabetes (Logistic Regression)
def predictRisk(age, hypertension, diabetes, cvd, copd, cancer, kidney_disease, fever, breath, cough, tachypnea, fatigue, diarrhea) -> []: 

    ### Initialize:
    # Intialize error = No
    error_flag = False
    predicted_result = None

    try:


        
        # Predict result:


        # Convert input to dataframe
        input = {"age":[age], "hypertension":[hypertension], "diabetes":[diabetes], \
                 "cvd":[cvd], "copd":[copd], "cancer":[cancer], \
                 "kidney disease":[kidney_disease], "fever":[fever], "shortness of breath":[breath], \
                "cough":[cough], "tachypnea":[tachypnea], "fatigue":[fatigue], "diarrhea":[diarrhea]}
        input_df = pd.DataFrame(input)

        # Load the model from disk
        filename = "FinalProject/Team4Final/LogisticRegression/predictorRisk.sav"
        risk_model = pickle.load(open(filename, 'rb'))

        # Predict the result from model 
        predicted_result = risk_model.predict(input_df)[0]
        print(("Predicted result : {}").format(predicted_result))



        # Save predicted result to Database
        
        # Curret date
        current_date = date.today()
        other_input = {"create_date":[current_date], "user_country":[user_country], "user_state":[user_state], "gender":[gender]}
        other_input_df = pd.DataFrame(other_input)

        # result
        result = {"outcome":[predicted_result]}
        result_df = pd.DataFrame(result)
        
        # Concatenate the 3 dataframes to match table 
        risk_results_df = pd.concat([input_df, result_df, other_input_df], axis=1)
        print(risk_results_df.head())



    except Exception as e:
        print(('Exception occured : {}').format(e))
        error_flag = True

    
    # Return
    return error_flag, predicted_result