"""Crea una función dias_para(fecha_str) que reciba una fecha en formato "YYYY-MM-DD" y devuelva cuántos días faltan desde hoy"""
from datetime import datetime


def dias_para(fecha_str):
    fecha_objetivo = datetime.strptime(fecha_str, "%Y-%m-%d")
    hoy = datetime.now()
    diff = fecha_objetivo-hoy
    print(f"Faltan {diff.days} dias para {fecha_str}")


dias_para("2025-12-31")
