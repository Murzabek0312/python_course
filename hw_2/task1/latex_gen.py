def gen_latex(data):
    col_len = len(data[0])

    latex_code = []
    latex_code.append("\\documentclass{article}")
    latex_code.append("\\usepackage[utf8]{inputenc}")
    latex_code.append("\\usepackage[T2A]{fontenc}")
    latex_code.append("\\usepackage[russian]{babel}")

    latex_code.append("\\begin{document}")
    latex_code.append(f"\\begin{{tabular}}{{{col_len} c c c}}")

    for d in data:
        latex_code.append(" & ".join(d) + " \\\\")

    latex_code.append("\\end{tabular}")
    latex_code.append("\\end{document}")

    res = "\n".join(latex_code)

    with open('example-latex.tex', 'w', encoding='utf-8') as f:
        f.write(res)

