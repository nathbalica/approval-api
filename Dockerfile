# Usa a imagem oficial do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências
RUN pip install -r requirements.txt

# Expõe a porta
EXPOSE 3000

# Comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
