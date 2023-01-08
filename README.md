## Pronóstico y detección de anomalías

Contiene:

1- Este Git contiene todos los códigos necesarios para cargar y compilar los modelos de Transformers para el pronóstico y detección de anomalías. 

2- Adicionalmente también contiene lo necesario para ejecuitar la GUI.

3- Los pesos y checkpoints se pueden encontrar en el siguiente link: https://drive.google.com/drive/folders/1S2N_-vIxboq7ZsZnxJAl80VVY-7XYhRV?usp=sharing

4- Los pesos y modelos guardados en JSON deben estar en la carpeta principal, junto a los demás archivos que se ven en el repositorio. El archivo.PTH debe estar ubicado      en la carpeta "Checkpoints" y dentro de la sub-carpeta que se encuentra allí.

Adicionalmente, para entrenar el modelo de pronóstico contenido aquí se puede obtener información adicional en el repositorio de sus creadores: https://github.com/zhouhaoyi/Informer2020

# ¿Cómo se utiliza?

Para ejecutar el sistema de pronóstico de detección y anomalías basta con ejecutar el archivo [Main_GUI.py](/Main_GUi.py), este se encargará de ejecutar la inferfaz que permita utilizar el sistema, en la ventana principal se encuentran los botones que permiten realizar un pronóstico de una ventana aleatoria de tiempo tomada desde la base de datos y posteriormente gráficar dicho pronóstico y detección de las anomalías en las señales.

# Base de datos personalizada

Si se requiere utilizar otros datos para predicción se debe agregar el arhivo .csv a la carpeta [data](/data/ETT/), y posteriormente ejecutar la GUI. Adicionalmente, si se desea reentrenar los modelos han de hacerse por separado. Para reentrenar el modelo de pronóstico es necesario usar comandos que están especificados en https://github.com/zhouhaoyi/Informer2020 y guardar los pesos en la carpeta [checkpoints](/checkpoints/informer_custom_ftM_sl96_ll48_pl24_dm512_nh8_el2_dl1_df2048_atprob_fc5_ebtimeF_dtTrue_mxTrue_test_0/). En el caso del modelo de detección de anomalías es posible ajustar parámetros y reentrenar modelo con el siguiente código de [GoogleColab](https://colab.research.google.com/drive/1Yini-tKGZ8_x9QohfvgElqLnFvwfBAqN?authuser=1), el cual guarda el modelo y pesos que pueden almacenarse en este directorio posteriormente.

# Principales archivos

Cómo se mencionó anteriormente, el archivo [Main_GUI.py](/Main_GUi.py) inicializa la interfaz y a su vez carga los pesos de los modelos ya entrenados. Por otra parte el botón "Realizar Pronóstico" cumple con la función de cargar los datos mediante el archivo [data_loader.py](/data/data_loader.py) y realizar el posterior pronóstico mediante el código [exp_informer.py](/exp/exp_informer.py) y guardará las predicciones en el archivo [real_prediction.npy](/results/informer_custom_ftM_sl96_ll48_pl24_dm512_nh8_el2_dl1_df2048_atprob_fc5_ebtimeF_dtTrue_mxTrue_test_0/real_prediction.npy). Finalmente estás últimas pasan al clasificador que realiza la tarea mediante la función Modelo() en el archivo [Main_GUI.py](/Main_GUi.py).
