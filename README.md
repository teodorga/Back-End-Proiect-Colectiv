# Pornire server back-end

In folderul de back-end se gaseste un manage.py, cu acel fisier avem de lucrat:
- Deschidem CMD in folderul de back-end unde se aflta manage.py
- "pip3 install -r requirements.txt" pentru a putea instala toate pachetele necesare
- "python manage.py makemigrations back_end" pentru a putea creea modelele local
- "python manage.py migrate" crearea DB ului
- "python manage.py runserver" si serverul este deschis

URL:
  /admin - platforma de manage server, putem adauga modele, sterge, etc. (Video trebuie sa fie .mp4)
  NOTE: Daca nu exista un superuser, se poate crea din cmd, tot cu manage.py -> "python manage.py createsuperuser"
  
  /courses - cursuri
  /tutorials/[id_course] - tutoriale
