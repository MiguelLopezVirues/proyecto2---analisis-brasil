# 📊 EDA - Public Revenue in Brazil
<div style="text-align: center;">
  <img src="assets/brazil-tax-overview.jpg" alt="portada" />
</div>

## 📝 Project Overview

The government of Brazil manages public revenue collection to finance services and projects that benefit society. However, actual revenue collection often differs from what was forecasted due to factors such as tax evasion and economic fluctuations.

This project aims to analyze historical revenue execution data from 2013 to 2021, identify patterns and problem areas, and propose recommendations to improve the accuracy of forecasts and the efficiency of revenue collection.

The issues to address include:

1. Discrepancies between forecasted and actual revenue.
2. Temporal evolution of revenue collection.
3. Performance by agency and managing unit.

## 📁 Project Structure

```bash
Proyecto2-EDA-Ingresos-Publicos-Brasil/
├── data/                # Raw and processed data
│   ├── cleaned_data.parquet
│   ├── concatenated_data.parquet
│   ├── datos-2013.csv
│   ├── datos-2014.csv
│   ├── datos-2015.csv
│   ├── datos-2016.csv
│   ├── datos-2017.csv
│   ├── datos-2018.csv
│   ├── datos-2019.csv
│   ├── datos-2020.csv
│   ├── datos-2021.csv
│   ├── diccionario_datos.csv
│   └── diccionario_datos.txt
├── notebooks/           # Jupyter notebooks with the analysis
│   ├── cleaning.ipynb
│   └── exploration.ipynb
├── src/                 # Processing and analysis scripts
│   └── support_cleaning.py
├── Pipfile              # Dependency management file
├── Pipfile.lock         # Lockfile for exact versions of dependencies
└── README.md            # Project documentation (this file)
```
## 🛠️ Installation and Requirements
This project requires the following tools and libraries:

Python 3.8+
pandas
numpy
matplotlib
seaborn
scikit-learn

**Documentation Links:**  
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)  
- [pandas Documentation](https://pandas.pydata.org/)  
- [NumPy Documentation](https://numpy.org/)  
- [Matplotlib Documentation](https://matplotlib.org/)  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  

#### Setting up the Environment with Pipenv

Clone this repository by going to the desired folder with you command line and cloning the environment:
```bash
git clone https://github.com/MiguelLopezVirues/proyecto2---analisis-brasil
```

To replicate the project's environment, you can use Pipenv with the included ``Pipfile.lock``:
```bash
pipenv install
pipenv shell  
```

Alternatively, install the dependencies from ``requirements.txt``:
```bash
pip install -r requirements.txt  
```

## 📊 Results and Conclusions
Check ``exploration.ipynb`` notebook for conclusions and recommendations.

## 🔄 Next Steps

- Polish ``fill_categories_forward_backward_massive()`` to fill in categorical NaNs.
- Analyse patterns in missing values to potentially uncover insights about unprofessional public revenue management.
- Explore advanced techniques for future revenue projections.

## 🤝 Contributions
Contributions are welcome. If you wish to improve the project, open a pull request or an issue.

## ✒️ Authors
Miguel López Virués - [GitHub Profile](https://github.com/MiguelLopezVirues)  


## 📜 License

This project is licensed under the MIT License.
