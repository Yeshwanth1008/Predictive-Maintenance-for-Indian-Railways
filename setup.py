from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="predictive-maintenance-indian-railways",
    version="1.0.0",
    author="Yeshwanth1008",
    author_email="your.email@example.com",
    description="Predictive Maintenance System for Indian Railways",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yeshwanth1008/Predictive-Maintenance-for-Indian-Railways",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="predictive maintenance, machine learning, railways, anomaly detection, time series",
    project_urls={
        "Bug Reports": "https://github.com/Yeshwanth1008/Predictive-Maintenance-for-Indian-Railways/issues",
        "Source": "https://github.com/Yeshwanth1008/Predictive-Maintenance-for-Indian-Railways",
        "Documentation": "https://github.com/Yeshwanth1008/Predictive-Maintenance-for-Indian-Railways/blob/main/README.md",
    },
)
