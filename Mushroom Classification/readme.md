[⬅️ Back to Main Page](../)

## Mushroom Classification

This project identifies poisonous mushrooms using the UCI Mushroom dataset. After converting categorical traits into one-hot columns and filling in missing values, I trained a Decision Tree that achieved almost perfect accuracy. A chi-square feature analysis showed that just five attributes related to odor and gills hold almost all predictive power, simplifying deployment while ensuring safety.

## Summary 
- Data cleaning: Converted all categorical features to dummy variables and filled in missing values using the most common value for each column.
- Model: Trained a Decision Tree classifier to distinguish between edible and poisonous mushrooms.
- Performance: Achieved nearly perfect accuracy (100%) on the test set.

## Limitations & Next Steps
- Model simplicity: Decision Trees are easy to interpret but can overfit; consider ensemble methods for better generalization.
- Test on different or larger mushroom datasets for robustness.
