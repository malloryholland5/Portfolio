## Predict Union Membership in 2028

This project forecasts union-membership rates across U.S. counties so companies can spot high-potential markets for new locations. Merging public labor-statistics tables with census demographics and cleaning the rows with missing values. I benchmarked an ARIMA model against a tuned Prophet model. The mean-absolute-percentage error to roughly 6 percent. Interactive county-level maps and demographic overlays translate the forecasts into clear, data-backed guidance on where to expand and how to budget for future labor negotiations.

## Summary
- Data cleaned: Merged labor stats with census demographics, dropped missing rows.
- Models: Compared ARIMA and tuned Prophet for time series forecasting.
- Performance: Best model achieved ~6% mean absolute percentage error (MAPE).
- Visualization: Built interactive county-level maps to show high-potential areas.
## Limitations & Next Steps
- Could add more features (e.g., economic trends, industry codes).
- Try additional forecasting models or ensemble approaches.
