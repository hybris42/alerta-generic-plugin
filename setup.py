from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="alerta-generic-plugin",
    version=version,
    description='Alerta generic plugin',
    packages=find_packages(),
    py_modules=['alerta_generic_plugin'],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'genericplugin = alerta_generic_plugin:AlertaGenericPlugin'
        ]
    }
)
