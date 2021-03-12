import streamlit as st

def home():

	st.title('Ocular Disease Intelligent Recognition (ODIR)')
	st.image('img/eye_couv.jpg')
	st.write('## A propos du projet')

	st.markdown('''
		Ce projet fait partie d’un challenge de **reconnaissance intelligente des maladies oculaires** , 
		s’appuyant sur une **base de données ophtalmiques de 5000 patients**. La tâche consiste à 
		développer le modèle d’apprentissage profond capable de reconnaître les maladies oculaires, à 
		partir d’images du fond de l’œil. 
	''')

	st.write(':point_left: Une étude des donnés est disponible dans la navbar.')
	st.write(':point_left: Les modèles de machines learnings développés sont aussi expliqués.')



	st.write('## Contexte')

	st.markdown('''
		La **détection** précoce des **maladies oculaires** est un moyen efficace et économique de prévenir la 
		cécité causée par le **diabète**, le **glaucome**, la **cataracte**, la dégénérescence maculaire liée à l’âge 
		(**DMLA**) et de nombreuses autres maladies. Selon l’Organisation mondiale de la Santé (OMS) à 
		l’heure actuelle, au moins **2,2 milliards de personnes dans le monde ont des déficiences visuelles**, 
		dont au moins 1 milliard ont une déficience visuelle qui **aurait pu être évitée**. La détection rapide 
		et automatique des maladies est essentielle et urgente pour réduire la charge de travail de 
		l’ophtalmologiste et prévenir les dommages visuels des patients. La vision par ordinateur et 
		l’apprentissage en profondeur peuvent détecter automatiquement les maladies oculaires après 
		avoir fourni des images de fond d’œil médical de haute qualité.
	''')
