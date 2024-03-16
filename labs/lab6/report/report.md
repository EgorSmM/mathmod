---
## Front matter
title: "Отчёт по лабораторной работе №6"
subtitle: "Задача об эпидемии"
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

Построить модель эпидемии в двух случаях:

1. Зараженные изолированы
2. Зараженных не удается изолировать

# Задание

1. Построить модели эпидемии в Julia
2. Построить модели эпидемии в Openmodelica

# Теоретическое введение

Рассмотрим простейшую модель эпидемии. Предположим, что некая изолированная популяция, состоящая из $N$ особей подразделяется на три группы. Первая группа -- это восприимчивые к болезни, но пока здоровые особи. Обозначим их через $S(t)$. Вторая группа –- это число инфицированных особей, которые являются распространителями инфекции. Обозначим их I(t). А третья группа, обозначающаяся через R(t) –- здоровые особи с иммунитетом к болезни. До того, как число заболевших не превышает критического значения $I^* $, считаем, что все больные изолированы и не заражают здоровых. Когда $I(t) > I^* $, тогда инфицирование способны заражать восприимчивых к болезни особей. Таким образом, скорость изменения числа $S(t)$ меняется по следующему закону:
$$
\begin{cases}
 \dot{S(t)} = 0, I(t) \leq I^* \\
 \dot{S(t)} = -aS(t), I(t) > I^* .
\end{cases}
$$

Поскольку каждая восприимчивая к болезни особь, которая, в конце концов, заболевает, сама становится инфекционной, то скорость изменения числа инфекционных особей представляет разность за единицу времени между заразившимися и теми, кто уже болеет и лечится, т.е.:
$$
\begin{cases}
 \dot{I(t)} = -bI(t), I(t) \leq I^* \\
 \dot{I(t)} = aS(t) - bI(t), I(t) > I^* .
\end{cases}
$$

А скорость изменения выздоравливающих особей (при этом приобретающие иммунитет к болезни):
$$
\dot{R(t)} = bI(t).
$$

Постоянные пропорциональности, $a, b$ -- это коэффициенты заболеваемости и выздоровления соответственно.

Для того, чтобы решения соответствующих уравнений определялось однозначно, необходимо задать начальные условия. Считаем, что в момент времени $t_0$ нет особей с иммунитетом к болезни ($R(t_0)=0$), а
число инфицированных и восприимчивых к болезни особей: $I(t_0)=I_0, S(t_0) = S_0$.

# Выполнение лабораторной работы

## Моделирование в Julia

Для начала введем параметры задачи:

```Julia
a = 0.1;
b = 0.15;
t = (0, 100);
```

Переменные $a, b$ являются коэффициентами заболеваемости и выздоровления соответственно.

Далее введем систему дифференциальных уравнений, характеризующую нашу модель.

```Julia
function syst!(dx,x,p,t)
    dx[1] = a*x[3]-b.*x[1];
    dx[2] = b.*x[1];
    dx[3] = -a*x[3];
end;
```

Теперь введем начальные условия задачи:

```Julia
x0 = [45, 3, 5457];
```

Решим систему дифференциальных уравнений первого порядка и запишем $I(t)$ в переменную $u_1$, $R(t)$ -- в $u_2$, а $S(t)$ в $u_3$:

```Julia
prob = ODEProblem(syst!, x0, t);
y = solve(prob, Tsit5(), saveat=0.2);
u1 = Vector{Float64}()
u3 = Vector{Float64}()
u2 = Vector{Float64}()
for i in range(1, length(y.t))
    push!(u1, y.u[i][1]);
    push!(u2, y.u[i][2]);
    push!(u3, y.u[i][3]);
end;
```

Построим график зависимости количества в каждой из групп от времени:

```Julia
t1 = [0:0.2:100];
plot(t1, [u2, u1, u3], label = ["Число восстановившихся" "Число заболевших" "Число неконтактировавших"], title = "Модель эпидемии");
savefig("name.png")
```

Для моего варианта получились следующие графики (рис. @fig:001, @fig:002).

![Число восстановившихся и болеющих при изоляции заболевших](image/3.png){ #fig:001 width=70% }

![Число восстановившихся и болеющих при невозможности изоляции заболевших](image/4.png){ #fig:002 width=70% }

## Моделирование с помощью Openmodelica

Аналогично первому случаю введем параметры $a, b$, а также параметр $N$ -- количество особей в популяции:

```Openmodelica
parameter Real N = 5505;
parameter Real a = 0.10;
parameter Real b = 0.15;
```

Введем переменные $I, R, S$:

```Openmodelica
Real I(start=45);
Real R(start=3);
Real S(start=5457);
```

Введем систему уравнений, описывающую нашу модель:

```Openmodelica
equation
  der(I) = a*S-b*I;
  der(R) = b*I;
  der(S) = -a*S;
```

Для моего варианта получились следующие графики (рис. @fig:003, @fig:004).

![Число восстановившихся и болеющих при изоляции заболевших](image/1.png){ #fig:003 width=70% }

![Число восстановившихся и болеющих при невозможности изоляции заболевших](image/2.png){ #fig:004 width=70% }

# Выводы

Была построена модель эпидемии. В случае изоляции зоболевших число зараженных сразу падает. В случае невозможности изоляции число зараженных в какой-то момент достигает своего пика, а потом падает.

# Список литературы{.unnumbered}


