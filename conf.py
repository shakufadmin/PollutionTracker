LIMITS = {
    "PM10": 37.5,
    "NO2": 200,
    "O3": 140,
    "SO2": 350,
    "Benzene": 3.9
}

STATION_MAPPING = {426: 'מצפה נטופה (אבן וסיד)', 334: 'ניידת - 2 רכבת ישראל (רכבת ישראל)',
                   538: 'בית העמק (מחצבת אושרת)', 427: 'טורעאן החדשה (אבן וסיד)', 537: 'געתון (מחצבת אושרת)',
                   536: 'כחל (מחצבות כפר גלעדי)', 11: 'גליל מערבי (המשרד להגנת הסביבה)',
                   326: 'כפר מסריק החדשה (המשרד להגנת הסביבה)', 47: 'ניידת -  2 (המשרד להגנת הסביבה)',
                   28: 'כפר מסריק 1 (המשרד להגנת הסביבה)', 387: 'מכללת תל חי (המשרד להגנת הסביבה)',
                   501: 'איבטין (חוצה ישראל)', 354: 'ד.עכו - חיפה (המשרד להגנת הסביבה)',
                   533: 'משרד הרישוי הישן (איגוד ערים חיפה)', 189: 'עצמאות חיפה (המשרד להגנת הסביבה)',
                   324: 'רגבים (איגוד ערים חיפה)', 137: 'קריית טבעון (איגוד ערים חיפה)',
                   86: 'נווה שאנן (איגוד ערים חיפה)', 380: 'דרום (איגוד ערים חיפה)',
                   517: 'נחל הקישון (איגוד ערים חיפה)', 91: 'שוק (איגוד ערים חיפה)', 92: 'קריית ים (איגוד ערים חיפה)',
                   393: 'חורב (איגוד ערים חיפה)', 87: 'נשר (איגוד ערים חיפה)', 93: 'קריית שפרינצק (איגוד ערים חיפה)',
                   344: 'ניידת חיפה (איגוד ערים חיפה)', 136: 'אחוזה (איגוד ערים חיפה)',
                   391: 'הרצל - בלפור (איגוד ערים חיפה)', 98: 'כפר חסידים (איגוד ערים חיפה)',
                   69: 'פארק הכרמל (חברת חשמל)', 90: 'אינשטיין (חברת חשמל)', 382: 'נווה גנים (איגוד ערים חיפה)',
                   97: 'קריית בנימין (איגוד ערים חיפה)', 68: 'כרמל צרפתי (חברת חשמל)',
                   322: 'ניידת - 4 (המשרד להגנת הסביבה)', 80: 'מרכז הכרמל (חברת חשמל)',
                   96: "צ'ק פוסט (איגוד ערים חיפה)", 499: 'קרית חיים - מערבית (איגוד ערים חיפה)', 29: 'קקל (חברת חשמל)',
                   88: 'מרכז העיר (איגוד ערים חיפה)', 1: 'עפולה (המשרד להגנת הסביבה)',
                   73: 'דחי (תחנת הכוח MRC(אלון תבור))', 72: 'דברת (תחנת הכוח MRC(אלון תבור))',
                   539: 'אחוזת ברק (תחנת הכוח MRC(אלון תבור))', 147: 'עין דור (תחנת הכוח MRC(אלון תבור))',
                   103: 'זכרון יעקב (None)', 472: 'נחשולים (איגוד ערים שרון-כרמל)',
                   140: 'טורבינת הגז קיסריה (חברת חשמל)', 110: 'כרם מהר"ל (איגוד ערים שרון-כרמל)',
                   375: 'כפר סבא (המשרד להגנת הסביבה)', 113: 'כביש 65 (איגוד ערים שרון-כרמל)',
                   452: 'מעיין צבי - איגוד (איגוד ערים שרון-כרמל)', 341: 'כפר הנוער שפיה (אבן וסיד)',
                   309: 'אום אל קוטוף (מחצבות)', 108: 'גן שמואל (איגוד ערים שרון-כרמל)',
                   109: 'המעפיל (איגוד ערים שרון-כרמל)', 455: 'חוף דור (נובל אנרגיה)',
                   114: 'מגל (איגוד ערים שרון-כרמל)', 308: 'ברטעה ישנה (מחצבות)',
                   454: 'ברקאי החדשה (איגוד ערים שרון-כרמל)', 456: 'מעיין צבי - נובל (נובל אנרגיה)',
                   505: 'חריש (המשרד להגנת הסביבה)', 100: 'אזור התעשייה (איגוד ערים שרון-כרמל)',
                   106: 'אתר החדרה נחלי מנשה (איגוד ערים שרון-כרמל)', 102: 'אליקים (איגוד ערים שרון-כרמל)',
                   107: 'גבעת עדה (איגוד ערים שרון-כרמל)', 321: 'קריית השרון (איגוד ערים שרון-כרמל)',
                   99: 'בית אליעזר (איגוד ערים שרון-כרמל)', 159: 'ברקאי - ישנה (איגוד ערים אשדוד)',
                   453: 'מוזיאון ראלי (איגוד ערים שרון-כרמל)', 398: 'ניידת - 8, אתר חפציבה (המשרד להגנת הסביבה)',
                   105: 'אליכין (איגוד ערים שרון-כרמל)', 112: 'עמיקם (איגוד ערים שרון-כרמל)',
                   305: 'ניידת קטנה (המשרד להגנת הסביבה)', 104: 'פרדס חנה (איגוד ערים שרון-כרמל)',
                   84: 'תחנת הכוח אורות רבין (חברת חשמל)', 154: 'רחוב אחוזה (המשרד להגנת הסביבה)',
                   111: 'דליית אל כרמל (איגוד ערים שרון-כרמל)', 428: 'קרון איגוד שרון-כרמל 2 (איגוד ערים שרון-כרמל)',
                   378: 'קציר (חברת חשמל)', 401: 'חפציבה (איגוד ערים שרון-כרמל)',
                   462: "ניידת נובל אנרג'י (נובל אנרגיה)", 46: 'ניידת -1 (המשרד להגנת הסביבה)', 416: 'ברטעה (מחצבות)',
                   3: 'אריאל (המשרד להגנת הסביבה)', 357: 'בני עטרות (רשות שדות התעופה)', 40: 'יד רמבם 1 (נשר)',
                   7: 'בית שמש (המשרד להגנת הסביבה)', 371: 'אור יהודה (רשות שדות התעופה)', 64: 'מודיעין (חברת חשמל)',
                   338: 'יד רמב"ם החדשה (נשר)', 78: 'אחיסמך (חברת חשמל)', 32: 'רחובות (המשרד להגנת הסביבה)',
                   510: 'רובע א (דנה הנדסה)', 465: 'אלעד (מחצבת מגדל צדק)', 77: 'כפר שמואל (חברת חשמל)',
                   31: 'מודיעין (המשרד להגנת הסביבה)', 473: 'עינת (מחצבת מגדל צדק)',
                   397: 'ניידת - 7 (המשרד להגנת הסביבה)', 76: 'כרמי יוסף (חברת חשמל)',
                   367: 'בית חשמונאי (בעלות משותפת)', 513: 'שכונת האמנים (נשר)', 348: 'תחנת רכבת וולפסון (רכבת ישראל)',
                   56: 'מכבי אש (חברת חשמל)', 19: 'גבעתיים (המשרד להגנת הסביבה)', 2: 'רחוב לחי (המשרד להגנת הסביבה)',
                   528: 'איילון (נתיבי איילון)', 339: 'ניידת - 5 (המשרד להגנת הסביבה)',
                   120: 'ניידת 1 אשדוד - לא פעילה (איגוד ערים אשדוד)', 386: 'תחנת רכבת קוממיות (רכבת ישראל)',
                   53: 'רחוב גיסין (המשרד להגנת הסביבה)', 385: 'תחנת רכבת יוספטל (רכבת ישראל)',
                   170: 'רחוב יפת (המשרד להגנת הסביבה)', 24: 'חולון (המשרד להגנת הסביבה)',
                   139: 'רחוב הרצל (המשרד להגנת הסביבה)', 346: 'תחנת רכבת השלום (רכבת ישראל)',
                   384: 'תחנת רכבת ההגנה (רכבת ישראל)', 55: 'שיכון בבלי (חברת חשמל)',
                   414: 'רחוב לוינסקי (תחנה מרכזית תל אביב)', 406: 'שכונת המשתלה (חברת חשמל)',
                   39: 'אוניברסיטה (המשרד להגנת הסביבה)', 34: 'כביש 4 (המשרד להגנת הסביבה)',
                   79: 'תורן רמת השרון (חברת חשמל)', 33: "רחוב ז'בוטינסקי (המשרד להגנת הסביבה)",
                   54: 'יד לבנים (חברת חשמל)', 59: 'הצפון החדש (חברת חשמל)', 82: 'לב תל אביב (חברת חשמל)',
                   26: 'רחוב יהודה המכבי (המשרד להגנת הסביבה)', 60: 'שיכון ל (חברת חשמל)',
                   13: 'בקעה (המשרד להגנת הסביבה)', 36: 'כיכר ספרא (המשרד להגנת הסביבה)',
                   458: 'רחוב דבורה הנביאה (המשרד להגנת הסביבה)',
                   310: 'רציף 10 תחנה מרכזית (התחנה המרכזית בירושלים ניהול)', 337: 'ניידת - 6 (המשרד להגנת הסביבה)',
                   509: 'מלכי ישראל (המשרד להגנת הסביבה)', 5: 'רחוב בר אילן (המשרד להגנת הסביבה)',
                   328: 'אזור תעשייה עטרות (עיריית ירושלים)', 193: 'רוממה (התחנה המרכזית בירושלים ניהול)',
                   21: 'גוש עציון (המשרד להגנת הסביבה)', 182: 'לוט (מפעלי ים המלח)', 184: 'נאות הכיכר (מפעלי ים המלח)',
                   183: 'נחל אשלים (מפעלי ים המלח)', 467: 'לב אשדוד (איגוד ערים אשדוד)',
                   468: 'אביגדור (תחנת כוח באר טוביה)', 121: 'רובע טו (איגוד ערים אשדוד)',
                   118: 'קבוצת יבנה (איגוד ערים אשדוד)', 160: 'שמשון (בעלות משותפת)', 65: 'יבנה (חברת חשמל)',
                   124: 'קריית גת (איגוד ערים אשקלון)', 126: 'שדרות (איגוד ערים אשקלון)',
                   125: 'קריית מלאכי (איגוד ערים אשקלון)', 116: 'גן יבנה (איגוד ערים אשדוד)', 379: 'זיקים (קצאא)',
                   117: 'גדרה (איגוד ערים אשדוד)', 511: 'קבוצת יבנה מערב (איגוד ערים אשדוד)',
                   307: 'אגן כימיקלים (אדמה אגן)', 115: 'אזור תעשייה קלה (איגוד ערים אשדוד)',
                   353: 'ניר גלים 2 (אדמה אגן)', 130: 'כרמיה (איגוד ערים אשקלון)', 365: 'בני דרום (איגוד ערים אשדוד)',
                   122: 'יד בנימין (איגוד ערים אשדוד)', 131: 'ארז (איגוד ערים אשקלון)',
                   469: 'תימורים (תחנת כוח באר טוביה)', 123: 'גן הורדים (איגוד ערים אשקלון)',
                   129: 'ניר ישראל (איגוד ערים אשקלון)', 128: 'שדה יואב (איגוד ערים אשקלון)',
                   61: 'ניר גלים 1 (חברת חשמל)', 383: 'רובע ט"ו החדשה (איגוד ערים אשדוד)',
                   535: 'איזור תעשייה צפוני (איגוד ערים אשדוד)', 127: 'גברעם (איגוד ערים אשקלון)',
                   423: 'פארק לכיש (איגוד ערים אשדוד)', 85: 'לוזית (חברת חשמל)', 156: 'אורט (איגוד ערים אשדוד)',
                   531: 'פלוגות (תחנת כוח או.פי.סי. צומת אנרגיה)', 157: 'יהלום (איגוד ערים אשדוד)',
                   306: 'מבקיעים (איגוד ערים אשקלון)', 71: 'כפר מנחם (חברת חשמל)', 63: 'גן דרום (חברת חשמל)',
                   405: 'שדרות ירושלים (איגוד ערים אשדוד)', 81: 'בת הדר (חברת חשמל)',
                   331: 'שכונת ההרחבה (איגוד ערים אשקלון)', 532: 'רובע הבנים (תחנת כוח או.פי.סי. צומת אנרגיה)',
                   119: 'בניה (איגוד ערים אשדוד)', 498: 'כפר נופש חיילים (נובל אנרגיה)',
                   132: 'קריית ההדרכה (מועצה נאות חובב)', 138: 'נחל בקע (מועצה נאות חובב)',
                   134: 'שגב שלום (מועצה נאות חובב)', 133: 'פזורה (מועצה נאות חובב)', 6: 'שכונה ו (המשרד להגנת הסביבה)',
                   345: 'גבעת התצפית (מועצה נאות חובב)', 158: 'נגב מזרחי (המשרד להגנת הסביבה)',
                   135: 'ירוחם (מועצה נאות חובב)', 530: 'כסייפה (המשרד להגנת הסביבה)',
                   186: 'נאות חובב דרום (מועצה נאות חובב)', 75: 'גבעת שמן (חברת חשמל)',
                   187: 'נאות חובב מזרח (מועצה נאות חובב)', 188: 'נאות חובב צפון (מועצה נאות חובב)',
                   417: 'אשלים (תחנת כוח אשלים)', 349: 'אולפנת בני עקיבא (מישור רותם)', 74: 'מחנה נתן (חברת חשמל)',
                   185: 'נאות חובב מרכזית (מועצה נאות חובב)', 400: 'קטורה (המשרד להגנת הסביבה)',
                   377: 'בית ספר גולדווטר (חברת חשמל)', 141: 'מש\'\' אילת חח"י (חברת חשמל)',
                   304: 'שכונת שחמון (נמל אילת)'}