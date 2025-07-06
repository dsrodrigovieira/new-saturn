from faker       import Faker
from app.schemas import UsuarioCreate

fake = Faker("pt_BR")  # opcional: usar contexto do Brasil

def create_fake_usuario():
    return UsuarioCreate(
        id=None,  # ID será gerado pelo banco de dados
        login   = fake.user_name(),
        senha   = fake.password(length=6),
        nome    = fake.name(),
        email   = fake.email(),
        status  = fake.random_element(elements=("A", "I"))    
    )
