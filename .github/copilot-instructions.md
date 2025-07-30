# Copilot Instructions for Indian Railways Predictive Maintenance

<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

## Project Overview
This is a machine learning project focused on predictive maintenance for Indian Railways. The project implements:

- Time series analysis of operational data
- LSTM Autoencoder for anomaly detection
- Survival analysis for Remaining Useful Life (RUL) prediction
- Interactive dashboard for real-time monitoring
- Cost-benefit analysis for maintenance optimization

## Code Style and Standards
- Use Python 3.8+ features and type hints where appropriate
- Follow PEP 8 coding standards
- Use meaningful variable names that reflect railway domain terminology
- Add comprehensive docstrings for all functions and classes
- Include proper error handling for data loading and model operations

## Key Libraries and Frameworks
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn, tensorflow/keras
- **Visualization**: matplotlib, seaborn, plotly
- **Time Series**: LSTM models for sequential data analysis
- **Dashboard**: plotly for interactive visualizations

## Domain-Specific Context
- Focus on railway maintenance terminology (RUL, MTBF, failure modes)
- Consider Indian Railways operational constraints and requirements
- Implement cost-effective maintenance strategies
- Ensure scalability for large railway networks

## File Organization
- `notebooks/`: Jupyter notebooks for analysis and experimentation
- `src/`: Production-ready Python modules
- `data/`: Raw and processed datasets
- `models/`: Trained model artifacts
- `docs/`: Documentation and reports
