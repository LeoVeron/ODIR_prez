import streamlit as st
CSS = """
i
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


def model():
    st.title('Model V0')
    st.write('### Une intelligence hors norme !')
    st.markdown('''
            ##
            ''')

    with st.beta_expander("CNN"):
        st.markdown('''
            **Modèle de base**: Détecter uniquement la Cataracte \n
            **Problèmatique**: Unbalancing \n
            **Point positif**: Rapide & nous permet d'avoir une première approche sur notre modèle
            ''')

        st.markdown('''
            ##
            ''')

        st.markdown('#### CNN')
        st.image('img/cnn_graph_1.jpeg', width=800)
        st.markdown('''
            ##
            ''')
        st.image('img/baseline_model_N_C_summary.png', width=500)
        st.markdown('''
            ##
            ''')
        st.markdown('#### CNN Scoring')
        st.image('img/score_baseline_model.png', width=500)

    with st.beta_expander("VGG16"):
        st.markdown('''
            **Architecture**: Entraîner à partir de 14 Millions d'image appartenant à 1000 classes \n
            **Point positif**: Nous permet d'entrainer notre modèle avec un nombre important de paramètre
            ''')

        st.markdown('''
            ##
            ''')

        st.markdown('#### VGG16')
        st.image('img/vgg16_graph_1.png', width=800)
        st.markdown('''
            ##
            ''')
        st.markdown('''
            ##
            ''')
        st.image('img/model_N_C_vgg16.png', width=800)
        st.markdown('''
            ##
            ''')
        st.markdown('''
            ##
            ''')
        st.markdown('#### VGG16 Scoring')
        st.image('img/model_VGG16_evaluate.png', width=800)

    st.markdown('''
                ##
                ''')
    st.markdown('''
                ##
                ''')
    st.markdown("""
            [Discover our AI](http://localhost:8501/)
        """)
