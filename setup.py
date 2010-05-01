from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.collage.blogging',
      version=version,
      description="A collective.blogging integration for Products.Collage.",
      long_description=open(os.path.join("collective", "collage", "blogging", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Davi Lima',
      author_email='davilima6@gmail.com',
      url='http://plone.org/products/collective.collage.blogging',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.collage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.autoinclude',  # Required for Plone 3.2 compatibility
          'Products.Collage',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
