"""Creates a HTML project folder and populates it with boilerplate
   files and folders."""
import os
import shutil
import subprocess

import isort  # noqa: F401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
def project_builder():
    """Creates some folders with os and copies the rest with shutil."""
    folder_name = input("What is the name of your project? ")
    folder = f"/usr/share/nginx/html/{folder_name}"

    os.mkdir(f"{folder}")
    os.mkdir(f"{folder}/actions")
    os.mkdir(f"{folder}/forms")
    os.mkdir(f"{folder}/pages")
    os.mkdir(f"{folder}/support_files")

    shutil.copy("/usr/share/nginx/html/html5_boilerplate/browserconfig.xml", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/.editorconfig", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/favicon-16x16.png", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/favicon-32x32.png", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/favicon.ico", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/LICENSE.txt", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/package.json", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/package-lock.json", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/robots.txt", folder)
    shutil.copy("/usr/share/nginx/html/html5_boilerplate/site.webmanifest", folder)

    shutil.copytree("/usr/share/nginx/html/html5_boilerplate/css", f"{folder}/css")
    shutil.copytree("/usr/share/nginx/html/support_services/template_python_files", f"{folder}/support_files")
    shutil.copytree("/usr/share/nginx/html/html5_boilerplate/js", f"{folder}/support_files/js")
    shutil.copytree("/usr/share/nginx/html/support_services/partials", f"{folder}/partials")


if __name__ == "__main__":
    project_builder()
