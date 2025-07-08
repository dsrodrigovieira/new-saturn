from app.models.empresas import Empresa
from tests.factories import create_fake_empresa

def test_create_empresa(client):
    emp = create_fake_empresa()
    response = client.post("/empresas", json=emp.model_dump())
    assert response.status_code == 201

def test_create_empresa_with_existing_cnpj_and_cnes(client, db_session):
    emp = create_fake_empresa()
    # Adiciona empresa original ao banco
    db_session.add(Empresa(**emp.model_dump()))
    db_session.commit()
    # Tenta cadastrar outra empresa com mesmo cnpj e cnes
    duplicate_emp = emp.model_copy()
    response = client.post("/empresas", json=duplicate_emp.model_dump())
    assert response.status_code == 409
    assert "Empresa com este CNPJ/CNES já existe" in response.json()["detail"]

def test_get_empresa(client, db_session):
    emp = create_fake_empresa()
    db_session.add(Empresa(**emp.model_dump()))
    db_session.commit()
    res_emp = db_session.query(Empresa).filter(Empresa.cnpj == emp.cnpj).first()
    assert res_emp is not None
    response = client.get(f"/empresas/{res_emp.id}")
    assert response.status_code == 200

def test_get_nonexistent_empresa(client):
    response = client.get("/empresas/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Empresa com ID 9999 não encontrada"

def test_update_empresa(client, db_session):
    emp = create_fake_empresa()
    db_session.add(Empresa(**emp.model_dump()))
    db_session.commit()
    res_emp = db_session.query(Empresa).filter(Empresa.cnpj == emp.cnpj).first()
    
    updated_emp = emp.model_copy(update={"razao": "Nova razão"})
    response = client.put(f"/empresas/{res_emp.id}", json=updated_emp.model_dump())
    assert response.status_code == 202
    
    updated_res_emp = db_session.query(Empresa).filter(Empresa.id == res_emp.id).first()
    assert updated_res_emp.razao == "Nova razão"

def test_update_nonexistent_empresa(client):
    emp = create_fake_empresa()
    response = client.put("/empresas/9999", json=emp.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "Empresa com ID 9999 não encontrada"    

def test_delete_empresa(client, db_session):
    emp = create_fake_empresa()
    db_session.add(Empresa(**emp.model_dump()))
    db_session.commit()
    res_emp = db_session.query(Empresa).filter(Empresa.cnpj == emp.cnpj).first()
    response = client.delete(f"/empresas/{res_emp.id}")
    assert response.status_code == 202
    deleted_emp = db_session.query(Empresa).filter(Empresa.id == res_emp.id).first()
    assert deleted_emp is None

def test_delete_nonexistent_empresa(client):
    response = client.delete("/empresas/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Empresa com ID 9999 não encontrada"