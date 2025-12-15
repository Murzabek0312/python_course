from src.latex_generator import gen_latex, gen_latex_image

def main():
    students_data = [
        ["Алиса", "20", "Москва", "4.5"],
        ["Борис", "22", "Санкт-Петербург", "4.2"],
        ["Виктория", "21", "Новосибирск", "4.8"],
        ["Дмитрий", "23", "Екатеринбург", "4.0"],
        ["Елена", "20", "Казань", "4.6"],
    ]

    latex_code = gen_latex(students_data)
    image_code = gen_latex_image("/Users/msuyundikov/Desktop/Снимок экрана 2025-12-14 в 23.46.35.png")

    latex_content = latex_code.replace(
        "\\end{document}",
        f"\n\n{image_code}\n\n\\end{{document}}"
    )

    with open('example-latex.tex', 'w', encoding='utf-8') as f:
        f.write(latex_content)

if __name__ == "__main__":
    main()
