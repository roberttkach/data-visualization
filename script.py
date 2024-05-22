import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_graph(csv_file, columns=None, plot_type='line'):
    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"File {csv_file} does not exist.")
        return

    # Reading data from the CSV file
    try:
        data = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Failed to read file {csv_file}. Error: {e}")
        return

    # If no columns specified, use all columns
    if not columns:
        columns = data.columns[1:]

    # Setting the style of seaborn
    sns.set(style="darkgrid")

    # Creating the plot
    for column in columns:
        if column not in data.columns:
            print(f"Column {column} does not exist in data.")
            continue

        if plot_type == 'line':
            sns.lineplot(data=data[column], label=column)
        elif plot_type == 'bar':
            sns.barplot(data=data[column], label=column)
        elif plot_type == 'hist':
            sns.histplot(data=data[column], label=column)
        else:
            print(f"Plot type {plot_type} not supported.")

    plt.legend()
    plt.show()

# Replace with the path to your CSV file
csv_file = "/path/to/your/file.csv"

# Specify the columns and plot type
columns = ['Column1', 'Column2']
plot_type = 'line'

create_graph(csv_file, columns, plot_type)
