import setuptools

setuptools.setup(
    name="url_shortener_app",
    version="0.0.1",
    author="Aleksey Podkidyshev",
    author_email="podkidyshev.as@phystech.edu",
    description="A small fastapi server package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)