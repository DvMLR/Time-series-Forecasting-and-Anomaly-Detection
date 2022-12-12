import sys
import matplotlib.pyplot as plt
from GUI import*
from PyQt5 import QtCore 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import matplotlib.colors as mcolors
import numpy as np
from utils.tools import dotdict
from exp.exp_informer import Exp_Informer
import torch
import os
import tensorflow as tf
from tensorflow import keras
from keras.models import model_from_json

#Aqui se inicializan parámetros y cargan pesos de transformer para pronósticos 

args = dotdict()
args.model = 'informer' # model of experiment, options: [informer, informerstack, informerlight(TBD)]
args.data = 'custom' # data
args.root_path = './data/ETT/' # root path of data file
args.data_path = 'Datos.csv' # data file
args.features = 'M' # forecasting task, options:[M, S, MS]; M:multivariate predict multivariate, S:univariate predict univariate, MS:multivariate predict univariate
args.target = 'X54' # target feature in S or MS task
args.freq = 'h' # freq for time features encoding, options:[s:secondly, t:minutely, h:hourly, d:daily, b:business days, w:weekly, m:monthly], you can also use more detailed freq like 15min or 3h
args.checkpoints = './checkpoints' # location of model checkpoints
args.seq_len = 96 # input sequence length of Informer encoder
args.label_len = 48 # start token length of Informer decoder
args.pred_len = 24 # prediction sequence length
# Informer decoder input: concat[start token series(label_len), zero padding series(pred_len)]
args.enc_in = 3 # encoder input size
args.dec_in = 3 # decoder input size
args.c_out = 3 # output size
args.factor = 5 # probsparse attn factor
args.d_model = 512 # dimension of model
args.n_heads = 8 # num of heads
args.e_layers = 2 # num of encoder layers
args.d_layers = 1 # num of decoder layers
args.d_ff = 2048 # dimension of fcn in model
args.dropout = 0.05 # dropout
args.attn = 'prob' # attention used in encoder, options:[prob, full]
args.embed = 'timeF' # time features encoding, options:[timeF, fixed, learned]
args.activation = 'gelu' # activation
args.distil = True # whether to use distilling in encoder
args.output_attention = False # whether to output attention in decoder
args.mix = True
args.padding = 0
args.freq = 'h'
args.batch_size = 32
args.learning_rate = 0.0001
args.loss = 'mse'
args.lradj = 'type1'
args.use_amp = False # whether to use automatic mixed precision training
args.num_workers = 0
args.itr = 1
args.train_epochs = 6
args.patience = 3
args.des = 'exp'
args.use_gpu = True if torch.cuda.is_available() else False
args.gpu = 0
args.use_multi_gpu = False
args.devices = '0,1,2,3'
Exp = Exp_Informer  #se llama al modelo
setting = 'informer_custom_ftM_sl96_ll48_pl24_dm512_nh8_el2_dl1_df2048_atprob_fc5_ebtimeF_dtTrue_mxTrue_test_0' #dirección dónde se encuentra guardado el mejor peso
exp = Exp(args) # se crea experimenmto junto a los argumentos (argumentos entran al modelo)

