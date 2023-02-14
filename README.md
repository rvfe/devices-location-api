# devices-location-api


O projeto foi desenvolvido com o FASTAPI e o banco de dados escolhido foi o postgres 

A api possui 2 rotas:
  - /position/ onde é possível tanto adicionar novos dispositivos com suas coordenadas(POST), como consultar os dispositivos já cadastrados(GET passando o device_id).
  - /devices/ esta rota permaneceu, pois é útil para testar cenários onde existe um dispositivo, mas não coordenadas associadas ao mesmo.
  
  
A estrutura do JSON a ser lido é o seguinte:

  [{
    device_id: 5555,
    latitude: -30.156180,
    longitude: -51.197909
    },{
    device_id: 5555,
    latitude: -30.178911,
    longitude: -51.197909
    },{
    device_id: 5555,
    latitude: -30.197632,
    longitude: -51.197909
    }]



Foi feito o commit do arquvio .env para facilitar os eventuais testes.

Para rodar o projeto, basta clonar o repositório e executar o comando:

```
docker-compose up -d --build
```

Para rodar o projeto, estando na raiz do projeto, execute:

```
uvicorn app.main:app --reload
```

Para rodar os testes, após clonar o projeto, execute o comando

```
pytest
```

O projeto é acessado em: 

```
http://127.0.0.1:8000/
```

A doc poderá ser encontrada em 

```
http://127.0.0.1:8000/docs
```


