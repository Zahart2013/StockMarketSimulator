# StockMarketSimulator
Програма Stocks Market Simulator дозволить усім її користувачам навчитись оперувати акціями на біржі без втрати капіталу, завдяки реалістичній симуляції всіх згенерованих процесів.
## РОБОТА ПРОГРАМИ
Користувач отримує графіки цін на акції 30ти компаній, оцінюючи ситуацію на ринку та власний поточний(стартовий) капітал, він може зробити рішення купити та продати акції тих чи інших компаній. Програма отримує ці запити та обробляє їх, повертаючи оновлений графік після одного пройденого циклу купівлі-продажу. Далі користувач може аналізувати свій вплив на глобальний ринок. Симуляція продовжується циклами до моменту виходу з програми.
## ОПИС МОДУЛІВ
main.py - основний модуль програми<br>
graphs.py - візуалізація поточних даних у графіку<br>
market.py - містить клас Market, котрий робить запити на актуальні дані, зберігає їх та обраховує<br>
network.py - містить клас Network, клас штучних інтелектів та їхньої взаємодії<br>
user.py - містить клас користувача, де зберігаються його рішення і капітали<br>
stocksim.kv - модуль на мові kivy, GUI
## ВСТАНОВЛЕННЯ ТА ВИКОРИСТАННЯ
Розархівувати архів дистрибутиву або застосувати .exe<br>
pip install -r requirements.txt<br>
python main.py
