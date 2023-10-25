
// // Fazendo a solicitação GET usando fetch
// function chamada_api(apiUrl) {
//     fetch(apiUrl)
//         .then(response => {
//             // Verificar se a resposta da solicitação é bem-sucedida (status 200)
//             if (!response.ok) {
//                 throw new Error('Erro na solicitação: ' + response.status);
//             }
//             // Parse a resposta JSON
//             return response.json();
//         })
//         .then(data => {
//             // Faça algo com os dados recuperados
//             console.log(data);
//         })
//         .catch(error => {
//             // Lidar com erros
//             console.error('Ocorreu um erro:', error);
//         });

// };

// function percentil() {
//     const apiUrl = '/new_js_percent';
//     chamada_api(apiUrl);
// };