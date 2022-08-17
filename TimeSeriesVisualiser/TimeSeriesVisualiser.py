import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=True,index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    fig,ax = plt.subplots(figsize=(30,10))
    plt.plot(df.index,df['value'])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Generate year labels
    year_labels = list(range(pd.DatetimeIndex(df_bar.index).year.min(),pd.DatetimeIndex(df_bar.index).year.max()+1))
    x = np.arange(len(year_labels))

    df_bar = df_bar.value.resample('M').mean()
    # Add in the first 4 months of 2016 which are missing - assign 0 to these values
    df_bar=df_bar.reindex(pd.date_range(start='2016-01-31',end=df_bar.index.max(),freq='M'),fill_value=0)

    jan_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 1].values.tolist()
    feb_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 2].values.tolist()
    mar_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 3].values.tolist()
    apr_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 4].values.tolist()
    may_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 5].values.tolist()
    jun_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 6].values.tolist()
    jul_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 7].values.tolist()
    aug_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 8].values.tolist()
    sep_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 9].values.tolist()
    oct_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 10].values.tolist()
    nov_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 11].values.tolist()
    dec_data = df_bar.loc[pd.DatetimeIndex(df_bar.index).month == 12].values.tolist()

    # Draw bar chart
    fig,ax = plt.subplots(figsize=(20,10))

    # Position grouped bars
    width=0.025
    jan = ax.bar(x-5.5*width,jan_data,width,label="January")
    feb = ax.bar(x-4.5*width,feb_data,width,label="February")
    mar = ax.bar(x-3.5*width,mar_data,width,label="March")
    apr = ax.bar(x-2.5*width,apr_data,width,label="April")
    may = ax.bar(x-1.5*width,may_data,width,label="May")
    jun = ax.bar(x-width/2,jun_data,width,label="June")
    jul = ax.bar(x+width/2,jul_data,width,label="July")
    aug = ax.bar(x+1.5*width,aug_data,width,label="August")
    sep = ax.bar(x+2.5*width,sep_data,width,label="September")
    oct = ax.bar(x+3.5*width,oct_data,width,label="October")
    nov = ax.bar(x+4.5*width,nov_data,width,label="November")
    dec = ax.bar(x+5.5*width,dec_data,width,label="December")

    # Draw axes and axes labels
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.set_title('Average page views on FreeCodeCamp per month')
    ax.set_xticks(x, year_labels)
    ax.legend()

    ax.bar_label(jan)
    ax.bar_label(feb)
    ax.bar_label(mar)
    ax.bar_label(apr)
    ax.bar_label(may)
    ax.bar_label(jun)
    ax.bar_label(jul)
    ax.bar_label(aug)
    ax.bar_label(sep)
    ax.bar_label(oct)
    ax.bar_label(nov)
    ax.bar_label(dec)

    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(25,10))

    sns.boxplot(x=df_box['year'],y=df_box['value'],data=df_box['value'],ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")  
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    sns.boxplot(x=df_box['month'],y=df_box['value'],data=df_box['value'],ax=ax[1],order=['Jan',
                                                                                        'Feb',
                                                                                        'Mar',
                                                                                        'Apr',
                                                                                        'May',
                                                                                        'Jun',
                                                                                        'Jul',
                                                                                        'Aug',
                                                                                        'Sep',
                                                                                        'Oct',
                                                                                        'Nov',
                                                                                        'Dec'])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
