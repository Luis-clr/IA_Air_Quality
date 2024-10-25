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
        updateProgress(data.qualidade_percentual);
    })
    .catch(error => console.error('Erro:', error));
});

document.getElementById('gerar_graficos').addEventListener('click', function () {
    fetch('http://127.0.0.1:5000/gerar_graficos')
    .then(response => response.json())
    console.log(response)

});

function updateProgress(percentage) {
const progressCircle = document.querySelector('.progress-circle');
const percentageText = document.getElementById('percentage-text');

// Atualiza o valor da porcentagem no centro do círculo
percentageText.textContent = `${percentage.toFixed(2)}%`;

// Definir a cor de fundo do círculo baseado na qualidade do ar
let circleColor;

if (percentage < 30) {
    circleColor = 'green'; // Verde para porcentagens abaixo de 30
} else if (percentage <= 60) {
    circleColor = 'yellow'; // Amarelo para porcentagens entre 30 e 60
} else {
    circleColor = 'red'; // Vermelho para porcentagens acima de 60
}

// Aplicar a cor ao círculo
progressCircle.style.setProperty('--percentage', percentage);
progressCircle.style.setProperty('background', `conic-gradient(${circleColor} calc(${percentage}% ), #e4e4e4 0)`);

// Garantir que o círculo mantenha seu formato
progressCircle.style.borderRadius = '50%';
}