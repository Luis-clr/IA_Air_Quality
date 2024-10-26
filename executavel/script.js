document.getElementById('form-calculo').addEventListener('submit', function (e) {
    e.preventDefault();

    const co2 =  parseFloat(document.getElementById('co2').value);
    const pm25 = document.getElementById('pm25').value;
    const umidade = parseFloat(document.getElementById('umidade').value);
    const temperatura = parseFloat(document.getElementById('temperatura').value);

    const dados = {
        CO2: co2,
        'PM2.5': pm25,
        Umidade: umidade,
        Temperatura: temperatura
    };
    console.log(dados)

    fetch('http://127.0.0.1:5000/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado_qualidade').textContent = `${data.qualidade_descricao} (${data.qualidade_percentual.toFixed(2)}%)`;
        progresso_barra(data.qualidade_percentual);
    })
    .catch(error => console.error('Erro:', error));
});

function recarrega_pagina() {

    setTimeout(function() {
        location.reload();
    }, 2000); 
}


function progresso_barra(percentage) {
const progresso_circulo = document.querySelector('.progresso_scores');
const porcentagem_textoo = document.getElementById('progresso_porcentam');


porcentagem_textoo.textContent = `${percentage.toFixed(2)}%`;


let circleColor;

if (percentage < 30) {
    circleColor = 'green'; // Verde para porcentagens abaixo de 30
} else if (percentage <= 60) {
    circleColor = 'yellow'; // Amarelo para porcentagens entre 30 e 60
} else {
    circleColor = 'red'; // Vermelho para porcentagens acima de 60
}

// Aplicar a cor ao círculo
progresso_circulo.style.setProperty('--percentage', percentage);
progresso_circulo.style.setProperty('background', `conic-gradient(${circleColor} calc(${percentage}% ), #e4e4e4 0)`);
progresso_circulo.style.borderRadius = '50%';
}