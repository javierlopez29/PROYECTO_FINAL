from langchain.memory import ConversationBufferWindowMemory


class GestorMemoria:

    def __init__(self):

        self.memoria = ConversationBufferWindowMemory(k=2)

    def guardar(self, entrada, salida):

        self.memoria.save_context(
            {"input": entrada},
            {"output": salida}
        )

    def obtener(self):

        return self.memoria.load_memory_variables({})["history"]
