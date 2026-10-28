# -*- coding: utf-8 -*-
"""Textos ampliados de cada página de servicio.

Por servicio:
  sobre    -> (titular, [párrafos], cita destacada)
  fichas   -> [(nombre, descripción, ideal para, [beneficios], dato práctico)]
  proceso  -> [(paso, explicación)]  · cómo es tu sesión
  cuidados -> [consejo]               · antes y después
Precios y duraciones tomados de la web y las redes del centro; lo demás, "consultar".
"""

DETALLE = {
    # ------------------------------------------------------------------ FACIALES
    "faciales": {
        "sobre": (
            "Un rostro bonito empieza por una piel sana",
            [
                "Tu piel cambia con las estaciones, con el estrés, con las hormonas y con el paso del tiempo. Por eso en Rocío Castelló no trabajamos con protocolos cerrados: cada facial se decide después de mirar tu piel de cerca, con equipo de diagnóstico profesional, y de escuchar qué te preocupa y qué quieres conseguir.",
                "Combinamos cosmética profesional de alta concentración, técnicas manuales orientales y aparatología de última generación. El resultado es una piel más limpia, luminosa y firme desde la primera sesión, y un plan de cuidado claro para que el cambio dure en casa.",
            ],
            "No es sólo un tratamiento facial: es tu hora de desconexión.",
        ),
        "fichas": [
            ("Higiene facial profunda", "Limpieza en profundidad que elimina impurezas, puntos negros y células muertas, y devuelve a la piel su capacidad de respirar. Termina con mascarilla e hidratación adaptadas a tu tipo de piel.", "Todas las pieles, una vez al mes", ["Poros más limpios y cerrados", "Piel fresca y luminosa", "Mejor absorción de tu cosmética"], "60 min · 48 €"),
            ("Higiene profunda y equilibrio", "La higiene completa con un paso extra de restauración: equilibra la producción de grasa, calma y refuerza la barrera de la piel.", "Pieles mixtas, grasas o desequilibradas", ["Menos brillos", "Barrera cutánea reforzada", "Tono más uniforme"], "65 €"),
            ("Hydronature · 9 tecnologías en 1", "Nuestro equipo de higiene más avanzado: limpia, exfolia, extrae, hidrata, aplica activos, calma y reafirma en una sola sesión, sin agresividad.", "Quien busca una limpieza perfecta y efecto «glow» inmediato", ["Extracción sin marcas", "Hidratación profunda", "Piel tersa al momento"], "Consultar"),
            ("Oxigenación e hidratación", "Aporta oxígeno y agua a las capas profundas de la piel. Ideal para pieles apagadas, deshidratadas o castigadas por el sol, el frío o la calefacción.", "Pieles apagadas o deshidratadas", ["Luminosidad", "Confort y elasticidad", "Efecto relleno de líneas finas"], "65 €"),
            ("Sensibilidad", "Protocolo calmante y reconfortante para pieles reactivas, con rojeces o que pican y tiran. Ingredientes suaves que devuelven el equilibrio.", "Pieles sensibles, reactivas o con rojeces", ["Calma inmediata", "Menos rojeces", "Piel más resistente"], "65 €"),
            ("Rejuvenecimiento", "Revitaliza, estimula e ilumina. Activos antiedad y técnicas de masaje que trabajan la firmeza y suavizan arrugas y líneas de expresión.", "A partir de los 30, o pieles que pierden firmeza", ["Piel más firme", "Arrugas suavizadas", "Rostro descansado"], "65 €"),
            ("Acné", "Equilibra, regula, desinfecta y ayuda a cicatrizar. Tratamos el brote activo y, después, las marcas que deja, siempre con mucha delicadeza.", "Pieles con acné activo, adolescentes y adultas", ["Menos brotes", "Piel desinflamada", "Marcas más suaves"], "65 €"),
            ("Hiperpigmentación", "Inhibe la melanina, unifica el tono y despigmenta. Se complementa con peelings y, si hace falta, con láser Q-Switched para manchas resistentes.", "Manchas solares, hormonales o por la edad", ["Tono unificado", "Manchas atenuadas", "Piel más luminosa"], "65 €"),
            ("Regeneración", "Exfolia, alisa y rejuvenece. Un protocolo renovador que acelera el recambio celular y deja una textura visiblemente más fina.", "Pieles con textura irregular o poros marcados", ["Textura más fina", "Poros menos visibles", "Luz"], "65 €"),
            ("Belleza al instante", "Rellena e ilumina para lucir buena cara en pocas horas. El favorito antes de una boda, un evento o una foto importante.", "Antes de un evento", ["Efecto flash", "Rostro jugoso", "Maquillaje perfecto"], "65 €"),
            ("Contorno de ojos", "Drena, rellena, hidrata y despigmenta la zona más delicada del rostro. Bolsas, ojeras y patas de gallo, tratadas con mimo.", "Bolsas, ojeras y líneas finas", ["Mirada descansada", "Menos hinchazón", "Ojeras más claras"], "65 €"),
            ("Esencias vegetales con Gua Sha y Cupping", "Dos técnicas orientales milenarias: la piedra Gua Sha esculpe y drena; las ventosas faciales activan la circulación. Todo con aceites vegetales.", "Rostros hinchados o tensos, y quien quiere desconectar", ["Óvalo más definido", "Drenaje y luz", "Relajación profunda"], "65 €"),
            ("Masaje Kobido", "El llamado «lifting japonés sin bisturí». Un masaje facial enérgico y preciso que reafirma, remodela e ilumina.", "Flacidez incipiente y amantes de los tratamientos naturales", ["Efecto lifting manual", "Músculos faciales tonificados", "Brillo natural"], "65 €"),
            ("Dermapen + vitaminas", "Micropunción controlada que estimula la producción natural de colágeno y elastina y permite que las vitaminas penetren en profundidad.", "Cicatrices de acné, poros, manchas y arrugas finas", ["Textura más lisa", "Cicatrices atenuadas", "Piel más densa"], "Consultar"),
            ("Hollywood Peeling · carbón activo", "El tratamiento favorito de las celebrities: una mascarilla de carbón y luz que exfolia, desintoxica y deja un brillo espectacular sin días de baja.", "Pieles grasas, poros dilatados o falta de luz", ["Poros cerrados", "Piel lisa", "Brillo inmediato"], "Consultar"),
            ("Muse con exosomas", "La última generación en regeneración: exosomas y células madre que dan a la piel instrucciones para repararse, con efecto flash y defensa total.", "Pieles maduras, cansadas o tras el verano", ["Luminosidad inmediata", "Regeneración celular", "Piel más fuerte"], "Consultar"),
            ("Tratamiento de Oro", "Oro de 24 quilates para nutrir, iluminar y aportar un efecto rejuvenecedor de auténtico lujo.", "Ocasiones especiales y pieles que piden un mimo extra", ["Luz", "Nutrición", "Sensación de lujo"], "Consultar"),
            ("Eliminación de verrugas", "Retiramos pequeñas verrugas y lesiones benignas de forma rápida y segura.", "Verrugas pequeñas en rostro o cuerpo", ["Rápido", "Seguro", "Sin marcas visibles"], "desde 20 €"),
        ],
        "proceso": [
            ("Diagnóstico", "Analizamos tu piel con equipo profesional y te preguntamos por tu rutina y tus objetivos. Es gratuito."),
            ("Preparación", "Desmaquillado, limpieza y exfoliación para que la piel reciba los activos al máximo."),
            ("Tratamiento", "El protocolo elegido para ti: extracción, aparatología, masaje, mascarilla… sin prisas."),
            ("Rutina en casa", "Te explicamos cómo cuidarte y qué cosmética usar para que el resultado dure."),
        ],
        "cuidados": [
            "Usa protector solar a diario, también en invierno.",
            "Evita maquillarte las 12 horas siguientes a una higiene profunda.",
            "Hidrata tu piel mañana y noche con la cosmética recomendada.",
            "Repite tu facial cada 4 a 6 semanas para mantener los resultados.",
        ],
    },

    # ------------------------------------------------------------------ TECNOLOGÍA
    "tecnologia": {
        "sobre": (
            "La tecnología que antes sólo estaba en las grandes ciudades",
            [
                "Cada temporada estudiamos qué equipos ofrecen resultados reales y seguros, y nos formamos con sus fabricantes antes de ponerlos a tu servicio. Así hemos ido incorporando Symmed, Hydronature, Tesla Med, Zionic y Evo Sculpt, entre otros.",
                "La aparatología no sustituye al criterio de una buena esteticista: lo potencia. Por eso cada sesión empieza con una valoración y cada protocolo combina la máquina adecuada con técnicas manuales y cosmética profesional.",
            ],
            "Resultados que se ven desde la primera sesión, sin agujas ni quirófano.",
        ),
        "fichas": [
            ("Tesla Med", "Tecnología con dos patentes mundiales que estimula los fibroblastos para producir colágeno, elastina y ácido hialurónico. Lifting, manchas, acné, estrías y labios sin infiltraciones.", "Rejuvenecimiento facial y corporal sin agujas", ["Efecto lifting", "Regeneración profunda", "Sin dolor"], "desde 85 €"),
            ("Symmed · diatermia y mesoterapia", "Radiofrecuencia que calienta las capas profundas de la piel y la reafirma, combinada con mesoterapia virtual para introducir activos.", "Arrugas, flacidez, papada, párpados, cuello y escote", ["Efecto buena cara inmediato", "Colágeno nuevo", "Sin pinchazos"], "69 €"),
            ("Zionic", "Radiofrecuencia y masaje activo rotacional en un solo cabezal: doble efecto térmico y mecánico para remodelar el cuerpo.", "Grasa localizada, celulitis, flacidez y glúteos", ["Reduce centímetros", "Alisa la piel de naranja", "Efecto push-up"], "69 € con presoterapia"),
            ("Hydronature", "Higiene facial con nueve tecnologías: limpia, exfolia, extrae, hidrata, aplica activos, calma y reafirma.", "Una limpieza perfecta para cualquier piel", ["Piel limpia y luminosa", "Hidratación", "Sin rojeces"], "Consultar"),
            ("Dermapen + vitaminas", "Micropunción controlada que activa la regeneración natural de la piel y potencia la penetración de vitaminas.", "Cicatrices, poros, manchas y textura", ["Piel más lisa", "Colágeno", "Luz"], "Consultar"),
            ("Evo Sculpt", "Electromagnetismo de alta intensidad: miles de contracciones musculares en 20 minutos para tonificar y definir.", "Abdomen y glúteos que necesitan tono", ["Músculo más firme", "Glúteos elevados", "Sin esfuerzo"], "Consultar"),
            ("Ondas de choque", "Pulsos acústicos que rompen la estructura de la celulitis, mejoran la circulación y reafirman.", "Celulitis rebelde y piel de naranja", ["Piel más lisa", "Mejor circulación", "Firmeza"], "50 €"),
            ("Cavitación", "Ultrasonidos de baja frecuencia que fragmentan el tejido graso para que el cuerpo lo elimine de forma natural.", "Grasa localizada en abdomen, cartucheras o brazos", ["Reducción de volumen", "No invasivo", "Sin reposo"], "50 €"),
            ("Radiofrecuencia corporal", "Calor profundo que estimula colágeno y elastina para devolver firmeza a la piel del cuerpo.", "Flacidez tras pérdida de peso o embarazo", ["Piel más firme", "Textura mejorada", "Efecto tensor"], "69 €"),
            ("Presoterapia", "Botas de presión que realizan un drenaje linfático mecánico, de pies a cintura.", "Retención de líquidos y piernas cansadas", ["Piernas ligeras", "Menos hinchazón", "Complemento ideal"], "15 €"),
            ("Láser de diodo 810 nm", "Depilación progresiva y definitiva con equipo médico, segura también en verano.", "Eliminar el vello de cualquier zona", ["Resultados desde la 1.ª sesión", "Sesiones cada 2 meses", "Casi indoloro"], "desde 10 €"),
            ("Láser Q-Switched", "Láser específico para fragmentar el pigmento de las manchas y atenuarlas.", "Manchas solares y de la edad", ["Tono unificado", "Rápido", "Preciso"], "Consultar"),
        ],
        "proceso": [
            ("Valoración", "Vemos la zona, hablamos de tu objetivo y elegimos el equipo adecuado. Sin compromiso."),
            ("Plan", "Te proponemos el número de sesiones y la combinación de técnicas, con precio cerrado."),
            ("Sesiones", "Cómodas, sin dolor y sin tiempo de recuperación: vuelves a tu día a día al momento."),
            ("Seguimiento", "Medimos y fotografiamos para que veas tu evolución sesión a sesión."),
        ],
        "cuidados": [
            "Bebe agua abundante los días de tratamiento corporal.",
            "Respeta la frecuencia de sesiones pautada: la constancia es la clave.",
            "Evita el sol directo en la zona tratada las 48 horas siguientes.",
            "Complementa en casa con la cosmética que te recomendemos.",
        ],
    },

    # ------------------------------------------------------------------ TESLA MED
    "tesla-med": {
        "sobre": (
            "Una tecnología única que sólo está en centros de prestigio",
            [
                "Tesla Med llegó a nuestro centro como un «notición»: un equipo con dos patentes mundiales que garantiza resultados de nivel médico sin infiltraciones, sin dolor y con total seguridad. Desde entonces es uno de los tratamientos más pedidos por nuestras clientas.",
                "Su secreto está en estimular los fibroblastos, las células que fabrican colágeno, elastina y ácido hialurónico reticular. La piel se regenera desde dentro, por eso los resultados son naturales y se notan desde la primera sesión.",
            ],
            "Porque no se trata sólo de verse bien, sino de renacer desde dentro.",
        ),
        "fichas": [
            ("Lifting antiage", "Reconstruye los tejidos y repara las fibras tensoras para un microlifting natural, no invasivo y patentado.", "Pérdida de firmeza y arrugas", ["Óvalo redefinido", "Piel más tensa", "Rejuvenecimiento visible"], "desde 85 €"),
            ("Párpados, bolsas y ojeras", "Tratamiento específico del contorno de ojos: reafirma el párpado, reduce bolsas y aclara la ojera.", "Mirada cansada o caída", ["Mirada abierta", "Menos bolsas", "Ojeras más claras"], "Consultar"),
            ("Relleno de labios sin agujas", "Repulpa, define y aumenta el volumen de los labios sin infiltración ni dolor.", "Labios finos o que han perdido volumen", ["Volumen natural", "Contorno definido", "Sin pinchazos"], "Consultar"),
            ("Código de barras", "Suaviza las arrugas verticales del labio superior regenerando la piel de la zona.", "Arrugas peribucales", ["Labio superior más liso", "Piel regenerada", "Natural"], "Consultar"),
            ("Acné, rosácea y cicatrices", "Calma la inflamación del acné activo y la rosácea y mejora las cicatrices que dejan.", "Pieles con brotes, rojeces o marcas", ["Menos inflamación", "Marcas atenuadas", "Tono uniforme"], "Consultar"),
            ("Manchas", "Regenera la piel y unifica el tono para atenuar manchas solares y hormonales.", "Hiperpigmentación", ["Manchas más claras", "Luz", "Piel uniforme"], "Consultar"),
            ("Papada y cuello", "Reduce y tonifica la zona de la papada y devuelve firmeza a cuello y escote.", "Flacidez en cuello y papada", ["Cuello más firme", "Óvalo definido", "Escote rejuvenecido"], "Consultar"),
            ("Estrías", "Las estrías no se eliminan, pero sí se atenúan: regeneramos el tejido y estimulamos colágeno.", "Estrías recientes o antiguas", ["Estrías menos visibles", "Piel más elástica", "Textura mejorada"], "Consultar"),
        ],
        "proceso": [
            ("Diagnóstico", "Valoramos tu piel y te explicamos qué puede hacer Tesla Med por ti."),
            ("Preparación", "Limpieza y aplicación de activos específicos para la zona a tratar."),
            ("Sesión Tesla Med", "El cabezal trabaja la piel sin dolor. Sólo notarás un ligero cosquilleo."),
            ("Resultado", "Efecto lifting y luminosidad visibles desde la primera sesión; el resultado completo llega con el protocolo."),
        ],
        "cuidados": [
            "Hidrata bien la piel los días posteriores.",
            "Usa protección solar alta durante todo el tratamiento.",
            "Evita sauna y ejercicio intenso las primeras 24 horas.",
            "Completa el protocolo recomendado para resultados duraderos.",
        ],
    },

    # ------------------------------------------------------------------ CORPORALES
    "corporales": {
        "sobre": (
            "Cada curva, cada contorno, cuenta una historia",
            [
                "El cuidado del cuerpo no es sólo estética: es salud, energía y equilibrio. Mientras muchos centros ofrecen tratamientos estándar, nosotras nos sumergimos en comprender tu cuerpo, tus metas y tus preocupaciones para diseñar un plan que dé resultados visibles y duraderos.",
                "Combinamos técnicas manuales como la maderoterapia o el lipodrenaje brasileño con tecnología como Zionic, ondas de choque o cavitación. Y te acompañamos sesión a sesión, con mediciones y fotografías para que veas tu evolución.",
            ],
            "Los cuerpos de verano se trabajan en invierno.",
        ),
        "fichas": [
            ("Zionic", "Radiofrecuencia y masaje activo rotacional. Elimina depósitos de grasa, mejora la celulitis, reafirma y drena. Protocolo recomendado de 6 sesiones.", "Grasa localizada, celulitis, flacidez y glúteos", ["Reduce centímetros", "Efecto push-up", "Indoloro"], "69 € + presoterapia"),
            ("Maderoterapia", "Técnica milenaria con herramientas de madera adaptadas a cada curva. Activa la circulación, rompe la celulitis y moldea.", "Celulitis, retención y remodelación", ["Silueta más definida", "Piel más lisa", "Circulación activa"], "50 €"),
            ("Lipodrenaje brasileño", "Masaje intenso que combina drenaje y modelado. Reduce la retención de líquidos y da un efecto tensor inmediato.", "Retención de líquidos e hinchazón", ["Cintura más marcada", "Efecto plano", "Ligereza"], "50 €"),
            ("Ondas de choque", "Pulsos acústicos que transforman la estructura de la celulitis y mejoran la firmeza y la circulación.", "Celulitis rebelde", ["Piel de naranja atenuada", "Firmeza", "Regeneración"], "50 €"),
            ("Cavitación", "Ultrasonidos que convierten la grasa en una sustancia líquida que el cuerpo elimina de forma natural. Alternativa no quirúrgica.", "Grasa localizada", ["Menos volumen", "Sin cirugía", "Sin reposo"], "50 €"),
            ("Radiofrecuencia corporal", "Calor profundo que estimula colágeno y elastina para una piel firme y elástica.", "Flacidez en abdomen, brazos o muslos", ["Piel tensa", "Textura mejorada", "Efecto acumulativo"], "69 €"),
            ("Evo Sculpt", "Electromagnetismo que genera miles de contracciones musculares para tonificar y definir sin esfuerzo.", "Abdomen y glúteos sin tono", ["Músculo definido", "Glúteos elevados", "20 minutos"], "Consultar"),
            ("Vacumterapia", "Ventosas y succión controlada que oxigenan los tejidos, combaten la celulitis y favorecen el drenaje.", "Celulitis y piernas pesadas", ["Oxigenación", "Drenaje", "Piel más lisa"], "Consultar"),
            ("Metaloterapia", "Terapia con metales que equilibra la energía, desintoxica y aporta un efecto rejuvenecedor a la piel.", "Quien busca un enfoque holístico", ["Equilibrio", "Detox", "Piel revitalizada"], "Consultar"),
            ("Envolturas", "Mascarillas corporales con ingredientes nutritivos y regenerativos que desintoxican e hidratan.", "Piel seca o apagada", ["Hidratación profunda", "Suavidad", "Frescor"], "Consultar"),
            ("Reducell", "Tratamiento 100 % manual en 4 fases: desintoxicación de choque, activación de la lipólisis, termogénesis y remodelación.", "Reducir volumen de forma progresiva", ["Detox", "Quema de grasa", "Reafirmación"], "4 sesiones · 99 €"),
            ("Presoterapia y drenaje", "Drenaje linfático mecánico o manual para eliminar líquidos y aliviar las piernas.", "Retención y piernas cansadas", ["Ligereza", "Menos hinchazón", "Circulación"], "desde 15 €"),
            ("Abdomen postparto", "Protocolo combinado para flacidez, diástasis y cicatriz de cesárea, con delicadeza y paciencia.", "Mamás que quieren recuperar su abdomen", ["Firmeza", "Cicatriz más suave", "Seguridad"], "Valoración gratuita"),
        ],
        "proceso": [
            ("Valoración", "Medimos, fotografiamos y escuchamos tu objetivo."),
            ("Plan a medida", "Combinamos técnicas manuales y aparatología según tu caso."),
            ("Sesiones", "Cómodas y sin tiempo de recuperación, con seguimiento en cada visita."),
            ("Resultados", "Comparamos medidas y fotos para que veas el cambio real."),
        ],
        "cuidados": [
            "Bebe al menos dos litros de agua al día durante el tratamiento.",
            "Acompaña con alimentación equilibrada y algo de actividad física.",
            "Usa en casa la cosmética reductora que te recomendemos.",
            "Respeta la frecuencia de sesiones: la constancia multiplica el resultado.",
        ],
    },

    # ------------------------------------------------------------------ LÁSER
    "depilacion-laser": {
        "sobre": (
            "Olvídate de la cuchilla para siempre",
            [
                "Contamos con un equipo médico de láser de diodo a 810 nm, la longitud de onda de referencia para eliminar el vello de forma progresiva y segura. Las sesiones son rápidas, prácticamente indoloras y se espacian cada dos meses, así que encajan en cualquier agenda.",
                "Además, puedes seguir tu tratamiento también en verano. Notarás resultados desde la primera sesión: menos vello, más fino y más lento en salir, hasta olvidarte de él.",
            ],
            "Adiós a la cera, las cuchillas, las irritaciones y los granitos.",
        ),
        "fichas": [
            ("Facial", "Labio superior, mentón, patillas o rostro completo, con el cabezal de precisión.", "Vello facial", ["Piel lisa", "Sin irritaciones", "Rápido"], "desde 10 €"),
            ("Axilas e ingles", "Las zonas más pedidas, con resultados muy visibles desde las primeras sesiones.", "Quien quiere olvidarse de la cuchilla", ["Sin granitos", "Sin manchas", "Comodidad"], "desde 30 €"),
            ("Piernas y brazos", "Zonas amplias tratadas en poco tiempo gracias al cabezal de gran tamaño.", "Piernas completas, medias o brazos", ["Sesiones rápidas", "Piel suave", "Ahorro de tiempo"], "desde 35 €"),
            ("Espalda, pecho y glúteos", "También para hombres: espalda, pecho y zonas de difícil acceso.", "Hombres y mujeres", ["Resultados duraderos", "Sin dolor", "Seguro"], "desde 20 €"),
            ("Packs combinados", "Las zonas más demandadas juntas a un precio especial: axilas + ingles, + piernas…", "Tratamiento completo", ["Mejor precio", "Una sola cita", "Comodidad"], "desde 49 €"),
        ],
        "proceso": [
            ("Valoración", "Revisamos tu tipo de piel y vello para ajustar el equipo."),
            ("Preparación", "Acudes con la zona rasurada el día anterior, sin cera ni pinzas."),
            ("Sesión", "El cabezal refrigerado trabaja la zona: sensación de calor suave."),
            ("Siguiente cita", "Repetimos cada dos meses hasta conseguir el resultado."),
        ],
        "cuidados": [
            "Rasura la zona 24 horas antes; no uses cera ni pinzas entre sesiones.",
            "Aplica protector solar en la zona tratada.",
            "Evita sauna, piscina con cloro y sol intenso las 48 horas siguientes.",
            "Hidrata la piel con aloe vera si notas calor.",
        ],
    },

    # ------------------------------------------------------------------ CERA E HILO
    "cera-hilo": {
        "sobre": (
            "La depilación de siempre, hecha con mimo",
            [
                "La cera sigue siendo uno de los métodos más rápidos y eficaces. Trabajamos con cera tibia y caliente según la zona y la sensibilidad de tu piel, con un proceso cuidadoso para que sea lo menos molesto posible y el resultado dure semanas.",
                "Para el rostro, nuestra especialidad es el hilo de algodón: extrae el vello desde el folículo sin tocar la piel, por eso es perfecto para pieles sensibles y permite diseñar las cejas con precisión milimétrica. Terminamos siempre con un masaje y aloe vera.",
            ],
            "Un buen diseño de cejas cambia por completo la expresión del rostro.",
        ),
        "fichas": [
            ("Diseño de cejas con hilo", "Estudiamos tus facciones y trazamos la ceja que mejor enmarca tu mirada, pelo a pelo, con hilo de algodón.", "Cejas definidas y pieles sensibles", ["Precisión milimétrica", "Sin irritación", "Masaje final"], "10 €"),
            ("Hilo facial", "Labio superior o rostro completo sin cejas. Ideal para el vello fino y las pieles que reaccionan a la cera.", "Vello facial fino", ["Respetuoso", "Rápido", "Sin rojeces duraderas"], "desde 8 €"),
            ("Cera facial", "Cejas, labio, mentón y patillas con cera de baja temperatura.", "Mantenimiento rápido", ["Rápido", "Duradero", "Económico"], "desde 5 €"),
            ("Cera corporal", "Piernas, ingles, axilas, espalda, brazos, pecho y glúteos, para mujer y hombre.", "Todo el cuerpo", ["Resultados de 3 a 5 semanas", "Piel suave", "Vello más débil con el tiempo"], "desde 5 €"),
            ("Diseño con henna", "Rellena huecos y da densidad y forma durante una semana aproximadamente, con tinte natural.", "Cejas finas o con huecos", ["Cejas más pobladas", "Natural", "Sin maquillaje"], "20 €"),
        ],
        "proceso": [
            ("Estudio", "Miramos tus facciones y la forma natural de tu ceja o la zona a depilar."),
            ("Depilación", "Hilo o cera, con la técnica más respetuosa para tu piel."),
            ("Calma", "Masaje con aloe vera para cerrar el poro y evitar rojeces."),
            ("Mantenimiento", "Te recomendamos cuándo volver para mantener el diseño."),
        ],
        "cuidados": [
            "No tomes el sol ni uses sauna las 24 horas siguientes.",
            "Exfolia el cuerpo dos veces por semana para evitar pelos enquistados.",
            "Deja crecer el vello unos 5 mm antes de la cera.",
            "Repite las cejas cada 3 o 4 semanas.",
        ],
    },

    # ------------------------------------------------------------------ PESTAÑAS
    "pestanas": {
        "sobre": (
            "La mirada es la joya del rostro",
            [
                "Tus ojos hablan antes que cualquier otra parte de ti: en una reunión, en una cita o en una foto. Por eso diseñamos cada servicio de pestañas a partir de tu mirada, la forma de tus ojos y el efecto que te hace sentir tú.",
                "Si te encantan tus pestañas naturales, el lifting las eleva, curva y oscurece durante semanas. Si buscas más, las extensiones pelo a pelo o de volumen ruso te dan densidad y longitud con un acabado ligero y cómodo. Y en todos los casos, adiós al rímel.",
            ],
            "Despierta cada mañana con la mirada hecha.",
        ),
        "fichas": [
            ("Lifting de pestañas y tinte", "Elevamos y curvamos tus pestañas desde la raíz y las teñimos para un efecto de máscara permanente. Dura de 4 a 8 semanas.", "Pestañas lacias o rectas", ["Mirada abierta", "Sin rizador", "Natural"], "45 €"),
            ("Extensiones clásicas pelo a pelo", "Una extensión sobre cada pestaña natural: realce sutil, elegante y muy natural.", "Primer contacto con las extensiones", ["Más longitud", "Efecto natural", "Ligeras"], "50 €"),
            ("Extensiones de volumen", "Abanicos de extensiones ultrafinas para multiplicar la densidad y lograr una mirada intensa.", "Quien busca impacto", ["Densidad", "Mirada de infarto", "Diseño a medida"], "60 €"),
            ("Volumen ruso", "La técnica más sofisticada de volumen, con abanicos hechos a mano para un resultado esponjoso y sofisticado.", "Ocasiones especiales y amantes del glamour", ["Máximo volumen", "Ligero", "Efecto terciopelo"], "Consultar"),
            ("Rellenos", "Reponemos las extensiones que se caen con el ciclo natural para que luzcas siempre perfectas.", "Mantenimiento cada 2 a 4 semanas", ["Siempre impecables", "Más económico", "Rápido"], "desde 25 €"),
        ],
        "proceso": [
            ("Diseño", "Estudiamos tu ojo y elegimos curvatura, grosor y longitud."),
            ("Preparación", "Limpiamos la pestaña y protegemos la piel con parches."),
            ("Aplicación", "Te tumbas, cierras los ojos y te relajas: muchas clientas se duermen."),
            ("Resultado", "Te enseñamos cómo cuidar tus pestañas en casa."),
        ],
        "cuidados": [
            "No mojes las pestañas las primeras 48 horas.",
            "Evita productos con aceites en la zona de los ojos.",
            "Lávalas a diario con un limpiador específico y péinalas.",
            "Nunca uses rizador sobre extensiones o lifting.",
        ],
    },

    # ------------------------------------------------------------------ CEJAS Y MICRO
    "cejas-micropigmentacion": {
        "sobre": (
            "La micropigmentación no es sólo estética, es armonía",
            [
                "Antes de trazar una sola línea estudiamos tus facciones, la forma de tu rostro y el color de tu piel y tu pelo. A partir de ahí elegimos la técnica y el tono que mejor te favorecen para un resultado natural, que se integre contigo.",
                "Con la micropigmentación de cejas, ojos o labios ahorras tiempo cada mañana y luces impecable las 24 horas, incluso en la piscina o en el gimnasio. Y si prefieres algo temporal, el diseño con henna da forma y densidad a tus cejas durante una semana.",
            ],
            "Tu rostro perfecto las 24 horas del día.",
        ),
        "fichas": [
            ("Cejas pelo a pelo", "Trazos finos que imitan el vello natural para rellenar huecos y redibujar la ceja con total realismo.", "Cejas despobladas o con huecos", ["Natural", "Definición", "Duradero"], "Consultar"),
            ("Cejas sombreadas", "Efecto polvo o maquillado, suave y difuminado, perfecto para un acabado elegante.", "Quien se maquilla las cejas a diario", ["Efecto maquillaje", "Uniforme", "Favorecedor"], "Consultar"),
            ("Labios", "Color, contorno y volumen visual. Rejuvenece el rostro y te olvidas del pintalabios.", "Labios sin color o con contorno difuso", ["Color natural", "Contorno definido", "Efecto volumen"], "Consultar"),
            ("Eyeliner clásico", "Una línea definida que agranda la mirada y no se corre.", "Amantes del eyeliner", ["Mirada intensa", "Sin retoques", "Precisión"], "Consultar"),
            ("Eyeliner sombreado y babyliner", "Versiones más difuminadas o ultrafinas para un efecto sutil.", "Quien busca algo discreto", ["Suave", "Elegante", "Natural"], "Consultar"),
            ("Entre pestañas", "Pigmento en la raíz de las pestañas que da sensación de densidad sin que se note.", "Pestañas finas o claras", ["Más densidad", "Invisible", "Mirada definida"], "Consultar"),
            ("Diseño de cejas con henna", "Tinte natural que rellena, define y da forma durante una semana aproximadamente.", "Cejas finas, claras o con huecos", ["Forma perfecta", "Natural", "Rápido"], "20 €"),
            ("Laminado de cejas", "Peina y fija el vello hacia arriba para unas cejas más pobladas y ordenadas.", "Cejas rebeldes o desordenadas", ["Efecto lleno", "Ordenadas", "Varias semanas"], "Consultar"),
        ],
        "proceso": [
            ("Consulta gratuita", "Estudiamos tu rostro, resolvemos dudas y elegimos técnica y tono."),
            ("Diseño", "Dibujamos el resultado sobre tu piel y no empezamos hasta que te encanta."),
            ("Pigmentación", "Con anestésico tópico y material estéril de un solo uso."),
            ("Retoque", "Revisamos el resultado y fijamos el pigmento al cabo de unas semanas."),
        ],
        "cuidados": [
            "No mojes ni maquilles la zona la primera semana.",
            "No arranques las costritas: caerán solas.",
            "Evita sol, sauna y piscina durante 15 días.",
            "Usa protector solar para que el color dure más.",
        ],
    },

    # ------------------------------------------------------------------ UÑAS
    "unas": {
        "sobre": (
            "La manicura se ha convertido en un arte",
            [
                "Tus manos y tus pies son una expresión de tu personalidad. Desde la elección del color hasta la técnica, cada detalle cuenta: por eso nos mantenemos al día en tendencias y técnicas y trabajamos con productos de calidad que cuidan tu uña natural.",
                "Esmaltado permanente que dura semanas, revestimiento para que tu uña crezca fuerte, acrigel para alargar sin esperar, manicura rusa para una cutícula impecable y diseños a mano alzada para lucir ese modelo que tenías guardado en Pinterest.",
            ],
            "Arriesga con el color y prueba ese diseño que tenías guardado.",
        ),
        "fichas": [
            ("Manicura con esmaltado permanente", "Una manicura perfecta y brillante durante semanas, resistente al día a día. Francesa, baby boomer o tu color favorito.", "Uñas perfectas sin preocuparte", ["Duración de 2 a 3 semanas", "Brillo intacto", "Secado inmediato"], "1 h · 19 €"),
            ("Revestimiento sobre uña natural", "Una fina capa de gel que protege y refuerza la uña para que el esmaltado dure más y crezca hasta el largo que deseas.", "Uñas débiles o que se rompen", ["Uña más fuerte", "Crece sin romperse", "Más duración"], "1 h 15 min · 24 €"),
            ("Uñas de acrigel", "La robustez de la porcelana con la flexibilidad del gel. Alarga la uña y consigue el largo que quieres sin esperar meses.", "Uñas cortas o mordidas", ["Largo inmediato", "Resistente", "Ligera"], "2 h · consultar"),
            ("Uñas de gel y XXL", "Construcción en gel con la forma y el largo que elijas, y su relleno periódico.", "Amantes de las uñas largas", ["Forma a medida", "Duración", "Diseños ilimitados"], "desde 39 €"),
            ("Manicura rusa", "Técnica con torno para trabajar la cutícula con precisión y un acabado limpísimo que dura más.", "Quien quiere una manicura impecable", ["Cutícula perfecta", "Esmalte más pegado al borde", "Acabado profesional"], "20 €"),
            ("Manicura japonesa", "Tratamiento natural con pasta y polvos minerales que nutre, fortalece y da brillo sin esmalte.", "Uñas naturales sanas y brillantes", ["Brillo natural", "Fortalece", "Sin esmalte"], "20 €"),
            ("Pedicura completa", "Eliminamos durezas, trabajamos cutículas y exfoliamos. Terminamos con crema nutritiva y masaje relajante.", "Pies cuidados todo el año", ["Pies suaves", "Sin durezas", "Masaje relajante"], "desde 25 €"),
            ("Pedicura spa", "La versión más completa, con baño, exfoliación, mascarilla y masaje prolongado.", "Un mimo de pies a cabeza", ["Relajación", "Hidratación profunda", "Pies de seda"], "35 €"),
            ("Nail art", "Decoraciones a mano alzada, francesas, baby boomer, efectos y piedras.", "Ocasiones especiales y amantes del diseño", ["Personalizado", "Tendencia", "Único"], "desde 1 €"),
        ],
        "proceso": [
            ("Elección", "Te enseñamos la carta de colores y diseños de temporada."),
            ("Preparación", "Limado, cutícula y preparación de la uña natural."),
            ("Aplicación", "Esmaltado, revestimiento o construcción, capa a capa."),
            ("Acabado", "Aceite de cutícula y crema: manos listas para presumir."),
        ],
        "cuidados": [
            "Usa guantes para fregar y limpiar con productos agresivos.",
            "Hidrata la cutícula a diario con aceite.",
            "No retires el esmalte permanente tú misma: te lo quitamos sin dañar la uña.",
            "Pide cita de relleno o retirada cada 3 semanas.",
        ],
    },

    # ------------------------------------------------------------------ RITUALES
    "rituales-masajes": {
        "sobre": (
            "Un regalo para todos los sentidos",
            [
                "Nuestros rituales duran noventa minutos y empiezan con un peeling corporal que elimina las células muertas. Después, una envoltura —una mascarilla para todo el cuerpo— nutre e hidrata la piel; una ducha, y un masaje completo de una hora que te deja en otro planeta. Al terminar, te llevas un detalle.",
                "Y para el día a día, masajes relajantes, circulatorios y localizados, además de fisioterapia y osteopatía de la mano de un profesional con formación en fisioterapia deportiva, neurológica, oncológica y respiratoria.",
            ],
            "Regalar un momento de desconexión no tiene precio.",
        ),
        "fichas": [
            ("Masaje relajante", "Una hora de masaje de cuerpo completo para soltar tensiones, reducir el estrés y dormir mejor.", "Estrés y cansancio", ["Desconexión total", "Músculos relajados", "Mejor descanso"], "1 h · 48 €"),
            ("Peeling corporal + masaje", "Exfoliación de todo el cuerpo seguida de masaje con aceites nutritivos.", "Piel apagada y ganas de mimo", ["Piel renovada", "Suavidad", "Relajación"], "1 h · 55 €"),
            ("Masaje circulatorio", "Movimientos ascendentes que activan la circulación y alivian las piernas cansadas.", "Piernas pesadas o hinchadas", ["Ligereza", "Menos hinchazón", "Bienestar"], "30 min · 30 €"),
            ("Masaje localizado", "Espalda, cuello y hombros: donde se acumula la tensión de las horas frente al ordenador.", "Contracturas y malas posturas", ["Alivio", "Movilidad", "Rapidez"], "30 min · 30 €"),
            ("Masaje facial anti-bruxismo", "Nuestro fisioterapeuta trabaja los puntos clave de la mandíbula, la cara y el cuello.", "Quien aprieta los dientes o tiene cefaleas", ["Menos tensión mandibular", "Mejor sueño", "Alivio cervical"], "Consultar"),
            ("Fisioterapia y osteopatía", "Terapia manual, osteopatía y fisioterapia deportiva, neurológica, oncológica y respiratoria.", "Dolor de espalda, lesiones o recuperación", ["Tratamiento profesional", "Alivio del dolor", "Plan personalizado"], "Consultar"),
            ("Presoterapia ocular y capilar", "Presoterapia en el contorno de ojos mientras te damos un masaje capilar que estimula el crecimiento del pelo.", "Un mimo diferente", ["Mirada descansada", "Cuero cabelludo activado", "Relax"], "Consultar"),
        ],
        "proceso": [
            ("Bienvenida", "Te recibimos con calma, música suave y aroma amaderado."),
            ("Peeling y envoltura", "Exfoliación y mascarilla corporal con el aroma de tu ritual."),
            ("Masaje", "Una hora de manos expertas, a tu ritmo y a tu presión."),
            ("Despedida", "Infusión, tiempo para volver en ti y un detalle para llevarte."),
        ],
        "cuidados": [
            "Llega unos minutos antes para empezar ya relajada.",
            "Bebe agua después del masaje para favorecer la eliminación de toxinas.",
            "Evita comidas copiosas justo antes de tu ritual.",
            "Si es un regalo, pídenos la tarjeta personalizada.",
        ],
    },

    # ------------------------------------------------------------------ COSMÉTICA
    "cosmetica": {
        "sobre": (
            "Los mejores productos para los mejores resultados",
            [
                "Nuestras esteticistas han seleccionado una gama de firmas líderes que comparten nuestro compromiso con la excelencia: ingredientes de primera calidad, tecnologías de vanguardia y, en muchos casos, fórmulas sin parabenos ni sulfatos y respetuosas con el medio ambiente.",
                "Te recomendamos sólo lo que tu piel necesita después de verla en cabina, para que el resultado del tratamiento continúe en casa. Y para regalar, preparamos cofres y packs con mucho mimo.",
            ],
            "La rutina adecuada multiplica el efecto de cada tratamiento.",
        ),
        "fichas": [
            ("Eberlin", "Cosmética natural de alta eficacia con activos botánicos. La usamos en cabina y la puedes llevar a casa.", "Pieles que buscan eficacia natural", ["Activos vegetales", "Resultados visibles", "Sensorialidad"], "Consultar"),
            ("Casmara", "Firma profesional con tratamientos específicos: RGnerin, contorno, despigmentantes y más.", "Tratamientos dirigidos", ["Alta concentración", "Específica", "Profesional"], "Consultar"),
            ("Ampollas de ácido hialurónico", "Hidratación profunda con efecto relleno: las arrugas finas se suavizan y la piel queda jugosa.", "Pieles deshidratadas o maduras", ["Efecto relleno", "Textura ligera", "Luz"], "Consultar"),
            ("Vitamina C", "El antioxidante esencial: reduce manchas, da luz y protege frente a la contaminación.", "Pieles apagadas o con manchas", ["Luminosidad", "Protección", "Tono uniforme"], "Consultar"),
            ("Sheet masks profesionales", "La calidad de cabina en formato mascarilla para un rescate inmediato en casa.", "Antes de un evento", ["Efecto inmediato", "Cómodo", "Profesional"], "Consultar"),
            ("Cosmética corporal reductora", "Fórmulas con triple acción lipolítica, anticelulítica y reafirmante para potenciar Zionic en casa.", "Quien sigue un tratamiento corporal", ["Activa la circulación", "Reduce la piel de naranja", "Reafirma"], "Consultar"),
            ("Cofres y packs regalo", "Selecciones preparadas para Navidad, Reyes, San Valentín o el Día de la Madre.", "Regalar y acertar", ["Presentación cuidada", "Productos profesionales", "A medida"], "Consultar"),
        ],
        "proceso": [
            ("Diagnóstico", "Vemos tu piel y tu rutina actual."),
            ("Selección", "Elegimos sólo los productos que necesitas, sin excesos."),
            ("Rutina", "Te explicamos el orden y la forma de aplicación."),
            ("Revisión", "En tu próxima visita ajustamos la rutina si hace falta."),
        ],
        "cuidados": [
            "Limpia la piel mañana y noche, aunque no te maquilles.",
            "Aplica los productos de más ligero a más denso.",
            "Protector solar siempre como último paso por la mañana.",
            "Consulta con nosotras antes de combinar activos potentes.",
        ],
    },
}
