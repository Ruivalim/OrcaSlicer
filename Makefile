# OrcaSlicer: fatiador 3D em C++ (fork do Rui, com fixes e plugins próprios)
#
# `make` ou `make help` lista os alvos. Este Makefile é uma fachada: cada alvo
# delega pro build_linux.sh (build do CI, no container Ubuntu 24.04) e pro
# ctest via scripts/run_unit_tests_linux.sh. Regra nova entra com `## descrição`
# na mesma linha pra aparecer no help.

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables --no-builtin-rules --no-print-directory
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

# ---------------------------------------------------------------------------
# Variáveis (?= permite sobrescrever: `make build BUILD_FLAGS=-istrlL`)
# ---------------------------------------------------------------------------

APP ?= orca-slicer

# Flags do build_linux.sh. O padrão usa o toolchain do cache de deps (GCC).
# O CI roda `-istrlL` (Clang + lld); a primeira vez com essa flag rebuilda
# as deps e o app do zero.
BUILD_FLAGS ?= -ist
BUILD       := ./build_linux.sh -g
RUN_BIN     ?= ./build/package/$(APP)

# Cores só quando stdout é um terminal (pipe e CI ficam limpos)
BOLD  :=
CYAN  :=
GREEN :=
RESET :=
ifneq ($(shell [ -t 1 ] && echo tty),)
  BOLD  := $(shell tput bold 2>/dev/null)
  CYAN  := $(shell tput setaf 6 2>/dev/null)
  GREEN := $(shell tput setaf 2 2>/dev/null)
  RESET := $(shell tput sgr0 2>/dev/null)
endif

##@ Geral

.PHONY: help
help: ## Lista os alvos disponíveis
	@awk 'BEGIN { FS = ":.*##"; printf "\n$(BOLD)$(APP)$(RESET)\n\nUso: make $(CYAN)<alvo>$(RESET)\n" } \
	  /^##@/ { printf "\n$(BOLD)%s$(RESET)\n", substr($$0, 5) } \
	  /^[a-zA-Z0-9_.\/-]+:.*?##/ { printf "  $(CYAN)%-18s$(RESET) %s\n", $$1, $$2 } \
	  END { printf "\n" }' $(MAKEFILE_LIST)

.PHONY: setup
setup: ## Compila as dependências no container (deps/build, demora na primeira vez)
	@echo "$(GREEN)▸ setup$(RESET)"
	$(BUILD) -d

##@ Desenvolvimento

.PHONY: run
run: build ## Roda o OrcaSlicer compilado
	@echo "$(GREEN)▸ run$(RESET)"
	$(RUN_BIN)

##@ Qualidade

.PHONY: test
test: ## Compila os testes e roda o ctest no container
	@echo "$(GREEN)▸ test$(RESET)"
	$(BUILD) -t
	./scripts/run_unit_tests_linux.sh

.PHONY: check
check: build test ## Tudo que o CI roda: build e test
	@echo "$(GREEN)✓ check ok$(RESET)"

##@ Build

.PHONY: build
build: ## Compila OrcaSlicer e empacota (padrão -ist; CI usa -istrlL)
	@echo "$(GREEN)▸ build$(RESET)"
	$(BUILD) $(BUILD_FLAGS)

.PHONY: clean
clean: ## Remove os diretórios de build (mantém deps/build)
	@echo "$(GREEN)▸ clean$(RESET)"
	rm -rf build build-dbg build-dbginfo
