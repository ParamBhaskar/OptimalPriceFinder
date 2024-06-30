<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">OPTIMALPRICEFINDER</h1>
</p>
<p align="center">
    <em>Find the best prices online!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/ParamBhaskar/OptimalPriceFinder?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ParamBhaskar/OptimalPriceFinder?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ParamBhaskar/OptimalPriceFinder?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ParamBhaskar/OptimalPriceFinder?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#features)
> - [ Repository Structure](#repository-structure)
> - [ Getting Started](#getting-started)
>   - [ Installation](#installation)
>   - [ Running OptimalPriceFinder](#running-OptimalPriceFinder)
>   - [ Screenshots](#screenshots)
> - [ Contributing](#contributing)

---

##  Overview

OptimalPriceFinder is a web application designed to compare prices of products from various e-commerce websites in real-time. It uses web scraping techniques to fetch prices and displays the optimal options to users.

---

##  Features

- Intelligent web scraping with Beautiful Soup to fetch and compare prices.
- Backend powered by Django, integrating seamlessly with a visually engaging frontend.
- Highly intuitive user interface providing real-time and precise results.
- Utilizes scrapingdog for proxies and user agents to scrape different e-commerce websites flawlessly.

---

##  Repository Structure

```sh
└── OptimalPriceFinder/
    ├── PSV
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── settings.cpython-310.pyc
    │   │   ├── settings.cpython-39.pyc
    │   │   ├── urls.cpython-310.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   ├── views.cpython-310.pyc
    │   │   ├── views.cpython-39.pyc
    │   │   ├── wsgi.cpython-310.pyc
    │   │   └── wsgi.cpython-39.pyc
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── views.py
    │   └── wsgi.py
    ├── amazon
    │   ├── amazon
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── __init__.cpython-39.pyc
    │   │   │   ├── items.cpython-310.pyc
    │   │   │   ├── items.cpython-39.pyc
    │   │   │   ├── settings.cpython-310.pyc
    │   │   │   └── settings.cpython-39.pyc
    │   │   ├── items.py
    │   │   ├── middlewares.py
    │   │   ├── pipelines.py
    │   │   ├── settings.py
    │   │   └── spiders
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   ├── __init__.cpython-310.pyc
    │   │       │   ├── __init__.cpython-39.pyc
    │   │       │   ├── amazon_search.cpython-310.pyc
    │   │       │   └── amazon_search.cpython-39.pyc
    │   │       ├── amazon_search.py
    │   │       ├── amazont.json
    │   │       └── data
    │   │           └── amazon_search_2023-06-20T00-58-08.csv
    │   └── scrapy.cfg
    ├── db.sqlite3
    ├── manage.py
    ├── media
    │   ├── bg.jpeg
    │   ├── dragon.ico
    │   └── logo.jpeg
    ├── pr_com
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── admin.cpython-310.pyc
    │   │   ├── admin.cpython-39.pyc
    │   │   ├── apps.cpython-310.pyc
    │   │   ├── apps.cpython-39.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── urls.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_product_unique_id.py
    │   │   ├── 0003_gostring.py
    │   │   ├── 0004_remove_product_feature_bullets_remove_product_image_and_more.py
    │   │   ├── 0005_product_onlinestore_product_product_url.py
    │   │   ├── 0006_contacted_user_delete_gostring.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-310.pyc
    │   │       ├── 0001_initial.cpython-39.pyc
    │   │       ├── 0002_product_unique_id.cpython-310.pyc
    │   │       ├── 0002_product_unique_id.cpython-39.pyc
    │   │       ├── 0003_gostring.cpython-310.pyc
    │   │       ├── 0004_remove_product_feature_bullets_remove_product_image_and_more.cpython-310.pyc
    │   │       ├── 0005_product_onlinestore_product_product_url.cpython-310.pyc
    │   │       ├── 0006_contacted_user_delete_gostring.cpython-310.pyc
    │   │       ├── __init__.cpython-310.pyc
    │   │       └── __init__.cpython-39.pyc
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── templates
        ├── cart.html
        ├── cartdisplay.html
        ├── clothes.html
        ├── electronics.html
        ├── food.html
        ├── furniture.html
        ├── index.html
        ├── index2.html
        ├── index3.html
        └── productDisplay.html
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `at least version 3`

###  Installation

1. Clone the OptimalPriceFinder repository:

```sh
git clone https://github.com/ParamBhaskar/OptimalPriceFinder
```

2. Change to the project directory:

```sh
cd OptimalPriceFinder
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running OptimalPriceFinder

Use the following command to run OptimalPriceFinder:

```sh
python manage.py runserver
```

###  Screenshots

1. HomePage
![image](https://github.com/ParamBhaskar/OptimalPriceFinder/assets/108367037/cfe68f04-4b07-4831-bea7-7015999d2ed6)

2. Electronics page
![image](https://github.com/ParamBhaskar/OptimalPriceFinder/assets/108367037/fd04c428-79d0-4031-b057-372d13c7a604)

3. Selecting Requirements/Preferences
![image](https://github.com/ParamBhaskar/OptimalPriceFinder/assets/108367037/b655a042-762e-4e55-a19e-60a1cb35cee2)

4. Showing Optimal Prices Result
![Screenshot from 2024-06-30 23-47-12](https://github.com/ParamBhaskar/OptimalPriceFinder/assets/108367037/3163edf0-4c1c-4d34-8478-7f556701d879)

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/ParamBhaskar/OptimalPriceFinder/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/ParamBhaskar/OptimalPriceFinder/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/ParamBhaskar/OptimalPriceFinder/issues)**: Submit bugs found or log feature requests for Optimalpricefinder.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/ParamBhaskar/OptimalPriceFinder
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>
---

[**Return**](#quick-links)

---
