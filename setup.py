from setuptools import setup, find_packages

version = '1.2.0'

setup(
    name='ckanext-scheming',
    version=version,
    description="Easy, sharable custom CKAN schemas",
    keywords='ckan',
    author='Government of Canada',
    author_email='ian@excess.org',
    url='https://github.com/ckan/ckanext-scheming',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyyaml',
        'ckanapi',
        'ckantoolkit>=0.0.2',
        'pytz'
    ],
    entry_points=\
    """
    [ckan.plugins]
    scheming_datasets=ckanext.scheming.plugins:SchemingDatasetsPlugin
    scheming_groups=ckanext.scheming.plugins:SchemingGroupsPlugin
    scheming_organizations=ckanext.scheming.plugins:SchemingOrganizationsPlugin
    """,
)
