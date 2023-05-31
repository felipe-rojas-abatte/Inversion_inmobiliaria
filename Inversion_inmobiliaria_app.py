import streamlit as st
import pandas as pd
   
def pago(valor_prestamo, interes_anual, plazo_años, tasa_aumento_UF, gastos_op):
       plazo_meses = plazo_años*12
       factor_reajuste_UF_anual = (1+tasa_aumento_UF/100)**12
       interes_mensual = (interes_anual*factor_reajuste_UF_anual/12)/100
       numerador = valor_prestamo*interes_mensual
       denominador = (1 - (1+interes_mensual)**(-plazo_meses))
       try:
           return numerador/denominador + gastos_op/plazo_meses
       except ZeroDivisionError as e:
              print("Error: Cannot divide by zero")
       return 0

def app():
    cols = st.columns(3)
    with cols[0]:
        uf_actual = st.number_input('Valor actual UF', value = 1.0)
    with cols[1]:
        valor_depa = st.number_input('Valor depa UF', value = 0.0)
    with cols[2]:
        pie = st.number_input('Pie %', value = 0.0)
    cols = st.columns(3)
    with cols[0]:
        interes_anual = st.number_input('Interés anual %', value = 0.0)
    with cols[1]:
        plazo_años = st.number_input('Plazo (años)', value = 0.0)
    with cols[2]:
        gastos_op = st.number_input('Gastos Operacionales $', value = 0.0)    
    cols = st.columns(3)
    with cols[0]:
        tasa_aumento_UF = st.number_input('Tasa aumento UF mensual %', value = 0.0)
                
    valor_a_financiar = valor_depa*(1.0 - pie/100)    
    valor_prestamo = uf_actual*valor_a_financiar
    
    cuota_mensual = pago(valor_prestamo, interes_anual, plazo_años, tasa_aumento_UF, gastos_op)
    
    ingreso_recomendado = cuota_mensual/0.25
    
    st.write("Valor a financiar: UF{:.0f} / ${:.0f}".format(valor_a_financiar, valor_prestamo))
    st.write("Cuota mensual a pagar: ${:.0f}".format(cuota_mensual))
    st.write("Ingreso total recomendado: ${:.0f}".format(ingreso_recomendado))
    
    
if __name__ == '__main__':
       st.title('Simulador de Crédito Hipotecario')
       st.write('Estima el valor de tu crédito hipotecario considerando las siguientes variables.')
       app()
       
       