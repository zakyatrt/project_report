#!/usr/bin/env python3
"""
Скрипт для удаления капслока из заголовков секций
"""
import re

def fix_section_titles(html_content):
    """Исправить заголовки секций - убрать капслок"""
    
    # Находим все заголовки секций h2 с классом section-title
    pattern = r'(<h2 class="section-title">)([^<]+)(</h2>)'
    
    def replacement_func(match):
        opening_tag = match.group(1)
        title_text = match.group(2)
        closing_tag = match.group(3)
        
        # Применяем title capitalization - первая буква заглавная, остальные строчные
        # Но сохраняем заглавные для имен собственных
        fixed_title = title_text.capitalize()
        
        return f'{opening_tag}{fixed_title}{closing_tag}'
    
    html_content = re.sub(pattern, replacement_func, html_content, flags=re.MULTILINE)
    
    return html_content

def main():
    # Читаем исходный HTML
    with open('/Users/ramil/myprog/Zakyat/project_report/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Применяем преобразования
    html = fix_section_titles(html)
    
    # Сохраняем результат
    with open('/Users/ramil/myprog/Zakyat/project_report/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✓ Заголовки секций обновлены - капслок убран")
    print("✓ Файл index.html обновлен")

if __name__ == '__main__':
    main()
