# Exploring LangChain! 🦜️🔗

Este repositorio contiene diversas pruebas y experimentos realizados para aprender y explorar las capacidades del framework [LangChain](https://langchain.com/). Aquí encontrarás ejemplos de cómo utilizar las distintas herramientas que proporciona LangChain para la creación de aplicaciones basadas en inteligencia artificial, flujos de trabajo y manejo de grandes lenguajes de modelo (LLM).


## Contenido

El contenido del repositorio permite ejecutar diferentes scripts de Python con el framework de Langchain con la idea de explorar:
- Utilizar LLM tanto de forma online como en local
- Conexiones API
- Desarrollo de agentes (Agents)
- Desarrollo de herramientas (Tools)
- Trazabilidad con LangSmith 


## Instalación

Para clonar este repositorio y comenzar a experimentar con LangChain, sigue estos pasos:

```bash
git clone https://github.com/gmachinromero/project-exploring-langchain.git
cd project-exploring-langchain
```

Asegúrate de tener instalado Python 3.11+ y pipenv para crear un entorno con todas las dependencias necesarias:

```bash
pipenv install
```

Adicionalmente necesitarás los token siguientes en un fichero de configuración `.env`:
- OPENAI_API_KEY
- PROXYCURL_API_KEY
- TAVILY_API_KEY
- LANGCHAIN_TRACING_V2
- LANGCHAIN_ENDPOINT
- LANGCHAIN_API_KEY
- LANGCHAIN_PROJECT

## Recursos
- https://python.langchain.com/v0.2/docs/introduction/
- Udemy: LangChain- Develop LLM powered applications with LangChain
