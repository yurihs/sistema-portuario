var fs = require('fs');

fs.existsSync("dist") || fs.mkdirSync("dist");
fs.copyFileSync('node_modules/jquery/dist/jquery.js', 'dist/jquery.js');
fs.copyFileSync('node_modules/bootstrap/dist/css/bootstrap.css', 'dist/bootstrap.css');
fs.copyFileSync('node_modules/bootstrap/dist/js/bootstrap.bundle.js', 'dist/bootstrap.bundle.js');
