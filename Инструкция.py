
######################################################
# Запуск :
# Запуск сервера осуществите командой python -m uvicorn main:app  (app.main:app - полный путь)
# 1.Для запуска и автоматической перезагрузки сервера:
# uvicorn app.main:app --reload   (только при тестировании--reload )

# pip install fastapi
# pip install sqlalchemy
# pip install slugify
# pip install pydantic
# pip install alembic

# alembic init migrations
# alembic revision --autogenerate -m "Initial migration"

#####################################################
# Примечание
#
# Команда uvicorn main:app ссылается на:
# * main: файл main.py (модуль Python).
# * app: объект, созданный внутри main.py на строке app = FastAPI().
# * --reload: перезагружает сервер при изменениях кода. Используется только для разработки.
