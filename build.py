import os
import jinja2

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

PAGES_DIR = os.path.join(PROJECT_PATH, 'templates/pages')
OUTPUT_DIR = os.path.join(PROJECT_PATH)


def build_site(pages_dir, output_dir):

    template_path = os.path.join(PROJECT_PATH, 'templates')
    template_loader = jinja2.FileSystemLoader(searchpath=template_path)
    template_env = jinja2.Environment( loader=template_loader)

    for dirpath, _, files in os.walk(pages_dir):
        for page in files:
            relative_dirpath = os.path.relpath(dirpath, pages_dir)
            relative_path = os.path.join(relative_dirpath, page)
            template_path = 'pages/' + relative_path
            print 'building: {}'.format(relative_path)
            page_template = template_env.get_template(template_path)
            template_vars = {
            }
            page_text = page_template.render(template_vars)

            output_page_path = os.path.join(output_dir, relative_path)
            output_dirpath = os.path.dirname(output_page_path)
            if not os.path.exists(output_dirpath):
                os.makedirs(output_dirpath)
            with open(output_page_path, 'w') as output_file:
                output_file.write(page_text)


if __name__ == '__main__':
    build_site(pages_dir=PAGES_DIR, output_dir=OUTPUT_DIR)
