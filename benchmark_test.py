import pandas as pd
import polars as pl
import time
import psutil
import os

def measure_memory():
    """Zmierz aktualne zużycie pamięci"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # MB

def benchmark_csv_loading():
    """Benchmark wczytywania CSV"""
    print("=== BENCHMARK: Wczytywanie CSV ===")
    
    # Pandas
    start_time = time.time()
    start_memory = measure_memory()
    df_pandas = pd.read_csv("data/titanic.csv")
    pandas_time = time.time() - start_time
    pandas_memory = measure_memory() - start_memory
    
    # Polars
    start_time = time.time()
    start_memory = measure_memory()
    df_polars = pl.read_csv("data/titanic.csv")
    polars_time = time.time() - start_time
    polars_memory = measure_memory() - start_memory
    
    print(f"Pandas: {pandas_time:.4f}s, {pandas_memory:.2f}MB")
    print(f"Polars: {polars_time:.4f}s, {polars_memory:.2f}MB")
    print(f"Przewaga Polars: {pandas_time/polars_time:.1f}x szybszy")
    print()
    
    return df_pandas, df_polars

def benchmark_filtering(df_pandas, df_polars):
    """Benchmark filtrowania"""
    print("=== BENCHMARK: Filtrowanie ===")
    
    # Pandas
    start_time = time.time()
    result_pandas = df_pandas[
        (df_pandas['Sex'] == 'female') & 
        (df_pandas['Pclass'] == 1) & 
        (df_pandas['Survived'] == 1)
    ]
    pandas_time = time.time() - start_time
    
    # Polars
    start_time = time.time()
    result_polars = df_polars.filter(
        (pl.col('Sex') == 'female') & 
        (pl.col('Pclass') == 1) & 
        (pl.col('Survived') == 1)
    )
    polars_time = time.time() - start_time
    
    print(f"Pandas: {pandas_time:.6f}s")
    print(f"Polars: {polars_time:.6f}s")
    if polars_time > 0:
        print(f"Przewaga Polars: {pandas_time/polars_time:.1f}x szybszy")
    print()

def benchmark_groupby(df_pandas, df_polars):
    """Benchmark grupowania"""
    print("=== BENCHMARK: Group By ===")
    
    # Pandas
    start_time = time.time()
    result_pandas = df_pandas.groupby('Pclass')['Age'].mean()
    pandas_time = time.time() - start_time
    
    # Polars
    start_time = time.time()
    result_polars = df_polars.group_by('Pclass').agg(pl.col('Age').mean())
    polars_time = time.time() - start_time
    
    print(f"Pandas: {pandas_time:.6f}s")
    print(f"Polars: {polars_time:.6f}s")
    if polars_time > 0:
        print(f"Przewaga Polars: {pandas_time/polars_time:.1f}x szybszy")
    print()

def benchmark_joins(df_pandas, df_polars):
    """Benchmark łączenia tabel"""
    print("=== BENCHMARK: Joins ===")
    
    # Przygotuj dane do joina
    ports_pandas = pd.DataFrame({
        'Embarked': ['C', 'Q', 'S'],
        'Port_Name': ['Cherbourg', 'Queenstown', 'Southampton']
    })
    
    ports_polars = pl.DataFrame({
        'Embarked': ['C', 'Q', 'S'],
        'Port_Name': ['Cherbourg', 'Queenstown', 'Southampton']
    })
    
    # Pandas
    start_time = time.time()
    result_pandas = df_pandas.merge(ports_pandas, on='Embarked', how='left')
    pandas_time = time.time() - start_time
    
    # Polars
    start_time = time.time()
    result_polars = df_polars.join(ports_polars, on='Embarked', how='left')
    polars_time = time.time() - start_time
    
    print(f"Pandas: {pandas_time:.6f}s")
    print(f"Polars: {polars_time:.6f}s")
    if polars_time > 0:
        print(f"Przewaga Polars: {pandas_time/polars_time:.1f}x szybszy")
    print()

if __name__ == "__main__":
    print("🚀 BENCHMARK: Pandas vs Polars")
    print("=" * 40)
    
    # Wczytaj dane
    df_pandas, df_polars = benchmark_csv_loading()
    
    # Testy wydajności
    benchmark_filtering(df_pandas, df_polars)
    benchmark_groupby(df_pandas, df_polars)
    benchmark_joins(df_pandas, df_polars)
    
    print("✅ Benchmark zakończony!") 