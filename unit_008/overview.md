## Unit 8: Introduction to Data Science in Python

### 1. Numerical Computing with NumPy
- **Introduction to NumPy**: Installing (`pip install numpy`), importing, and creating arrays (1D, 2D).
  - *Sample Code*:  
    ```python
    import numpy as np
    
    # Create arrays
    arr1d = np.array([1, 2, 3, 4])
    arr2d = np.array([[1, 2], [3, 4]])
    print(arr1d)  # Output: [1 2 3 4]
    print(arr2d)  # Output: [[1 2] [3 4]]
    ```
  - *Exercise*: 
    1. Install NumPy and create a 1D array from a list of 5 numbers; print its shape using `arr.shape`.
    2. Create a 2D array (3x2) with zeros using `np.zeros()` and print it.

- **Important NumPy Objects, Methods, and Operations**: Arrays, indexing/slicing, broadcasting, basic math/stats (e.g., `sum`, `mean`, `std`).
  - *Sample Code*:  
    ```python
    import numpy as np
    
    # Indexing and slicing
    arr = np.array([10, 20, 30, 40])
    print(arr[1:3])  # Output: [20 30]
    
    # Broadcasting
    arr2d = np.array([[1, 2], [3, 4]])
    print(arr2d + 10)  # Output: [[11 12] [13 14]]
    
    # Math and stats
    data = np.array([1, 2, 3, 4, 5])
    print(np.sum(data))  # Output: 15
    print(np.mean(data))  # Output: 3.0
    print(np.std(data))  # Output: 1.4142135623730951
    ```
  - *Exercise*: 
    1. Create an array of 10 random integers using `np.random.randint(1, 100, 10)`; compute its mean and standard deviation.
    2. Use broadcasting to multiply a 2D array by 2 and slice the first column.

### 2. Data Manipulation with Polars
- **Introduction to Polars and Comparison to Pandas**: Installing (`pip install polars`), creating DataFrames, and contrasting with Pandas.
  - *Sample Code*:  
    ```python
    import polars as pl
    import pandas as pd
    
    # Polars DataFrame
    df_polars = pl.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    })
    print(df_polars)  # Output: Polars DataFrame
    
    # Pandas equivalent
    df_pandas = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    })
    print(df_pandas)  # Output: Pandas DataFrame
    ```
  - *Exercise*: 
    1. Install Polars and create a DataFrame with 4 rows of student data (name, grade); print it.
    2. Create a Pandas DataFrame with the same data and compare the output format.

- **Basic Polars Operations**: Filtering, grouping, aggregation, and joining.
  - *Sample Code*:  
    ```python
    import polars as pl
    
    df = pl.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "salary": [50000, 60000, 70000]
    })
    
    # Filtering
    older = df.filter(pl.col("age") > 28)
    print(older)  # Output: Bob, Charlie rows
    
    # Grouping and aggregation
    avg_salary = df.group_by("age").agg(pl.col("salary").mean())
    print(avg_salary)
    
    # Join
    df2 = pl.DataFrame({"age": [25, 30], "dept": ["HR", "IT"]})
    joined = df.join(df2, on="age", how="left")
    print(joined)
    ```
  - *Exercise*: 
    1. Filter a Polars DataFrame to show rows where grade > 80; print the result.
    2. Group a Polars DataFrame by a category (e.g., department) and compute the average of a numerical column.

### 3. Data Visualization with Matplotlib
- **Creating Simple Plots**: Line plots, scatter plots, and customization (labels, titles).
  - *Sample Code*:  
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 2, 3])
    
    plt.plot(x, y, marker='o')
    plt.title("Simple Line Plot")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.show()
    ```
  - *Exercise*: 
    1. Install Matplotlib (`pip install matplotlib`) and create a line plot for y = x^3 (x from 0 to 5).
    2. Create a scatter plot with 10 points and add a title, labels, and grid.

- **Random Plots**: Generating random data with NumPy and plotting it.
  - *Sample Code*:  
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = np.random.normal(0, 1, 100)
    
    plt.scatter(x, y, color='blue')
    plt.title("Random Scatter Plot")
    plt.xlabel("X")
    plt.ylabel("Random Y")
    plt.show()
    ```
  - *Exercise*: 
    1. Generate 50 random points using `np.random.rand(50)` and create a scatter plot.
    2. Plot a line of 100 random walk steps using `np.random.normal().cumsum()`.

### 4. Enhanced Visualization with Seaborn
- **Introduction to Seaborn**: Installing (`pip install seaborn`), creating statistical plots (e.g., pair plots, heatmaps).
  - *Sample Code*:  
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # Load sample dataset
    tips = sns.load_dataset("tips")
    
    # Scatter plot
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
    plt.title("Tips vs Total Bill")
    plt.show()
    
    # Heatmap
    import numpy as np
    corr = np.corrcoef(np.random.rand(3, 3))
    sns.heatmap(corr, annot=True)
    plt.show()
    ```
  - *Exercise*: 
    1. Install Seaborn and create a pair plot for the "iris" dataset (`sns.load_dataset("iris")`).
    2. Generate a 4x4 random correlation matrix with NumPy and plot a heatmap with annotations.

### 5. Histograms and Integration
- **Histograms with Matplotlib and NumPy**: Creating histograms from data distributions.
  - *Sample Code*:  
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    data = np.random.normal(100, 15, 1000)
    
    plt.hist(data, bins=30, edgecolor='black')
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
    ```
  - *Exercise*: 
    1. Generate 500 uniform random numbers with `np.random.uniform(0, 100, 500)` and create a histogram with 20 bins.
    2. Create a histogram from a Polars DataFrame column containing random data.

- **Integrating Libraries**: Combining NumPy, Polars, and Matplotlib for end-to-end workflows.
  - *Sample Code*:  
    ```python
    import polars as pl
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Polars DataFrame with NumPy random data
    np.random.seed(42)
    df = pl.DataFrame({
        "x": np.random.rand(50),
        "y": np.random.rand(50)
    })
    
    # Scatter plot
    plt.scatter(df["x"], df["y"], color='red')
    plt.title("Scatter from Polars + NumPy")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    ```
  - *Exercise*: 
    1. Create a Polars DataFrame from NumPy random normals; plot a histogram of one column.
    2. Filter a Polars DataFrame (e.g., values > 0.5) and create a scatter plot of the filtered data.

### 6. Polars vs. Pandas Comparison
- **Comparing Polars and Pandas**: Key differences in performance, syntax, and use cases for Unit 8.
  - *Sample Code*:  
    ```python
    import polars as pl
    import pandas as pd
    import numpy as np
    import time
    
    # Generate sample data
    data = {"value": np.random.rand(1000)}
    
    # Polars performance
    start = time.time()
    df_polars = pl.DataFrame(data)
    polars_result = df_polars.filter(pl.col("value") > 0.5).mean()
    polars_time = time.time() - start
    print(f"Polars time: {polars_time:.4f} seconds")
    
    # Pandas equivalent
    start = time.time()
    df_pandas = pd.DataFrame(data)
    pandas_result = df_pandas[df_pandas["value"] > 0.5].mean()
    pandas_time = time.time() - start
    print(f"Pandas time: {pandas_time:.4f} seconds")
    ```
  - *Exercise*: 
    1. Create a Polars and Pandas DataFrame with identical data; compare their filtering output.
    2. Write a program that measures the time to group and aggregate a Polars vs. Pandas DataFrame.
   
&copy; 2025 LogosTeach - All Rights Reserved
