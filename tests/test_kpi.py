from app.models.kpis import Kpi
from tests.factories import create_fake_kpi

def test_create_kpi(client):
    kpi = create_fake_kpi()
    response = client.post("/kpis", json=kpi.model_dump())
    assert response.status_code == 201

def test_create_empresa_with_existing_title(client, db_session):
    kpi = create_fake_kpi()
    # Adiciona empresa original ao banco
    db_session.add(Kpi(**kpi.model_dump()))
    db_session.commit()
    # Tenta cadastrar outra empresa com mesmo cnpj e cnes
    duplicate_kpi = kpi.model_copy()
    response = client.post("/kpis", json=duplicate_kpi.model_dump())
    assert response.status_code == 409
    assert "KPI com este título já existe" in response.json()["detail"]

def test_get_kpi(client, db_session):
    kpi = create_fake_kpi()
    db_session.add(Kpi(**kpi.model_dump()))
    db_session.commit()
    res_kpi = db_session.query(Kpi).filter(Kpi.titulo == kpi.titulo).first()
    assert res_kpi is not None
    response = client.get(f"/kpis/{res_kpi.id}")
    assert response.status_code == 200
        
def test_get_nonexistent_kpi(client):
    response = client.get("/kpis/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "KPI com ID 9999 não encontrado"   

def test_update_kpi(client, db_session):
    kpi = create_fake_kpi()
    db_session.add(Kpi(**kpi.model_dump()))
    db_session.commit()
    res_kpi = db_session.query(Kpi).filter(Kpi.titulo == kpi.titulo).first()
    
    updated_kpi = kpi.model_copy(update={"titulo": "Novo Título"})
    response = client.put(f"/kpis/{res_kpi.id}", json=updated_kpi.model_dump())
    assert response.status_code == 202
    
    updated_res_kpi = db_session.query(Kpi).filter(Kpi.id == res_kpi.id).first()
    assert updated_res_kpi.titulo == "Novo Título"

def test_update_nonexistent_kpi(client):
    kpi = create_fake_kpi()
    response = client.put("/kpis/9999", json=kpi.model_dump())
    assert response.status_code == 404
    assert response.json()["detail"] == "KPI com ID 9999 não encontrado"

def test_delete_kpi(client, db_session):
    kpi = create_fake_kpi()
    db_session.add(Kpi(**kpi.model_dump()))
    db_session.commit()
    res_kpi = db_session.query(Kpi).filter(Kpi.titulo == kpi.titulo).first()
    response = client.delete(f"/kpis/{res_kpi.id}")
    assert response.status_code == 202
    deleted_kpi = db_session.query(Kpi).filter(Kpi.id == res_kpi.id).first()
    assert deleted_kpi is None

def test_delete_nonexistent_kpi(client):
    response = client.delete("/kpis/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "KPI com ID 9999 não encontrado"