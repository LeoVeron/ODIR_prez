import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

def data():

    st.title('ODIR DataSet')
    st.write('## Contenu')
    st.markdown('''
        La base de données ODIR se compose de données ophtalmiques structurée de 5 000 patients, 
        accompagnés de photographies couleur du fond de l’œil gauche et droit. Les photographies sont 
        annotés par des mots clés du diagnostic médical. Grâce à ces étiquettes il est possible de classés 
        les patients en 8 catégories :
    ''')
    st.markdown('''  
        - Normal (N),
        - diabète (D),
        - glaucome (G),
        - Cataracte (C),
        - Dégénérescence maculaire liée à l’âge (A),
        - Hypertension (H),
        - Myopie pathologique (M),
        - Autres maladies/anomalies (O)
    ''')
    
    
    df= pd.read_csv('data/full_df_cleaned_v3.csv')
    
    st.write('## Age des patients')
    ages = pd.concat([pd.DataFrame(np.arange(95)),df['Patient Age'].value_counts() ], axis=1).fillna(0)['Patient Age']
    st.bar_chart(ages)
    
    
    st.write('## Répartition des maladies')
    distcounts = df['tarstr'].value_counts().head(8)
    distlabels = ['Normal', 'Diabète', 'Autres maladies', 'Cataracte', \
        'Dégénérescence maculaire liée à l’âge', 'Glaucome', 'Myopie pathologique', 'Hypertension']
    
    fig = plt.figure()#figsize =(10, 5)) 
    plt.pie(distcounts, labels = distlabels, autopct='%1.1f%%')
    # plt.title('Distribution de diagnostiques dans la population')
    st.pyplot(fig=fig)
    # age_df = pd.read_csv('data/ages.csv')
    # st.bar_chart(age_df['Patient Age'])

    st.write('## Pour les curieux...')
    with st.beta_expander("Voir des images de catégorie 'Normal' "):
           st.image('img/N.JPG')
    with st.beta_expander("Voir des images de catégorie 'Diabète'"):
           st.image('img/D.JPG')
    with st.beta_expander("Voir des images de catégorie 'Glaucome'"):
           st.image('img/G.JPG')
    with st.beta_expander("Voir des images de catégorie 'Cataracte'"):
           st.image('img/C.JPG')
    with st.beta_expander("Voir des images de catégorie 'Dégénérescence maculaire liée à l’âge'"):
           st.image('img/A.JPG')
    with st.beta_expander("Voir des images de catégorie 'Myopie pathologique'"):
           st.image('img/M.JPG')
    with st.beta_expander("Voir des images de catégorie 'Hypertension'"):
           st.image('img/H.JPG')
           
    st.write('')
    st.write('')
    st.write('')    
    st.write('## Préparation de la donnée')
    st.markdown('''  
        - Séparer les images de l'oeil droit et gauche afin d'obtenir des labels indépendants (un seul oeil peut présenter des symptoms)
        - Enlever les images de mauvaises qualités (Lentille poussiéreuse, disque optique invisible)
        - Enlever le peu de patients présentants plusieurs symptoms
        - Resizer les images pour ne pas avoir des images trop grandes à traiter
    ''')
           

    


    
    
    
    
