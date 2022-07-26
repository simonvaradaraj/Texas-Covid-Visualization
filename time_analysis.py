# Visualizing the Growth in Covid 19 Cases in Texas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Data gathered from https://dshs.texas.gov/coronavirus/AdditionalData.aspx 
# TEXAS DEPARTMENT OF STATE HEALTH SERVICES - Last Updated July 23rd 2022

# vaccsheets is a dictionary that holds a dataframe interpretation of the excel sheets on the vaccine data spreadsheet
vaccsheets = pd.read_excel("COV19-vaccine-data-by-county.xlsx", sheet_name=None)
covidsheets = pd.read_excel("texasnewcases.xlsx", sheet_name=None)

fig, axes = plt.subplots(nrows=1, ncols=3)

# FORMATTING THE VACCINATION SHEET

# dropping useless info on the vaccination spreadsheet
del vaccsheets['By Vaccination Date']['People with at least One Booster Dose']

# formatting the dates in the excel sheet to pandas datetime values
vaccsheets['By Vaccination Date']['Vaccination Date'] = pd.to_datetime(vaccsheets['By Vaccination Date']['Vaccination Date'], format='%Y-%m-%d %H:%M:%S.%f')
vaccsheets['By Vaccination Date']['People Vaccinated with at least One Dose'] /= 1000
vaccsheets['By Vaccination Date']['People Fully Vaccinated '] /= 1000


# FORMATTING THE COVID CASE SHEET

# creating a list of all the covid cases in 2020-2022
cases2020 = np.array(covidsheets['New Cases by County 2020'].iloc[257][-19:-2])
cases2021 = np.array(covidsheets['New Cases by County 2021'].iloc[257][1:])
cases2022 = np.array(covidsheets['New Cases by County 2022'].iloc[257][1:])

allcases = np.concatenate((cases2020, cases2021, cases2022), axis = None) / 1000


# One can use the same data for time, since graphs are both over the same timeframe


# creating a dataframe of the dates and cases
covidframe = pd.DataFrame({'': vaccsheets['By Vaccination Date']['Vaccination Date'], 'Cases':allcases})
covidframe.plot(x = '', y = ["Cases"], ax= axes[0], color = "#FFAAA6")
axes[0].set_ylabel("Cases in thousands")
# gets rid of annoying label
axes[0].set_xlabel("")
axes[0].set_title("COVID-19 Cases in Texas")

# plotting partially vaccinated doses over time
vaccsheets['By Vaccination Date'].plot(x = "Vaccination Date", y = ["People Vaccinated with at least One Dose"], ax=axes[1])
axes[1].set_ylabel("Single Vaccinated people in thousands")
axes[1].set_xlabel("")
axes[1].set_title("COVID-19 Single Vaccinations in Texas")

# plotting Fully vaccinated people over time
vaccsheets['By Vaccination Date'].plot(x = "Vaccination Date", y = ["People Fully Vaccinated "], ax=axes[2], color = '#009b77')
axes[2].set_ylabel("Fully Vaccinated people in thousands")
axes[2].set_title("COVID-19 Full Vaccinations in Texas")



# definitely can make this a lot cleaner
axes[0].set_xlim([datetime.date(2020, 12, 14), datetime.date(2022, 7, 22)])
axes[1].set_xlim([datetime.date(2020, 12, 14), datetime.date(2022, 7, 22)])
axes[2].set_xlim([datetime.date(2020, 12, 14), datetime.date(2022, 7, 22)])

plt.show()
