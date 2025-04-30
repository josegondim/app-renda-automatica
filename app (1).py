
import json
import streamlit as st

# Carregar o plano de 90 dias
with open("plano_90_dias_completo.json", "r", encoding="utf-8") as f:
    plano = json.load(f)

st.set_page_config(page_title="Renda Automática com IA", layout="centered")

st.title(plano["plano_nome"])
st.subheader("Plano de 90 dias para renda automática com IA")
st.markdown(f"**Público-alvo:** {plano['publico_alvo']}")

# Barra lateral com dias
dias = [f"Dia {item['dia']}" for item in plano["tarefas_diarias"]]
selecionado = st.sidebar.selectbox("Escolha o dia:", dias)

# Mostrar tarefa do dia
dia_atual = int(selecionado.split()[1])
tarefa = next((item["tarefa"] for item in plano["tarefas_diarias"] if item["dia"] == dia_atual), "Tarefa não encontrada")

st.write(f"### Tarefa do {selecionado}")
st.write(tarefa)

# Marcar como concluído (simulação)
if st.button("Marcar como concluído"):
    st.success("Tarefa marcada como concluída (simulação)")
