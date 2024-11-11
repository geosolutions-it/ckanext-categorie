from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='ckanext-categorie',
    version=version,
    description="Translates `group` into `categoria` in messages",
    long_description='''\
    ''',
    classifiers=[],
    keywords='',
    author='GeoSolutions SRL',
    author_email='info@geosolutionsgroup.com',
    url='https://github.com/geosolutions-it/ckanext-categorie',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''

    [ckan.plugins]
    categorie=ckanext.categorie.plugin:CategoriePlugin

    [babel.extractors]
    ckan = ckan.lib.extract:extract_ckan
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    },
)
