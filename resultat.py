from traitement import traier_fichier
from periode import definir_periode_elephant
from distance import distance_par_jour_km,distance_par_nuit_jour_km
from activite_elephant import Activite_elephant_m,Activite_elephant_km,duree_marche_repos_km
from direction_geographique import direction_chaque_heure,calcule_direction_par_semaine,calcul_angle
df=traier_fichier("observations.observation.csv")
print(df)
