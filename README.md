# selenium_gmail
- Для запуска необходим python 3.6 и выше
- Из корневой папки проекта необходимо выполнить команду pip install -r requirements.txt
- Для запуска теста, необходимо из корня проекта выполнить команду pytest

1. К сожалению не успел сделать возможность запускать кроссплатформенно, поэтому в файле selenium_gmail\fixture\application.py необходимо изменить путь в соответствии с Вашей OS

2. В связи с тем, что при логине в почту gmail с неизвестного IP, Gmail запрашивает аутентификацию по номеру мобильного телефона, необходимо в тесте прописать "тестовую почту" p.s Параметры почты и письма, специально не вынесены из теста т.к. тест 1

