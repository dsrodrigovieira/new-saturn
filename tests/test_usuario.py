from app.models.usuarios import Usuario
from tests.factories import create_fake_usuario

def test_create_usuario(client):
    usr = create_fake_usuario()
    response = client.post("/usuarios", json=usr.model_dump())
    assert response.status_code == 201

def test_create_usuario_with_existing_login(client, db_session):
    usr = create_fake_usuario()
    # Add the user to the database first
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    # Try to create another user with the same login
    response = client.post("/usuarios", json=usr.model_dump())
    assert response.status_code == 409
    assert response.json()["detail"] == f"Usuário com login '{usr.login}' já existe"

def test_get_usuario(client, db_session):
    usr = create_fake_usuario()
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    res_usr = db_session.query(Usuario).filter(Usuario.login == usr.login).first()
    assert res_usr is not None
    response = client.get(f"/usuarios/{res_usr.id}")
    assert response.status_code == 200

def test_get_nonexistent_usuario(client):
    response = client.get("/usuarios/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário com ID 9999 não encontrado"

def test_update_usuario(client, db_session):
    usr = create_fake_usuario()
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    res_usr = db_session.query(Usuario).filter(Usuario.login == usr.login).first()
    
    updated_usr = usr.model_copy(update={"email": "Novo email"})
    response = client.put(f"/usuarios/{res_usr.id}", json=updated_usr.model_dump())
    assert response.status_code == 202
    
    updated_res_usr = db_session.query(Usuario).filter(Usuario.id == res_usr.id).first()
    assert updated_res_usr.email == "Novo email"

def test_update_nonexistent_usuario(client):
    usr = create_fake_usuario()
    response = client.put("/usuarios/9999", json=usr.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário com ID 9999 não encontrado"

def test_delete_usuario(client, db_session):
    usr = create_fake_usuario()
    db_session.add(Usuario(**usr.model_dump()))
    db_session.commit()
    res_usr = db_session.query(Usuario).filter(Usuario.login == usr.login).first()
    response = client.delete(f"/usuarios/{res_usr.id}")
    assert response.status_code == 202
    deleted_usr = db_session.query(Usuario).filter(Usuario.id == res_usr.id).first()
    assert deleted_usr is None

def test_delete_nonexistent_usuario(client):
    response = client.delete("/usuarios/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário com ID 9999 não encontrado"