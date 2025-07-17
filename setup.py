from setuptools import setup, find_packages

setup(
    name="radix-sort-visualizer",
    version="1.0.0",
    description="A visual educational tool for understanding the Radix Sort algorithm",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "radix-sort-visualizer=radixsortvisualizer:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
    ],
    include_package_data=True,
    zip_safe=False,
) 