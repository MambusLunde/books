from setuptools import setup, find_packages

setup(name="books",
      version="0.1.0",
      description="Just having fun scraping",
      author="Mats Lunde",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="immambus@gmail.com",
      )