import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

# Read in the data
from pikl_prog import astral_df, gmm_df , lal_df, amrut_df, alkyl_df,ap_df,divis_df,titan_df, tcs_df, tata_elxsi_df

df_t = gmm_df.copy()

# Initialize the app
app = dash.Dash(__name__,)
# app = dash.Dash(__name__, external_stylesheets=['style.css'])

server = app.server

dropdown_options2 = [{'label': 'Astral', 'value': 'astral_df'},
                    {'label': 'GMM', 'value': 'gmm_df'},
                    {'label': 'Dr. Lal Pathlabs', 'value': 'lal_df'},
                    {'label': 'Amrutanjan', 'value': 'amrut_df'},
                     {'label': 'Alkyl Amines', 'value': 'alkyl_df'},
                     {'label': 'Asian Paints', 'value': 'ap_df'},
                     {'label': 'Divis Labs', 'value': 'divis_df'},
                     {'label': 'TCS', 'value': 'tcs_df'},
                     {'label': 'TATA Elxsi', 'value': 'tata_elxsi_df'},
                     {'label': 'Titan', 'value': 'titan_df'}]

fig_eps=px.line(df_t, x='date', y='EPS in Rs',
                       title='Earnings',
                       labels={'value': 'EPS in Rs'},
                       color_discrete_sequence=['green'],
                       template='plotly_white'
                       ).update_layout(
                            yaxis=dict(title='EPS in Rs', titlefont=dict(color='blue')),
                            legend=dict(y=1.1, orientation='h')
                        ).update_traces(
                            line=dict(width=3)
                        ).add_trace(
                            px.bar(df_t, x='date', y='EPS Growth %',
                                   color_discrete_sequence=['brown'],
                                   labels={'value': 'EPS Growth %'},
                                   template='plotly_white').update_traces(
                                opacity=0.5,
                                yaxis='y2',
                                showlegend=True,
                            ).data[0]
                        ).update_layout(
                            yaxis=dict(title='EPS in Rs', titlefont=dict(color='green')),
                            yaxis2=dict(title='EPS Growth %', titlefont=dict(color='brown'), overlaying='y', side='right'),
                            legend=dict(y=1.1, orientation='h')
                        ).add_shape(  # Add horizontal ref. line
                            dict(
                                type='line',
                                xref='paper',
                                x0=0,
                                x1=1,
                                yref='y2',
                                y0=0.2,
                                y1=0.2,
                                line=dict(color='green', width=2, dash='dash')
                            )
                        )
fig_roce=px.bar(df_t, x='date', y=['Fixed assets purchased', 'FCF'],
                      title='Performance Metrics',
                      labels={'value': 'Fixed assets purchased'},
                      barmode='group',
                      # acolor_discrete_sequence=['blue', 'green'],
                      color_discrete_map={'Fixed assets purchased': 'blue',
                                          'FCF': np.where(df_t['FCF'] < 0, 'red', 'green')},
                      template='plotly_white').update_traces(
                      marker=dict(line=dict(width=1, color='black')),
                      textposition='outside',
                    ).add_trace(
                        px.line(df_t, x='date', y='ROCE %',
                                color_discrete_sequence=['brown'],
                                labels={'value': 'ROCE %'},
                                template='plotly_white').update_traces(
                            line=dict(width=3),
                            yaxis='y2',
                            showlegend=True,
                        ).data[0]
                    ).update_layout(
                        yaxis=dict(title='Fixed assets purchased and FCF', titlefont=dict(color='green')),
                        yaxis2=dict(title='ROCE %', titlefont=dict(color='brown'), overlaying='y', side='right'),
                        legend=dict(y=1.1, orientation='h')
                    ).add_shape(  # Add horizontal ref. line
                        dict(
                            type='line',
                            xref='paper',
                            x0=0,
                            x1=1,
                            yref='y2',
                            y0=0.15,
                            y1=0.15,
                            line=dict(color='brown', width=2, dash='dash')
                        )
                    )

fig_sales = px.line(df_t, x='date', y=['Sales\xa0-', 'Operating Profit', 'Net Profit'],
                 title='Sales and Net Profit',
                 labels={'value': 'Amount in Rs'},
                 color_discrete_sequence=['green', 'brown', 'blue'],
                 template='plotly_white'
                 ).update_layout(
                yaxis=dict(title='Amount in Rs', titlefont=dict(color='blue')),
                legend=dict(y=1.1, orientation='h')
            ).update_traces(
                line=dict(width=3)
            ).add_trace(
                px.bar(df_t, x='date', y='Sales Growth %',
                       color_discrete_sequence=['brown'],
                       labels={'value': 'Sales Growth %'},
                       template='plotly_white'
                       ).update_traces(
                    opacity=0.5,
                    yaxis='y2',
                    showlegend=True,
                ).data[0]
            ).update_layout(
                yaxis=dict(title='Sales-Profits', titlefont=dict(color='green')),
                yaxis2=dict(title='Sales Growth %', titlefont=dict(color='green'), overlaying='y', side='right'),
                legend=dict(y=1.1, orientation='h')
            ).add_shape(  # Add horizontal ref. line
                dict(
                    type='line',
                    xref='paper',
                    x0=0,
                    x1=1,
                    yref='y2',
                    y0=0.10,
                    y1=0.10,
                    line=dict(color='green', width=2, dash='dash')
                )
            )

