import language_tool_python
import time
tool = language_tool_python.LanguageTool('en-US')
start_time = time.time()

user = input("Enter any sentence: ")
matches = tool.check(user)
if matches:
    print("The sentence contain the grammatical errors.")
    for match in matches:
      if match.ruleId == 'Grammar':
            print(match)
else:
    print("The sentence you have written is correct.")
end_time = time.time()

time_taken = end_time - start_time
print(f"The time taken to write the sentence = {time_taken} seconds.")