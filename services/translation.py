class TranslationService:
    # The 6 core languages for the Crisis and Damage Response Assessment
    SUPPORTED_LANGUAGES = {
        "en": "English",
        "ar": "العربية",
        "fr": "Français",
        "es": "Español",
        "sw": "Kiswahili",
        "pt": "Português"
    }

    # RTL logic specifically for Arabic
    @staticmethod
    def is_rtl(lang: str) -> bool:
        return lang == "ar"

    @staticmethod
    def get_ui_labels(lang: str):
        translations = {
            "en": {
                "hero_title": "Map Damage. <br>Accelerate Recovery.",
                "hero_subtitle": "In the first 48 hours of a crisis, your data is the most valuable tool for response. Identify damaged buildings to help UNDP partners deploy aid where it is needed most.",
                "btn_report": "Submit Damage Report",
                "btn_map": "View Community Map",
                "aria_report": "Submit a new damage report to UNDP",
                "aria_map": "View the interactive community damage map"
            },
            "ar": {
                "hero_title": "رسم خرائط الأضرار. <br>تسريع التعافي.",
                "hero_subtitle": "في أول 48 ساعة من الأزمة، بياناتك هي الأداة الأكثر قيمة للاستجابة. حدد المباني المتضررة لمساعدة شركاء برنامج الأمم المتحدة الإنمائي في نشر المساعدات حيث تشتد الحاجة إليها.",
                "btn_report": "تقديم تقرير الأضرار",
                "btn_map": "عرض خريطة المجتمع",
                "aria_report": "تقديم تقرير أضرار جديد إلى برنامج الأمم المتحدة الإنمائي",
                "aria_map": "عرض خريطة أضرار المجتمع التفاعلية"
            },
            "fr": {
                "hero_title": "Cartographier les Dommages. <br>Accélérer la Reprise.",
                "hero_subtitle": "Dans les 48 premières heures d'une crise, vos données sont l'outil le plus précieux pour la réponse. Identifiez les bâtiments endommagés pour aider les partenaires du PNUD à déployer l'aide là où elle est le plus nécessaire.",
                "btn_report": "Signaler des Dommages",
                "btn_map": "Voir la Carte",
                "aria_report": "Soumettre un nouveau rapport de dommages au PNUD",
                "aria_map": "Voir la carte interactive des dommages"
            },
            "es": {
                "hero_title": "Mapear Daños. <br>Acelerar la Recuperación.",
                "hero_subtitle": "En las primeras 48 horas de una crisis, sus datos son la herramienta más valiosa para la respuesta. Identifique los edificios dañados para ayudar a los socios del PNUD a desplegar la ayuda donde más se necesita.",
                "btn_report": "Reportar Daños",
                "btn_map": "Ver Mapa Comunitario",
                "aria_report": "Enviar un nuevo informe de daños al PNUD",
                "aria_map": "Ver el mapa interactivo de daños comunitarios"
            },
            "sw": {
                "hero_title": "Ramani ya Uharibifu. <br>Harakisha Ufufuaji.",
                "hero_subtitle": "Katika saa 48 za kwanza za shida, data yako ndio zana yenye thamani zaidi kwa majibu. Tambua majengo yaliyoharibiwa kusaidia washirika wa UNDP kupeleka msaada pale unapohitajika zaidi.",
                "btn_report": "Wasilisha Ripoti ya Uharibifu",
                "btn_map": "Tazama Ramani ya Jamii",
                "aria_report": "Wasilisha ripoti mpya ya uharibifu kwa UNDP",
                "aria_map": "Tazama ramani ya jamii inayoingiliana ya uharibifu"
            },
            "pt": {
                "hero_title": "Mapear Danos. <br>Acelerar a Recuperação.",
                "hero_subtitle": "Nas primeiras 48 horas de uma crise, os seus dados são a ferramenta mais valiosa para a resposta. Identifique edifícios danificados para ajudar os parceiros do PNUD a mobilizar ajuda onde ela é mais necessária.",
                "btn_report": "Comunicar Danos",
                "btn_map": "Ver Mapa Comunitario",
                "aria_report": "Enviar um novo relatório de danos ao PNUD",
                "aria_map": "Ver o mapa interativo de danos comunitários"
            }
        }
        
        # Fallback to English if the requested language isn't supported
        return translations.get(lang, translations["en"])
