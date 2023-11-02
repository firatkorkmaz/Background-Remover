# Background Remover
A simple program to remove background from multiple images by using the **rembg** library.

## General Information
This program removes background from images by asking the user to enter either image filename(s) or image folder name from the input and saves the new images in (.png) format.

<img title="Car with BG" src="https://github.com/firatkorkmaz/Background-Remover/blob/main/car.jpg" width=400> <img title="Car without BG" src="https://github.com/firatkorkmaz/Background-Remover/blob/main/car_rembg.png" width=400>

<img title="Cat with BG" src="https://github.com/firatkorkmaz/Background-Remover/blob/main/cat.png" width=400> <img title="Cat without BG" src="https://github.com/firatkorkmaz/Background-Remover/blob/main/cat_rembg.png" width=400>

## Technologies
This project is created with:
* Python
* Jupyter Notebook

## Setup & Run
Although an automatic installation command is placed in the source code for the **rembg** library, it can also be manually installed by:
```
pip install rembg
```
There are 2 different files to run the program in different ways:
1. **Remove_Background.ipynb** can be run with Jupyter Notebook:
```
pip install jupyter
```
```
jupyter notebook
```
2. **Remove_Background.py** can be run directly with Python:
```
python Remove_Background.py
```
There are also 2 different images given as input file examples: **car.jpg**, **cat.png** with their saved results: **car_rembg.png**, **cat_rembg.png**
