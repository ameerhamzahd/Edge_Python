from setuptools import setup, find_packages

setup(
    name="count_letters_package",                      # Project name
    version="1.0.0",                      # Version number
    packages=find_packages(),             # Automatically include all packages
    description="A package for counting specific letters in text.",      # Short description
    author="Ameer Hamzah Daiyan",                   # Your name
    author_email="ameerhamzah.daiyan@gmail.com",# Your email
        # URL of your project/repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',              # Minimum Python version
)
