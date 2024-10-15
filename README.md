## Порядок работы над курсовой

Предварительно посмотреть видео - [CI/CD для PHP проекта с автотестами на GitHub Actions](https://dzen.ru/video/watch/670b261c8a8ab555fea6d063)  
Зарегистрировать свой аккаунт на [GitHub.com](https://github.com)  
Добавить на него исходный код своего курсового проекта с прошлого учебного года (проект интернет-магазина выбранной вами тематики на PHP)  
Добиться запуска проекта, добавить инструмент автотестирования PHPUnit, написать модульные тесты на PHPUnit (не менее 3), убедиться в их успешном выполнении, написать пайплайн и добиться его выполнения на GitHub Actions.  
Как это сделать? - пошаговая инструкция [здесь](https://github.com/Coopteh/IS211/tree/auto-testing-01)  
Сделать 2 скриншота для курсовой работы - два сценария проверки: позитивный с успешным прохождением тестов и негативный (с получением ошибки в ходе выполнения пайплайна)  
– скриншоты страницы использованием GitHub Actions с развернутым этапом тестирования.  

## Порядок сдачи курсовой 

Открываете свой репозиторий с проектом на GitHub и показываете выполненные 2 сценария запуска паплайна на GitHub Actions (позитивный и негативный).  
Защищаете свою распечатанную курсовую работу, структура которой отвечает заданной в этом документе.   
Счастливый и удовлетворенный, получаете допуск к экзаменационной сессии.  

## Структура курсовой работы по Внедрению

Тема: **Автоматизация процессов непрерывной интеграции и поставки для веб-приложения <Название вашего проекта>**

Цель работы: 
• Изучить концепцию CI/CD и ее преимущества.
• Изучить популярные инструменты для CI/CD 
• Изучить принципы и практики автоматизированного тестирования с использованием PHPUnit.
• Создать CI/CD пайплайн для существующего веб-приложения на PHP, включая этапы сборки и тестирования.
• Продемонстрировать автоматизацию процесса непрерывной интеграции и поставки.

Примечание: В этом варианте курсовой работы, вы будете изучать CI/CD на примере уже существующего веб-приложения, написанного на PHP.   
Это позволит вам сосредоточиться на практической реализации CI/CD без необходимости тратить время на разработку приложения с нуля.  

Содержание:
1. Введение:
• Определение CI/CD, его этапы и преимущества.
• Актуальность темы и ее практическое значение в контексте разработки веб-приложений.
• Формулировка цели и задач курсовой работы.
```
Задачи:
1. Изучить концепцию CI/CD
2. Изучить автоматизированное тестирование
3. Создать модульные тесты для веб-приложения
4. Создать CI/CD пайплайн для веб-приложения
5. Провести тестирование CI/CD пайплайна
6. Проанализировать результаты внедрения CI/CD
```
2. Обзор инструментов CI/CD:
• Анализ популярных инструментов CI/CD (GitHub CI/CD, GitLab CI/CD, Jenkins, CircleCI и другие).
• Сравнительный анализ инструментов по функционалу, удобству использования, стоимости и другим критериям.
• Выбор подходящего инструмента для реализации CI/CD пайплайна в рамках курсовой работы (GitHub CI/CD).

3. Изучение автоматизированного тестирования:
• Обзор основных принципов и практик автоматизированного тестирования.
• Изучение фреймворка PHPUnit для тестирования PHP кода.
• Примеры написания unit-тестов для PHP-приложений.

4. Выбор и описание веб-приложения:
• Краткое описание ранее разработанного веб-приложения на PHP (название, для кого, зачем).
• Описание функционала и архитектуры выбранного приложения.
• Анализ существующего кода и идентификация потенциальных проблем.

5. Создание модульных тестов для веб-приложения
• Обоснование проверки маршрутов веб-приложения
• Описание проверок и написание unit-тестов для проекта.

6. Реализация CI/CD пайплайна:
• Настройка выбранного CI/CD инструмента (GitHub Actions).
• Описание этапов CI/CD пайплайна:
  * Сборка: Скачивание кода из репозитория, установка зависимостей, компиляция кода (если требуется).
  * Тестирование: Запуск unit-тестов с использованием PHPUnit.
  * Развертывание: Загрузка собранного приложения на тестовый или продуктивный сервер.
• Написание конфигурационных файлов для автоматизации этапов пайплайна.
• Реализация механизма доставки изменений (с использованием  GitHub Actions).

7. Проведение тестирования CI/CD пайплайна:
• Запуск CI/CD пайплайна для проверки его работоспособности.
• Два сценария проверки: позитивный с успешным прохождением тестов и негативный (с получением ошибки в ходе выполнения пайплайна) – Скриншоты страницы использованием  GitHub Actions  с развернутым этапом тестирования.

8. Оценка результатов внедрения CI/CD:
• Анализ положительных и отрицательных сторон внедрения CI/CD.
• Выявление улучшений в процессе разработки и развертывания приложения.
• Предложения по дальнейшему развитию CI/CD пайплайна (добавить шаги по поставке и развертыванию на производственные и тестовые сервера).
 
9. Заключение:
• Обобщение результатов курсовой работы.
• Выводы о практической ценности CI/CD для разработки веб-приложений.
• Предложения по дальнейшим исследованиям в области CI/CD.

10. Список использованной литературы:
Уилсон Кристи, Грокаем Continuous Delivery, Издательство: Питер, Серия: Библиотека программиста, 2014г., 400с.
Хориков Владимир, Принципы юнит-тестирования, Издательство: Прогресс книга, Серия: Для профессионалов, 2021г., 320с.
Фарли Дейвид, Хамбл Джез, Непрерывное развертывание ПО: автоматизация процессов сборки, тестирования и внедрения новых версий программ, Издательство: Диалектика-Вильямс, Серия: Signature Series, 2019г., 380с.

12. Приложения:
• файл CI/CD пайплайна
• файл модульных тестов PHPUnit

Важно:
• В курсовой работе должны быть использованы современные практики CI/CD.
• Работа должна быть структурирована и оформлена в соответствии с требованиями учебного заведения.
• Убедитесь, что в работе приведены ссылки на источники информации.
