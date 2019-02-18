import soco

IP = "192.168.1.4"

speaker = soco.SoCo(IP)

speaker.switch_to_line_in()
speaker.volume = 100
speaker.play()
