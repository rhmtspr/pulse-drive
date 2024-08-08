# Pulse Drive
An web application for car rental

## How to run the program
1. create virtual environment.
2. open the virtual environment.
3. install all necessary packages.
```
pip install -r requirements.txt
```
3. create databases in phpmyadmin, the name should be the same as in the settings.py (car_rental).
4. run mysql and apache in xampp.
5. make migrations
```
py manage.py makemigrations
```
7. migrate
```
py manage.py migrate
```
## Screenshots
1. Login Page

![login_page_PD](https://github.com/user-attachments/assets/e98fbaac-b353-4278-87b0-23b081ac1873)

2. Home Page

![home_page_PD](https://github.com/user-attachments/assets/37cfb3f8-6153-4248-993e-330e210d54c8)

4. Car Detail Page

![car_detail_page_PD](https://github.com/user-attachments/assets/e71ec24d-3651-4202-b9fc-b983f6a1524d)

5. My Transactions Page

![my_transaction_page_PD](https://github.com/user-attachments/assets/e7d31ffb-634b-41cb-89ce-c2cc7c82c59b)

6. My Reviews Page

![my_reviews_page_PD](https://github.com/user-attachments/assets/6345ddc3-e387-4efd-ae7a-362296ba4e9f)

7. Rent Page

![rent_page_PD](https://github.com/user-attachments/assets/7b903970-01a0-4e52-8d12-c136dc5a1839)
