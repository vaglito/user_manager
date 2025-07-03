# 🧱 Backend Hexagonal con FastAPI, CQRS y RabbitMQ

Este proyecto implementa una arquitectura hexagonal moderna en Python, utilizando **FastAPI** como framework principal, principios de **CQRS** para separar responsabilidades, y **RabbitMQ** para la comunicación asíncrona.

## 🔧 Características principales

- 🔁 Arquitectura Hexagonal (Ports & Adapters)
- 🧠 Separación entre comandos y queries (CQRS)
- 🐇 Integración con RabbitMQ
- 🧪 Pruebas unitarias desacopladas con mocks
- 💡 Inyección de dependencias con `dependency-injector`
- ✅ Tipado estricto con Pydantic

## 📁 Estructura del proyecto

```
project/
├── apps/
│   ├── auth/              # Contexto de autenticación
│   └── users/             # Contexto de usuarios
│       ├── application/   # Casos de uso
│       ├── domain/        # Entidades y puertos
│       └── infrastructure/# Repositorios e implementaciones externas
├── core/                  # Configuración general, contenedor DI, etc.
├── tests/                 # Pruebas unitarias y de integración
├── main.py                # Punto de entrada de la app
└── README.md
```

## 🚀 Instalación y ejecución

1. **Clona el repositorio**

```bash
git clone https://github.com/vaglito/user_manager
cd user_manager
```

2. **Crea un entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecuta la aplicación**

```bash
uvicorn main:app --reload
```

## 🧪 Ejecutar tests

```bash
pytest
```

Ejecuta todos los tests en la carpeta `tests/`, usando mocks para aislar las dependencias.

## 🧪 Ejemplo de test unitario con mocks

```python
from unittest.mock import MagicMock

def test_create_user_use_case_directly():
    from apps.users.application.commands.create_user import CreateUserUseCase
    from apps.users.domain.entities import User

    mock_repo = MagicMock()
    mock_hasher = MagicMock()

    user_data = User(email="test@example.com", password="123456", first_name="Test", last_name="User")
    mock_repo.create.return_value = user_data
    mock_hasher.hash_password.return_value = "hashedpass"

    use_case = CreateUserUseCase(mock_repo, mock_hasher)
    result = use_case.execute(user_data)

    assert result.email == "test@example.com"
    mock_hasher.hash_password.assert_called_once_with("123456")
    mock_repo.create.assert_called_once()
```

## 🧵 Inyección de dependencias

Usamos `Dependency Injector` para manejar las dependencias:

```python
class Container(containers.DeclarativeContainer):
    db = providers.Singleton(DatabaseSession)

    user_repository = providers.Factory(
        SQLAlchemyUserRepository,
        session_factory=db.provided.session
    )

    hasher_service = providers.Factory(PasswordHasherService)

    create_user_use_case = providers.Factory(
        CreateUserUseCase,
        user_repository=user_repository,
        hasher_service=hasher_service
    )
```

## 🐇 Integración con RabbitMQ

La mensajería se maneja con `aio-pika`. Puedes definir consumidores y publishers dentro de cada contexto.

```python
connection = await aio_pika.connect_robust(RABBITMQ_URL)
channel = await connection.channel()
await channel.default_exchange.publish(...)
```


### 👨‍💻 Autor

Desarrollado por **César Enrique González Carvajal**  
📧 cesargonzalez390@gmail.com  
🐍 Apasionado por Python, diseño limpio y software modular

---