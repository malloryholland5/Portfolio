[⬅️ Back to Main Page](../)

## R&D Spending and Revenue Growth

This project explores whether companies that invest more in R&D experience higher revenue growth. I pulled SEC financial data from 2008 to 2022, focusing on revenue, net income, and R&D spending, then merged it with industry codes. After cleaning the data and calculating year-over-year growth, I tested Random Forest and Gradient Boosting models, which showed weak performance with R² values near zero. A lagged OLS regression revealed a stronger relationship—each $1M increase in R&D was linked to about $10M in revenue the following year, with R² = 0.27. I also used K-Means clustering to group companies by average R&D and growth patterns. The four clusters—high, moderate, conservative, and inefficient investors—highlighted which firms turn R&D spending into actual results.

## Cleaning
- Data processing: Cleaned and merged data, dropped incomplete rows, assigned industry labels, and calculated year-over-year sales and R&D growth.

## Modeling & Analysis:
- Random Forest and Gradient Boosting: Machine learning models on R&D and industry variables showed very weak predictive power (R² near 0).
- Lagged OLS regression: Showed each $1M increase in prior-year R&D spending was linked to about $10M in revenue the following year (R² = 0.27).
- K-Means clustering: Grouped companies into four clusters by average R&D investment and growth pattern (high, moderate, conservative, inefficient investors).
- Visualization: Included scatter plots, bar charts by industry, and cluster analysis to explore relationships and company groupings.

## Limitations & Next Steps
- Model performance: ML models did not explain much variance, suggesting that other factors may drive growth or that the relationship is complex.
- Add more variables (e.g., company size, region, market sector).
- Validate clusters with alternative methods or across different time windows.

## Data: 
- SEC filings from 2008–2022, including revenue, net income, R&D spending, and industry codes.
