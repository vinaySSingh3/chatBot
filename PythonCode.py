import aiml

kernal = aiml.Kernel()
kernal.learn("std-startup.xml")
kernal.respond("LOAD AIML B")

print(">NoobBOT: I am NoobBot")

while True:
    input_text = input(">Human: " )
    response = kernal.respond(input_text)
    print(">NoobBOT: "+ response)


