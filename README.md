# MCU_Relay (relay_modbus_lib)

Python-Bibliothek zum Steuern einer MCU-basierten Relay-Matrix (z. B. Waveshare 32 Relaymatrix) über Modbus/Serial-Schnittstellen. Die Bibliothek bietet einfache Funktionen zum Ein-/Ausschalten von Relais, zum Abfragen des Relaiszustands und zur Integration in Testprojekte.

Kurzbeschreibung
- Ziel: Eine kleine, wiederverwendbare API, um Relais über eine MCU/Modbus-Schnittstelle zu schalten.
- Fokus: Einfachheit, lokale Entwicklung und Integration in Beispielprojekte im Workspace.

Projektstruktur
- `relay_modbus_lib/relay.py` – Haupt-API zum Schalten der Relais
- `relay_modbus_lib/utils.py` – Hilfsfunktionen

Voraussetzungen
- Python 3.10+
- Serielle Schnittstelle oder ein Modbus-zu-Serial-Gateway (z. B. USB-Serial Adapter)

Installation (Entwicklung)
1. Virtuelle Umgebung anlegen und aktivieren:

	python -m venv .venv
	source .venv/bin/activate

2. Installieren (editable), ausgehend vom Workspace-Layout:

	pip install -e .

3. Für die lokale Integration im benachbarten Projekt (z. B. `test_RFM`) ggf. editable installieren:

	pip install -e ../relay_modbus_lib

Verwendung (Beispiel)
In Python-Code:

```python
from relay_modbus_lib.relay import RelayController

# Beispiel: initialisieren
rc = RelayController(port='/dev/ttyUSB0', baudrate=19200, slave_id=1)

# Relais 0 einschalten
rc.set_relay(0, True)

# Zustand abfragen
state = rc.get_relay(0)
print('Relay 0:', state)
```

Tests
- Testfälle finden sich im übergeordneten Workspace-Projekt `test_RFM/tests/`.
- Lokale Tests mit `pytest` ausführen:

	pytest -q

Entwicklung
- API-Änderungen bitte rückwärtskompatibel halten.
- Ergänze Unit-Tests in `tests/` für neue Funktionalität.

FAQ / Troubleshooting
- Verbindung schlägt fehl: Überprüfe `port`, `baudrate` und ob das Gerät vom System erkannt wird (`dmesg`, `ls /dev/tty*`).
- Falsche Adressen: Stelle sicher, dass `slave_id` mit der MCU übereinstimmt.

Contributing
- Fork, branch, commit und PR mit Beschreibung der Änderungen und Tests.

Lizenz
- Keine Lizenzdatei im Repo. Bitte bei Bedarf eine passende Lizenz ergänzen.

Kontakt
- Bei Fragen: Issue im Repo eröffnen.

