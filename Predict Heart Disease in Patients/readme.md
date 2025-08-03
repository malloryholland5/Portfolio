[⬅️ Back to Main Page](../)

## ❤️‍🩹Predict Heart Disease in Patients
This project uses the UCI Cleveland Heart Disease dataset to predict whether a patient has heart disease, aiming to support early diagnosis using standard clinical features. After removing incomplete records and converting the diagnosis to a simple healthy/sick classification, I explored key variables like chest pain type, maximum heart rate, and the number of major vessels. I trained both Logistic Regression and Random Forest models, using GridSearch for tuning and evaluating performance with metrics such as accuracy, recall, and ROC-AUC. The Random Forest model achieved the highest accuracy at 90%, especially reducing false negatives, and identified chest pain, ST depression, and major vessel count as top predictors. Despite the dataset’s small size and older diagnostic methods, the results show that these models can be integrated into routine patient care to flag at-risk individuals and support doctors with data-backed decisions. Ethical guidelines were followed throughout, with careful attention to patient privacy and transparent reporting of all methods and limitations.

## Summary
- Data cleaned: Removed incomplete records, converted diagnosis to binary (healthy/sick).
- Models: Compared Logistic Regression and Random Forest (with GridSearch tuning).
- Performance: Random Forest achieved 90% accuracy and reduced false negatives.
- Insights: Top predictors were chest pain type, ST depression, and major vessel count.

## ⏭ Limitations & Next Steps
- Small, older dataset may not fully represent today’s patients.
- Could add more features or validate on larger, newer datasets.
