var fs = require('fs');

fs.existsSync("dist") || fs.mkdirSync("dist");
fs.copyFileSync('node_modules/jquery/dist/jquery.js', 'dist/jquery.js');
fs.copyFileSync('node_modules/bootstrap/dist/css/bootstrap.css', 'dist/bootstrap.css');
fs.copyFileSync('node_modules/bootstrap/dist/js/bootstrap.bundle.js', 'dist/bootstrap.bundle.js');
fs.copyFileSync('node_modules/feather-icons/dist/feather.js', 'dist/feather.js');
fs.copyFileSync('node_modules/cleave.js/dist/cleave.js', 'dist/cleave.js');
fs.copyFileSync('node_modules/chart.js/dist/Chart.js', 'dist/chart.js');
