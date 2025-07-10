from app.models.metricas import Metrica
from tests.factories import create_fake_metricas

def test_create_metricas(client):
    metricas = create_fake_metricas()
    response = client.post("/metricas", json=metricas.model_dump())
    assert response.status_code == 201

def test_create_metricas_with_existing_competencia(client, db_session):
    metricas = create_fake_metricas()
    db_session.add(Metrica(**metricas.model_dump()))
    db_session.commit()
    duplicate_metricas = metricas.model_copy()
    response = client.post("/metricas", json=duplicate_metricas.model_dump())
    assert response.status_code == 409
    assert f"Já existem métricas para o CNES {metricas.cnes} na competência de {metricas.mes}/{metricas.ano}." in response.json()["detail"]

def test_get_metrica(client, db_session):
    metricas = create_fake_metricas()
    db_session.add(Metrica(**metricas.model_dump()))
    db_session.commit()
    res_metrica = db_session.query(Metrica).filter(Metrica.cnes == metricas.cnes,
                                                   Metrica.ano == metricas.ano,
                                                   Metrica.mes == metricas.mes).first()
    assert res_metrica is not None
    response = client.get(f"/metricas/{res_metrica.cnes}/{res_metrica.ano}/{res_metrica.mes}")
    assert response.status_code == 200
        
def test_get_nonexistent_metrica(client):
    response = client.get("/metricas/9999/9999/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Não foram encontradas métricas para o CNES 9999 na competência de 99/9999."

def test_update_metrica(client, db_session):
    metricas = create_fake_metricas()
    db_session.add(Metrica(**metricas.model_dump()))
    db_session.commit()
    res_metrica = db_session.query(Metrica).filter(Metrica.cnes == metricas.cnes,
                                                   Metrica.ano == metricas.ano,
                                                   Metrica.mes == metricas.mes).first()    
    updated_metrica = metricas.model_copy(update={"partos_vag": 100})
    response = client.put(f"/metricas/{res_metrica.cnes}/{res_metrica.ano}/{res_metrica.mes}", json=updated_metrica.model_dump(exclude={"cnes", "ano", "mes"}))
    assert response.status_code == 202    
    updated_res_metrica = db_session.query(Metrica).filter(Metrica.cnes == metricas.cnes,
                                                   Metrica.ano == metricas.ano,
                                                   Metrica.mes == metricas.mes).first()
    assert updated_res_metrica.partos_vag == 100

def test_update_nonexistent_metrica(client):
    metricas = create_fake_metricas()
    response = client.put("/metricas/9999/9999/99", json=metricas.model_dump(exclude={"cnes", "ano", "mes"}))
    assert response.status_code == 404
    assert response.json()["detail"] == "Não foram encontradas métricas para o CNES 9999 na competência de 99/9999."

def test_delete_metrica(client, db_session):
    metricas = create_fake_metricas()
    db_session.add(Metrica(**metricas.model_dump()))
    db_session.commit()
    res_metrica = db_session.query(Metrica).filter(Metrica.cnes == metricas.cnes,
                                                   Metrica.ano == metricas.ano,
                                                   Metrica.mes == metricas.mes).first()
    response = client.delete(f"/metricas/{res_metrica.cnes}/{res_metrica.ano}/{res_metrica.mes}")
    assert response.status_code == 202
    deleted_kpi = db_session.query(Metrica).filter(Metrica.cnes == metricas.cnes,
                                                   Metrica.ano == metricas.ano,
                                                   Metrica.mes == metricas.mes).first()
    assert deleted_kpi is None

def test_delete_nonexistent_metrica(client):
    response = client.delete("/metricas/9999/9999/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Não foram encontradas métricas para o CNES 9999 na competência de 99/9999."