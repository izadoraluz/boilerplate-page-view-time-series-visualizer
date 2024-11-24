import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar os dados e preparar o DataFrame
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Limpar os dados
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# Função para o gráfico de linhas
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# Função para o gráfico de barras
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month

    # Agrupar os dados
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Criar o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 8))
    df_grouped.plot(kind='bar', ax=ax)

    # Ajustar os rótulos e a legenda
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig

# Função para os gráficos de caixa
def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = df.index.year
    df_box['month'] = df.index.month
    df_box['month_name'] = df.index.strftime('%b')  # Formatar os meses como abreviações (Jan, Feb, ...)

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Box plot por ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Box plot por mês
    sns.boxplot(x='month_name', y='value', data=df_box, ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig

