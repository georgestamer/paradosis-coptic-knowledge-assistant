from app.utils.arabic import normalize_arabic
from app.services.search_service import find_content
FALLBACK = 'عذراً، لم أجد شرحاً معتمداً لهذا الموضوع في قاعدة بيانات PARADOSIS.\n\nيمكنك تجربة اسم آخر أو كتابة (مساعدة) لمعرفة المواضيع المتاحة.'
def reply(db, text: str) -> str:
    n = normalize_arabic(text)
    if any(x in n for x in ('السلام عليكم','مرحبا','اهلا')):
        return 'أهلاً بك في PARADOSIS ✝️\n\nأنا مساعدك لاستكشاف وفهم تراث الكنيسة القبطية الأرثوذكسية.\n\nيمكنك سؤالي عن الألحان والطقوس والقداس والمراجع الكتابية والأعياد والتقاليد الكنسية.'
    if any(x in n for x in ('مساعده','ماذا يمكنك','help')):
        return 'يمكنني شرح المحتوى المعتمد عن الألحان والطقوس والصلوات والأعياد والتقاليد والمراجع الكتابية.'
    for phrase in ('اشرح','عايز شرح','ممكن تفهمني','معلومات عن','ابحث عن','tell me about'):
        n = n.replace(phrase, ' ')
    content = find_content(db, n) if db is not None else None
    if content is None: return FALLBACK
    refs = '\n'.join(f'• {r.reference_text}' for r in content.references)
    return f'✝️ {content.title}\n\n{content.content}' + (f'\n\n📖 المراجع الكتابية:\n{refs}' if refs else '')
