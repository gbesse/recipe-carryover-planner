# recipe-carryover-planner

## Français

Ordonner des lots avec contamination et nettoyage dépendant de la transition.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m recipe_carryover_planner examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Recherche exacte par sous-ensembles et dernier lot : coût de nettoyage dirigé, seuil de contamination de la destination et résidu après nettoyage. Retourne l’ordre et chaque nettoyage nécessaire. Contrairement à FabResume, optimise une séquence neuve et non une reprise.

### Limites

12 lots maximum, coût entier, premier lot sans contamination antérieure, une transition de nettoyage déclarée par paire ; aucun modèle chimique ni contrôle machine.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Order batches with transition-dependent contamination and cleaning.

Synthetic data; no network access or secret required.

```sh
python -m recipe_carryover_planner examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Exact subset-and-last-batch search with directed cleaning cost, destination carryover limit and after-clean residue. Returns order and every required cleaning step. Unlike FabResume, optimizes a new sequence rather than recovery.

### Limits

At most 12 batches, integer cost, first batch starts clean, one declared cleaning transition per pair; no chemical model or machine control.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Ordenar lotes con contaminación y limpieza dependientes de la transición.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m recipe_carryover_planner examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Búsqueda exacta por subconjunto y último lote con coste de limpieza dirigido, límite de contaminación del destino y residuo posterior. Devuelve orden y cada limpieza necesaria. A diferencia de FabResume, optimiza una secuencia nueva, no recuperación.

### Límites

Máximo 12 lotes, coste entero, primer lote limpio, una transición de limpieza declarada por par; sin modelo químico ni control de máquina.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.atomicmachines.com/
- https://github.com/gbesse/fabresume
