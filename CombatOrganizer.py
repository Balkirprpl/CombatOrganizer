characters = []


def mainMenu():
   i = input('''Select option:
   1  * Add creature.
   2  * List loaded characters
   3  * Creature info.
   4  * Damage calculator.
   5  * Roll innitiative.
   6  * Load encounter.
   exit

Selected option: ''')
   return i

class Creature:
   name = ''
   hp = 0
   ac = 0
   speed = 0
   str_ = 0
   dex = 0
   con = 0
   int_ = 0
   wis = 0
   cha = 0
   prof = 0
   skills = []
   actions = []
   id = 0
   xp = 0

   def __init__(self, stats):
      i = stats
      self.name = i[0]
      self.hp = i[1]
      self.ac = i[2]
      self.speed = i[3]
      self.str_ = i[4]
      self.dex = i[5]
      self.con = i[6]
      self.int_ = i[7]
      self.wis = i[8]
      self.cha = i[9]
      self.prof = i[10]
      for j in i[11].split(','):
         self.skills.append(j)
      for j in i[12].split(','):
         self.actions.append(j)
      self.id = len(characters)
      self.xp = i[13]

if __name__ == "__main__":
   while (True):
      i = mainMenu()
      if i == 'exit':
         exit()
      if i == '1':
         if input("Select from file? (y/n) ") == 'y':
            n = input("How many? ")
            filename = input('Filename = ')
            stats = open(filename)
            a = stats.read().split()
            x = Creature(a)
            for i in range(int(n)):
               characters.append(x)
            print('Character added.\n\n')

         else:
            stats = input('\nInput: Name, HP, AC, Speed, STR, DEX, CON, INT, WIS, CHA, Proficiency, Skills (Comma Separated), Actions (comma separated), xp\n')
            x = Creature(stats.split())
            characters.append(x)
      if i == '2':
         for j in characters:
            #print(j, j.skills, j.prof, j.xp)
            print('''Name: {0}
ac = {2}
speed = {3}
str = {4}
dex = {5}
con = {6}
int = {7}
wis = {8}
cha = {9}
prof = {10}
skills = {11}
actions = {12}
id = {13}
xp = {14}\n\n'''.format(j.name, j.hp, j.ac, j.speed, j.str_, j.dex, j.con, j.int_, j.wis, j.cha, j.prof, str(j.skills)[1:-1].replace("'", ''), str(j.actions).replace("'", '')[1:-1], j.id, j.xp))
