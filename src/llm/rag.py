from salamandra_client import SalamandraClient

file_path = './src/summarizer/data/finetune.txt'


with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


client = SalamandraClient()
instrucció = "Es pot reconèixer pel b2 de català?"

print(client.give_prediction(instrucció, file_content))
