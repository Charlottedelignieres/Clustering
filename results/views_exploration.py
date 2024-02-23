from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def exploration_page(request):
    # Charger les données
    df = pd.read_csv('/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/data/df_2_clusters.csv')

    # Créer la première figure (Expenses)
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    sns.histplot(df["MntAllProducts"], color='red', ax=axes[0])
    axes[0].set_title('Distribution de Expenses')
    df["MntAllProducts"].plot.box(color='red', ax=axes[1])
    axes[1].set_title('Boîte à moustaches de Expenses')
    plt.tight_layout()

    # Sauvegarder la première figure
    chemin_expenses_figure = "/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/static/expenses_figure.png"
    plt.savefig(chemin_expenses_figure)
    plt.close()

    # Créer la deuxième figure (Income)
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    sns.histplot(df["Income"], color='red', ax=axes[0])
    axes[0].set_title('Distribution de Income')
    axes[0].tick_params(axis='x', rotation=45)
    df["Income"].plot.box(color='red', ax=axes[1])
    axes[1].set_title('Boîte à moustaches de Income')
    plt.tight_layout()

    # Sauvegarder la deuxième figure
    chemin_income_figure = "/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/static/income_figure.png"
    plt.savefig(chemin_income_figure)
    plt.close()

    # Créer la troisième figure (Age_group)
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    df["Age_group"].value_counts().plot(kind='bar', color='red', ax=axes[0])
    axes[0].set_title("Distribution des Ages des clients")
    axes[0].set_xlabel("Age")
    axes[0].set_ylabel("Nombre de clients")
    axes[0].tick_params(axis='x', rotation=45)

    # Quatrième figure (Kids)
    df['TotalChildHome'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=axes[1])
    axes[1].set_title("Distribution enfants par foyer")

    # Sauvegarder la troisième et la quatrième figure
    chemin_combined_figure = "/Users/charlottedelignieres/Desktop/Formation_Data_Scientist/Projet_semaine_6/src/results/static/combined_figure.png"
    plt.savefig(chemin_combined_figure)
    plt.close()

    # Passer les chemins des fichiers temporaires au template
    context = {
        "chemin_expenses_figure": chemin_expenses_figure,
        "chemin_income_figure": chemin_income_figure,
        "chemin_combined_figure": chemin_combined_figure
    }

    return render(request, 'exploration.html', context)
