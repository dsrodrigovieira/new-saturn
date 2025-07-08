from faker                import Faker
from app.schemas.usuarios import UsuarioBase
from app.schemas.empresas import EmpresaBase
from app.schemas.kpis     import KpiBase

fake = Faker("pt_BR")  # opcional: usar contexto do Brasil

def create_fake_usuario():
    return UsuarioBase(
        id = None,
        login = fake.user_name(),
        senha = fake.password(length=8),
        nome_completo = fake.name(),
        empresa_id = fake.random_int(min=1, max=100),
        email = fake.email(),
        dt_criacao = None,
        ativo = True,
        dt_atualizacao = None,
        ultimo_login = None,
    )

def create_fake_empresa():
    return EmpresaBase(
        id=None,
        cnpj=fake.cnpj(),
        cnes=fake.random_int(min=1000000, max=9999999),
        razao=fake.company(),
        fantasia=fake.company_suffix(),
        cep=fake.postcode(),
        numero_endereco=fake.building_number(),
        site=fake.url(),
        telefone=fake.phone_number(),        
        email=fake.company_email(),
        dt_criacao=None,        
        ativo=True,        
        dt_atualizacao=None,
    )

def create_fake_kpi():
    return KpiBase(
        titulo=fake.catch_phrase(),
        descricao=fake.text(max_nb_chars=100),
        dominio=fake.word(),
        unidade=fake.random_element(elements=["%", "/1000 pacientes-dia", "Número absoluto"]),
        meta=round(fake.pyfloat(left_digits=2, right_digits=1, min_value=0, max_value=100)),
        meta_descricao=fake.sentence(),
        sequencia=fake.random_int(min=1, max=10),
        direcao_favoravel=fake.random_element(elements=["C", "D"]),
        caminho_documentacao=fake.url(),
        ativo=True,
        dt_criacao=None,
        dt_atualizacao=None,
    )