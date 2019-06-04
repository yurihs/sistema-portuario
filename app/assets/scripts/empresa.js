$(function() {
    new Cleave('input[name=cnpj]', {
        delimiters: ['.', '.', '/', '-'],
        blocks: [2, 3, 3, 4, 2],
        uppercase: true
    });
});
