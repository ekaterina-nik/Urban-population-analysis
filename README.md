# Urban-population-analysis

Выводы и прогнозы.
1. В выбранных городах с численностью населения наиболее близкой к средней по сегменту (Сокол, Химки, Ярославль) и в наиболее крупных по численности городах датасета (Москва, Краснодар) на первый взгляд модель довольно хорошо описывает распределение численности населения по годам (но есть пара точек похожих на выбросы - Сокол, 
Ярославль - этот момент требует более глубокой проверки). Также, для более глубокого анализа, необходимо рассматривать отклонения смоделированных данных от фактических в пределах погрешности.
2. Для городов, по которым построены барплоты, в диапазоне с 2000 по 2037 год (диапазон выбран как достаточный для наглядности - +15 лет от текущего года) видим следующее: падение и затем незначительный рост численности населения для города Сокол (low сегмент - население до 127138 чел. - это условная градация, средняя величина фактической численности населения по всему датафрейму), рост и далее выход на стабильный уровень для города Химки (middle сегмент - от 127138 до 500000 чел.), незначительное падение и дальнейший рост для города Ярославль (large сегмент - от 500000 до 1 млн.чел.), рост населения в Москве и Краснодаре (extra large сегмент - свыше 1 млн.чел.), причем в Краснодаре рост большей интенсивности, чем в Москве.
3. Для полноценного прогноза по будущему увеличению/падению численности населения в городах из разных сегментов, необходимо проработать информацию по достаточно большому количеству выборок из каждого сегмента. В данном случае сделана только одна выборка. Но уже по ней видна некая закономерность, а именно:
- падение численности населения для городов из low сегмента, рост и выход на стабильный уровень для городов из middle сегмента, малая изменчивость численности населения для городов из large сегмента и постоянный рост населения для городов из extra large сегмента.
4. Чтобы оценить экономические перспективы городов, основываясь на росте или падении численности населения, необходимо знать, на основе каких факторов было построено моделирование численности населения, а также дополнительные параметры (например, соотношение в структуре населения между разными категориями граждан: трудоспособные, пенсионеры, дети). Т.к. вообще говоря есть 2 подхода к анализу зависимости между темпами роста населения и экономическими показателями: чем больше население - тем меньше природных ресурсов на душу населения - экономический спад; чем больше населения (в первую очередь трудоспособного) - увеличивается количество рабочей силы, растет интеллектуальный потенциал общества - рост экономического развития.   
