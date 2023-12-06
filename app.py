import os
	
from mlforkids import MLforKidsImageProject

# treat this key like a password and keep it secret!
key =""
DEBUG = True

ml_out = myproject = MLforKidsImageProject(key)
ml_out2 = myproject.train_model()

if DEBUG == True:
	# this will train your model and might take a little while
	print(ml_out + ml_out2)

# CHANGE THIS to the image file you want to recognize

print("Aperte ctrl-C para sair do programa.")
while True:
	filename = input(f"Digite o nome do arquivo .jpg da imagem de satélite a ser analisada: ")
	try:
		demo = myproject.prediction(filename)
		label = demo["class_name"]
		confidence = demo["confidence"]

		# CHANGE THIS to do something different with the result
		print ("Resultado:\n\t'%s'\n\tConfiança: %d%%" % (label, confidence))
		if confidence < 60:
			print("ALERTA: baixa confiança")
	except:
		print(f"Erro. Verifique se o arquivo está na pasta. lista de arquivos:")
		print("\n\t\t".join(os.listdir()))
		

