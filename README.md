# ClasfModel_4101_Taller3
Taller 3 de Algoritmos de clasificación

Andrés Mauricio Martínez Celis &nbsp;  &nbsp; &nbsp;     202322624 <br>
Danilo Andrés Alfonso Bohórquez  &nbsp;      201611827 <br>
Jairo Vladimir Chaparro Rodríguez     201531080 <br>
Oscar Duvan Giraldo Romero  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  202324939   <br>  

Estructura de carpetas:<br>
Taller3 <br>
├── Api<br>
└── main.py<br>
└── model.py<br>
└── shapValues.py<br>
├── Archivos<br>
└── churn_historic.json<br>
└── churn_future.json<br>
├── Models<br>
└── DecisionTreeBest.joblib<br>
└── Gxboost.joblib<br>
└── LogisticRegression.joblib<br>
└── NeuronalNewtwork.joblib<br>
└── RandomForest.joblib<br>
└── Clasificacion_Churn.ipynb<br>
└── A/B_testing.ipynb<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── base_ventas.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── COMPRAS 2023 Dashboard.xlsm (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Dataset_Operacion_Anual.csv (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── base_ventas.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── BodegasSAP.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── DatosCQ.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── INFORMACION INVENTARIO Y VENTAS 22-09-2023.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── INVENTARIO (CODIGO DE PRODCUTOS).xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── arima.csv (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>

# Api:
La api se construyo con FastAPI mediante codigo python, la Api maneja dos metodos POST, el primero es /{model_version}/predict en este metodo se puede variar entre 1 y 2, cuando se realiza la consulta este devuelve un JSON con la predicción y el resultado de Churn y el metodo /{model_version}/explain en este metodo se explica el peso de las variables en un Shap.

# Clasificacion_Churn.ipynb:
Este cuaderno de trabajo contiene la exploración y calidad de datos del dataframe historico, adicional a que se presentan las principales relaciones que intuimos iban a ser relevantes sobre los modelos para predecir la variable objetivo Churn, adicional contiene todo el proceso de entrenamiento para los modelos, Regresion lineal, Random Forest, Xgboost y redes neuronales multicapa.

# A/B_testing.ipynb:
Este cuaderno de trabajo contiene la exploración y calidad de datos del dataframe futuro, adicional a que se plantea la evaluación del A/B testing y se presentan las metricas de los modelos.

Contacto: jv.chaparro@uniandes.edu.co, o.giraldor@uniandes.edu.co, da.alfonso2@uniandes.edu.co,am.martinezc123@unaindes.edu.co
