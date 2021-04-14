# frelabpy
This is our project for FRE Lab Fall 2020

Command lines

Extraction(absolute path):
```
-process "jiwu_extraction" -log "../" -mapping "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/JiWu_extraction_mapping.xlsx" -output "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/JiWu.csv" -input "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/JiWu_extraction_input.xlsx" -run_date "102120" -Trans_method " " -description "COURSE" -Trans_date "102120" 
```
Extraction(relative path):
```
-process "jiwu_extraction" -log "../" -mapping "../../../data/JiWu_extraction_mapping.xlsx" -output "../../../data/JiWu.csv" -input "../../../data/JiWu_extraction_input.xlsx" -run_date "102120" -Trans_method " " -description "COURSE" -Trans_date "102120" 
```

Transformation(absolute path):

```
-process "jiwu_transformation" -log "../" -output "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/JiWu_transformation_output_groupby.csv" -input "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/jiwu.csv" -Trans_date "102120" -mapping " " -run_date "102120" -description "COURSE" -Trans_method "groupby"
```

```
-process "jiwu_transformation" -log "../" -output "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/JiWu_transformation_output_pivot.csv" -input "C:/Users/JIWU5/OneDrive/Documents/NYU-2020-0903/6861-Python Lab/Project/frelabpy/data/jiwu.csv" -Trans_date "102120" -mapping " " -run_date "102120" -description "COURSE" -Trans_method "pivot"
```


Transformation(relative path):

```
-process "jiwu_transformation" -log "../" -output "../../../data/JiWu_transformation_output_groupby.csv" -input "../../../data/jiwu.csv" -Trans_date "102120" -mapping " " -run_date "102120" -description "COURSE" -Trans_method "groupby"
```

```
-process "jiwu_transformation" -log "../" -output "../../../data/JiWu_transformation_output_pivot.csv" -input "../../../data/jiwu.csv" -Trans_date "102120" -mapping " " -run_date "102120" -description "COURSE" -Trans_method "pivot"
```

1.Extraction:
Input:
	JiWu_extraction_input.csv
Mapping:
	JiWu_extraction_mapping.xlsx
Output:
	JiWu.csv

2.Transformation:
Input: 
	JiWu.csv
Output:
	JiWu_transformation_output.csv

groupby:[semester and course] for calculating the number of students who select the course
