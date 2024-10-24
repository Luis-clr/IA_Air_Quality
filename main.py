import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk


# Map the numerical output to linguistic terms
def map_qualidade(resultado_desgaste):
    if resultado_desgaste < 30:
        return "Boa"
    elif 1 <= resultado_desgaste <= 60: 
        return "Moderada"
    else:
        return "Ruim"


# Função para calcular o desgaste
def Calcular_qualidade_Ar():
    co2_func = int(entrada_co2.get())
    pm25_func = int(entrada_pm25.get())
    umidade_func = int(entrada_umidade.get())
    temperatura_func = int(entrada_temperatura.get())


    qualidade_do_ar_simulador.input['CO2'] = co2_func
    qualidade_do_ar_simulador.input['PM2.5'] = pm25_func
    qualidade_do_ar_simulador.input['UMIDADE'] = umidade_func
    qualidade_do_ar_simulador.input['TEMPERATURA'] = temperatura_func

    
    qualidade_do_ar_simulador.compute()

    resultado_desgaste = qualidade_do_ar_simulador.output["QUALIDADE"]
    resultado_texto = map_qualidade(resultado_desgaste)
    print("A qualidade do AR é de", qualidade_do_ar_simulador.output['QUALIDADE'], "%")
    resultado_label.config(text=f"A qualidade do AR É {resultado_texto}")

 
# Cria uma instância da janela
janela = tk.Tk()
janela.title("Air Quality")

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


# CO2 Baixo
rule1 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Boa'])
rule2 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Boa'])
rule3 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Boa'])
rule4 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Boa'])
rule5 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule6 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule7 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule8 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule9 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Ruim'])

rule10 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule11 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule12 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule13 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule14 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule15 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule16 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule17 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule18 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Ruim'])

rule19 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule20 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule21 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule22 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule23 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule24 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule25 = ctrl.Rule(co2['Baixo'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule26 = ctrl.Rule(co2['Baixo'] & pm25['Medio'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule27 = ctrl.Rule(co2['Baixo'] & pm25['Alto'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])

# CO2 Medio
rule28 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Boa'])
rule29 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule30 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule31 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Boa'])
rule32 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule33 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule34 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule35 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule36 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Ruim'])

rule37 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule38 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule39 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule40 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Boa'])
rule41 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule42 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule43 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule44 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule45 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Ruim'])

rule46 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule47 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule48 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule49 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule50 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Moderada'])
rule51 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule52 = ctrl.Rule(co2['Medio'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule53 = ctrl.Rule(co2['Medio'] & pm25['Medio'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule54 = ctrl.Rule(co2['Medio'] & pm25['Alto'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])

# CO2 Alto
rule55 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule56 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule57 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Fria'], qualidade_ar['Ruim'])
rule58 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule59 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Moderada'])
rule60 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Normal'] & temperatura['Fria'], qualidade_ar['Ruim'])
rule61 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Ruim'])
rule62 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Ruim'])
rule63 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Alta'] & temperatura['Fria'], qualidade_ar['Ruim'])

rule64 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule65 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule66 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Agradavel'], qualidade_ar['Ruim'])
rule67 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule68 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Moderada'])
rule69 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Normal'] & temperatura['Agradavel'], qualidade_ar['Ruim'])
rule70 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Ruim'])
rule71 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Ruim'])
rule72 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Alta'] & temperatura['Agradavel'], qualidade_ar['Ruim'])

rule73 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule74 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule75 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Baixo'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule76 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule77 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule78 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Normal'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule79 = ctrl.Rule(co2['Alto'] & pm25['Baixo'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule80 = ctrl.Rule(co2['Alto'] & pm25['Medio'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])
rule81 = ctrl.Rule(co2['Alto'] & pm25['Alto'] & umidade['Alta'] & temperatura['Quente'], qualidade_ar['Ruim'])


# Criação do Controlador Nebuloso e Simulação
qualidade_ar_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12,
    rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, 
    rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, 
    rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, 
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, 
    rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, 
    rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, 
    rule79, rule80, rule81
])
qualidade_do_ar_simulador = ctrl.ControlSystemSimulation(qualidade_ar_ctrl)


# Plot do gráfico
def exibir_grafico():
    pm25.view(sim=qualidade_do_ar_simulador)
    co2.view(sim=qualidade_do_ar_simulador)
    umidade.view(sim=qualidade_do_ar_simulador)
    temperatura.view(sim=qualidade_do_ar_simulador)
    qualidade_ar.view(sim=qualidade_do_ar_simulador)


# Cria um frame para organizar os widgets
frame = tk.Frame(janela)
frame.pack(padx=50, pady=50)

# Label para o título
titulo_label = tk.Label(frame, text="Air Quality - Diagnóstico de qualidade do AR",font=("Helvetica", 20),fg="#1473e6")
titulo_label.pack(side="top", padx=50, pady=50)

# Entrada de dados
co2_label = tk.Label(frame,text="Quantidade de CO2 na Atmosfera",font=("Helvetica", 14))
co2_label.pack(pady=5)
entrada_co2 = tk.Entry(frame)
entrada_co2.pack(pady=5)

# Label e entrada para poluentes
pm25_label = tk.Label(frame, text="Quantidade de particulas pulentes PM2.5", font=("Helvetica", 14))
pm25_label.pack(pady=5)
entrada_pm25 = tk.Entry(frame)
entrada_pm25.pack(pady=5)

# Label umidade do ar
umidade_label = tk.Label(frame, text="UMIDADE do AR %", font=("Helvetica", 14))
umidade_label.pack(pady=5)
entrada_umidade = tk.Entry(frame)
entrada_umidade.pack(pady=5)

# Label de temperatura
temperatura_label = tk.Label(frame, text="Temperatura em  C°", font=("Helvetica", 14))
temperatura_label.pack(pady=5)
entrada_temperatura = tk.Entry(frame)
entrada_temperatura.pack(pady=5)


# Botão para calcular a qualidade do ar
calcular_botao = tk.Button(frame, text="Calcular Qualidade do AR", command=Calcular_qualidade_Ar, bg="#1473e6", fg="white")
calcular_botao.pack(pady=30)

# Botão para exibir o gráfico
exibir_grafico_botao = tk.Button(frame, text="Exibir Gráfico", command=exibir_grafico, bg="#1473e6", fg="white")
exibir_grafico_botao.pack(pady=15)

# Label para exibir o resultado
resultado_label = tk.Label(frame, text="", font=("Helvetica", 16), fg="red")
resultado_label.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()