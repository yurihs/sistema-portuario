def register_template_filters(app):
    @app.template_filter()
    def extract(item, container):
        value = container[item]
        return value

