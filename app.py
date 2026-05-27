from app.agent import AgenteMultimodal

def main():
    agente = AgenteMultimodal()

    print("Agente multimodal iniciado")
    print("Escribe 'salir' para terminar")

    while True:
        entrada = input("\nUsuario: ")

        if entrada.lower() == "salir":
            break

        respuesta = agente.ejecutar(entrada)
        print("\nRespuesta:\n", respuesta)


if __name__ == "__main__":
    main()
