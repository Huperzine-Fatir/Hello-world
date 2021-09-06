#这个程序没有什么用，至少暂时。这只是我的Python初学练手文件，就好像一本跟着教科书随意写写画画的草稿本。
# 我写下这个注释的时候是2021.8.21.7:00。但这个文件的建立仅是2021.8.11.15:49而已。
print("Hello, new world!")
print(int(5.9))
message = "Raining raining got a million."
print(message)
message = "I'm in a bad mood now."
print(message)
my_mood = "Bad"
print("My current mood is " + my_mood + ".")

#第二天 8.17
mouse_name = "XiAo LiN"
print(mouse_name.title())
print(mouse_name.upper())
print(mouse_name.lower())
print("My pet mouse's name is " + mouse_name.title() + ".")
real_name = "lin"
chaperon_name = "xiao"
Full_name = chaperon_name + " " + real_name
print(Full_name)
Full_name = f"{chaperon_name} {real_name}"
print("My best beloved pet is called" + " " + Full_name.title() + ".")
print(f"My cutest pet is called {Full_name.title()}.")
message = f"{Full_name} is quite cute but I'm so depressed so that I don't wanna talk about it with my friend Raining."
print(message)
print("What did you say?")
print("I've just said: " + f"'{message}'")
print("\tBTW, I've been in negative mood for a time.")
print("\\t" + " " + "makes some spaces")
print("I got c \nut")
print("\\n means going to the next row.")
print("I called her: \n\tXiaoWang \n\tLinLin \n\tRaining \n\tBaobeier")
message_with_many_spaces = " electrophoresis "
print(message_with_many_spaces + "Blocker")
print(message_with_many_spaces.rstrip() + "Blocker")
print("Blocker" + message_with_many_spaces + "Blocker")
print("Blocker" + message_with_many_spaces.rstrip() + "Blocker")
print("Blocker" + message_with_many_spaces.lstrip() + "Blocker")
print("Blocker" + message_with_many_spaces.strip() + "Blocker")

#第三天 8.21
message = "I got up before 6:00 today. That's amazingly early."
print(message)
a_famous_person = "XiaoHanYu"
message = f"{a_famous_person} once said:\"You shall never been ignoring the esscential reality.\""
print(message)
print(2 * 3)
print(0.2 + 0.1)
print(10 * (0.2 + 0.1))
print(int(10 * (0.2 + 0.1)))
the_distance = 132_7000
print(the_distance)
x, y, z = 0, 0, 0
print(x, y, z)
print(x + y + z)
print(message + a_famous_person)
x, y, z = 1, 2, 3
print(x, y, z)
ETERNAL_THINGS = "nothing"
print(f"Eternal things,{ETERNAL_THINGS}.")
message = "But I will be always hardworking to chase the eternal. Always!"
print(message)
ETERNAL_THINGS = "could be anything"
print(f"Eternal things, {ETERNAL_THINGS}.")
print("\n\n\n")
#import this 我想在后面再显示一次hhh
print("\n\n\tI feel so tired, after a whole day of doing nothing.")
pets = ["ocp", "dog", "cat", "turtle", "ant", "silkworm", "fish", "'mouse'", "sparrow"]
print(pets)
print(pets[6])
print(f"My most beloved pet nowadays is a {pets[7].title()}.")
print(pets[-1])
pets[7] = "BALB/C"
print(pets)
she = ["OCP", "Raining", "Raining", "Raining"]
print(she[1])
print(she[2])
print(she[3])
print(she)
she.append("Raining")
print(she)
she = []
she.append("OCP")
she.append("Raining")
she.append("Raining")
she.append("Raining")
she.append("Raining")
she.append("Raining")
print(she)
she[0] = "Raining"
print(she)
she[0] = "OCP"
print(she)
she.insert(2, "Ohh")
print(she)
she.insert(4, "Ohh")
print(she)
del she[-1]
print(she)
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
print(list.pop())
list.pop()
print(list)
print(list.pop(6))
print(list)
list.remove(5)
print(list)
guest = ["OCP", "Alice", "Ben", "Candy", "David"]
print(f"I would like to invite {guest[1]}, {guest[2]}, {guest[3]}, {guest[4]} for the anniversary dinner.")
print(f"{guest[1]} is not going to join us, sorry.")
guest.remove("Alice")
print(guest)
guest.insert(1,"Alan")
print(guest)
print(f"But, {guest[1]} has joined us!!!")
print(f"Finally, I would like to invite {guest[1]}, {guest[2]}, {guest[3]}, {guest[4]} for the anniversary dinner.")
print("Besides, there is another good news. We are having a larger table tonight! \n\tWhich means three more guests!!!")
guest.insert(1, "Annable")
guest.insert(4, "Candy")
guest.append("Daniel")
print(f"Solemnly announcing, we have {guest} tonight!!!")

#第四天 9.6
#悔过
message = "I am just trying to print a \" in this sentence."
print(message)
message = 'And this \".'
print(message)
print("\n\n\n")
import this #好长但是里面的道理我都懂
list = ["OCP", "A", "B", "C", "D"]
print(list)
print(list[1]," ",list[2]," ",list[3]," ",list[4])
#正在测试Github