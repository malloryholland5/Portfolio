[⬅️ Back to Main Page](../)

## 🤟🏼 ALS Patient Clustering

This project groups ALS patients into clinical subgroups. After filtering out unrelated lab features and scaling the data, I tested various cluster counts, finding that a two-cluster K-Means model was the best fit. The model was confirmed through silhouette analysis and visualized using a two-component PCA plot. Despite achieving a silhouette score of only 0.35, I identified two distinct patient profiles that can help guide clinicians in providing better care plans.

## Summary
- Data cleaned: Removed unrelated features, filtered columns by correlation, scaled values.
- Model: K-Means clustering; two clusters chosen using silhouette analysis (score ≈ 0.35).
- Visualization: PCA scatterplot revealed two patient subgroups.
- Insights: Two distinct profiles may support better clinical planning.

## ⏭ Limitations & Next Steps
- Low silhouette score suggests weak cluster separation.
- Could try different clustering algorithms or feature engineering.
