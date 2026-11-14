from app.utils.arabic import normalize_arabic
FALLBACK = 'عذراً، لم أجد شرحاً معتمداً لهذا الموضوع في قاعدة بيانات PARADOSIS.'
def reply(db, text: str) -> str:
    n = normalize_arabic(text)
    if any(x in n for x in ('السلام عليكم','مرحبا','اهلا')):
        return 'أهلاً بك في PARADOSIS ✝️\n\nأنا مساعدك لاستكشاف وفهم تراث الكنيسة القبطية الأرثوذكسية.\n\nيمكنك سؤالي عن الألحان والطقوس والقداس والمراجع الكتابية والأعياد والتقاليد الكنسية.'
    if any(x in n for x in ('مساعده','ماذا يمكنك','help')):
        return 'يمكنني شرح المحتوى المعتمد عن الألحان والطقوس والصلوات والأعياد والتقاليد والمراجع الكتابية.'
    return FALLBACK
