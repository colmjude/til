import jinja2
from config import Config

from application.jinja_filters import generate_tag_url, format_timestamp_to_date


config = Config()


def create_jinja_env():
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


def register_globals(env):
    env.globals["current_year"] = config.CURRENT_YEAR


def register_filters(env):
    env.filters["tag_url"] = generate_tag_url
    env.filters["timestamp_to_date"] = format_timestamp_to_date


def setup_jinja():
    env = create_jinja_env()
    register_globals(env)
    register_filters(env)
    return env
