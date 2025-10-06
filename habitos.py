from datetime import datetime

print("¡Bienvenido! Aquí puedes registrar tus hábitos ambientales.")
print("Escribe un hábito que tengas y utiliza palabras clave de las secciones sugeridas (puedes agregar detalles):")
print("Ejemplos de hábitos positivos:")
print("  - Usé bicicleta, caminé, ahorré energía, utilicé paneles solares, evité combustibles")
print("  - Cuidé bosques, planté árboles, protegí la Amazonía, conservé suelos, preservé agua")
print("  - Cultivé orgánico, reduje fertilizantes, protegí suelos, sembré biodiversidad, ahorré agua")
print("  - Fabriqué ecológico, reutilicé materiales, usé transporte público, manejé eléctrico, reduje CO₂")
print("  - Limpié playas, recogí basura, reciclé desechos, cuidé costas, protegí corales, preservé océanos")
print("  - Defendí selva, cuidé ríos, apoyé minería responsable, protegí comunidades, conservé ecosistemas")
print("Ejemplos de hábitos negativos:")
print("  - Quemé carbón, petróleo, gasté gas natural, contaminé aire")
print("  - Talé bosques, corté árboles, destruí Amazonía, liberé CO₂, provoqué sequías")
print("  - Usé fertilizantes, crié vacas, produje metano, contaminé suelos, degradé tierras")
print("  - Construí cemento, fabriqué acero, manejé autos, volé aviones, navegué barcos, emití CO₂")
print("  - Boté basura, arrojé residuos, deseché plásticos, contaminé océanos, dañé corales, afecté plancton")
print("  - Extraje oro, talé selva, contaminé ríos, vertí tóxicos, destruí ecosistemas")
print("Si tienes una empresa, también puedes registrar hábitos empresariales usando las palabras clave sugeridas.")

