# Taller 3 de Algoritmos de clasificación

Andrés Mauricio Martínez Celis &nbsp;  &nbsp; &nbsp;     202322624 <br>
Danilo Andrés Alfonso Bohórquez  &nbsp;      201611827 <br>
Jairo Vladimir Chaparro Rodríguez     201531080 <br>
Oscar Duvan Giraldo Romero  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  202324939   <br>  

Estructura de carpetas:<br>
Taller3 <br>
├── Api<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── main.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── model.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── shapValues.py<br>
├── Archivos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── churn_historic.json<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── churn_future.json<br>
├── Models<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── DecisionTreeBest.joblib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Gxboost.joblib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── LogisticRegression.joblib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── NeuronalNewtwork.joblib<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── RandomForest.joblib<br>
├── Clasificacion_Churn.ipynb<br>
├── A/B_testing.ipynb<br>

### Api:
La api se construyo con FastAPI mediante codigo python, la Api maneja dos metodos POST, el primero es /{model_version}/predict en este metodo se puede variar entre 1 y 2, cuando se realiza la consulta este devuelve un JSON con la predicción y el resultado de Churn y el metodo /{model_version}/explain en este metodo se explica el peso de las variables en un Shap.

##### Enlace Youtube verificación de API: https://youtu.be/EWZLyiynm6c

### Clasificacion_Churn.ipynb:
Este cuaderno de trabajo contiene la exploración y calidad de datos del dataframe historico, adicional a que se presentan las principales relaciones que intuimos iban a ser relevantes sobre los modelos para predecir la variable objetivo Churn, adicional contiene todo el proceso de entrenamiento para los modelos, Regresion lineal, Random Forest, Xgboost y redes neuronales multicapa.

### A/B_testing.ipynb:
Este cuaderno de trabajo contiene la exploración y calidad de datos del dataframe futuro, adicional a que se plantea la evaluación del A/B testing y se presentan las metricas de los modelo; **En este cuaderno se responden las preguntas del literal 5 del taller**

Contacto: jv.chaparro@uniandes.edu.co, o.giraldor@uniandes.edu.co, da.alfonso2@uniandes.edu.co,am.martinezc123@unaindes.edu.co
