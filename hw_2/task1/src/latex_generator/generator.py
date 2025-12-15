def gen_latex(data):
    col_len = len(data[0])

    latex_code = []
    latex_code.append("\\documentclass{article}")
    latex_code.append("\\usepackage[utf8]{inputenc}")
    latex_code.append("\\usepackage[T2A]{fontenc}")
    latex_code.append("\\usepackage[russian]{babel}")
    latex_code.append("\\usepackage{graphicx}")

    latex_code.append("\\begin{document}")
    latex_code.append(f"\\begin{{tabular}}{{{' '.join(['c'] * col_len)}}}")

    for d in data:
        latex_code.append(" & ".join(d) + " \\\\")

    latex_code.append("\\end{tabular}")
    latex_code.append("\\end{document}")

    return "\n".join(latex_code)

def gen_latex_image(image_path, width="0.8\\textwidth"):
    return f"\\includegraphics[width={width}]{{{image_path}}}"
