import soco

IP = "192.168.1.3"

speaker = soco.SoCo(IP)

speaker.switch_to_line_in()
speaker.volume = 100
speaker.play()
