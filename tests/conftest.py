import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.models  # Garante o registro das tabelas no metadata
from app.main import app
from app.database import Base
from app.dependencies import get_db


# Cria arquivo temporário para o banco de testes
db_fd, db_path = tempfile.mkstemp()
SQLALCHEMY_TEST_URL = f"sqlite:///{db_path}"

# Engine e sessão
engine_test = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Fixture para sessão do banco
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine_test)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine_test)

# Fixture do client com override da dependência get_db
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# Finaliza e limpa o banco após todos os testes
def teardown_module(module):
    os.close(db_fd)
    os.unlink(db_path)
