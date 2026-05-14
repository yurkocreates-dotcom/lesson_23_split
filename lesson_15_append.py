tools = [
    "ChatGPT",
    "Claude",
    "Midjourney",
    "Runway"
]
tools.remove( "Runway")
print(tools)

tasks = [
    "Learn Python",
    "Build AI app",
    "Study German",
    "Workout"
]
tasks.remove( "Study German")
tasks.remove( "Workout")
print("Remaining Tasks:")
for task in tasks:
    print('-',task)