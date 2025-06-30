# Northwest Georgia Housing Market 
This project uses public data from Redfin to estimate how long single-family homes in Northwest Georgia will be on the market. It also identifies when sellers should consider adjusting prices. After cleaning the data by removing unnecessary columns, filling in missing price-drop values, and filtering out extreme outliers, I built a basic Linear Regression model and a tuned Random Forest model. A survival curve shows important milestones at 15, 30, and 60 days when buyer interest decreases. County-level dashboards provide clear guidance on listing prices, timing for price cuts, and marketing strategies. 

# Best Model for Predicting Loan Status 
This project aims to predict if a loan application will be approved. I cleaned the data, converted text fields into numeric features, and tested three models. Hyperparameter tuning revealed that a Logistic Regression model achieved the best accuracy at about 80 percent, outperforming the other models while remaining easy to explain. The outcome is a practical tool that helps lenders make faster and fairer decisions. 

# Handwritten Digit Classification 
This project recognizes handwritten digits using the MNIST dataset. After scaling the images and converting labels, I trained a compact two-block Convolutional Neural Network (CNN) with dropout and max-pooling. The model achieved 99 percent accuracy in under ten epochs. A confusion matrix showed that the digits 2 and 4 are still challenging, indicating areas for future improvement. The result is a lightweight, high-accuracy classifier that can be useful for any analytics team. 

# Fuel-Efficiency Prediction 
This project predicts a car's fuel efficiency based on engine specs and weight. After correcting missing horsepower values and encoding the origin, I compared a basic Linear Regression model with a tuned Decision Tree. The Linear Regression model achieved an R² of 0.82, while the Decision Tree improved accuracy to 0.86 but showed some overfitting. This project provides a clear, data-backed tool to help buyers and automakers understand real-world fuel costs. 

# ALS Patient Clustering 
This project groups ALS patients into clinical subgroups. After filtering out unrelated lab features and scaling the data, I tested various cluster counts, finding that a two-cluster K-Means model was the best fit. The model was confirmed through silhouette analysis and visualized using a two-component PCA plot. Despite achieving a silhouette score of only 0.35, I identified two distinct patient profiles that can help guide clinicians in providing better care plans. 

# Union Membership Trends & Forecast 
This project forecasts union-membership rates across U.S. counties so companies can spot high-potential markets for new locations. Merging public labor-statistics tables with census demographics and cleaning the rows with missing values. I benchmarked an ARIMA model against a tuned Prophet model. The mean-absolute-percentage error to roughly 6 percent. Interactive county-level maps and demographic overlays translate the forecasts into clear, data-backed guidance on where to expand and how to budget for future labor negotiations.  

# Mushroom Classification 
This project identifies poisonous mushrooms using the UCI Mushroom dataset. After converting categorical traits into one-hot columns and filling in missing values, I trained a Decision Tree that achieved almost perfect accuracy. A chi-square feature analysis showed that just five attributes related to odor and gills hold almost all predictive power, simplifying deployment while ensuring safety. 

# API Weather Lookup 
This project creates a simple command-line tool that provides instant weather reports based on city names or ZIP codes. It has clear prompts and strong error handling to make it user-friendly for non-technical users. The underlying code showcases practical skills in API usage, JSON handling, and reusable function design, which are valuable in data engineering tasks. 
Will use another project from this semester. 
Will use another project from this semester. 
