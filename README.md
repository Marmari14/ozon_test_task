# ozon_test_task

## Установка
Создайте и активируйте виртуальное окружение, затем установите зависимости:
### Windows
``` bash
py -m venv venv
source venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
### macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск тестов
Тесты написаны на PyTest. Запустить основной сценарий можно так:
``` bash
pytest -s -v
```

## Просмотр отчета Allure
Для просмотра отчета Allure на вашем компьютере уже должен быть установлен [Allure](https://allurereport.org/docs/install/).
Для создания отчета выполните команду:
```
pytest -s -v --alluredir=test_result 
```
в результате будут запущены тесты и создана папка test_result.

Для просмотра созданного отчета перейдите в директорию с проектом к командной строке и введите команду:
``` bash
allure serve test_result\ 
```