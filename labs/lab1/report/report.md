---
## Front matter
title: "Отчет по лабораторной работе №1"
subtitle: "Работа с Git"
author: "Смирнов-Мальцев Егор Дмитриевич"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Познакомится с системой Git.

# Задание

Провести базовую настройку Git, создать репозиторий и исследовать различные возможности системы.

# Теоретическое введение

Git - это свободное распространяема система контроля версий. Она предназначена для быстрой и эффективной обработки проектов любого размера.

# Выполнение лабораторной работы

Установил все переводы строк текстовых файлов в главном репозитории одинаковыми. Поставил флаг для избежания нечитаемых строк (рис. [-@fig:001]).

![Настройка Git](image/1.png){ #fig:001 width=70% }

Создал файл Hello.html, инициализировал репозиторий и закоммитил файл (рис. [-@fig:002]).

![Создание репозитория](image/2.png){ #fig:002 width=70% }

Отредактировал файл Hello.html, проиндексировал изменения и закоммитил их (рис. [-@fig:003]).

![Внесение изменений](image/3.png){ #fig:003 width=70% }

Еще раз изменил этот файл, проиндексировал его, не закоммитив изменил его еще раз и проверил статус репозитория (рис. [-@fig:004]).

![Внесение изменений без коммита](image/4.png){ #fig:004 width=70% }

Закоммитил проиндексированные изменения и проверил статус репозитория (рис. [-@fig:005]).

![Коммит проиндексированных изменений](image/5.png){ #fig:005 width=70% }

Вывел сохраненные версии репозитория (рис. [-@fig:006]).

![Лог версий](image/6.png){ #fig:006 width=70% }

Перешел в первую версию репозитория (рис. [-@fig:007]).

![Первая версия репозитория](image/7.png){ #fig:007 width=70% }

Вернулся в последнюю версию репозитория (рис. [-@fig:008]).

![Последняя версия репозитория](image/8.png){ #fig:008 width=70% }

Пометил ее тэгом, перешел в предпоследнюю версию и пометил ее тоже. (рис. [-@fig:009]).

![Работа с тэгами](image/9.png){ #fig:009 width=70% }

Проверил у каких версий стоят тэги (рис. [-@fig:010]).

![Версии с тэгами](image/10.png){ #fig:010 width=70% }

Изменил hello.html и без коммита перешел к текуще версии файла. Изменения пропали (рис. [-@fig:011]).

![Изменение файла без индексирование](image/11.png){ #fig:011 width=70% }

Изменил файл Hello.html, проиндексировав его и откатился к предыдущей версии (рис. [-@fig:012]).

![Откат проиндексированного файла](image/12.png){ #fig:012 width=70% }

Изменил файл Hello.html, закоммитил изменения и откатился к предыдущей версии (рис. [-@fig:013]).

![Откат закоммиченных изменений](image/13.png){ #fig:013 width=70% }

Пометил тэгом произведенные в предыдущем шаге изменения и перешел к правильной версии (рис. [-@fig:014]).

![Переход к правильной версии](image/14.png){ #fig:014 width=70% }

Удалил неправильные версии (рис. [-@fig:015]).

![Удаление версий](image/15.png){ #fig:015 width=70% }

Изменил файл и добавил изменения в уже существующий коммит (рис. [-@fig:016]).

![Добавление изменений в существующий коммит](image/16.png){ #fig:016 width=70% }

Создал папку и перенес в нее файл (рис. [-@fig:017]).

![Перенос файла](image/17.png){ #fig:017 width=70% }

Создал файл index.html (рис. [-@fig:018]).

![Перенос файла](image/18.png){ #fig:018 width=70% }

Изучил данные, хранящиеся в папке .git (рис. [-@fig:019]).

![Перенос файла](image/19.png){ #fig:019 width=70% }

Открыл хэш дерева (рис. [-@fig:020]).

![Информация о хэшах дерева репозитория](image/20.png){ #fig:020 width=70% }

Открыл нужную версию файла по хэшу (рис. [-@fig:021]).

![Работа с объектами по хэшу](image/21.png){ #fig:021 width=70% }

Создал новую ветку и в ней закоммитил новый файл (рис. [-@fig:022]).

![Создание новой ветки](image/22.png){ #fig:022 width=70% }

Изменил остальные файлы в новой ветке (рис. [-@fig:023]).

![Изменения в новой ветке](image/23.png){ #fig:023 width=70% }

Попереключался между ветками (рис. [-@fig:024]).

![Переход между ветками](image/24.png){ #fig:024 width=70% }

Произвел изменения в старой ветке (рис. [-@fig:025]).

![Изменения в старой ветке](image/25.png){ #fig:025 width=70% }

Просмотрел текущее дерево репозитория (рис. [-@fig:026]).

![Дерево репозитория](image/26.png){ #fig:026 width=70% }

# Выводы

С помощью системы Git можно запоминать произведенные изменения и создавать различны ветки изменений.

# Список литературы{.unnumbered}

::: {#refs}
:::
