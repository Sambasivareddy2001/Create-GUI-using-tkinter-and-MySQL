import streamlit as st
import pandas as pd
import plotly.express as px

# Function to generate Pareto chart
def generate_pareto_chart(df, threshold):
    # Your data processing code here...
    # For demonstration purposes, let's assume the data processing logic
    # involves sorting the values and calculating cumulative percentage
    columns = df.columns.tolist()
    df_sorted = df.sort_values(by=[columns[1]], ascending=False)
    df_sorted['cumulative_percentage'] = (df_sorted[columns[1]].cumsum() / df_sorted[columns[1]].sum()) * 100
    df_pareto = df_sorted[df_sorted['cumulative_percentage'] <= threshold]

    # Create Pareto chart
    fig = px.bar(df_pareto, x=df_pareto.index, y=columns[1], labels={'index': 'Category', 'value': 'Frequency'})
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    fig.add_scatter(x=df_pareto.index, y=df_pareto['cumulative_percentage'], name='Cumulative Percentage',
                    mode='lines+markers', line=dict(color='firebrick', width=2))

    return fig

# Function to display "About" information for Pareto
def about_pareto():
    st.subheader("About Pareto Analysis (80/20 Rule)")
    st.write("The Pareto Principle, also known as the 80/20 rule, states that roughly 80% of the effects come from 20% of the causes.")
    st.write("In the context of Pareto chart, it helps to identify the most significant factors contributing to a problem.")
    st.write("To create a Pareto chart, upload your data and select the threshold for analysis.")

# Function to display chart and about information for Pareto
def show_pareto_chart(df, threshold):
    st.subheader('Pareto Chart')
    st.plotly_chart(generate_pareto_chart(df, threshold), use_container_width=True)
    st.sidebar.success("This is a Pareto chart")

# Function to display "About" information for Scatter plot
def about_scatter():
    st.subheader("About Scatter Plot")
    st.write("A scatter plot is a two-dimensional data visualization technique that shows the relationship between two variables.")
    st.write("It helps in understanding the correlation between the variables.")
    st.write("To create a scatter plot, upload your data and select the variables to plot.")

# Function to display chart and about information for Scatter plot
def show_scatter_plot(df=None):
    st.subheader('Scatter Plot')
    st.plotly_chart(generate_scatter_plot(df), use_container_width=True)
    st.sidebar.success("This is a Scatter plot")

# Function to generate Scatter plot
def generate_scatter_plot(df):
    # Your data processing and scatter plot generation code here...
    # For demonstration purposes, let's create a simple scatter plot
    fig = px.scatter(df, x='x_values', y='y_values', labels={'x_values': 'X', 'y_values': 'Y'}, title='Scatter Plot')
    return fig

# Function to display "About" information for Distribution plot
def about_distribution():
    st.subheader("About Distribution Plot")
    st.write("A distribution plot displays the distribution of a dataset.")
    st.write("It helps in visualizing the spread and central tendency of the data.")
    st.write("To create a distribution plot, upload your data and select the variable to plot.")

# Function to display chart and about information for Distribution plot
def show_distribution_plot(df=None):
    st.subheader('Distribution Plot')
    st.plotly_chart(generate_distribution_plot(df), use_container_width=True)
    st.sidebar.success("This is a Distribution plot")

# Function to generate Distribution plot
def generate_distribution_plot(df):
    # Your data processing and distribution plot generation code here...
    # For demonstration purposes, let's create a simple distribution plot
    fig = px.histogram(df, x='values', labels={'values': 'Value'}, title='Distribution Plot')
    return fig

# Function to display "About" information for Control chart
def about_control():
    st.subheader("About Control Chart")
    st.write("A control chart is a statistical tool used to monitor and maintain the stability of a process over time.")
    st.write("It helps in identifying any trends, shifts, or abnormalities in the process.")
    st.write("To create a control chart, upload your data and select the variables to monitor.")

# Function to display chart and about information for Control chart
def show_control_chart(df=None):
    st.subheader('Control Chart')
    st.plotly_chart(generate_control_chart(df), use_container_width=True)
    st.sidebar.success("This is a Control chart")

# Function to generate Control Chart
def generate_control_chart(df):
    # Your data processing and control chart generation code here...
    # For demonstration purposes, let's create a simple control chart
    fig = px.line(df, x='dates', y='values', labels={'dates': 'Date', 'values': 'Value'}, title='Control Chart')
    return fig

# Main function
def main():
    st.sidebar.title('Root Cause Analysis')

    # Show other charts with icons
    icons = {
        f'Pareto 📊📈': '📊📈',
        'Scatter ⚫': '⚫',
        'Distribution 1 📈': '📈',
        'Distribution 2 📊': '📊',
        'Control Chart 📉': '📉'
    }

    # Radio button to select option
    option = st.sidebar.radio('Select Option', [
        f'📋 About',
        f'📊 Chart'
    ])

    if 'About' in option:
        st.subheader("Please select Chart for getting info of chart")
        for chart_name, icon in icons.items():
            if st.sidebar.button(f'{icon} {chart_name}', key=f'{chart_name}'):
                #st.subheader(f'{chart_name} Options')
                if 'Pareto' in chart_name:
                    about_pareto()
                elif 'Scatter' in chart_name:
                    about_scatter()
                elif 'Distribution'in  chart_name :
                    about_distribution()
                elif 'Control Chart' in chart_name :
                    about_control()
    elif 'Chart' in option:
        st.subheader("Please select Chart for getting plot")
        selected_chart = st.sidebar.radio("Select Chart", list(icons.keys()))

        if selected_chart:
            uploaded_file = st.sidebar.file_uploader(f'Upload data for {selected_chart}', type=['csv', 'xlsx'])
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
                if 'Pareto' in selected_chart:
                    threshold = st.slider('Threshold', 0, 100, 80, 5)
                    show_pareto_chart(df, threshold)
                elif 'Scatter' in selected_chart:
                    show_scatter_plot(df)
                elif 'Distribution' in selected_chart:
                    show_distribution_plot(df)
                elif 'Control Chart' in selected_chart:
                    show_control_chart(df)

# Run the app
if __name__ == "__main__":
    main()
