var fs = require('fs');

fs.copyFileSync('node_modules/jquery/dist/jquery.js', 'app/assets/vendor/jquery.js');
fs.copyFileSync('node_modules/bootstrap/dist/css/bootstrap.css', 'app/assets/vendor/bootstrap.css');
fs.copyFileSync('node_modules/bootstrap/dist/js/bootstrap.bundle.js', 'app/assets/vendor/bootstrap.bundle.js');
