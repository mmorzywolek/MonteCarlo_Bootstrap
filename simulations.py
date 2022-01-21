import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import matplotlib.pyplot as plt
import functions

def monte_carlo():
    st.title("Projekt zaliczeniowy Symulacje Monte Carlo")
    st.markdown("Symulacja alokacji budżetu marketingowego na przykładzie wykorzystania symulacji Monte Carlo.")
    st.markdown("Jako producent chcę wprowadzić na rynek dobro X. Aby produkt wprowadzić z sukcesem muszę oszacować jego cenę w warunkach niepewności"
                "co do tego jaki będzie finalny koszt wyprodukowania dobra X. "
                "Aby produkt sprzedawał się z sukcesem muszę również oszacować jaki budżet marketingowy powinienem zainwestować "
                "z dostępnego aby zmaksymalizować prawdopodobny zwrot.")

    st.markdown("***")

    st.markdown("Zmienne użyte do symulacji:")
    st.markdown("1. unit_cost - zmienna która muszę założyć \n"
                "2. unit_price - nie znając kosztu produkcji muszę oszacować cenę dobra która przyniesie zysk \n"
                "3. marketing_budget - do wydania dysponujemy budżetem wielkości 50 000 do 100 000 \n"
                "4. unit_sold - ilość sprzedanych produktów, w tym przypadku ilość szacowana jest na podstawie wielkości zainwestowanego budżetu")

    st.markdown("***")

    st.markdown("Głównym celem projektu jest: ")
    st.markdown("1. Zaprojektowanie symulacji w oparciu o metodę Monte Carlo \n"
                "2. Przełożenie rozwiązania na prawdziwy problem natury biznesowej \n")

    st.markdown("***")

    st.title("** SYMULACJA **")

    st.markdown("**OSZACOWANIE ŚREDNIEGO KOSZTU I CENY**")

    st.markdown("W pierwszej części założymy średni koszt produkcji oraz cenę ofertową. "
                "Zakładamy że rozkład tych dwóch zmiennych jest rozkładem trójkątnym (np.random.triangular).  ")


    unit_price = st.slider(label="Wybierz średnią cenę ofertową dobra X ",
                           max_value=60,
                           min_value=30,
                           step=5)

    unit_cost = st.slider(label="Wybierz średni koszt produkcji dobra X",
                          max_value=45,
                          min_value=20,
                          step=5)
    margin = (unit_price - unit_cost) / unit_cost
    st.markdown(f"Marża brutto: {margin *100: .2f}%")
    st.markdown("***")
    st.markdown("KOD:")
    st.code("def get_items_ad_triangular(unit_price, unit_cost, N):\n "

    "price_item = np.random.triangular(size=N, left=unit_price-25.0, right=unit_price+10.0, mode=unit_price)\n "
    "cost_item = np.random.triangular(size=N, left=unit_cost-5.0, right=unit_cost+10.0, mode=unit_cost) "

    "return price_item, cost_item")

    st.markdown("***")

    st.markdown("**ILOŚĆ LOSOWAŃ Z ROZKŁADU**")
    st.markdown("Następnie określamy liczbę losowań z rozkładów "
                "które możemy traktować w tym kontekście jako “próby sprzedaży”.")

    N = st.slider(label="Ilość losowań",
                  max_value=10000,
                  min_value=2500,
                  value=5000,
                  step=1000)
    st.markdown("***")

    st.markdown(f"Tak kształtują się rozkłady dla ceny ofertowej oraz kosztów produkcji przy danych średnich oraz {N} losowaniach.")

    price_item, cost_item = functions.get_items_ad_triangular(unit_price, unit_cost, N)
    hist_data = [price_item, cost_item]
    group_label = ['Unit Price', 'Unit Cost']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("***")
    st.markdown('**BUDŻET MARKETINGOWY**')
    st.markdown("Następnie określamy dostępny budżet marketingowy, "
                "do wydania mamy od 50 000 zł do 100 000 zł. To jak dużo zdecydujemy się wydać wpłynie na wielkość sprzedaży.")
    ad_budget = st.slider(label="Wybierz wielkość budżetu marketingowego (PLN'000)",
                          max_value=50,
                          min_value=100,
                          step=10)


    st.markdown("***")
    st.markdown("** WYNIK **")
    st.markdown(f"Tak kształtuje się rozkład przewidywanego zysku przy **{N} próbach** z budżetem marketingowym wynoszącym **{ad_budget * 1000}zł** "
                f"przy średniej cenie ofertowej wynoszącej **{unit_price}zł** i średnim koszcie produkcji dobra równym **{unit_cost}zł**.")
    profit_item, prob_profit = functions.ad_calc_profit(price_item, cost_item, ad_budget)
    hist_data = [profit_item]
    group_label = ['estymowany zysk']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[3000], curve_type='normal')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("***")
    st.markdown("** POGŁĘBIONA ANALIZA **")
    st.markdown("Kluczowe wnioski wynikające z symulacji: ")
    avg_profit = sum(profit_item) / len(profit_item)
    above_null = prob_profit * 100
    roi = (sum(profit_item) / len(profit_item) - ad_budget * 1000) * 100 / (ad_budget * 1000)
    st.text(f"Średni zysk: {avg_profit: .2f}zł")
    st.text(f"Prawdopodobieństwo wyjścia na *0*: {above_null: .2f}%")
    st.text(f"Średni zwrot (ROI) z budżetu zainwestowanego: "
            f"{roi: .2f}%")

def show_author():
    st.markdown("Autor: Maciej Morzywołek"
                "[Twitter](https://twitter.com/m_morzywolek).")


def show_random_walk():
    st.title("Randon Walk Simulator")
    n = st.slider("Set the number of steps", 10, 1000)
    m = st.slider("Set the number of random walks", 1, 100)
    submit = st.button("Run")
    if submit:
        def simlutaion(m, n):
            random_walks = []

            # Simulate random walk
            for i in range(m):
                # Create a list to store the steps
                steps = []
                # Initialize the step
                step = 0
                # Simulate the steps
                for j in range(n):
                    # Generate a random number
                    r = np.random.rand()
                    # If the random number is less than 0.5, move downwards
                    if r < 0.5:
                        step -= 1
                    # If the random number is greater than 0.5, move upwards
                    else:
                        step += 1
                    # Append the step to the steps list
                    steps.append(step)
                # Append the steps list to the random_walks list
                random_walks.append(steps)

            # Plot the random walks
            for i in range(m):
                plt.plot(random_walks[i])
            return st.pyplot()

        simlutaion(m, n)

