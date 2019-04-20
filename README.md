##Создать окружение и установить зависимости
```
virtualenv .venv
pip install -r req.txt
```

##База данных PostgreSQL:
```sql
create user cleverbots with password 'cleverbots';
create database cleverbots with owner cleverbots;
```
##Выполнить миграции:
`./manage.py migrate`
##Создать суперюзера: 
`./manage.py createsuperuser`

###Примечания:

Желательно сначала добавить картинки через админку.

Фильтрация по size выполнена на основе размера картинки (веса).