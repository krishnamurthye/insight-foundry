from radon.complexity import cc_visit


def get_complexity_metrics(code, language):
    if language.lower() != "python":
        return []
    try:
        return [{"name": f.name, "complexity": f.complexity} for f in cc_visit(code)]
    except Exception:
        return []
