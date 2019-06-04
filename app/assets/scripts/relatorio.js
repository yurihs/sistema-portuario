$(function (){
    Chart.defaults.global.layout.padding.top = 20;
    Chart.defaults.global.title.display = true;
    Chart.defaults.global.title.fontSize = 18;
    Chart.defaults.global.title.fontColor = 'rgb(33, 37, 41)';
    Chart.defaults.global.title.position = 'top';

    // Comum entre relatórios
    // ======================

    const canvasTipoDeCargaPorQuantidade = document.getElementById('graficoTipoDeCargaPorQuantidade');
    if (canvasTipoDeCargaPorQuantidade) {
        new Chart(
            canvasTipoDeCargaPorQuantidade.getContext('2d'),
            {
                type: 'doughnut',
                data: dadosTipoDeCargaPorQuantidade,
                options: {
                    title: {
                        text: 'Quantidades de tipos de carga'
                    }
                }
            }
        );
    }

    // Relatório geral
    // ===============

    const canvasEmpresaPorNumeroDeViagens = document.getElementById('graficoEmpresaPorNumeroDeViagens');
    if (canvasEmpresaPorNumeroDeViagens) {
        new Chart(
            canvasEmpresaPorNumeroDeViagens.getContext('2d'),
            {
                type: 'horizontalBar',
                data: dadosEmpresaPorNumeroDeViagens,
                options: {
                    title: {
                        text: 'Viagens por empresa',
                    },
                    legend: {
                        display: false
                    }
                }
            });
    }
    const canvasEmpresaPorTipoDeCarga = document.getElementById('graficoEmpresaPorTipoDeCarga');
    if (canvasEmpresaPorTipoDeCarga) {
        new Chart(
            canvasEmpresaPorTipoDeCarga.getContext('2d'),
            {
                type: 'horizontalBar',
                data: dadosEmpresaPorTipoDeCarga,
                options: {
                    title: {
                        text: 'Tipos de carga por empresa'
                    },
                    scales: {
                        yAxes: [{
                            stacked: true
                        }]
                    }
                }
            });
    }

    // Relatório específico
    // ====================

    const canvasNavioPorNumeroDeViagens = document.getElementById('graficoNavioPorNumeroDeViagens');
    if (canvasNavioPorNumeroDeViagens) {
        new Chart(
            canvasNavioPorNumeroDeViagens.getContext('2d'),
            {
                type: 'horizontalBar',
                data: dadosNavioPorNumeroDeViagens,
                options: {
                    title: {
                        text: 'Viagens por navio',
                    },
                    legend: {
                        display: false
                    }
                }
            });
    }
    const canvasNavioPorTipoDeCarga = document.getElementById('graficoNavioPorTipoDeCarga');
    if (canvasNavioPorTipoDeCarga) {
        new Chart(
            canvasNavioPorTipoDeCarga.getContext('2d'),
            {
                type: 'horizontalBar',
                data: dadosNavioPorTipoDeCarga,
                options: {
                    title: {
                        text: 'Tipos de carga por navio'
                    },
                    scales: {
                        yAxes: [{
                            stacked: true
                        }]
                    }
                }
            });
    }


});
