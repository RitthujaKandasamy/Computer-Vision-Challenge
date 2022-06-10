# What is Sudoku?

Sudoku is a combinational number-placement puzzle. The objective of sudoku is to fill a 9×9 grid with some digits in such a way so that each column, row, and nine 3×3 subgrids contain all of the digits from 0-9.

In sudoku, the algorithm will put a number in an empty space and then move on to the next empty space, if anywhere some criteria fail then it will turn back to some previous solutions and changes it according to the criteria. It continues until it finds a final solution that matches all the criteria.

![sudoku](https://user-images.githubusercontent.com/99767517/173079264-58980e28-bb7c-45ab-9944-eb3da718168a.png)


### Some Requirement to predict Sudoku in opencv

<details>
<summary>Window</summary>



|     Vision      |         Instructions                                                                 |        
| --------------- | ------------------------------------- |
|      3.9        | <a href="https://pypi.org/project/opencv-python/">To install opencv-python</a>       |
| [conda-forge]   | `conda install -c conda-forge zoxide` |
| [Homebrew]      | `brew install zoxide`                 |
| [MacPorts]      |                   |        


</details>

Python = version 3.9
openCV = version 4.5.5
Numpy = version 1.22
Matplotlib = version 3.5
