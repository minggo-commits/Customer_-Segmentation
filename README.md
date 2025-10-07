# 📊 Customer Segmentation Platform

A web-based customer segmentation application built with Streamlit that uses K-Means clustering to help businesses analyze and group their customers based on various features.

## 🌟 Overview

This platform enables users to perform customer segmentation analysis through an intuitive web interface. Upload your customer data, select relevant features, and visualize how your customers naturally group together using machine learning clustering algorithms.

## ✨ Features

- **File Upload Support**: Upload customer data in CSV, XLS, or XLSX formats
- **Interactive Feature Selection**: Choose which customer attributes to use for clustering
- **Flexible Clustering**: Adjust the number of clusters (k) from 2 to 10
- **Data Preprocessing**: Automatic data cleaning, normalization, and standardization
- **Visual Analysis**: 2D PCA visualization of customer clusters
- **Cluster Summaries**: Detailed statistics and member counts for each segment
- **Real-time Results**: Instant segmentation with interactive visualizations

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/minggo-commits/Customer_-Segmentation.git
cd Customer_-Segmentation
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

1. **Upload Data**: Click the upload button and select your customer data file (CSV/XLS/XLSX)
2. **Select Features**: Choose which columns/features you want to use for segmentation
3. **Set Cluster Count**: Use the slider to select the desired number of customer segments (k)
4. **Run Segmentation**: Click the "🚀 Lakukan Segmentasi" button to perform clustering
5. **Analyze Results**: 
   - View your data with assigned cluster labels
   - Examine the 2D visualization of clusters
   - Review cluster summaries with average values and member counts

## 📁 Project Structure

```
Customer_-Segmentation/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── src/
│   ├── preprocessing.py        # Data preprocessing and scaling
│   ├── clustering.py           # K-Means clustering implementation
│   ├── visualization.py        # Cluster visualization functions
│   └── utils.py               # Utility functions for file loading
└── README.md                  # Project documentation
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[scikit-learn](https://scikit-learn.org/)**: Machine learning (K-Means, PCA, StandardScaler)
- **[Matplotlib](https://matplotlib.org/)**: Data visualization
- **[openpyxl](https://openpyxl.readthedocs.io/)**: Excel file support

## 🔍 Algorithm Details

### K-Means Clustering
The application uses K-Means clustering algorithm to segment customers into distinct groups based on their features. The algorithm:
- Groups customers with similar characteristics together
- Minimizes variance within each cluster
- Uses PCA (Principal Component Analysis) for 2D visualization

### Data Preprocessing
- Handles missing values by removing rows with NaN
- Converts string numbers to numeric format
- Standardizes features using StandardScaler for better clustering performance

## 📊 Example Use Cases

- **Retail**: Segment customers by purchase behavior, spending patterns, and frequency
- **E-commerce**: Group users by browsing habits, cart values, and engagement metrics
- **Marketing**: Identify customer personas for targeted campaigns
- **Banking**: Classify customers by transaction patterns and account activity

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available for educational and commercial use.

## 👤 Author

[minggo-commits](https://github.com/minggo-commits)

## 🙏 Acknowledgments

- Built with Streamlit for rapid web app development
- Powered by scikit-learn for machine learning capabilities
- Designed for ease of use and practical business applications
