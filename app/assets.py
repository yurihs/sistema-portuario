from flask_assets import Bundle

app_css = Bundle(
    'app.css',
    output='styles/app.css'
)

app_js = Bundle(
    'app.js',
    'usuario.js',
    output='scripts/app.js'
)

vendor_css = Bundle(
    'bootstrap.css',
    output='styles/vendor.css'
)

vendor_js = Bundle(
    'jquery.js',
    'bootstrap.bundle.js',
    'feather.js',
    'cleave.js',
    filters=['rjsmin'],
    output='scripts/vendor.js'
)
