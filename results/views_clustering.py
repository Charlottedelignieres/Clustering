from django.shortcuts import render
import pandas as pd
import plotly.express as px
from results.utils import hist_plot

# Fonction hist_plot

def clustering_page(request):
    # Charger les données depuis un fichier CSV ou tout autre source
    df = pd.read_csv('/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/data/df_2_clusters.csv')

    # Appeler la fonction hist_plot pour créer la figure interactive
    fig = hist_plot(
        data_frame=df,
        col_x='Income',
        title='Histogram of income per cluster',
        height=450,
        width=800
    )

    # Sauvegarder la figure sous forme de fichier image
    chemin_figure_income = "/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/static/Income_cluster.png"
    fig.write_image(chemin_figure_income)

    fig_total_amount = hist_plot(
        data_frame=df,
        col_x='MntAllProducts',
        title='Histogram of total amount spent per cluster',
        height=450,
        width=800
    )
    
    # Sauvegarder la deuxième figure sous forme de fichier HTML
    chemin_figure_total_amount = "/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/static/Total_amount_cluster.html"
    fig_total_amount.write_html(chemin_figure_total_amount)

    # Passer le chemin du fichier HTML au template
    context = {
        "chemin_figure_income": chemin_figure_income,
        "chemin_figure_total_amount": chemin_figure_total_amount
    }

    return render(request, 'clustering.html', context)
