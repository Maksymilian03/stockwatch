# stockwatch
Aplikacja do śledzenia akcji na giełdzie,
dodawania ich do swoich obserwacji oraz sprawdzania ceny przez api Alpha Vantage

## Technologie
- Django
- Django REST Framework

## Funkcjonalności
- Rejestracja i logowanie użytkowników
- Zarzadzanie obserwowanymi akcjami na giełdzie
- Mozliwosc sprawdzenia ceny aktualne i z ceny z daty dodania akcji do obserwacji 
- Testy jednostkowe


## Instalacja
```bash
git clone https://github.com/Maksymilian03/stockwatch
cd stockwatch
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
echo "API_KEY=twój_klucz" > .env
python manage.py migrate
python manage.py runserver
```



## Endpointy API
| Metoda | Endpoint | Opis |
|--------|----------|------|
| POST | /register/ | Rejestracja |
| POST | /login/ | Logowanie |
| GET/POST | /stocks/ | Akcje |
| GET | /stocks/{id}/price/ | Cena Akcji |
| GET | /stocks/{id}/price_at_date/ | Cena Akcji z dnia dodania do obserwacji|

## Uruchamianie testów 
```bash
python manage.py test
```