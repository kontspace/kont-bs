from django import template
import mistune

register = template.Library()


def markdown(content):
    renderer = mistune.Renderer(escape=True, hard_wrap=True)
    markdown = mistune.Markdown(renderer=renderer)

    return markdown(content)

register.filter(markdown)