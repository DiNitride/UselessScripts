ALPHABET = {
	"a": "Alpha",
	"b": "Bravo",
	"c": "Charlie",
	"d": "Delta",
	"e": "Echo",
	"f": "Foxtrot",
	"g": "Golf",
	"h": "Hotel",
	"i": "India",
	"j": "Juliett",
	"k": "Kilo",
	"l": "Lima",
	"m": "Mike",
	"n": "November",
	"o": "Oscar",
	"p": "Papa",
	"q": "Quebec",
	"r": "Romeo",
	"s": "Sierra",
	"t": "Tango",
	"u": "Uniform",
	"v": "Victor",
	"w": "Whiskey",
	"x": "Xray",
	"y": "Yankee",
	"z": "Zulo"
}

def convert(inp: str):
        out = ""
        for letter in inp:
                if letter == " ":
                        l = "\n"
                else:
                        l = f"{ALPHABET[letter]} "
                out += f"{l}"
        return out


if __name__ == "__main__":

        output = input("Text to Convert: ").lower()
        print(convert(output))
        input("Press any key to continue...")
	
