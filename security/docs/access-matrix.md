# Access matrix

| Role | Public content | Own result | Anonymized aggregate | Demo config |
|---|---:|---:|---:|---:|
| visitor | allow | deny | deny | deny |
| learner | allow | allow (own only) | deny | deny |
| reviewer | allow | deny | allow | deny |
| admin | allow | deny | allow | allow |

Роль не принимается из пользовательского JSON как доверенный факт. Неизвестная роль/действие → deny.
