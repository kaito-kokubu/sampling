from email import header
import matplotlib.pyplot as plt
import pandas as pd

def main():
    file_date = input('Enter the date of log file: ')
    file_path = "./output/log_" + file_date + ".csv"
    df = pd.read_csv(file_path, names=('Time', 'Shunt', 'Bus', 'Current'))
    df['Power'] = df['Shunt'] * df['Current']
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Power'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Power (mW)')
    plt.show()
    plt.savefig(f"./output/plot_{file_date}.png")



if __name__ == "__main__":
    main()
