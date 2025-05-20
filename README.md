pip install logiled 
pip install SoundCard

my keyboard thing is a logitech G213 so it only lights up in 5 zones, change line 20-24 to um whatever

.set_lighting
.set_lighting_for_target_zone
.set_lighting_for_key_with_hid_code
.set_lighting_for_key_with_key_name
.set_lighting_for_key_with_quartz_code 
.set_lighting_for_key_with_scan_code
