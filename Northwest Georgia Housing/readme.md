[⬅️ Back to Main Page](../)

## 🏡 Northwest Georgia Housing Market

This project uses public data from Redfin to estimate how long single-family homes in Northwest Georgia will be on the market. It also identifies when sellers should consider adjusting prices. After cleaning the data by removing unnecessary columns, filling in missing price-drop values, and filtering out extreme outliers, I built a basic Linear Regression model and a tuned Random Forest model. A survival curve shows important milestones at 15, 30, and 60 days when buyer interest decreases. County-level dashboards provide clear guidance on listing prices, timing for price cuts, and marketing strategies.

## Summary
- Data cleaned: Dropped unnecessary columns, filled missing price-drop values, filtered out outliers.
- Models: Compared Linear Regression and tuned Random Forest for predicting days on market (DOM).
- Performance: Tuned Random Forest achieved MAE ≈ 15 days and R² ≈ 0.60.
- Insights: Survival curve revealed key selling milestones at 15, 30, and 60 days; dashboards provide county-level guidance on pricing and timing.

## ⏭ Limitations & Next Steps
- Could add more features (e.g., macroeconomic factors, listing quality).
- Explore advanced models or ensemble approaches.
