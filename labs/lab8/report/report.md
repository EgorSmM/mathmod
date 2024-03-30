---
## Front matter
title: "Отчет по лабораторной работе №8"
subtitle: "Модель конкуренции 2 фирм"
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

Построить модели конкуренции двух фирм.

# Задание

1. Создать модель конкуренции 2 фирм без учета социально-психологических факторов.
2. Создать модель конкуренции 2 фирм с учетом социально-психологических факторов.

# Теоретическое введение

Рассмотрим две фирмы, производящие взаимозаменяемые товары одинакового качества и находящиеся в одной рыночной нише. Последнее означает, что у потребителей в этой нише нет априорных предпочтений, и они приобретут тот или иной товар, не обращая внимания на знак фирмы. В этом случае, на рынке устанавливается единая цена, которая определяется балансом суммарного предложения и спроса. Иными словами, в рамках нашеймодели конкурентная борьба ведётся только рыночными методами. То есть, конкуренты могут влиять на противника путем изменения параметров своего производства: себестоимость, время цикла, но не могут прямо вмешиваться в ситуацию на рынке («назначать» цену или влиять на потребителей каким-либо иным способом.)

Уравнения динамики оборотных средств запишем в виде:
$$
\begin{cases}
\dfrac{dM_1}{dt} = -\frac{M_1}{\tau_1}+N_1q(1-\frac{p}{p_{cr}}p-\kappa_1)
\dfrac{dM_2}{dt} = -\frac{M_2}{\tau_1}+N_2q(1-\frac{p}{p_{cr}}p-\kappa_2),
\end{cases}
$$
где $\kappa_1$ и $\kappa_2$ меры эластичности функции спроса по цене, $p$ -- стоимость продукта, $p_{cr}$ критическая стоимость продукта, $q$ -- максимальная потребность одного человека в продукте в единицу времени, $N$ -- число потребителей производимого продукта, $M$ -- оборотные средства продукта.

Второй случай -- когда используются психологические факторы. Модель в этом случае будет выглядеть следующим образом:
$$
\begin{cases}
\dfrac{dM_1}{dt} = -\frac{M_1}{\tau_1}+N_1q(1-\frac{p}{p_{cr}}p-\kappa_1)
\dfrac{dM_2}{dt} = -\frac{M_2}{\tau_1}+N_2q(1-\frac{p}{p_{cr}}p-\kappa_2),
\end{cases}
$$

# Выполнение лабораторной работы

## Моделирование в Julia

Для начала введем параметры задачи:

```Julia
p_cr = 27.0;
N=37.0;
q=1.0;
tau_1 = 17.0;
tau_2 = 16.0;
p_1_tilda = 15;
p_2_tilda = 12;

a_1 = p_cr/((tau_1)^2*(p_1_tilda)^2*N*q);
a_2 = p_cr/((tau_2)^2*(p_2_tilda)^2*N*q);
b = p_cr/((tau_1)^2*(p_1_tilda)^2*(tau_2)^2*(p_2_tilda)^2*N*q);;
c_1 = (p_cr-p_1_tilda)/tau_1/p_1_tilda;
c_2 = (p_cr-p_2_tilda)/tau_2/p_2_tilda;
t = (0, 25)
```

Далее введем систему дифференциальных уравнений, характеризующую нашу модель.

```Julia
function syst!(dx,x,p,t)
    dx[1] = x[1]-b/c_1*x[1]*x[2]-a_1/c_1*(x[1])^2;
    dx[2] = c_2/c_1*x[2]-(b/c_1+0.00024)*x[1]*x[2]-a_2/c_1*(x[2])^2;
end;
```

Теперь введем начальные условия задачи:

```Julia
x0 = [7, 7.7];
```

Решим дифференциальное уравнение первого порядка и запишем оборотные средства первой и второй фирм в переменные $u_1$ и $u_2$ соответственно:

```Julia
prob = ODEProblem(syst!, x0, t);
y = solve(prob, Tsit5(), saveat=0.01);
u1 = Vector{Float64}()
u2 = Vector{Float64}()
for i in range(1, length(y.t))
    push!(u1, y.u[i][1]);
    push!(u2, y.u[i][2]);
end;
```

Построим график зависимости количества оборотных средств от времени:

```Julia
t1 = [0:0.01:25];
plot(t1./c_1, [u1, u2], label = ["Фирма 1" "Фирма 2"], title = "Изменение оборотных средств");
xlabel!("Нормированное время")
ylabel!("Оборотные средства")
savefig("name.png")
```

Для моего варианта получились следующие графики (рис. @fig:001, @fig:002).

![Без учета психологических факторов](image/1.png){ #fig:001 width=70% }

![С учетом психологических факторов](image/2.png){ #fig:002 width=70% }

## Моделирование с помощью Openmodelica

Введем параметры задачи:

```Openmodelica
parameter Real p_cr = 27.0;
parameter Real N=37.0;
parameter Real q=1.0;
parameter Real tau_1 = 17.0;
parameter Real tau_2 = 16.0;
parameter Real p_1_tilda = 15;
parameter Real p_2_tilda = 12;

parameter Real a_1 = p_cr/((tau_1)^2*(p_1_tilda)^2*N*q);
parameter Real a_2 = p_cr/((tau_2)^2*(p_2_tilda)^2*N*q);
parameter Real b = p_cr/((tau_1)^2*(p_1_tilda)^2*(tau_2)^2*(p_2_tilda)^2*N*q);
parameter Real c_1 = (p_cr-p_1_tilda)/tau_1/p_1_tilda;
parameter Real c_2 = (p_cr-p_2_tilda)/tau_2/p_2_tilda;
```

Введем переменные:

```Openmodelica
Real M1(start=7);
Real M2(start=7.7);
```

Введем систему уравнений, описывающую нашу модель:

```Openmodelica
equation
  der(M1) = M1-b/c_1*M1*M2-a_1/c_1*(M1)^2;
  der(M2) = c_2/c_1*M2-(b/c_1)*M1*M2-a_2/c_1*(M2)^2; 
```

Для моего варианта получились следующие графики (рис. @fig:003, @fig:004).

![Без учета психологических факторов](image/1mo.png){ #fig:003 width=70% }

![С учетом психологических факторов](image/2mo.png){ #fig:004 width=70% }

Максимальная эффективность рекламы во втором случае жостигается при $t=0.0073$.

# Выводы

Мы построили модели конкуренции 2 фирм.

# Список литературы{.unnumbered}