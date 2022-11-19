from setuptools import setup, find_packages

def get_requirements(file):
    with open(file) as f:
        req = f.readlines()
    return [r.strip() for r in req]

setup(
    name="scr_package",
    version="0.0.2",
    # Otra opción es importar módulo a módulo en una lista: packages=['dmedina_package', 'dmedina_package.translator']
    packages=find_packages(),
    #python_requires='>=3.6',
    #install_requires=get_requirements('requirements.txt'),
)