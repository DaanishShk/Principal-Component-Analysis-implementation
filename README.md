# Principal Component Analysis implementation
As my semester project I tried to code the process for Principal Component Analysis (PCA) utilizing the QR algorithm to get the eigen values and then the eigen vectors using numpy and pandas (not the built-in function in linalg). The program is slower than the built-in function but gives an almost identical result.

## INTRODUCTION

The project aims to offer the user an easy method of performing PCA on the data they have recorded using the Eigen vectors of the data set so that further analysis becomes easier. After selecting the excel file a simple click of the execute button produces the intended result which can be saved at any location.

## IMPLEMENTATION DETAILS

The project is a standalone desktop application entirely written in python. The important libraries used are numpy, pandas and tkinter. Numpy is used so that the data is stored in an array-like format instead of a list of references to boost the speed of execution whereas Pandas is used to retrieve and store data from external files which are excel sheets for this project.

The code for PCA was written without the use of the built-in libraries in sklearn (only used for cross verification of the results). The data is first standardised after determining the mean and standard deviation of the dataset so that all variables have equal contribution to the analysis. Then the covariance matrix of the standardised data is computed upon which the QR algorithm is applied.

The covariance matrix thus converges to an upper triangular matrix whose diagonal elements are nothing but the Eigen values of the principal components. Using these Eigen values, the respective Eigen vectors are calculated through the process of Gaussian elimination. Now that we know the Eigen vectors of the dataset, the dataset and Eigen vector matrix are multiplied to produce the required end result. The number of components in the matrix is determined by the percent variance distribution the user desires.

The UI of the application is also written in python using the library tkinter that comes pre-installed with the latest version of python. The code required to implement menus, dialog boxes, buttons and widgets was added to the program by importing the respective classes from the tkinter library.

After opening the application, the user first needs to load the data. Clicking on ‘Excel File’ and choosing the location gets this done. Then pressing the ‘Execute’ button performs PCA and displays the results in the large text box. The information displayed depends on what options have been checked in the menu. The number of components is decided by the scaling widget present at the bottom of the side menu.

The text widget can be cleared by pressing the ‘Clear’ button. The results of the last execution are temporarily stored until the next PCA is performed. If the user wants to save the data first, he can do so by clicking on the ‘Save’ button, then selecting the location and file name. This saves a multi-sheet excel file that contains the resultant data, Eigen values, Eigen vectors and the variance ratios of each component.

The size of the window is kept locked so that resizing does not warp the positioning of the widgets in the tkinter window. All buttons and check buttons either call a function or update the value of a variable specially defined for it. The ‘Information’ drop down can be accessed for quick help and developer info if needed.

The pandas library was used to read data from the excel sheet and store it in a data frame. 
