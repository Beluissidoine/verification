from setuptools import setup, find_packages


setup(
    name="verification",
    version="0.0.1",
    author="Ghislain Beluis",
    author_email="ghislainbella3@gmail.com",
    url="https://github.com/Beluissidoine/verification",
    description="C'est un package qui verifie la saisie des utilisateurs que se soit les nombres ou les lettres elle permet aussi de verifié que l'utilisateur a entrer la valeur demander",
    packages=find_packages(),
    readme="README.md",
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
)
