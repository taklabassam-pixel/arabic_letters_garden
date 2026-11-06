import json
import time

# 1. تعريف القائمة أولاً بكل الحروف والكلمات
alphabet_data = [
    # حرف الألف
    {"letter": "أَ", "letterName": "أَلِفُنْ", "sound": "أَ", "word": "أَسَدٌ", "id": "alif_fatha"},
    {"letter": "أُ", "letterName": "أَلِفُنْ", "sound": "أُ", "word": "أُذُنٌ", "id": "alif_damma"},
    {"letter": "إِ", "letterName": "أَلِفُنْ", "sound": "إِ", "word": "إِبْرِيقٌ", "id": "alif_kasra"},
    
    # حرف الباء
    {"letter": "بَ", "letterName": "بَاءُنْ", "sound": "بَ", "word": "بَطَّةٌ", "id": "baa_fatha"},
    {"letter": "بُ", "letterName": "بَاءُنْ", "sound": "بُ", "word": "بُرْتُقَالٌ", "id": "baa_damma"},
    {"letter": "بِ", "letterName": "بَاءُنْ", "sound": "بِ", "word": "بِطِّيخٌ", "id": "baa_kasra"},
    
    # حرف التاء
    {"letter": "تَ", "letterName": "تَاءُنْ", "sound": "تَ", "word": "تَمْرٌ", "id": "taa_fatha"},
    {"letter": "تُ", "letterName": "تَاءُنْ", "sound": "تُ", "word": "تُفَّاحٌ", "id": "taa_damma"},
    {"letter": "تِ", "letterName": "تَاءُنْ", "sound": "تِ", "word": "تِمْسَاحٌ", "id": "taa_kasra"},
    
    # حرف الثاء
    {"letter": "ثَ", "letterName": "ثَاءُنْ", "sound": "ثَ", "word": "ثَعْلَبٌ", "id": "thaa_fatha"},
    {"letter": "ثُ", "letterName": "ثَاءُنْ", "sound": "ثُ", "word": "ثُعْبَانٌ", "id": "thaa_damma"},
    {"letter": "ثِ", "letterName": "ثَاءُنْ", "sound": "ثِ", "word": "ثِيَابٌ", "id": "thaa_kasra"},
    
    # حرف الجيم
    {"letter": "جَ", "letterName": "جِيمُنْ", "sound": "جَ", "word": "جَمَلٌ", "id": "jeem_fatha"},
    {"letter": "جُ", "letterName": "جِيمُنْ", "sound": "جُ", "word": "جُبْنٌ", "id": "jeem_damma"},
    {"letter": "جِ", "letterName": "جِيمُنْ", "sound": "جِ", "word": "جِسْرٌ", "id": "jeem_kasra"},
    
    # حرف الحاء
    {"letter": "حَ", "letterName": "حَاءُنْ", "sound": "حَ", "word": "حَمَامَةٌ", "id": "haa_fatha"},
    {"letter": "حُ", "letterName": "حَاءُنْ", "sound": "حُ", "word": "حُدودٌ", "id": "haa_damma"},
    {"letter": "حِ", "letterName": "حَاءُنْ", "sound": "حِ", "word": "حِصَانٌ", "id": "haa_kasra"},
    
    # حرف الخاء
    {"letter": "خَ", "letterName": "خَاءُنْ", "sound": "خَ", "word": "خَرُوفٌ", "id": "khaa_fatha"},
    {"letter": "خُ", "letterName": "خَاءُنْ", "sound": "خُ", "word": "خُبْزٌ", "id": "khaa_damma"},
    {"letter": "خِ", "letterName": "خَاءُنْ", "sound": "خِ", "word": "خِرَافٌ", "id": "khaa_kasra"},
    
    # حرف الدال
    {"letter": "دَ", "letterName": "دَالُنْ", "sound": "دَ", "word": "دَرَّاجَةٌ", "id": "dal_fatha"},
    {"letter": "دُ", "letterName": "دَالُنْ", "sound": "دُ", "word": "دُبٌّ", "id": "dal_damma"},
    {"letter": "دِ", "letterName": "دَالُنْ", "sound": "دِ", "word": "دِيكٌ", "id": "dal_kasra"},
    
    # حرف الذال
    {"letter": "ذَ", "letterName": "ذَالُنْ", "sound": "ذَ", "word": "ذَرَّةٌ", "id": "dhal_fatha"},
    {"letter": "ذُ", "letterName": "ذَالُنْ", "sound": "ذُ", "word": "ذُبَابَةٌ", "id": "dhal_damma"},
    {"letter": "ذِ", "letterName": "ذَالُنْ", "sound": "ذِ", "word": "ذِئْبٌ", "id": "dhal_kasra"},
    
    # حرف الراء
    {"letter": "رَ", "letterName": "رَاءُنْ", "sound": "رَ", "word": "رَفٌّ", "id": "raa_fatha"},
    {"letter": "رُ", "letterName": "رَاءُنْ", "sound": "رُ", "word": "رُمَّانٌ", "id": "raa_damma"},
    {"letter": "رِ", "letterName": "رَاءُنْ", "sound": "رِ", "word": "رِجْلٌ", "id": "raa_kasra"},
    
    # حرف الزاي
    {"letter": "زَ", "letterName": "زَايُنْ", "sound": "زَ", "word": "زَرَافَةٌ", "id": "zay_fatha"},
    {"letter": "زُ", "letterName": "زَايُنْ", "sound": "زُ", "word": "زُهْرِيَّةٌ", "id": "zay_damma"},
    {"letter": "زِ", "letterName": "زَايُنْ", "sound": "زِ", "word": "زِرٌّ", "id": "zay_kasra"},
    
    # حرف السين
    {"letter": "سَ", "letterName": "سِينُنْ", "sound": "سَ", "word": "سَمَكَةٌ", "id": "seen_fatha"},
    {"letter": "سُ", "letterName": "سِينُنْ", "sound": "سُ", "word": "سُكَّرٌ", "id": "seen_damma"},
    {"letter": "سِ", "letterName": "سِينُنْ", "sound": "سِ", "word": "سِنْجَابٌ", "id": "seen_kasra"},
    
    # حرف الشين
    {"letter": "شَ", "letterName": "شِينُنْ", "sound": "شَ", "word": "شَمْسٌ", "id": "sheen_fatha"},
    {"letter": "شُ", "letterName": "شِينُنْ", "sound": "شُ", "word": "شُرْطِيٌّ", "id": "sheen_damma"},
    {"letter": "شِ", "letterName": "شِينُنْ", "sound": "شِ", "word": "شِفَاهٌ", "id": "sheen_kasra"},
    
    # حرف الصاد
    {"letter": "صَ", "letterName": "صَادُنْ", "sound": "صَ", "word": "صَقْرٌ", "id": "saad_fatha"},
    {"letter": "صُ", "letterName": "صَادُنْ", "sound": "صُ", "word": "صُورَةٌ", "id": "saad_damma"},
    {"letter": "صِ", "letterName": "صَادُنْ", "sound": "صِ", "word": "صِيصَانٌ", "id": "saad_kasra"},
    
    # حرف الضاد
    {"letter": "ضَ", "letterName": "ضَادُنْ", "sound": "ضَ", "word": "ضَبُعٌ", "id": "daad_fatha"},
    {"letter": "ضُ", "letterName": "ضَادُنْ", "sound": "ضُ", "word": "ضُبٌّ", "id": "daad_damma"},
    {"letter": "ضِ", "letterName": "ضَادُنْ", "sound": "ضِ", "word": "ضِرْسٌ", "id": "daad_kasra"},
    
    # حرف الطاء
    {"letter": "طَ", "letterName": "طَاءُنْ", "sound": "طَ", "word": "طَائِرَةٌ", "id": "taa_alt_fatha"},
    {"letter": "طُ", "letterName": "طَاءُنْ", "sound": "طُ", "word": "طُيُورٌ", "id": "taa_alt_damma"},
    {"letter": "طِ", "letterName": "طَاءُنْ", "sound": "طِ", "word": "طِفْلٌ", "id": "taa_alt_kasra"},
    
    # حرف الظاء
    {"letter": "ظَ", "letterName": "ظَاءُنْ", "sound": "ظَ", "word": "ظَرْفٌ", "id": "zhaa_fatha"},
    {"letter": "ظُ", "letterName": "ظَاءُنْ", "sound": "ظُ", "word": "ظُفْرٌ", "id": "zhaa_damma"},
    {"letter": "ظِ", "letterName": "ظَاءُنْ", "sound": "ظِ", "word": "ظِلٌّ", "id": "zhaa_kasra"},
    
    # حرف العين
    {"letter": "عَ", "letterName": "عَيْنُنْ", "sound": "عَ", "word": "عَنْكَبوتٌ", "id": "ain_fatha"},
    {"letter": "عُ", "letterName": "عَيْنُنْ", "sound": "عُ", "word": "عُصْفُورٌ", "id": "ain_damma"},
    {"letter": "عِ", "letterName": "عَيْنُنْ", "sound": "عِ", "word": "عِنَبٌ", "id": "ain_kasra"},
    
    # حرف الغين
    {"letter": "غَ", "letterName": "غَيْنُنْ", "sound": "غَ", "word": "غَزَالٌ", "id": "ghain_fatha"},
    {"letter": "غُ", "letterName": "غَيْنُنْ", "sound": "غُ", "word": "غُرَابٌ", "id": "ghain_damma"},
    {"letter": "غِ", "letterName": "غَيْنُنْ", "sound": "غِ", "word": "غِطَاءٌ", "id": "ghain_kasra"},
    
    # حرف الفاء
    {"letter": "فَ", "letterName": "فَاءُنْ", "sound": "فَ", "word": "فَرَاشَةٌ", "id": "faa_fatha"},
    {"letter": "فُ", "letterName": "فَاءُنْ", "sound": "فُ", "word": "فُلَّةٌ", "id": "faa_damma"},
    {"letter": "فِ", "letterName": "فَاءُنْ", "sound": "فِ", "word": "فِيلٌ", "id": "faa_kasra"},
    
    # حرف القاف
    {"letter": "قَ", "letterName": "قَافُنْ", "sound": "قَ", "word": "قَمَرٌ", "id": "qaaf_fatha"},
    {"letter": "قُ", "letterName": "قَافُنْ", "sound": "قُ", "word": "قُـبَّعَةٌ", "id": "qaaf_damma"},
    {"letter": "قِ", "letterName": "قَافُنْ", "sound": "قِ", "word": "قِـرْدٌ", "id": "qaaf_kasra"},
    
    # حرف الكاف
    {"letter": "كَ", "letterName": "كَافُنْ", "sound": "كَ", "word": "كَلْبٌ", "id": "kaaf_fatha"},
    {"letter": "كُ", "letterName": "كَافُنْ", "sound": "كُ", "word": "كُرَةٌ", "id": "kaaf_damma"},
    {"letter": "كِ", "letterName": "كَافُنْ", "sound": "كِ", "word": "كِتَابٌ", "id": "kaaf_kasra"},
    
    # حرف اللام
    {"letter": "لَ", "letterName": "لَامُنْ", "sound": "لَ", "word": "لَيْثٌ", "id": "lam_fatha"},
    {"letter": "لُ", "letterName": "لَامُنْ", "sound": "لُ", "word": "لُعْبَةٌ", "id": "lam_damma"},
    {"letter": "لِ", "letterName": "لَامُنْ", "sound": "لِ", "word": "لِسَانٌ", "id": "lam_kasra"},
    
    # حرف الميم
    {"letter": "مَ", "letterName": "مِيمُنْ", "sound": "مَ", "word": "مَوْزٌ", "id": "meem_fatha"},
    {"letter": "مُ", "letterName": "مِيمُنْ", "sound": "مُ", "word": "مُخْتَبَرٌ", "id": "meem_damma"},
    {"letter": "مِ", "letterName": "مِيمُنْ", "sound": "مِ", "word": "مِقصٌّ", "id": "meem_kasra"},
    
    # حرف النون
    {"letter": "نَ", "letterName": "نُونُنْ", "sound": "نَ", "word": "نَمِرٌ", "id": "noon_fatha"},
    {"letter": "نُ", "letterName": "نُونُنْ", "sound": "نُ", "word": "نُجُومٌ", "id": "noon_damma"},
    {"letter": "نِ", "letterName": "نُونُنْ", "sound": "نِ", "word": "تِصْفٌ", "id": "noon_kasra"},
    
    # حرف الهاء
    {"letter": "هَ", "letterName": "هَاءُنْ", "sound": "هَ", "word": "هَدِيَّةٌ", "id": "haa_alt_fatha"},
    {"letter": "هُ", "letterName": "هَاءُنْ", "sound": "هُ", "word": "هُدْهُدٌ", "id": "haa_alt_damma"},
    {"letter": "هِ", "letterName": "هَاءُنْ", "sound": "هِ", "word": "هيلٌ", "id": "haa_alt_kasra"},
    
    # حرف الواو
    {"letter": "وَ", "letterName": "وَاوُنْ", "sound": "وَ", "word": "وَرْدَةٌ", "id": "waw_fatha"},
    {"letter": "وُ", "letterName": "وَاوُنْ", "sound": "وُ", "word": "وُصُولٌ", "id": "waw_damma"},
    {"letter": "وِ", "letterName": "وَاوُنْ", "sound": "وِ", "word": "وِسَادَةٌ", "id": "waw_kasra"},
    
    # حرف الياء
    {"letter": "يَ", "letterName": "يَاءُنْ", "sound": "يَ", "word": "يَدٌ", "id": "yaa_fatha"},
    {"letter": "يُ", "letterName": "يَاءُنْ", "sound": "يُ", "word": "يُوسُفِيٌّ", "id": "yaa_damma"},
    {"letter": "يِ", "letterName": "يَاءُنْ", "sound": "يِ", "word": "يِينَاعٌ", "id": "yaa_kasra"}
]

# 2. حلقة المعالجة والتشغيل الآمن
print("--- بدء عملية المعالجة والتوليد بشكل آمن ---")

for item in alphabet_data:
    letter = item['letter']
    word = item['word']
    letter_name = item['letterName']
    
    # تجهيز النص بدون رموز قد تسبب مشاكل
    text_to_process = f"{letter_name}، {letter}، {word}".replace("...", "")
    
    try:
        print(f"جاري معالجة: {letter_name} .. {letter} .. {word}")
        
        # [ضع كود التوليد الصوتي الخاص بك هنا إن وجد]
        time.sleep(0.1) 
        
        print(f"✔️ تمت المعالجة بنجاح: {letter}  ,   {word}")
        
    except Exception as e:
        print(f"❌ خطأ أثناء معالجة ({word}): {e}")
        continue

# حفظ البيانات المحدثة في ملف JSON داخل نفس المجلد
with open('letters_updated.json', 'w', encoding='utf-8') as f:
    json.dump(alphabet_data, f, ensure_ascii=False, indent=4)

print("\nتم حفظ ملف 'letters_updated.json' بنجاح!")