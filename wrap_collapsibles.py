#!/usr/bin/env python3
"""
Скрипт для обертывания финансовых документов и таблиц в сворачиваемые блоки
"""
import re

def wrap_financial_docs(html_content):
    """Обернуть блоки финансовых документов в details/summary"""
    
    # Pattern: <div class="docs-list">...<div class="bold">Финансовые документы:</div>...<ol>...</ol></div>
    pattern = r'(<div class="docs-list">)\s*(<div class="bold">Финансовые документы:</div>)\s*(<ol>.*?</ol>)\s*(</div>)'
    
    replacement = r'''<details>
                <summary>Финансовые документы</summary>
                \1\3\4
            </details>'''
    
    html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
    
    return html_content

def wrap_tables(html_content):
    """Обернуть таблицы в details/summary"""
    
    # Pattern: <div class="table-wrapper">... (опциональное название) <table>...</table></div>
    pattern = r'(<div class="table-wrapper">)\s*(?:(<div class="bold center-text"[^>]*>)([^<]+)(</div>))?\s*(<table>.*?</table>)\s*(</div>)'
    
    def replacement_func(match):
        wrapper_start = match.group(1)
        title_open = match.group(2) or ''
        title_text = match.group(3) or 'Таблица'
        title_close = match.group(4) or ''
        table_content = match.group(5)
        wrapper_end = match.group(6)
        
        # Если есть заголовок, используем его для summary
        if title_text:
            summary_text = title_text.strip()
        else:
            summary_text = 'Таблица'
        
        return f'''<details>
                <summary>{summary_text}</summary>
                {wrapper_start}{table_content}{wrapper_end}
            </details>'''
    
    html_content = re.sub(pattern, replacement_func, html_content, flags=re.DOTALL)
    
    return html_content

def main():
    # Читаем исходный HTML
    with open('/Users/ramil/myprog/Zakyat/project_report/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Применяем преобразования
    html = wrap_financial_docs(html)
    html = wrap_tables(html)
    
    # Сохраняем результат
    with open('/Users/ramil/myprog/Zakyat/project_report/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✓ Финансовые документы и таблицы обернуты в сворачиваемые блоки")
    print("✓ Файл index.html обновлен")

if __name__ == '__main__':
    main()
