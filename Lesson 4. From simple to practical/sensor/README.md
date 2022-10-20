Система собирает инф с датчиков, в ней есть модуль логирования, который заносит в журнал все обращения к датчикам.  
В системе есть модуль,выполняющий обращение для получения данных с датчиков и модуль генерации html-представления.  
Запуска системы осуществялется из головного модуля.

## Модуль 1: сбор инф с датчиков (data_provider)
    get_temperature, get_pressure, get_wind_speed
    температура, давление, скорость ветра
## Модуль 2: логирование (logger)
    temperature_logger, pressure_logger wind_speed_logger
## Модуль 3: UI (user_interface)
    temperature_view, pressure_view, wind_speed_view
## Модуль 4: HTML-генератор (html_creater)
    create
## Модуль 5: главный модуль (main)
    ...