import os
from pathlib import Path

# Global counters and issue tracking
ERRORS = 0
WARNINGS = 0
ERROR_LIST = []
WARNING_LIST = []
WORKSPACE_ROOT = Path.cwd()


# Convert absolute path to relative path
def _relative_path(path):
    try:
        return str(Path(path).relative_to(WORKSPACE_ROOT))
    except (ValueError, AttributeError):
        return str(path)


# Helper function for logging
def _log(level, file, msg, counter_list):
    rel_file = _relative_path(file)
    counter_list.append((rel_file, msg))
    print(f"::{level} file={rel_file}::{msg}")
    print(f"\033[90m  → {rel_file}: {msg}\033[0m")


# Log error
def error(file, msg):
    global ERRORS
    ERRORS += 1
    _log('error', file, msg, ERROR_LIST)


# Log warning
def warning(file, msg):
    global WARNINGS
    WARNINGS += 1
    _log('warning', file, msg, WARNING_LIST)


# Helper to write issue list with truncation
def _write_issue_list(f, title, issue_list, list_length, item_type):
    f.write(f"### {title}\n")
    for file, msg in issue_list[:list_length]:
        f.write(f"- **{file}**: {msg}\n")
    if len(issue_list) > list_length:
        f.write(f"\n_...und {len(issue_list) - list_length} weitere {item_type} (siehe Logs)_\n")


# Write summary to GitHub Actions summary
def actions_summary():
    summary_file = os.getenv('GITHUB_STEP_SUMMARY')
    if not summary_file:
        return
    
    list_length = 30                    # Limit list length to avoid too long summaries
    with open(summary_file, 'w') as f:
        f.write("# 📋 Ergebnisse des PR-Checks\n\n")
        
        if ERRORS:
            f.write(f"## ❌ Fehlgeschlagen: {ERRORS} Fehler, {WARNINGS} Warnung(en)\n\n")
            _write_issue_list(f, "Fehler", ERROR_LIST, list_length, "Fehler")
            if WARNING_LIST:
                f.write("\n")
                _write_issue_list(f, "Warnungen", WARNING_LIST, list_length, "Warnungen")
        elif WARNINGS:
            f.write(f"## ⚠️ Check bestanden mit {WARNINGS} Warnung(en)\n\n")
            _write_issue_list(f, "Warnungen", WARNING_LIST, list_length, "Warnungen")
        else:
            f.write("## ✅ Alle Checks bestanden!\n\n")
            f.write("Keine Fehler oder Warnungen gefunden. Gute Arbeit! 🎉\n")


# Console summary
def console_summary():
    print("\n" + "="*60)
    if ERRORS:
        print(f"❌ {ERRORS} Fehler und {WARNINGS} Warnung(en) gefunden")
        return 1
    elif WARNINGS:
        print(f"⚠️ Bestanden mit {WARNINGS} Warnung(en)")
    else:
        print("✅ Alle Checks bestanden!")
    return 0