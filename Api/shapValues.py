import joblib
import shap
import pandas as pd
import numpy as np


def explainSelection(datas,model):
    preprocesador = model.named_steps['preprocessor']
    selector_caracteristicas = model.named_steps['selectkbest']
    modelo_final = model.named_steps['classifier']
    X_test_preprocesado = preprocesador.transform(datas)
    nombres_features_preprocesados = preprocesador.get_feature_names_out(input_features=datas.columns)
    X_test_preprocesado_df = pd.DataFrame(X_test_preprocesado, columns=nombres_features_preprocesados)
    indices_seleccionados = selector_caracteristicas.get_support()
    X_test_preprocesado_seleccionado = X_test_preprocesado_df.iloc[:, indices_seleccionados]
    X_test_preprocesado_seleccionado = X_test_preprocesado_df.iloc[:, indices_seleccionados]
    explainer = shap.TreeExplainer(modelo_final)
    shap_values = explainer.shap_values(X_test_preprocesado_seleccionado)
    resultados = []
    for i in range(X_test_preprocesado_seleccionado.shape[0]):
        fila = {
            "index": X_test_preprocesado_seleccionado.index[i],
            "features": X_test_preprocesado_seleccionado.iloc[i].to_dict(),
            "shap_values": shap_values[i].tolist()
        }
        resultados.append(fila)
    entry = resultados[0]
    features = entry['features']
    shap_values = entry['shap_values'][0]
    shap_values_abs = [abs(value) for value in shap_values]
    result_list = [{f'{feature}': value} for feature, value in zip(features.keys(), shap_values_abs)]
    nuevo_diccionario = {}
    for diccionario in result_list:
        nuevo_diccionario.update(diccionario)

    return nuevo_diccionario

