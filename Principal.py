import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis Linguísticas
co2 = ctrl.Antecedent(np.arange(0,1001,1), 'CO2')
pm25 = ctrl.Antecedent(np.arange(0,366,1), 'PM2.5')
umidade = ctrl.Antecedent(np.arange(0, 101, 1), 'UMIDADE')
temperatura = ctrl.Antecedent(np.arange(-10, 51, 1), 'TEMPERATURA')  # Temperatura em °C

qualidade_ar = ctrl.Consequent(np.arange(0, 101, 1), 'QUALIDADE')


# Conjuntos de Termos Linguísticos (membership function tipo trapezoidal)

co2['Baixo'] = fuzz.trapmf(co2.universe, [0, 0, 300, 400])
co2['Medio'] = fuzz.trapmf(co2.universe, [350, 450, 650, 750])
co2['Alto'] = fuzz.trapmf(co2.universe, [700, 850, 1000, 1000])

pm25['Baixo'] = fuzz.trapmf(pm25.universe, [0, 0, 30, 50])
pm25['Medio'] = fuzz.trapmf(pm25.universe, [30, 50, 80, 120])
pm25['Alto'] = fuzz.trapmf(pm25.universe, [100, 150, 365, 365])

umidade['Baixo'] = fuzz.trimf(umidade.universe, [0, 0, 30])
umidade['Normal'] = fuzz.trimf(umidade.universe, [20, 50, 80])
umidade['Alta'] = fuzz.trimf(umidade.universe, [70, 100, 100])

temperatura['Fria'] = fuzz.trimf(temperatura.universe, [-10, -10, 15])
temperatura['Agradavel'] = fuzz.trimf(temperatura.universe, [10, 20, 30])
temperatura['Quente'] = fuzz.trimf(temperatura.universe, [28, 35, 50])


qualidade_ar['Boa'] = fuzz.trapmf(qualidade_ar.universe, [0, 0, 30, 40])
qualidade_ar['Moderada'] = fuzz.trapmf(qualidade_ar.universe, [30, 40, 60, 70])
qualidade_ar['Ruim'] = fuzz.trapmf(qualidade_ar.universe, [60, 70, 85, 100])


co2.view()
pm25.view()
umidade.view()
temperatura.view()
qualidade_ar.view()

rule1 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule2 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule3 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule4 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule5 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Ruim'])

rule6 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule7 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule8 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule9 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])

rule10 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Ruim'])
rule11 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule12 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Ruim'])

qualidade_ar_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
qualidade_do_ar_simulador = ctrl.ControlSystemSimulation(qualidade_ar_ctrl)

# Entrando com alguns valores para qualidade da dinheiro e do pessoal
qualidade_do_ar_simulador.input['CO2'] = 200
qualidade_do_ar_simulador.input['PM2.5'] = 10
qualidade_do_ar_simulador.input['UMIDADE'] = 50
qualidade_do_ar_simulador.input['TEMPERATURA'] = 20

#Computando o resultado
qualidade_do_ar_simulador.compute()

pm25.view(sim=qualidade_do_ar_simulador)
co2.view(sim=qualidade_do_ar_simulador)
umidade.view(sim=qualidade_do_ar_simulador)
temperatura.view(sim=qualidade_do_ar_simulador)
qualidade_ar.view(sim=qualidade_do_ar_simulador)


print("A qualidade do AR é de", qualidade_do_ar_simulador.output['QUALIDADE'], "%") 
# Changed 'QUALIDADE' to 'qualidade' to match the actual output dictionary key
