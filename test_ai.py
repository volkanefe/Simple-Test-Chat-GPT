import openai, json, os

with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "config.json", encoding="utf-8") as config_file:
    config = json.load(config_file)



openai.api_key = config["api_key"]

model_engine = "text-davinci-003"

questions = str(input())

completion = openai.Completion.create(engine = model_engine, prompt = questions, max_tokens = 1024, n = 1, stop = None, temperature = 0.9)


answers = completion.choices[0].text
print(answers)