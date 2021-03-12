import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
        - Diabetes (D),
        - Glaucoma (G),
        - Cataract (C),
        - Age related Macular Degeneration (A),
        - Hypertension (H),
        - Pathological Myopia (M),
        - Other diseases/abnormalities (O)
    ''')
    
    df= pd.read_csv('data/full_df_cleaned_v3.csv')

    fig, (ax1) = plt.subplots(1, 1, figsize=(20,5))
    sns.histplot(ax=ax1, x="Patient Age", data=df, kde=True, bins=90)
    ax1.set_title("distribution d'Age  dans  df")
    st.pyplot()

    
    
    
    
