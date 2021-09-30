LIGHTS = False
BOT_PREFIX = "!"

####### ALL COMMANDS #######
def cmd_welcome(cmd_args=[]):
  print("Bot: Welcome to the server. Please be sure to read the rules.")

def cmd_lights(cmd_args=[]):
  global LIGHTS
  
  if len(cmd_args) >= 1:
    if cmd_args[0].lower() == "on":
      LIGHTS = True
    elif cmd_args[0].lower() == "off":
      LIGHTS = False
    else:
      print("Wrong syntax of lights. Use lights <on/off>")
      return
  if len(cmd_args) <= 0:
    LIGHTS = not LIGHTS
  status = "on" if LIGHTS else "off"
  print(f"Bot: Aiden turned the lights {status}")

def cmd_greet(cmd_args=[]):
  if len(cmd_args) <= 0:
    print("Bot: Please enter a name after the command to greet!")
    return
  print(f"Bot: Greetings go out to {' '.join(cmd_args)}")
############################


def get_command():
  return input("Aiden: ")

def handle_command():
  cmd = get_command().strip().split(" ")

  if cmd[0].lower() == "exit":
    quit()

  commands = {
    f"{BOT_PREFIX}welcome": cmd_welcome,
    f"{BOT_PREFIX}lights": cmd_lights,
    f"{BOT_PREFIX}greet": cmd_greet
  }

  func = commands.get(cmd[0])

  if callable(func) == True:
    func(cmd[1:len(cmd)])

while True:
  handle_command()
