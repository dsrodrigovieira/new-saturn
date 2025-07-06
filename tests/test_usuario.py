from app.models      import Usuario
from tests.factories import create_fake_usuario

def test_create_usuario(client):
    usr = create_fake_usuario()
    response = client.post("/users", json=usr.model_dump())
    assert response.status_code == 201

def test_get_usuario(client, db_session):
    usr = create_fake_usuario()
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    res_usr = db_session.query(Usuario).filter(Usuario.login == usr.login).first()
    assert res_usr is not None
    response = client.get(f"/users/{res_usr.id}")
    assert response.status_code == 200

def test_delete_usuario(client, db_session):
    usr = create_fake_usuario()
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    res_usr = db_session.query(Usuario).filter(Usuario.login == usr.login).first()
    response = client.delete(f"/users/{res_usr.id}")
    assert response.status_code == 202
    deleted_usr = db_session.query(Usuario).filter(Usuario.id == res_usr.id).first()
    assert deleted_usr is None

def test_get_nonexistent_usuario(client):
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário com ID 9999 não encontrado"

def test_delete_nonexistent_usuario(client):
    response = client.delete("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário com ID 9999 não encontrado"