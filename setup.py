from setuptools import setup, find_packages
setup(
    name = "weatherGov",
    version = "0.1.0",
    packages = find_packages(),
    scripts = ['weatherGov/main.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['requests>=2.10.0', 'googlemaps>=2.4.4', 'defusedxml>=0.4.1'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the weatherGov package, too:
        'weatherGov': ['*.msg'],
    },

    # metadata for upload to PyPi
    author = "Charles Keith Brown",
    author_email = "charles.k.brown@gmail.com",
    description = "weatherGov is a simple wrapper to grab weather data from forecast.weather.gov for a given latitude and longitude derived through google's geocode API (key required)",
    license = "MIT",
    keywords = "weatherGov Weather WeatherGov",
    url = "https://www.github.com/cixelsydcb/weatherGov",

)
