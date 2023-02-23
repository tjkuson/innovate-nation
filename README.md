# Innovate-Nation
[![CMake Badge](https://img.shields.io/github/actions/workflow/status/tjkuson/innovate-nation/ci.yml?branch=main)](https://github.com/tjkuson/innovate-nation/actions/workflows/ci.yml)

Event :Xander Hackathon
--------------------------------------
## Project Objective
The project basically cleans a dataset which can be a CSV, JSON or XML file and transform it into the desired output file format. 
## Creating the dataset through Webscraping
- Import the necessary libraries.
- Choose a website to scrape.
- Create a function to accept cookies.
- Identify the data you want to scrape.
- Create functions to scrape the selected data.
- Create function to save the data in a local file.
- For this project the created file is CSV.
## Data Cleaning and Transformation
- Import the necessary libraries.
- Read the file and check if the filepath exists.
- Reads the file into a dataframe.
- Check for null values in the dataset.
- Ask an input from the user as to how he wants to handle the missing data. 
- The user can replace the NULL with:
    * A new value.
    * The mean of the column.
    * The median of the column.
    * The mode of the column.
    * A zero
    * Drop the entire column if the Missing value ratio exceeds the user inputted ratio.
- Seperate functions are created for each of these cases.
-   Necessary exception handling while
    * Replacing the Null with a new value from the user.
    * Validating the user inputted ratio.
- Write the dataframe into the desired file format. 
    
# Usage

To run cleaner module, ensure you have the required dependencies installed. Then run the following command:

```bash
python3 -m cleaner
```

