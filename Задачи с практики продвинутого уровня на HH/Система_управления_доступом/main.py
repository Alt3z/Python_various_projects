class UserManager:
   def __init__(self):
       self.users = {}

   def add_user(self, name, level = 1):
       self.users[name] = level

   def remove_user(self, name):
       if name in self.users.keys():
           del self.users[name]

   def promote(self, name):
       if name in self.users.keys():
           if self.users[name] < 10:
               self.users[name] += 1

   def demote(self, name):
       if name in self.users.keys():
           if self.users[name] >0:
               self.users[name] -= 1

   def get_users(self):
       for user in self.users.keys():
           print(f"{user}:{self.users[user]}")
       if len(self.users) == 0:
           print("Никто")


user_manager = UserManager()
input_string = []
while True:
   try:
      line = input()
      if line == "":
         break
   except EOFError:
      break
   input_string.append(line)
   if line == "get_users":
       break

for command in input_string:
    command = command.split(" ")

    if command[0] == "add_user":
        if len(command) == 3:
            user_manager.add_user(command[1], int(command[2]))
        else:
            user_manager.add_user(command[1])
    elif command[0] == "remove_user":
        user_manager.remove_user(command[1])
    elif command[0] == "promote":
        user_manager.promote(command[1])
    elif command[0] == "demote":
        user_manager.demote(command[1])
    elif command[0] == "get_users":
        user_manager.get_users()