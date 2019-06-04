$(function (){
    var graficoEmpresaPorNumeroDeViagens = new Chart(
        $('#graficoEmpresaPorNumeroDeViagens')[0].getContext('2d'),
        {
            type: 'horizontalBar',
            data: dadosEmpresaPorNumeroDeViagens,
            options: {
                title: {
                    display: true,
                    text: 'Viagens por empresa',
                    fontSize: 18,
                    fontColor: 'rgb(33, 37, 41)',
                    position: 'top'
                },
                legend: {
                    display: false
                }
        }
    });
    var graficoEmpresaPorTipoDeCarga = new Chart(
        $('#graficoEmpresaPorTipoDeCarga')[0].getContext('2d'),
        {
            type: 'horizontalBar',
            data: dadosEmpresaPorTipoDeCarga,
            options: {
                title: {
                    display: true,
                    text: 'Tipos de carga por empresa',
                    fontSize: 18,
                    fontColor: 'rgb(33, 37, 41)',
                    position: 'top'
                },
                scales: {
                    yAxes: [{
                        stacked: true
                    }]
                }
        }
    });
});