fig_cash = px.area(df_t, x='date', y=['Cash from Operating Activity\xa0+', 'Cash from Investing Activity\xa0+'],
                 title='Cash Flow',
                 labels={'value': 'Amount in Rs'},
                 color_discrete_sequence=['green', 'red'],
                 template='plotly_white',
                 ).update_layout(
                yaxis=dict(title='Amount in Rs', titlefont=dict(color='blue')),
                legend=dict(y=1.1, orientation='h'),
                hovermode="x",
                margin=dict(t=30, l=10, r=10, b=10),
                uniformtext=dict(minsize=8, mode='hide')
                )




# Create a dropdown menu to select the column to plot
dropdown_options = [{'label': 'op_ratio', 'value': 'op_ratio'},
                    {'label': 'np_ratio', 'value': 'np_ratio'},
                    {'label': 'OPM %', 'value': 'OPM %'}]  #
# Create the initial plot
fig = px.line(df_t, x='date', y='OPM %', title='Trend over Time')


# Update the plot based on the selected dropdown option
def update_plot(selected_df, column):
    if selected_df == 'astral_df':
        df_t = astral_df.copy()
    elif selected_df == 'gmm_df':
        df_t = gmm_df.copy()
    elif selected_df == 'lal_df':
        df_t = lal_df.copy()
    elif selected_df == 'amrut_df':
        df_t = amrut_df.copy()
    elif selected_df == 'alkyl_df':
        df_t = alkyl_df.copy()
    elif selected_df == 'ap_df':
        df_t = ap_df.copy()
    elif selected_df == 'divis_df':
        df_t = divis_df.copy()
    elif selected_df == 'titan_df':
        df_t = titan_df.copy()
    elif selected_df == 'tcs_df':
        df_t = tcs_df.copy()
    elif selected_df == 'tata_elxsi_df':
        df_t = tata_elxsi_df.copy()






    avg = df_t[column].mean()
    # Remove the existing average trace before adding the new one
    fig.data = [trace for trace in fig.data if trace.name != 'Average']
    fig.update_traces(y=df_t[column])
    # Add the average line
    fig.add_trace(go.Scatter(x=df_t['date'], y=[avg] * len(df_t), mode='lines', name='Average'))
    fig.data[0].y = df_t[column]


###### APP LAYOUT ###################################################################
app.layout = html.Div([

    dcc.Dropdown(id='dropdown-df', options=dropdown_options2, value='gmm_df',
                 style={'width': '50%', 'display': 'inline-block'}),

    html.H1('EPS and Financial Metrics'),
    ####### EPS #####
    dcc.Graph(
        id='eps-plot',
        figure=fig_eps,
        style={'width': '50%', 'display': 'inline-block'}
    ),

    ####### ROCE #####
    dcc.Graph(
        id='performance-metrics-plot',
        figure=fig_roce,
        style={'width': '50%', 'display': 'inline-block'}
    ),
    ###### SALES #######
    dcc.Graph(
        id='sales-net-profit-plot',
        figure=fig_sales,
        style={'width': '50%', 'display': 'inline-block'}
    ),
    ###### CASH FLOW ######
    dcc.Graph(
        id='cashflow-plot',
        figure=fig_cash,
        style={'width': '50%', 'display': 'inline-block'}
    ),

    ################
    dcc.Dropdown(id='dropdown-column', options=dropdown_options, value='op_ratio'),
    dcc.Graph(id='custom-plot',
              figure=fig,
              style={'width': '50%', 'display': 'inline-block'}),


])

