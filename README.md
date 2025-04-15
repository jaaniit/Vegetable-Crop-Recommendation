🥦 Vegetable Stock Management System


The **Vegetable Stock Management System** is a data-driven application designed to assist farmers in optimizing their crop choices and pricing strategies. By leveraging machine learning and real-time data analysis, this system supports informed decision-making to improve agricultural efficiency and market profitability.

---

📊 Dashboard Preview

🔗 **[Click here to view the Power BI Dashboard (.pbix)](https://github.com/jaaniit/Vegetable-Crop-Recommendation/blob/main/Crop%20Recommendation.pbix)**  
(*Note: Download and open with Power BI Desktop to explore the interactive dashboard.*)

🎯 Objective

This project utilizes machine learning to analyze historical agricultural data and climate trends to,

- Recommend the most suitable vegetables to cultivate during specific time periods and climatic conditions.
- Predict market prices for different vegetables post-harvest to guide profitable farming decisions.

The system aims to empower farmers and agricultural planners with actionable insights, thereby enhancing productivity and income.

🛠️ Tools & Technologies Used

| Tool/Technology       | Description                                 |
|-----------------------|---------------------------------------------|
| Python (Pandas, Scikit-learn) | Data preprocessing, ML model training |
| Power BI              | Visualization & reporting dashboard         |
| Jupyter Notebook      | Model development & exploratory analysis    |
| Microsoft Excel       | Initial data analysis & tabulation          |
| CSV/SQL               | Data storage and management                 |



🧹 Data Preparation

- **Data Acquisition**: Collected 130,000+ records of vegetable pricing and climate data from 2020 to 2025.
- **Cleaning**: Removed nulls, corrected inconsistent entries, and formatted date fields.
- **Feature Engineering**: Extracted key features like `Month`, `Temperature`, `Rainfall`, and `Region`.
- **Label Encoding**: Categorical data such as vegetable type and region were encoded for machine learning compatibility.
- **Model Input Structuring**: Separated datasets for classification and regression tasks.

🤖 Machine Learning Modules

🔍 1. Cultivation Recommendation (Classification)

**Goal**: Recommend the most suitable vegetables to cultivate in a given month based on climatic conditions.

- **Input Features**: Month, Region, Temperature, Rainfall, Humidity
- **Target**: Vegetable Commodity
- **Algorithm Used**: Random Forest Classifier
- **Performance Metric**: Accuracy, F1-Score



💰 2. Price Prediction (Regression)

**Goal**: Predict post-harvest market price of vegetables.

- **Input Features**: Month, Region, Vegetable Type, Temperature, Rainfall, Humidity
- **Target**: Price per Unit (LKR/kg)
- **Algorithm Used**: Random Forest Regressor
- **Performance Metric**: RMSE, R² Score


💡 Insights & Key Findings

### 1. **Vegetable Recommendations**
- Recommendations are highly influenced by climate conditions such as temperature and rainfall.
- Certain vegetables show consistent suitability across multiple months, while others are highly seasonal.

### 2. **Market Price Forecasting**
- Prices tend to peak for select vegetables during low-production months.
- Regional factors significantly influence price fluctuation patterns.
- Higher rainfall months often correlate with reduced vegetable prices due to higher yields.

---

## 📄 Paginated Reports (Power BI)

Included printable, detailed paginated reports to assist agricultural officers and policymakers in:

- Reviewing crop recommendations by month and region.
- Forecasting vegetable market trends by season.
- Comparing economic potential across different vegetables.

---

## ✅ Conclusion

The **Vegetable Stock Management System** offers a scalable, data-driven solution for sustainable agriculture. By combining predictive analytics and intuitive dashboards, this system equips farmers, cooperatives, and policymakers with vital tools to boost productivity and reduce financial risk in vegetable cultivation and marketing.

