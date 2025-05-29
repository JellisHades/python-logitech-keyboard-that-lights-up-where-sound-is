from logiled import LogitechLed, load_dll
import soundcard as sc

load_dll()
led = LogitechLed()

SamplingRate = 1000
Frequency = 100 * 50

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SamplingRate) as mic:
	while True:
		DataRecording = mic.record(numframes=1)[0]
        
		LeftChannel = min(abs(DataRecording[0] * Frequency), 100)
		RightChannel = min(abs(DataRecording[1] * Frequency), 100)
		Average = (LeftChannel + RightChannel) / 5	
		RightMid = (Average + RightChannel) / 2
		LeftMid = (Average + LeftChannel) / 2
        
		led.set_lighting_for_target_zone(1, 0, 0, int(LeftChannel))
		led.set_lighting_for_target_zone(2, 0, 0, int(LeftMid))
		led.set_lighting_for_target_zone(3, 0, 0, int(Average))
		led.set_lighting_for_target_zone(4, 0, 0, int(RightMid))
		led.set_lighting_for_target_zone(5, 0, 0, int(RightChannel))
