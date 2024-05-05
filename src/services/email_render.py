from jinja2 import Environment, select_autoescape, FileSystemLoader

from utils.consts import TEMPLATES_PATH


class HTMLEmailRender:
    def __init__(self, username: str, url: str):
        self.username = username
        self.url = url

    def render(self, template_name: str) -> str:
        env = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH),
        autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template(f'{template_name}.html')
        html = template.render(
            url=self.url,
            username=self.username
        )

        return html
    