from pydantic import BaseModel
from typing import Optional, List

class MetricaBase(BaseModel):
    """
    Schema base para métricas, contendo campos que são compartilhados
    entre a criação e a leitura de dados.
    """
    partos_vag: Optional[int] = None
    partos_ces: Optional[int] = None
    cli_sai_ant: Optional[int] = None
    cli_reint: Optional[int] = None
    cir_sai_ant: Optional[int] = None
    cir_reint: Optional[int] = None
    pac_dia: Optional[int] = None
    pcr_eventos: Optional[int] = None
    cli_neo_precoce_sai: Optional[int] = None
    cli_neo_precoce_obitos: Optional[int] = None
    cli_neo_precoce_pac_dia: Optional[int] = None
    cli_neo_tardio_sai: Optional[int] = None
    cli_neo_tardio_obitos: Optional[int] = None
    cli_neo_tardio_pac_dia: Optional[int] = None
    cli_pedi_sai: Optional[int] = None
    cli_pedi_obitos: Optional[int] = None
    cli_pedi_pac_dia: Optional[int] = None
    cli_ad_sai: Optional[int] = None
    cli_ad_obitos: Optional[int] = None
    cli_ad_pac_dia: Optional[int] = None
    cli_idoso_sai: Optional[int] = None
    cli_idoso_obitos: Optional[int] = None
    cli_idoso_pac_dia: Optional[int] = None
    cir_neo_precoce_sai: Optional[int] = None
    cir_neo_precoce_obitos: Optional[int] = None
    cir_neo_precoce_pac_dia: Optional[int] = None
    cir_neo_tardio_sai: Optional[int] = None
    cir_neo_tardio_obitos: Optional[int] = None
    cir_neo_tardio_pac_dia: Optional[int] = None
    cir_pedi_sai: Optional[int] = None
    cir_pedi_obitos: Optional[int] = None
    cir_pedi_pac_dia: Optional[int] = None
    cir_ad_sai: Optional[int] = None
    cir_ad_obitos: Optional[int] = None
    cir_ad_pac_dia: Optional[int] = None
    cir_idoso_sai: Optional[int] = None
    cir_idoso_obitos: Optional[int] = None
    cir_idoso_pac_dia: Optional[int] = None
    total_pac_emerg: Optional[int] = None
    total_tempo_perm_emerg_hr: Optional[int] = None
    pac_emerg_nvl2: Optional[int] = None
    tempo_total_emerg_nvl2_min: Optional[int] = None
    pac_emerg_nvl3: Optional[int] = None
    tempo_total_emerg_nvl3_min: Optional[int] = None
    total_cir_limpas: Optional[int] = None
    cir_com_antibiotico: Optional[int] = None
    total_cir_limpas_ant: Optional[int] = None
    total_infeccoes: Optional[int] = None
    ui_neo_cvc_dia: Optional[int] = None
    ui_neo_infec: Optional[int] = None
    ui_pedi_cvc_dia: Optional[int] = None
    ui_pedi_infec: Optional[int] = None
    ui_ad_cvc_dia: Optional[int] = None
    ui_ad_infec: Optional[int] = None
    uti_neo_cvc_dia: Optional[int] = None
    uti_neo_infec: Optional[int] = None
    uti_pedi_cvc_dia: Optional[int] = None
    uti_pedi_infec: Optional[int] = None
    uti_ad_cvc_dia: Optional[int] = None
    uti_ad_infec: Optional[int] = None
    ui_neo_cvd_dia: Optional[int] = None
    ui_neo_itu: Optional[int] = None
    ui_pedi_cvd_dia: Optional[int] = None
    ui_pedi_itu: Optional[int] = None
    ui_ad_cvd_dia: Optional[int] = None
    ui_ad_itu: Optional[int] = None
    uti_neo_cvd_dia: Optional[int] = None
    uti_neo_itu: Optional[int] = None
    uti_pedi_cvd_dia: Optional[int] = None
    uti_pedi_itu: Optional[int] = None
    uti_ad_cvd_dia: Optional[int] = None
    uti_ad_itu: Optional[int] = None
    cli_total_pac: Optional[int] = None
    cli_profilaxia: Optional[int] = None
    cir_orto_total_pac: Optional[int] = None
    cir_orto_prof: Optional[int] = None
    cir_nao_orto_total_pac: Optional[int] = None
    cir_nao_orto_prof: Optional[int] = None
    quedas_com_dano: Optional[int] = None
    eventos_sentinela: Optional[int] = None

    class Config:
        """Configurações do modelo Pydantic."""
        from_attributes = True
        orm_mode = True

class Metrica(MetricaBase):
    """Schema para a criação de um novo registro de métrica."""
    cnes: int
    ano: int
    mes: int

Metricas = List[Metrica]

class MetricaConfirmaAlteracao(BaseModel):
    cnes: int
    ano: int
    mes: int

    class Config:
        from_attributes = True
        orm_mode = True