# Quick Start Guide

## Getting Started with Predictive Maintenance for Indian Railways

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/Yeshwanth1008/Predictive-Maintenance-for-Indian-Railways.git
cd Predictive-Maintenance-for-Indian-Railways

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Preparation

1. Place your railway datasets in the `data/raw/` folder:
   - `schedules.json`: Train scheduling data
   - `stations.json`: Station network data
   - `trains.json`: Train fleet information

2. Update file paths in the notebook to match your data location

### 3. Running the Analysis

```bash
# Launch Jupyter Notebook
jupyter notebook notebooks/Predictive-Maintenance-for-Indian-Railways.ipynb
```

### 4. Key Components

- **Data Loading**: Automatically loads and preprocesses railway data
- **Anomaly Detection**: LSTM Autoencoder for identifying unusual patterns
- **RUL Prediction**: Estimates remaining useful life of components
- **Visualization**: Interactive dashboards for monitoring

### 5. Customization

- Modify hyperparameters in the notebook cells
- Add new sensor data sources
- Customize visualization themes
- Adjust anomaly detection thresholds

### 6. Deployment

- Export trained models from `models/` folder
- Use the interactive dashboard for real-time monitoring
- Integrate with existing railway management systems

## Troubleshooting

- **File Path Issues**: Update data file paths in the notebook
- **Memory Errors**: Reduce batch size or use data sampling
- **GPU Issues**: Switch to CPU by commenting out GPU configurations

## Next Steps

1. Explore the Jupyter notebook
2. Run all cells to see the complete analysis
3. Modify parameters to fit your specific use case
4. Deploy the system for your railway network
