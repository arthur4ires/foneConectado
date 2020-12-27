import subprocess
from time import sleep
from pulsectl import Pulse

sinkInput = Pulse('volume').sink_input_list()[0]

def foneConectado(saidaComando, sink_input):
	if len(saidaComando.stdout.readlines()) < 2:
		Pulse('volume').volume_set_all_chans(sink_input, 1)
		return True
	else:
		Pulse('volume').volume_set_all_chans(sink_input, 0.1)
		return False

while True:
	sleep(0.5)
	infoFone = subprocess.Popen(['cat /proc/asound/card0/codec#0 | grep "Pin-ctls: 0x40: OUT"'],stdout=subprocess.PIPE, shell=True)
	try:
		if foneConectado(infoFone, sinkInput) == True:
			print('fone on')
		else:
			foneInicial = False
			print('fone off')
	except:
		print("servidor de áudio off")
		continue