@app.callback(
    [Output('eps-plot', 'figure'),
     Output('performance-metrics-plot', 'figure'),
     Output('sales-net-profit-plot', 'figure'),
     Output('cashflow-plot', 'figure')],
    Input('dropdown-df', 'value')
)
def update_graph(selected_df):
    # Update graph based on selected_value
    if selected_df == 'astral_df':
        df_t = astral_df.copy()
    elif selected_df == 'gmm_df':
        df_t = gmm_df.copy()
    elif selected_df == 'lal_df':
        df_t = lal_df.copy()
    elif selected_df == 'amrut_df':
        df_t = amrut_df.copy()
    elif selected_df == 'alkyl_df':
        df_t = alkyl_df.copy()
    elif selected_df == 'ap_df':
        df_t = ap_df.copy()
    elif selected_df == 'divis_df':
        df_t = divis_df.copy()
    elif selected_df == 'titan_df':
        df_t = titan_df.copy()
    elif selected_df == 'tcs_df':
        df_t = tcs_df.copy()
    elif selected_df == 'tata_elxsi_df':
        df_t = tata_elxsi_df.copy()

    fig_eps = px.line(df_t, x='date', y='EPS in Rs',
                      title='Earnings',
                      labels={'value': 'EPS in Rs'},
                      color_discrete_sequence=['green'],
                      template='plotly_white'
                      ).update_layout(
        yaxis=dict(title='EPS in Rs', titlefont=dict(color='blue')),
        legend=dict(y=1.1, orientation='h')
    ).update_traces(
        line=dict(width=3)
    ).add_trace(
        px.bar(df_t, x='date', y='EPS Growth %',
               color_discrete_sequence=['brown'],
               labels={'value': 'EPS Growth %'},
               template='plotly_white').update_traces(
            opacity=0.5,
            yaxis='y2',
            showlegend=True,
        ).data[0]
    ).update_layout(
        yaxis=dict(title='EPS in Rs', titlefont=dict(color='green')),
        yaxis2=dict(title='EPS Growth %', titlefont=dict(color='brown'), overlaying='y', side='right'),
        legend=dict(y=1.1, orientation='h')
    ).add_shape(  # Add horizontal ref. line
        dict(
            type='line',
            xref='paper',
            x0=0,
            x1=1,
            yref='y2',
            y0=0.2,
            y1=0.2,
            line=dict(color='green', width=2, dash='dash')
        )
    )
    fig_roce = px.bar(df_t, x='date', y=['Fixed assets purchased', 'FCF'],
                      title='Performance Metrics',
                      labels={'value': 'Fixed assets purchased'},
                      barmode='group',
                      # acolor_discrete_sequence=['blue', 'green'],
                      color_discrete_map={'Fixed assets purchased': 'blue',
                                          'FCF': np.where(df_t['FCF'] < 0, 'red', 'green')},
                      template='plotly_white').update_traces(
        marker=dict(line=dict(width=1, color='black')),
        textposition='outside',
    ).add_trace(
        px.line(df_t, x='date', y='ROCE %',
                color_discrete_sequence=['brown'],
                labels={'value': 'ROCE %'},
                template='plotly_white').update_traces(
            line=dict(width=3),
            yaxis='y2',
            showlegend=True,
        ).data[0]
    ).update_layout(
        yaxis=dict(title='Fixed assets purchased and FCF', titlefont=dict(color='green')),
        yaxis2=dict(title='ROCE %', titlefont=dict(color='brown'), overlaying='y', side='right'),
        legend=dict(y=1.1, orientation='h')
    ).add_shape(  # Add horizontal ref. line
        dict(
            type='line',
            xref='paper',
            x0=0,
            x1=1,
            yref='y2',
            y0=0.15,
            y1=0.15,
            line=dict(color='brown', width=2, dash='dash')
        )
    )

    fig_sales = px.line(df_t, x='date', y=['Sales\xa0-', 'Operating Profit', 'Net Profit'],
                        title='Sales and Net Profit',
                        labels={'value': 'Amount in Rs'},
                        color_discrete_sequence=['green', 'brown', 'blue'],
                        template='plotly_white'
                        ).update_layout(
        yaxis=dict(title='Amount in Rs', titlefont=dict(color='blue')),
        legend=dict(y=1.1, orientation='h')
    ).update_traces(
        line=dict(width=3)
    ).add_trace(
        px.bar(df_t, x='date', y='Sales Growth %',
               color_discrete_sequence=['brown'],
               labels={'value': 'Sales Growth %'},
               template='plotly_white'
               ).update_traces(
            opacity=0.5,
            yaxis='y2',
            showlegend=True,
        ).data[0]
    ).update_layout(
        yaxis=dict(title='Sales-Profits', titlefont=dict(color='green')),
        yaxis2=dict(title='Sales Growth %', titlefont=dict(color='green'), overlaying='y', side='right'),
        legend=dict(y=1.1, orientation='h')
    ).add_shape(  # Add horizontal ref. line
        dict(
            type='line',
            xref='paper',
            x0=0,
            x1=1,
            yref='y2',
            y0=0.10,
            y1=0.10,
            line=dict(color='green', width=2, dash='dash')
        )
    )

    fig_cash = px.area(df_t, x='date', y=['Cash from Operating Activity\xa0+', 'Cash from Investing Activity\xa0+'],
                       title='Cash Flow',
                       labels={'value': 'Amount in Rs'},
                       color_discrete_sequence=['green', 'red'],
                       template='plotly_white',
                       ).update_layout(
        yaxis=dict(title='Amount in Rs', titlefont=dict(color='blue')),
        legend=dict(y=1.1, orientation='h'),
        hovermode="x",
        margin=dict(t=30, l=10, r=10, b=10),
        uniformtext=dict(minsize=8, mode='hide')
    )


    return [fig_eps,fig_roce,fig_sales,fig_cash]


@app.callback(Output('custom-plot', 'figure'), [Input('dropdown-df', 'value'),
                                                Input('dropdown-column', 'value')])
def update_figure(selected_df,column):
    update_plot(selected_df,column)
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
