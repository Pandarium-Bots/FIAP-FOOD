

// Fazendo a solicitação GET usando fetch
async function chamada_api(apiUrl) {

    return await fetch(apiUrl)
        .then(response => {
            // Verificar se a resposta da solicitação é bem-sucedida (status 200)
            if (!response.ok) {
                throw new Error('Erro na solicitação: ' + response.status);
            }
            // Parse a resposta JSON
            return response.json();
            
        })
        .then(data => {
            // Faça algo com os dados recuperados
            console.log(data);
            return data.percent;
        })
        .catch(error => {
            // Lidar com erros
            console.error('Ocorreu um erro:', error);
        });

};


async function percentil() {
    const apiUrl = '/new_js_percent';
    var percentil = await chamada_api(apiUrl);
    console.log(percentil)
    return percentil;
};



$(document).ready( async function () {



    var options = {
        series: [
            {
                name: "Mysql",
                data: [28, 29, 33, 36, 32, 32, 33]
            },
            {
                name: "PostgreSql",
                data: [12, 11, 14, 18, 17, 13, 13]
            },
            {
                name: "Aurora",
                data: [33, 42, 14, 51, 33, 71, 13]
            },
            {
                name: "Neptune",
                data: [17, 34, 22, 18, 28, 13, 2]
            }
        ],
        chart: {
            height: 350,
            type: 'line',
            dropShadow: {
                enabled: true,
                color: '#000',
                top: 18,
                left: 7,
                blur: 10,
                opacity: 0.2
            },
            toolbar: {
                show: false
            }
        },
        colors: ['#383838', '#66DA26','#040fb0','#a83523'],
        dataLabels: {
            enabled: true,
        },
        stroke: {
            curve: 'smooth'
        },
        title: {
            text: 'Quantidade de instancias ao longo do tempo',
            align: 'left',
            style: {
                fontSize: '14px',
                fontWeight: 'bold',
                fontFamily: undefined
            },

        },
        grid: {
            borderColor: '#e7e7e7',
            row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
            },
        },
        markers: {
            size: 3
        },
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            labels: {
                style: {
                    // colors: '#ffffff'
                }
            },
            title: {
                text: 'Month',
                style: {
                    // color: '#ffffff'
                },
            }
        },
        legend: {
            position: 'top',
            horizontalAlign: 'right',
            floating: true,
            offsetY: -25,
            offsetX: -5
        }
    };

    var chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();

    var chart_2 = new ApexCharts(document.querySelector("#chart_2"), options);
    chart_2.render();

    var chart_3 = new ApexCharts(document.querySelector("#chart_3"), options);
    chart_3.render();

    var chart_4 = new ApexCharts(document.querySelector("#chart_4"), options);
    chart_4.render();

    var jubileu = await percentil();
    console.log(jubileu)


    var options = {
        series: [jubileu],
        chart: {
            height: 350,
            type: 'radialBar',
            toolbar: {
                show: true
            }
        },
        title: {
            text: '% Bancos com Certificado RDS_CA_2019',
            align: 'center',
            fontWeight: 'bold',
            color: '#050001',
        },
        plotOptions: {
            radialBar: {
                startAngle: -135,
                endAngle: 225,
                hollow: {
                    margin: 0,
                    size: '70%',
                    background: '#fff',
                    image: undefined,
                    imageOffsetX: 0,
                    imageOffsetY: 0,
                    position: 'front',
                    dropShadow: {
                        enabled: true,
                        top: 3,
                        left: 0,
                        blur: 4,
                        opacity: 0.24
                    }
                },
                track: {
                    background: '#fff',
                    strokeWidth: '67%',
                    margin: 0, // margin is in pixels
                    dropShadow: {
                        enabled: true,
                        top: -3,
                        left: 0,
                        blur: 4,
                        opacity: 0.35
                    }
                },

                dataLabels: {
                    show: true,
                    name: {
                        offsetY: -10,
                        show: true,
                        color: '#888',
                        fontSize: '17px'
                    },
                    value: {
                        formatter: function (val) {
                            return parseInt(val);
                        },
                        color: '#111',
                        fontSize: '36px',
                        show: true,
                    }
                }
            }
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: 'horizontal',
                shadeIntensity: 0.5,
                gradientToColors: ['#a8071f'],
                inverseColors: false,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 70]
            }
        },
        stroke: {
            lineCap: 'round'
        },
        labels: ['Percent'],
    };

    var chart_semi_circle = new ApexCharts(document.querySelector("#chart_semi_circle"), options);
    chart_semi_circle.render();

});

