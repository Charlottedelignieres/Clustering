import plotly.express as px


# Fonction pour tracer un histogramme
def hist_plot(data_frame, col_x, title, height=400, width=800):
  fig_hist = px.histogram(
      data_frame=data_frame,
      title=title,
      width=width,
      height=height,
      x=col_x,
      # y='',
      # orientation='h',
      color='cluster',
      category_orders={
          'cluster':[0, 1]},
      color_discrete_sequence=['skyblue','firebrick'],
      # color_discrete_map={0:'skyblue', 1:'firebrick'},
      # pattern_shape='cluster',
      # pattern_shape_sequence=["x", "-", "+", ".", "|", "/", "\\"],
        # Besoin de "\\" pour échapper la caractère spécial "\"
      # pattern_shape_map={0:"x", 1:"-"},
      # facet_row='',
      # facet_row_spacing=0.05,
      # facet_col='',
      # facet_col_wrap=2,
      # facet_col_spacing=0.05,
      # hover_name='',
      # hover_data=['', ''],
      # labels={'':''}, # pour changer le nom des labels
      marginal='box',
      opacity=0.7,
      barmode='overlay',
      # barnorm='percent',
      # histfunc='count',
      # histnorm='density',
      # log_x=False, log_y=False,
      # range_x=[50,950],
      # range_y=[0,1700],
  )

  fig_hist.update_layout(
      paper_bgcolor = 'white', # nom de couleur (CSS name) pour le papier (arrière-plan)
      plot_bgcolor='white', # nom de couleur (CSS name) pour le fond du graphique
      title={
          'font':{
              # 'color':'steelblue', # 'darkgreen',
              # 'family':'Arial',
              'size':24
          },
          'x':0.5,
          'xanchor': 'center', # Centrage horizontal du titre
          'y': 0.97,
          'yanchor': 'top', # aligmenent vertical du titre
          # 'yref':'paper', # Référence pour 'y' ('container' (défaut) ou 'paper')
          'pad':{
              # 'b':50,
              # 't':20
          },
      },
      legend={
          'bgcolor':'white', # 'mediumturquoise',
          'bordercolor':'black',
          'borderwidth':1,
          # 'entrywidth':0,
          # 'entrywidthmode':'pixels',
          # 'itemwidth':40,
          'font': {
              # 'color':'darkslategrey',
              #'family':'Open Sans, verdana, arial, sans-serif',
              'size': 14},
          'title':{
              # 'text':'', # Personnalise le titre de la légende
              'font': {
                  # 'color':'black',
                  'size': 16, # Ajuste taille titre de la légende
                  # 'family': , #
              },
              # 'side':'left',
          },
          # 'xref':'paper', # or 'container'
          'x':0.99,
          'xanchor':'right', #'center',
          # 'yref':'paper', # or 'container'
          'y':0.72,
          'yanchor':'top', # 'bottom',
          'orientation': 'v'
      },
      margin={
          'autoexpand':True,
          'b':20,
          'l':20,
          'r':20,
          't':40,
          'pad':0,
      }, # ajustement des marges,
  )

  fig_hist.update_traces(marker_line_width=0.5,marker_line_color="black")

  fig_hist.update_xaxes(
      showline=True, linewidth=2, linecolor='black',
      showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash',
      title_standoff=3,
  )
  fig_hist.update_yaxes(
      showline=True, linewidth=2, linecolor='black',
      showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash',
      title_standoff=3,
  )

  return fig_hist