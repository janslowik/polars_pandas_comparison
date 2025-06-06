# Polars vs Pandas Performance Comparison

A comprehensive benchmarking project comparing the performance and capabilities of **Polars** and **Pandas** libraries for data analysis tasks. This project demonstrates the advantages and use cases for both libraries through practical examples using Titanic dataset analysis and fraud detection scenarios.

## 📊 Project Overview

This project provides side-by-side comparisons of:
- **Data manipulation and analysis workflows**
- **Performance benchmarks** on datasets of varying sizes
- **Memory efficiency** comparisons
- **Lazy evaluation capabilities** (Polars-specific)
- **Streaming data processing** capabilities

## 🗂️ Project Structure

```
polars_pandas_comparison/
├── data/
│   └── generate_transactions.py     # Synthetic transaction data generator
├── notebooks/
│   ├── 1_titanic_analysis_pandas.ipynb    # Pandas-based Titanic analysis
│   ├── 2_titanic_analysis_polars.ipynb    # Polars-based Titanic analysis
│   ├── 3_fraud_detection_pandas.ipynb     # Pandas fraud detection workflow
│   ├── 4_fraud_detection_polars.ipynb     # Polars fraud detection workflow
│   ├── 5_fraud_detection_polars_lazy.ipynb        # Polars lazy evaluation
│   └── 6_fraud_detection_polars_lazy_stream.ipynb # Polars streaming
├── titanic.csv                           # Titanic dataset
├── pyproject.toml                       # Project dependencies
└── README.md                           # This documentation
```

## 🔧 Dependencies

The project uses Python 3.12+ with the following key dependencies:

- **polars** (>=1.30.0) - Fast DataFrame library
- **pandas** (>=2.3.0) - Traditional DataFrame library  
- **faker** (>=37.3.0) - Synthetic data generation
- **seaborn** (>=0.13.2) - Data visualization
- **pyarrow** (>=20.0.0) - Columnar data format support
- **tqdm** (>=4.67.1) - Progress bars
- **ipykernel** (>=6.29.5) - Jupyter notebook support

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd polars_pandas_comparison
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   poetry shell
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt  # If available
   ```

### Usage

1. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Run the analysis notebooks** in order:
   - Start with Titanic analysis (`1_titanic_analysis_pandas.ipynb`, `2_titanic_analysis_polars.ipynb`)
   - Proceed to fraud detection comparisons (`3_fraud_detection_pandas.ipynb`, `4_fraud_detection_polars.ipynb`)
   - Explore advanced Polars features (`5_fraud_detection_polars_lazy.ipynb`, `6_fraud_detection_polars_lazy_stream.ipynb`)

## 📈 Data Generation Script

### Transaction Data Generator

The project includes a sophisticated synthetic transaction data generator (`data/generate_transactions.py`) that creates realistic credit card transaction datasets for fraud detection analysis.

#### Features:
- **Configurable dataset size** (by number of rows or target file size in GB)
- **Realistic fraud patterns** based on country mismatch
- **Merchant reuse patterns** for realistic transaction distributions
- **Customizable fraud probability** and user base size
- **Progress tracking** for large dataset generation

#### Usage:

**Generate by number of rows:**
```bash
python data/generate_transactions.py --num_rows 1000000 --output data/transactions_1m.csv
```

**Generate by target file size:**
```bash
python data/generate_transactions.py --est_size_gb 1.0 --output data/transactions_1gb.csv
```

**Advanced configuration:**
```bash
python data/generate_transactions.py \
    --num_rows 5000000 \
    --output data/custom_transactions.csv \
    --fraud_prob 0.02 \
    --n_users 2000 \
    --n_merchants 500 \
    --merchant_reuse_ratio 0.7
```

#### Parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--num_rows` | Number of transaction rows to generate | Required* |
| `--est_size_gb` | Target file size in GB | Required* |
| `--output` | Output CSV file path | `transactions.csv` |
| `--fraud_prob` | Fraud probability (0.0-1.0) | `0.01` |
| `--n_users` | Number of unique users | `1000` |
| `--n_merchants` | Number of shared merchants | `100` |
| `--merchant_reuse_ratio` | Fraction using shared merchants | `0.8` |

*Either `--num_rows` or `--est_size_gb` is required.

#### Generated Data Schema:

| Column | Type | Description |
|--------|------|-------------|
| `user_id` | int | Unique user identifier |
| `timestamp` | string | ISO format transaction timestamp |
| `amount` | float | Transaction amount (5.0-5000.0 USD) |
| `currency` | string | Always "USD" |
| `card_number` | string | Fake credit card number |
| `merchant` | string | Merchant name |
| `country` | string | Transaction country |
| `is_fraud` | boolean | Fraud flag (true for fraudulent transactions) |

#### Fraud Detection Logic:
- **Normal transactions**: Occur in user's home country
- **Fraudulent transactions**: Occur in random foreign countries
- Configurable fraud probability affects the likelihood of fraudulent transactions

## 📊 Analysis Workflows

### 1. Titanic Dataset Analysis
- **Data exploration** and statistical summaries
- **Data cleaning** and missing value handling
- **Survival analysis** by passenger characteristics
- **Performance comparison** between Pandas and Polars approaches

### 2. Fraud Detection Analysis
- **Large-scale transaction processing**
- **Fraud pattern identification**
- **Aggregation and grouping operations**
- **Memory usage optimization**
- **Streaming processing capabilities** (Polars)

## 🏆 Key Comparisons

### Performance Metrics Evaluated:
- **Execution time** for various operations
- **Memory consumption** during processing
- **Data loading speed**
- **Aggregation performance**
- **Filtering and transformation efficiency**

### Polars Advantages:
- **Faster execution** on large datasets
- **Lower memory usage**
- **Lazy evaluation** for query optimization
- **Streaming capabilities** for datasets larger than RAM
- **Better parallelization**

### Pandas Advantages:
- **Mature ecosystem** and extensive documentation
- **Wider community support**
- **More third-party integrations**
- **Familiar API** for most data scientists

## 📋 Requirements

- **Python**: 3.12+
- **RAM**: Minimum 8GB recommended for large dataset analysis
- **Storage**: Sufficient space for generated datasets (can be 10GB+ for comprehensive testing)

## 🤝 Contributing

Feel free to contribute by:
- Adding new benchmark scenarios
- Improving the data generation script
- Adding more comprehensive performance metrics
- Extending the analysis workflows

## 📄 License

This project is for educational and benchmarking purposes. Please ensure compliance with relevant data protection regulations when using synthetic data generation techniques in production environments.

## 👤 Author

**Jan Słowik** (jas.slowik@gmail.com)

---

*This project demonstrates practical applications of modern data processing libraries and provides insights for choosing the right tool for specific data analysis tasks.*
