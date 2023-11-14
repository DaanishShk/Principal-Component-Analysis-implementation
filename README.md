# Principal Component Analysis implementation

The project is a tool to perform Principal Component Analysis (PCA) to get the eigen values and eigen vectors. This implementation utilizes the QR algorithm.

[![Python][python]](#)
[![Numpy][numpy]](#)
[![Pandas][pandas]](#)


## Description

The project is a standalone desktop application written in python. Numpy is used so that the data is stored in an array-like format instead of a list of references to boost the speed of execution. Pandas is used to retrieve and store data from external files which are excel sheets for this project.

The code for PCA was written without the use of the built-in libraries in sklearn (only used for cross verification of the results). 

Following are the steps involved in reaching the result:

1. The data is first standardised after determining the mean and standard deviation of the dataset so that all variables have equal contribution to the analysis. 
2. Then the covariance matrix of the standardised data is computed upon which the QR algorithm is applied. 
3. Using the Eigen values, the respective Eigen vectors are calculated through the process of Gaussian elimination. The dataset and Eigen vector matrix are multiplied to produce the required end result. 
4. The number of components in the matrix is determined by the percent variance distribution the user desires.

After opening the application, the user first needs to load the data. Clicking on ‘Excel File’ and choose the location of the excel sheet. Then pressing the ‘Execute’ button performs PCA and displays the results in the large text box. 

The information displayed depends on what options have been checked in the menu. The number of components is decided by the scaling widget present at the bottom of the side menu.

The results of the last execution are temporarily stored until the next PCA is performed. If the user wants to save the data first, he can do so by clicking on the ‘Save’ button, then selecting the location and file name. This saves a multi-sheet excel file that contains the resultant data, Eigen values, Eigen vectors and the variance ratios of each component.


## Built with

The following technologies were used for development:
1. [Numpy](https://numpy.org/) - support for multi-dimensional arrays and matrices
2. [Pandas](https://pandas.pydata.org/) - library for data manipulation and analysis

## Getting Started
For building and running the application you need:

- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/) or higher

### Running the application locally

Create a new virtual environment for the project. Install the dependencies given in the  `requirements.txt` file using the following command: 
```
pip install -r requirements.txt
```

Execute the python script using the following command:
```shell
python Principal_Component_Analysis.py
```
A jupyter notebook is also provided for the algorithm along with the sample data used in file `Test.xlsx` .

## Author

Daanish Shaikh - [@github](https://github.com/DaanishShk)\
repo link - [Principal-Component-Analysis-implementation](https://github.com/DaanishShk/Principal-Component-Analysis-implementation)


## License

This project is licensed under the MIT License.

[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white


<!-- ## INTRODUCTION

The project aims to offer the user an easy method of performing PCA on the data they have recorded using the Eigen vectors of the data set so that further analysis becomes easier. After selecting the excel file a simple click of the execute button produces the intended result which can be saved at any location.

 -->

 <!-- 3. The covariance matrix thus converges to an upper triangular matrix whose diagonal elements are nothing but the Eigen values of the principal components.  -->