$(function () {
    var cleaveCPF = new Cleave('input[name=cpf]', {
        delimiters: ['.', '.', '-'],
        blocks: [3, 3, 3, 2],
        uppercase: true
    });
});
