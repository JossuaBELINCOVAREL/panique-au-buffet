# 🃏 Panique au Buffet

Un petit jeu de cartes solo en Python où l'objectif est simple : atteindre un score le plus proche possible de zéro !  
Affrontez une IA gourmande dans un buffet chaotique rempli d'aliments aux effets imprévisibles !

## 🎮 Principe du jeu

- 25 cartes de nourriture, avec des valeurs allant de -5 à +5  
- 7 tours de jeu  
- À chaque tour :
  - 3 cartes sont révélées
  - Le joueur et l’IA choisissent chacun une carte, en alternant l’ordre de choix à chaque tour
  - La carte restante retourne dans le paquet (qui est remélangé)
- Certaines cartes ont des **effets spéciaux visibles** qui modifient leur valeur ou influencent les scores :
  - `Double la valeur de la carte`
  - `Inverse le signe de la valeur`
  - `Ajoute +3 au score du joueur`
  - `Échange les scores joueur et IA`
- Le but : **terminer avec un score total le plus proche possible de 0**

## 🚀 Objectifs

- ✅ Version solo contre une IA  
- ✅ Alternance du joueur qui commence  
- ✅ Affichage des effets des cartes lors du choix  
- 🔜 Interface web simple et mobile-friendly (à venir)  
- 🔜 Illustrations cartoon 
- ✅ Open source, gratuit et déployable facilement  

## 📦 Installation

```bash
git clone https://github.com/JossuaBELINCOVAREL/panique-au-buffet.git
cd panique-au-buffet
pip install -r requirements.txt
```

## 🛠️ Lancement
```bash
python app/main.py
```

## 🧪 Tests Unitaires
```bash
pytest
```

## 🤝 Contribuer
Les contributions sont les bienvenues ! Voici comment faire :

1. Fork le projet  
2. Crée une branche :  
```bash
git checkout -b ma-fonctionnalite
```
3. Commits tes modifications :
```bash
git commit -m 'Ajout de fonctionnalité'
```
4. Pousse la branche :
```bash
git push origin ma-fonctionnalite
```
5. Ouvre une Pull Request 🧵