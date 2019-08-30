var fs = require('fs');

fs.existsSync("dist") || fs.mkdirSync("dist");
fs.existsSync("dist/static") || fs.mkdirSync("dist/static");
fs.copyFileSync('node_modules/jquery/dist/jquery.js', 'dist/jquery.js');
fs.copyFileSync('node_modules/bootstrap/dist/css/bootstrap.css', 'dist/bootstrap.css');
fs.copyFileSync('node_modules/bootstrap/dist/js/bootstrap.bundle.js', 'dist/bootstrap.bundle.js');
fs.copyFileSync('node_modules/feather-icons/dist/feather.js', 'dist/feather.js');
fs.copyFileSync('node_modules/cleave.js/dist/cleave.js', 'dist/cleave.js');
fs.copyFileSync('node_modules/chart.js/dist/Chart.js', 'dist/chart.js');
fs.copyFileSync('node_modules/typeface-signika/files/signika-latin-700.woff', 'dist/static/signika-bold.woff');
fs.copyFileSync('node_modules/typeface-signika/files/signika-latin-700.woff2', 'dist/static/signika-bold.woff2');
fs.copyFileSync('node_modules/flatpickr/dist/flatpickr.js', 'dist/flatpickr.js');
fs.copyFileSync('node_modules/flatpickr/dist/l10n/pt.js', 'dist/flatpickr-pt.js');
fs.copyFileSync('node_modules/flatpickr/dist/flatpickr.css', 'dist/flatpickr.css');
