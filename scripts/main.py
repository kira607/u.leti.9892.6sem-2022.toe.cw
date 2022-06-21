import helpers
import latex


def get_variants_table():
    c = (
        '114 -- ИН $ u_1 $;'
        '224 -- $ R_н = 1 $;'
        '313 -- $ R_3 = 2 $;'
        '434 -- $ R_4 = 2 $;'
        '513 -- $ L_5 = 0.5 $;'
        '632 -- $ L_6 = 1 $;'
    )
    table = latex.LatexTable(
        2, 'c', caption="Цепь",
        caption_pos='bottom', label='circ',
    )
    table.set_header('Вариант', 'Цепь')
    table.add_row('1', c)
    return table.render()

def get_task_plot():
    pic = latex.LatexPicture(
        'task_plot',
        'Форма входного сигнала',
        'task_plot',
    )
    return pic.render()

def overlay_method():
    items=[]
    for i in (1, 2, 3):
        pic = latex.LatexPicture(
            f'circ_overlay_{i}',
            f'Метод наложения - {i}',
            f'circ_overlay_{i}',
        )
        m = "'" * i
        p = f'$ u{m}_{{L_5}} = ... $\n\n$ u{m}_{{L_6}} = ... $'
        item = '\n\n'.join((f'\\item Из схемы замещения на рис. \\ref{{{pic.label}}}:', p, pic.render()))
        items.append(item)
    items = "\n\n".join(items)
    return f'\\begin{{enumerate}}\n{items}\n\\end{{enumerate}}'

def main():
    print(overlay_method())


if __name__ == '__main__':
    main()
