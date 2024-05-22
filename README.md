# Data Visualization with Pandas and Seaborn

This Python script allows you to create various types of plots (line, bar, or histogram) for data from a CSV file using the Pandas and Seaborn libraries. You can specify the columns to be plotted and the type of plot you want to create.

## Prerequisites

Before running the script, you need to install the following Python libraries:

- `pandas`: You can install it using `pip install pandas`.
- `matplotlib`: You can install it using `pip install matplotlib`.
- `seaborn`: You can install it using `pip install seaborn`.

## Usage

1. Open the script in a text editor.
2. Replace `/path/to/your/file.csv` with the actual path to your CSV file.
3. Optionally, specify the columns you want to plot by modifying the `columns` list.
4. Optionally, change the `plot_type` variable to `'line'`, `'bar'`, or `'hist'` depending on the type of plot you want to create.
5. Save the script and run it using a Python interpreter.

The script will create the specified plot(s) and display them in a new window.

## How it Works

The script defines a function called `create_graph()` that takes the following arguments:

- `csv_file`: The path to the CSV file containing the data.
- `columns` (optional): A list of column names to be plotted. If not provided, all columns except the first one will be used.
- `plot_type` (optional): The type of plot to create. Supported values are `'line'` (default), `'bar'`, and `'hist'`.

Here's what the `create_graph()` function does:

1. It checks if the specified CSV file exists. If not, it prints an error message and returns.
2. It attempts to read the data from the CSV file using `pd.read_csv()`. If an error occurs during reading, it prints an error message and returns.
3. If no columns are specified, it uses all columns except the first one (assuming the first column is an index or identifier).
4. It sets the style of the Seaborn plots to `'darkgrid'` using `sns.set(style="darkgrid")`.
5. For each column specified (or all columns if none are specified):
   - If the column doesn't exist in the data, it prints a warning message and continues to the next column.
   - Depending on the `plot_type`, it creates a line plot (`sns.lineplot()`), bar plot (`sns.barplot()`), or histogram (`sns.histplot()`) for the column's data.
6. It adds a legend to the plot using `plt.legend()`.
7. It displays the plot(s) using `plt.show()`.

In the main part of the script, it calls the `create_graph()` function with the specified `csv_file`, `columns`, and `plot_type`.

## Dependencies

- `pandas`: A Python library for data manipulation and analysis.
- `matplotlib`: A plotting library for Python, which is used by Seaborn for creating visualizations.
- `seaborn`: A data visualization library based on matplotlib, providing a high-level interface for creating attractive and informative statistical graphics.

## Notes

- Make sure to replace `/path/to/your/file.csv` with the actual path to your CSV file.
- The script assumes that the CSV file has a header row with column names.
- If you specify columns that don't exist in the data, the script will print a warning message and skip those columns.
- The script uses the `'darkgrid'` style for the plots, but you can change it to any other style supported by Seaborn by modifying the `sns.set(style="darkgrid")` line.
- If you want to customize the plots further (e.g., change colors, labels, or axes), you can modify the respective Seaborn function calls (`sns.lineplot()`, `sns.barplot()`, or `sns.histplot()`).
