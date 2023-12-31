from crazyradio import Crazyradio
import time

# init radio as sender
def radio_tx_init(channel=100, data_rate=Crazyradio.DR_250KPS, mode=Crazyradio.MODE_PTX):
	radio = Crazyradio()
	radio.set_channel(channel)
	radio.set_data_rate(data_rate)
	radio.set_mode(mode)
	return radio

# TX test
def radio_tx_test(radio):
	for i in range(0, 100):
		res = radio.send_packet([i])
		print(res.data)

	radio.close()
	return

# Send packet through radio
def radio_send_pkt(radio, data):
	res = radio.send_packet(data)
	return res