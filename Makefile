# Atalhos para as ferramentas em tools/. Apresentar não precisa de nada disto: basta abrir o presentation.html.
PY ?= python3

.PHONY: build cue check layout links pdf bundle dist qr serve deps

build:            ## src/ → presentation.html
	$(PY) tools/build.py

cue:              ## docs/CUE-SHEET.md a partir dos slides (tempos, cliques, notas)
	$(PY) tools/make_cue_sheet.py

check:           ## o que o CI roda: presentation.html em dia com src/ + checagem de layout
	$(PY) tools/build.py --check
	$(PY) tools/check_layout.py

layout: build    ## texto vazando, sobreposto ou fora da forma, e erros de JS
	$(PY) tools/check_layout.py

links:            ## testa os links das referências (precisa de internet)
	$(PY) tools/check_links.py

pdf: build       ## dist/recnplay-2026.pdf
	$(PY) tools/export_pdf.py

bundle: build    ## dist/recnplay-2026.html (arquivo único)
	$(PY) tools/bundle.py

dist: bundle pdf ## backup completo para o dia do evento

qr:               ## assets/qr.svg para outra URL: make qr URL=https://…
	$(PY) tools/make_qr.py $(URL)

serve:            ## http://localhost:8000/presentation.html
	$(PY) -m http.server 8000

deps:             ## dependências das ferramentas (o deck em si não precisa de nenhuma)
	pip install -r requirements.txt && $(PY) -m playwright install chromium
