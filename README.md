# 🦠 Chile COVID-19 Mortality Analysis (2020-2024)

### 📃 Description:
This project focuses on analyzing **COVID-19** mortality data in **Chile** from **2020 to 2024**. With at least 60,000 records, the dataset provides critical insights into the impact of the pandemic on the population. 
<br>
The project leverages **Python** for data processing and analysis and **Google Sheets** for collaborative data exploration.

## 🎯 Key objectives

- Cleaning and organizing the mortality dataset for meaningful analysis.
- Exploring trends and patterns, such as mortality rates by region, age, or time.
- Visualizing data to communicate insights effectively.
- Building reproducible workflows for data analysis and reporting.

## 🗄️ Data Dictionary 

| Variable Name | Description                                     | Data Type | Values                        |
|-------------------------|---------------------------------------------------|-----------|-------------------------------|
| ANO_DEF | Year of the death date | Number | N/A |
| SEXO | Gloss identifying biological sex | Number | 1: Male, 2: Female, 9: Other |
| EDAD_TIPO | Unit of age measurement | Number | 1: Years, 2: Months, 3: Days |
| EDAD_CANT | Numerical record of the patient's age at admission| Number | N/A |
| CODIGO_COMUNA_RESIDENCIA | Code of the commune of residence of the deceased, according to the political-administrative division updated in 2019| Number | N/A |
| GLOSA_COMUNA_RESIDENCIA | Gloss of the commune of residence of the deceased, according to the political-administrative division updated in 2019 | Text | N/A |
| GLOSA_REG_RES | Gloss of the region of residence| Text | N/A |
| DIAG1 | Basic cause of death | Text | N/A |
| CAPITULO_DIAG1 | ICD-10 chapter according to the cause of death | Text | N/A |
| GLOSA_CAPITULO_DIAG1 | Gloss of the ICD-10 chapter according to the cause of death | Text | N/A |
| CODIGO_GRUPO_DIAG1 | Group code of the cause of death according to ICD-10 | Text | N/A |
| GLOSA_GRUPO_DIAG1 | Gloss of the group code of the cause of death according to ICD-10 | Text | N/A |
| CODIGO_CATEGORIA_DIAG1 | Category code of the cause of death according to ICD-10 | Text | N/A |
| CODIGO_SUBCATEGORIA_DIAG1 | Category code of the cause of death according to ICD-10 | Text | N/A |
| GLOSA_SUBCATEGORIA_DIAG1 | Gloss of the category code of the cause of death according to ICD-10 | Text | N/A |
| DIAG2 | External cause of death | Text | N/A |
| CAPITULO_DIAG2 | ICD-10 chapter according to the cause of death | Text | N/A |
| GLOSA_CAPITULO_DIAG2 | Gloss of the ICD-10 chapter according to the cause of death | Text | N/A |
| CODIGO_GRUPO_DIAG2 | Group code of the cause of death according to ICD-10 | Text | N/A |
| GLOSA_GRUPO_DIAG2 | Gloss of the group code of the cause of death according to ICD-10 | Text | N/A |
| CODIGO_CATEGORIA_DIAG2 | Category code of the cause of death according to ICD-10 | Text | N/A |
| GLOSA_CATEGORIA_DIAG2 | Gloss of the category code of the cause of death according to ICD-10 | Text |N/A |
| CODIGO_SUBCATEGORIA_DIAG2 | Category code of the cause of death according to ICD-10 | Text | N/A |
| GLOSA_SUBCATEGORIA_DIAG2 | Gloss of the category code of the cause of death according to ICD-10 | Text | N/A |
| LUGAR_DEFUNCION | Describes the place where the death occurs | Text | N/A |


<br>

## 🎖️ Acknowledgment
The data used in this project, including COVID-19 mortality records in Chile from 2020 to 2024, is provided by the Chilean government’s open data platform:
<br>
- [Defunciones por COVID19](https://datos.gob.cl/dataset/defunciones-por-covid19)

Special thanks to **Pamela Suarez** ***(deis@minsal.cl)*** for creating and curating the dataset. I acknowledge and appreciate her work in making this information publicly accessible.
<br>
<br>
I acknowledge and thank the Ministerio de salud and related governmental agencies for making this data publicly available.
