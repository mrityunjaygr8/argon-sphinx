from setuptools import setup


setup(
    name="",
    package_data={("sphinx_argon"): [
        "theme.conf",
        "*.html",
        "static/css/*.css"
    ]},
    include_package_data=True,
    entry_points={
        "sphinx.html_themes": [
            "sphinx_argon = sphinx_argon"
        ]
    }
)