def habitos():
    # Definición de secciones positivas (sin cambios)
    secciones_positivas = {
        "1": {"palabras": [
            "usé bicicleta", "usé calles", "usé energía", "usé paneles solares",
            "caminé calles", "caminé energía",
            "ahorré energía", "ahorré paneles solares",
            "utilicé paneles solares", "utilicé energía",
            "evité combustibles", "evité energía"
        ], "reflexion": "¡Gran trabajo! Usar medios de transporte sostenibles o energías limpias ayuda a reducir tu huella de carbono."},
        "1.2": {"palabras": [
            "usó energías renovables", "usó paneles solares", "usó transporte limpio",
            "invirtió energías renovables", "invirtió paneles solares", "invirtió transporte limpio",
            "redujo combustibles fósiles", "redujo energías sucias",
            "recicló energías renovables", "recicló paneles solares",
            "fomentó energías renovables", "fomentó paneles solares", "fomentó transporte limpio"
        ], "reflexion": "¡Tu empresa está marcando la diferencia! Usar energías renovables reduce el impacto ambiental."},
        "2": {"palabras": [
            "cuidé bosques", "cuidé árboles", "cuidé Amazonía", "cuidé suelos", "cuidé agua", "cuidé hábitats", "provoqué árboles",
            "planté bosques", "planté árboles", "planté Amazonía", "planté suelos", "planté agua", "planté hábitats", "provoqué bosques",
            "protegí bosques", "protegí árboles", "protegí Amazonía", "protegí suelos", "protegí agua", "protegí hábitats",
            "preservé bosques", "preservé árboles", "preservé Amazonía", "preservé suelos", "preservé agua", "preservé hábitats"
        ], "reflexion": "¡Excelente! Proteger los bosques y el agua es clave para mantener el equilibrio de los ecosistemas."},
        "2.2": {"palabras": [
            "reforestó áreas", "reforestó bosques", "reforestó Amazonía", "reforestó suelos",
            "cuidó áreas", "cuidó bosques", "cuidó Amazonía", "cuidó suelos", "provocó bosques",
            "plantó áreas", "plantó bosques", "plantó Amazonía", "plantó suelos", "provocó árboles",
            "protegí áreas", "protegí bosques", "protegí Amazonía", "protegí suelos"
        ], "reflexion": "¡Gran iniciativa! Reforestar y proteger bosques ayuda a combatir el cambio climático."},
        "3": {"palabras": [
            "cultivé orgánico", "cultivé suelos", "cultivé agua",
            "reduje fertilizantes", "reduje suelos", "reduje agua",
            "protegí suelos", "protegí agua",
            "sembré biodiversidad", "sembré suelos",
            "ahorré agua", "ahorré suelos"
        ], "reflexion": "¡Fantástico! La agricultura sostenible preserva la tierra y promueve la biodiversidad."},
        "3.2": {"palabras": [
            "cultivó orgánico", "cultivó suelos", "cultivó agua",
            "reduje fertilizantes", "reduje suelos", "reduje agua",
            "implementó prácticas sostenibles", "implementó suelos", "implementó agua",
            "protegí suelos", "protegí agua",
            "ahorré agua", "ahorré suelos"
        ], "reflexion": "¡Sostenible! Las prácticas agrícolas responsables cuidan el suelo y los recursos."},
        "4": {"palabras": [
            "fabriqué ecológico", "fabriqué materiales",
            "reutilicé materiales",
            "usé transporte público",
            "manejé eléctrico",
            "reduje CO₂"
        ], "reflexion": "¡Buen hábito! Reducir emisiones y reutilizar materiales contribuye a un futuro más limpio."},
        "4.2": {"palabras": [
            "fabricó materiales reciclados", "fabricó emisiones", "fabricó maquinaria limpia", "fabricó transporte eléctrico", "fabricó procesos",
            "redujo materiales reciclados", "redujo emisiones", "redujo maquinaria limpia", "redujo transporte eléctrico", "redujo procesos",
            "modernizó materiales reciclados", "modernizó emisiones", "modernizó maquinaria limpia", "modernizó transporte eléctrico", "modernizó procesos",
            "usó materiales reciclados", "usó emisiones", "usó maquinaria limpia", "usó transporte eléctrico", "usó procesos",
            "optimizó materiales reciclados", "optimizó emisiones", "optimizó maquinaria limpia", "optimizó transporte eléctrico", "optimizó procesos"
        ], "reflexion": "¡Innovador! Usar materiales reciclados y tecnologías limpias es un paso hacia la sostenibilidad."},
        "5": {"palabras": [
            "limpié playas", "limpié basura", "limpié desechos", "limpié costas", "limpié océanos",
            "recogí playas", "recogí basura", "recogí desechos", "recogí costas", "recogí océanos",
            "reciclé playas", "reciclé basura", "reciclé desechos", "reciclé costas", "reciclé océanos",
            "cuidé playas", "cuidé basura", "cuidé desechos", "cuidé costas", "cuidé océanos",
            "protegí playas", "protegí basura", "protegí desechos", "protegí costas", "protegí océanos"
        ], "reflexion": "¡Admirable! Cuidar los océanos y reducir desechos protege la vida marina."},
        "5.2": {"palabras": [
            "limpió playas", "limpió basura", "limpió desechos", "limpió costas", "limpió ecosistemas marinos",
            "recogió playas", "recogió basura", "recogió desechos", "recogió costas", "recogió ecosistemas marinos",
            "reciclé playas", "reciclé basura", "reciclé desechos", "reciclé costas", "reciclé ecosistemas marinos",
            "cuidé playas", "cuidé basura", "cuidé desechos", "cuidé costas", "cuidé ecosistemas marinos",
            "protegí playas", "protegí basura", "protegí desechos", "protegí costas", "protegí ecosistemas marinos"
        ], "reflexion": "¡Ejemplar! Proteger los mares y reciclar desechos es crucial para la salud oceánica."},
        "6": {"palabras": [
            "defendí selva", "defendí ríos", "defendí minería responsable", "defendí comunidades", "defendí ecosistemas", "defendí hábitats",
            "cuidé selva", "cuidé ríos", "cuidé minería responsable", "cuidé comunidades", "cuidé ecosistemas", "cuidé hábitats",
            "apoyé selva", "apoyé ríos", "apoyé minería responsable", "apoyé comunidades", "apoyé ecosistemas", "apoyé hábitats",
            "protegí selva", "protegí ríos", "protegí minería responsable", "protegí comunidades", "protegí ecosistemas", "protegí hábitats",
            "conservé selva", "conservé ríos", "conservé minería responsable", "conservé comunidades", "conservé ecosistemas", "conservé hábitats"
        ], "reflexion": "¡Increíble! Proteger ecosistemas y comunidades es esencial para un planeta saludable."},
        "6.2": {"palabras": [
            "respetó regulaciones", "respetó minería responsable", "respetó ríos", "respetó comunidades", "respetó ecosistemas",
            "practicó regulaciones", "practicó minería responsable", "practicó ríos", "practicó comunidades", "practicó ecosistemas",
            "cuidé regulaciones", "cuidé minería responsable", "cuidé ríos", "cuidé comunidades", "cuidé ecosistemas",
            "protegí regulaciones", "protegí minería responsable", "protegí ríos", "protegí comunidades", "protegí ecosistemas",
            "conservé regulaciones", "conservé minería responsable", "conservé ríos", "conservé comunidades", "conservé ecosistemas"
        ], "reflexion": "¡Responsable! La minería sostenible y el cuidado de comunidades protegen el entorno."}
    }

    # Definición de secciones negativas (sin cambios)
    secciones_negativas = {
        "1.2": {"palabras": [
            "quemé carbón", "usé combustibles", "usó combustibles fósiles", "fomenta combustibles fósiles", "fomentó combustibles fósiles", "quemé petróleo", "quemé gas natural",
            "gasté carbón", "gasté petróleo", "gasté gas natural", "fomenté combustibles fósiles",
            "contaminé carbón", "contaminé petróleo", "contaminé gas natural",
            "contaminé aire"
        ], "reflexion": "Quemar combustibles fósiles contribuye al cambio climático. Considera usar energías renovables."},
        "2.1": {"palabras": [
            "talé bosques", "talé árboles", "talé Amazonía",
            "corté bosques", "corté árboles", "corté Amazonía",
            "destruí bosques", "destruí árboles", "destruí Amazonía",
            "liberé CO₂", "liberé sequías",
            "provoqué CO₂", "provoqué sequías"
        ], "reflexion": "Destruir bosques daña los ecosistemas. Plantar árboles puede ser una gran alternativa."},
        "3.1": {"palabras": [
            "usé fertilizantes", "usé vacas", "usé metano",
            "crié fertilizantes", "crié vacas", "crié metano",
            "produje fertilizantes", "produje vacas", "produje metano",
            "contaminé suelos", "contaminé tierras",
            "degradé suelos", "degradé tierras"
        ], "reflexion": "El uso intensivo de fertilizantes y ganadería daña el suelo. Opta por prácticas orgánicas."},
        "4.1": {"palabras": [
            "construí cemento", "construí acero", "construí autos", "construí aviones", "construí barcos", "construí CO₂",
            "fabriqué cemento", "fabriqué acero", "fabriqué autos", "fabriqué aviones", "fabriqué barcos", "fabriqué CO₂",
            "manejé cemento", "manejé acero", "manejé autos", "manejé aviones", "manejé barcos", "manejé CO₂",
            "volé cemento", "volé acero", "volé autos", "volé aviones", "volé barcos", "volé CO₂",
            "navegué cemento", "navegué acero", "navegué autos", "navegué aviones", "navegué barcos", "navegué CO₂", "use co2",
            "emití cemento", "emití acero", "emití autos", "emití aviones", "emití barcos", "emití CO₂", "redujo suelos2", "redujo prácticas sostenibles", "redujo agua", "fabrique co2"
        ], "reflexion": "Las emisiones de CO₂ afectan el clima. Usar transporte público o eléctrico puede ayudar."},
        "5.1": {"palabras": [
            "boté basura", "boté residuos", "boté plásticos",
            "arrojé basura", "arrojé residuos", "arrojé plásticos",
            "deseché basura", "deseché residuos", "deseché plásticos",
            "contaminé océanos", "contaminé corales", "contaminé plancton",
            "dañé océanos", "dañé corales", "dañé plancton", "limpié corales", "recogí corales"
        ], "reflexion": "Contaminar los océanos daña la vida marina. Reciclar y limpiar playas es una solución."},
        "6.1": {"palabras": [
            "extraje oro", "extraje selva", "extraje ríos", "extraje tóxicos", "extraje ecosistemas",
            "talé oro", "talé selva", "talé ríos", "talé tóxicos", "talé ecosistemas",
            "contaminé oro", "contaminé selva", "contaminé ríos", "contaminé tóxicos", "contaminé ecosistemas",
            "vertí oro", "vertí selva", "vertí ríos", "vertí tóxicos", "vertí ecosistemas",
            "destruí oro", "destruí selva", "destruí ríos", "destruí tóxicos", "destruí ecosistemas"
        ], "reflexion": "La minería irresponsable daña el entorno. Apoya prácticas sostenibles y responsables."},
        "1.3": {"palabras": [
            "quemó carbón", "quemó petróleo", "quemó gas natural", "quemó aire", "quemó efecto invernadero",
            "utilizó carbón", "utilizó petróleo", "utilizó gas natural", "utilizó aire", "utilizó efecto invernadero",
            "gastó carbón", "gastó petróleo", "gastó gas natural", "gastó aire", "gastó efecto invernadero",
            "contaminó carbón", "contaminó petróleo", "contaminó gas natural", "contaminó aire", "contaminó efecto invernadero",
            "intensificó carbón", "intensificó petróleo", "intensificó gas natural", "intensificó aire", "intensificó efecto invernadero"
        ], "reflexion": "Tu empresa contribuye al calentamiento global. Invierte en energías limpias."},
        "2.3": {"palabras": [
            "taló bosques", "taló árboles", "taló selva", "taló CO₂", "taló sequías",
            "cortó bosques", "cortó árboles", "cortó selva", "cortó CO₂", "cortó sequías",
            "destruyó bosques", "destruyó árboles", "destruyó selva", "destruyó CO₂", "destruyó sequías",
            "liberé bosques", "liberé árboles", "liberé selva", "liberé CO₂", "liberé sequías",
            "provocó bosques", "provocó árboles", "provocó selva", "provocó CO₂", "provocó sequías"
        ], "reflexion": "La deforestación empresarial daña el planeta. Reforesta y protege los bosques."},
        "3.3": {"palabras": [
            "usó fertilizantes químicos", "usó ganado intensivo", "usó metano", "usó suelos", "usó tierras",
            "crió fertilizantes químicos", "crió ganado intensivo", "crió metano", "crió suelos", "crió tierras",
            "produjo fertilizantes químicos", "produjo ganado intensivo", "produjo metano", "produjo suelos", "produjo tierras",
            "contaminó fertilizantes químicos", "contaminó ganado intensivo", "contaminó metano", "contaminó suelos", "contaminó tierras",
            "degradé fertilizantes químicos", "degradé ganado intensivo", "degradé metano", "degradé suelos", "degradé tierras", "reduje suelos", "reduje biodiversidad", "reduje agua"
        ], "reflexion": "Las prácticas intensivas dañan el suelo. Adopta métodos orgánicos y sostenibles."},
        "4.3": {"palabras": [
            "produjo cemento", "produjo acero", "produjo autos contaminantes", "produjo aviones", "produjo barcos", "produjo CO₂",
            "usó cemento", "usó acero", "usó autos contaminantes", "usó aviones", "usó barcos", "usó CO₂",
            "operó cemento", "operó acero", "operó autos contaminantes", "operó aviones", "operó barcos", "operó CO₂",
            "emitió cemento", "emitió acero", "emitió autos contaminantes", "emitió aviones", "emitió barcos", "emitió CO₂", "redujo materiales reciclados", "redujo maquinaria limpia", "redujo transporte eléctrico"
        ], "reflexion": "Las emisiones industriales son perjudiciales. Moderniza con tecnologías limpias."},
        "5.3": {"palabras": [
            "botó basura", "botó residuos", "botó plásticos", "botó mares", "botó aguas", "botó corales", "botó plancton",
            "arrojó basura", "arrojó residuos", "arrojó plásticos", "arrojó mares", "arrojó aguas", "arrojó corales", "arrojó plancton",
            "deseché basura", "deseché residuos", "deseché plásticos", "deseché mares", "deseché aguas", "deseché corales", "deseché plancton",
            "contaminó basura", "contaminó residuos", "contaminó plásticos", "contaminó mares", "contaminó aguas", "contaminó corales", "contaminó plancton",
            "acidificó basura", "acidificó residuos", "acidificó plásticos", "acidificó mares", "acidificó aguas", "acidificó corales", "acidificó plancton",
            "dañé basura", "dañé residuos", "dañé plásticos", "dañé mares", "dañé aguas", "dañé corales", "dañé plancton", "limpió corales", "recogió corales"
        ], "reflexion": "La contaminación marina empresarial es grave. Implementa reciclaje y limpieza."},
        "6.3": {"palabras": [
            "extrajo oro ilegalmente", "extrajo selva", "extrajo ríos", "extrajo químicos tóxicos", "extrajo hábitats",
            "talé oro ilegalmente", "talé selva", "talé ríos", "talé químicos tóxicos", "talé hábitats",
            "contaminé oro ilegalmente", "contaminé selva", "contaminé ríos", "contaminé químicos tóxicos", "contaminé hábitats",
            "vertió oro ilegalmente", "vertió selva", "vertió ríos", "vertió químicos tóxicos", "vertió hábitats",
            "destruí oro ilegalmente", "destruí selva", "destruí ríos", "destruí químicos tóxicos", "destruí hábitats"
        ], "reflexion": "La minería ilegal daña ecosistemas. Adopta prácticas éticas y sostenibles."}
    }

    # Manejo de entrada con protección contra EOFError
    while True:
        try:
            HABITO = input("Escribe tu hábito ambiental: ")
            if HABITO.strip() == "":
                print("La entrada está vacía. Por favor, escribe un hábito.")
                continue
            break
        except EOFError:
            print("No se recibió entrada. Por favor, intenta de nuevo.")

    # Normalización
    def remove_accents(text):
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
            'ã': 'a', 'õ': 'o', 'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u'
        }
        for accented, unaccented in replacements.items():
            text = text.replace(accented, unaccented)
        return text

    habito_lower = HABITO.lower()
    habito_normalized = remove_accents(habito_lower).split()

    def any_word_present(phrase, input_words):
        phrase_words = remove_accents(phrase.lower()).split()
        return any(word in input_words for word in phrase_words)

    seccion_detectada = None
    es_negativo = False
    for seccion, datos in secciones_negativas.items():
        for palabra in datos["palabras"]:
            if any_word_present(palabra, habito_normalized):
                seccion_detectada = seccion
                es_negativo = True
                break
        if seccion_detectada:
            break

    if not seccion_detectada:
        for seccion, datos in secciones_positivas.items():
            for palabra in datos["palabras"]:
                if any_word_present(palabra, habito_normalized):
                    seccion_detectada = seccion
                    es_negativo = False
                    break
            if seccion_detectada:
                break

    if seccion_detectada:
        print(f"Hábito registrado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if es_negativo:
            print("Tu hábito tiene un impacto negativo en el medio ambiente. Reflexiona sobre cómo puedes mejorar y contribuir a un planeta más sano.")
            print(f"Sección detectada: {seccion_detectada}")
            print(f"Recomendación: {secciones_negativas[seccion_detectada]['reflexion']}")
        else:
            print("¡Excelente hábito! Tus acciones ayudan a cuidar el planeta. Sigue así y motiva a otros a hacer lo mismo.")
            print(f"Sección detectada: {seccion_detectada}")
            print(f"Recomendación: {secciones_positivas[seccion_detectada]['reflexion']}")
    else:
        print("No se pudo clasificar tu hábito. Usa palabras clave de las secciones sugeridas para obtener una recomendación.")


habitos()