#Aquí se carga el modelo de clasificación
optimizer=keras.optimizers.Adam(learning_rate=1e-3)
json_file = open('model_guardado5.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# cargar los pesos del nuevo modelo
loaded_model.load_weights("weights.best5.hdf5")
print("Cargar modelo del disco")

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
 
        #Botones y barras
        self.ui.pushButton.clicked.connect(self.barra)
        self.ui.pushButton.clicked.connect(modelo)
        self.ui.pushButton.clicked.connect(self.Gen_Data)
        self.ui.pushButton_2.clicked.connect(self.informacion)


        #Entradas
        self.start = False
        self.grafica1 = Canvas_grafica('Tiempo','Corriente')
        self.ui.verticalLayout_9.addWidget(self.grafica1)
        self.grafica2 = Canvas_grafica('Tiempo','Vib L.A')
        self.ui.verticalLayout_10.addWidget(self.grafica2)
        self.grafica3 = Canvas_grafica('Tiempo','Vib L.L')
        self.ui.verticalLayout_11.addWidget(self.grafica3)

        #PRONOSTICO
        self.grafica4 = Canvas_grafica('Tiempo','Corriente')
        self.ui.verticalLayout_12.addWidget(self.grafica4)
        self.grafica5 = Canvas_grafica('Tiempo','Vib L.A')
        self.ui.verticalLayout_13.addWidget(self.grafica5)
        self.grafica6 = Canvas_grafica('Tiempo','Vib L.L')
        self.ui.verticalLayout_14.addWidget(self.grafica6)

        #DETECTOR
        self.grafica7 = Canvas_grafica('Tiempo','Corriente')
        self.ui.verticalLayout_15.addWidget(self.grafica7)
        self.grafica8 = Canvas_grafica('Tiempo','Vib L.A')
        self.ui.verticalLayout_16.addWidget(self.grafica8)
        self.grafica9 = Canvas_grafica('Tiempo','Vib L.L')
        self.ui.verticalLayout_17.addWidget(self.grafica9)

    def barra(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.ui.progressBar.setValue(self.completed)
    
    def Gen_Data(self):

        self.grafica1.grafica_datos1('Tiempo','Corriente',0)
        self.grafica2.grafica_datos1('Tiempo','Vib L.A',1)
        self.grafica3.grafica_datos1('Tiempo','Vib L.L',2)

        self.grafica4.grafica_datos2('Tiempo','Corriente',0)
        self.grafica5.grafica_datos2('Tiempo','Vib L.A',1)
        self.grafica6.grafica_datos2('Tiempo','Vib L.L',2)

        self.grafica7.grafica_datos3('Tiempo','Corriente',0)
        self.grafica8.grafica_datos4('Tiempo','Vib L.A',1, )
        self.grafica9.grafica_datos5('Tiempo','Vib L.L',2)

    def informacion(self):
        total_anom = self.ui.total.text()
        total_anom = str(n_anomalias)
        self.ui.total.setText(total_anom)

        anom_corriente = self.ui.corriente.text()
        anom_corriente = str(len(anomalias_corrientes))
        self.ui.corriente.setText(anom_corriente)

        anom_vibla = self.ui.vibla.text()
        anom_vibla = str(len(anomalias_vibla))
        self.ui.vibla.setText(anom_vibla)

        anom_vibll = self.ui.vibll.text()
        anom_vibll = str(len(anomalias_vibll))
        self.ui.vibll.setText(anom_vibll)

        if n_anomalias>20:
            msg = QMessageBox()
            msg.setWindowTitle('ADVERTENCIA')
            msg.setText('Se ha detectado un número elevado de anomalías')
            x = msg.exec_()
        

def modelo():
    #Esta funcion permite realizar inferencias con los modelos ya cargados
    exp.predict(setting, True) #Esta funcion viene desde otro codigo que realiza la inferencia y guarda la salida en un archivo.npy
    pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
    v = pronóstico.reshape((pronóstico.shape[0], pronóstico.shape[1], 1)) #se prepara la entrada para el siguiente modelo
    # evaluar el modelo cargado desde el disco con los datos 
    loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer)
    clasificador = loaded_model.predict(v)
    folder_path = './results/' + setting +'/'
    np.save(folder_path+'real_class.npy', clasificador)
    puntos_anomalos() #se llama para creer dataframes que permitan obtener la ubicacion (en tiempo y variable) sobre las anomalías 

def puntos_anomalos():
    #Esta funcion sirve para localizar todos los puntos anómalos existentes y a que variables corresponden
    global n_anomalias, anomalias_corrientes, anomalias_vibla, anomalias_vibll
    pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
    categoria=np.load('./results/'+setting+'/real_class.npy') #se carga pronóstico desde archivo .npy
    pred_category = np.zeros(24)
    i=0

    #Crea un array que dice si existen anomalías o no según el modelo
    while i<=23:
        pred_category[i] = np.argmax(categoria[i])
        i = i+1 

    x1 = list(pronóstico[:, 0])
    x2 = list(pronóstico[:, 1])
    x3 = list(pronóstico[:, 2])
    x4 = list(pred_category)
    tabla=[x1]+[x2]+[x3]+[x4]
    tabla=np.transpose(tabla)
    columnas = ['Corriente','VibLA','VibLL','anomalias']
    tabla = pd.DataFrame(tabla, columns=columnas)
    #estas últimas 3 son para comparar los limites (de las reglas de nelson) y así obtener los indices para las gráficas
    anomalias_corrientes = tabla.loc[(tabla.Corriente > 274) | (tabla.Corriente < 253)] 
    anomalias_vibla = tabla.loc[(tabla.VibLA > 2.85) | (tabla.VibLA <  1.99)]
    anomalias_vibll = tabla.loc[(tabla.VibLL > 2.18) | (tabla.VibLL < 1.2)]
    n_anomalias = len(anomalias_corrientes) + len(anomalias_vibla) + len(anomalias_vibll) #total de anomalías encontradas

class Canvas_grafica(FigureCanvas):

    #Se crea gráfica vacía para iniicializar la interfaz
    def __init__(self,xlabel, ylabel, parent=None, width=5, height=4, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='lightsteelblue')
        self.axes = fig.add_subplot(111)
        super(Canvas_grafica, self).__init__(fig)
        self.axes.grid()
        self.axes.margins(x=0)
        self.axes.set_ylabel(ylabel)
        self.axes.set_xlabel(xlabel)

    #Graficas de entrada
    def grafica_datos1(self, xlabel, ylabel, canal):
        entradas = np.load('./results/'+setting+'/entradas.npy') #se cargan entradas desde archivo .npy
        self.axes.cla()  # Clear the canvas.
        self.axes.grid()
        self.axes.plot(entradas[:,canal])
        self.axes.set_ylabel(ylabel)
        self.axes.set_xlabel(xlabel)
        self.draw()

    #Graficas de pronósticos
    def grafica_datos2(self, xlabel, ylabel, canal):
        pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
        self.axes.cla()  # Clear the canvas.
        self.axes.grid()
        self.axes.plot(pronóstico[:,canal])
        self.axes.set_ylabel(ylabel)
        self.axes.set_xlabel(xlabel)
        self.draw()
    
    #Graficas de anomalías
    def grafica_datos3(self, xlabel, ylabel, canal):
        #anomalías para corrientes
        #Si existen anomalias se usa el primer plot, de esta forma se evita un error que se podría producir si no se detectan anomalías
        if  anomalias_corrientes.empty is False:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.scatter(anomalias_corrientes.index, anomalias_corrientes[ylabel], c='r')
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()
        
        else:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()
        
    def grafica_datos4(self, xlabel, ylabel, canal):

        #anomalías para VIBLA
        #Si existen anomalias se usa el primer plot, de esta forma se evita un error que se podría producir si no se detectan anomalías
        if  anomalias_vibla.empty is False:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.scatter(anomalias_vibla.index, anomalias_vibla[ylabel], c='r')
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()
        else:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()
        
    
    def grafica_datos5(self, xlabel, ylabel, canal):

        #anomalías para VIBLL
        #Si existen anomalias se usa el primer plot, de esta forma se evita un error que se podría producir si no se detectan anomalías
        if anomalias_vibla.empty is False:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.scatter(anomalias_vibll.index, anomalias_vibll[ylabel], c='r')
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()
        else:
            pronóstico = np.load('./results/'+setting+'/real_prediction.npy') #se carga pronóstico desde archivo .npy
            self.axes.cla()  # Clear the canvas.
            self.axes.grid()
            self.axes.plot(pronóstico[:,canal])
            self.axes.set_ylabel(ylabel)
            self.axes.set_xlabel(xlabel)
            self.draw()

        

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())