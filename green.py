import os

sys.path.append(os.path.dirname(__file__))

import versioneer
here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

    "jsonschema",
    "numpy",
    "pooch",
    "pymatting",
    "scipy",
    "dev": [
        "imagehash",
        "pytest",
        "setuptools",
        "twine",
        "wheel",
    ],
    "gpu": ["onnxruntime-gpu"],
        "aiohttp",
        "click",
        "gradio",
        "uvicorn",
    ],

entry_points = {
    ],
}

setup(
    name="rembg",
    url="https://github.com/danielgatis/rembg",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="remove, background, u2net",
    packages=find_packages(),
    extras_require=extras_require,