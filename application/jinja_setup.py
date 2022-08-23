import jinja2


def setup_jinja():

    multi_loader = jinja2.ChoiceLoader(
        [
            jinja2.FileSystemLoader(searchpath="./templates"),
            jinja2.PrefixLoader(
                {
                    "colmjude-frontend": jinja2.PackageLoader("colmjude_frontend"),
                }
            ),
        ]
    )
    return jinja2.Environment(loader=multi_loader)
