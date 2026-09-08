#!/usr/bin/env python3
"""Build es/index.html from index.html.

The Spanish edition is the English page with every visible string swapped.
Structure, CSS, JS and structured data are shared, so a feature added to the
English page reaches the Spanish one on the next run. Every replacement is
asserted: if the English source text changes, the build fails and names the
string, which is the point. Run from the repo root:  python3 tools/build-es.py
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'index.html').read_text()

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if (count is None and n == 0) or (count is not None and n != count):
        sys.exit(f'build-es: expected {count} of {old[:70]!r}, found {n}')
    s = s.replace(old, new)

# ── document ──
rep('<html lang="en">', '<html lang="es">')
rep('<title>Primo Strategic Communication · Meaning that moves institutions</title>',
    '<title>Primo Strategic Communication · Sentido que mueve instituciones</title>')
rep('<meta name="description" content="Primo Strategic Communication. Jesse Cruz: fifteen years of strategic communication inside the UN system, UNICEF, and the Forest Stewardship Council. Strategy, campaigns, editorial, and measurement for public institutions, from the UN system to government agencies.">',
    '<meta name="description" content="Primo Strategic Communication. Jesse Cruz: quince años de comunicación estratégica dentro del sistema de las Naciones Unidas, UNICEF y el Forest Stewardship Council. Estrategia, campañas, editorial y medición para instituciones públicas, del sistema de la ONU a las agencias de gobierno.">')
rep('<meta property="og:description" content="Fifteen years of strategic communication inside the UN system. Strategy, campaigns, editorial, and measurement for public institutions, from the UN system to government agencies.">',
    '<meta property="og:description" content="Quince años de comunicación estratégica dentro del sistema de la ONU. Estrategia, campañas, editorial y medición para instituciones públicas, del sistema de la ONU a las agencias de gobierno.">')
rep('<meta property="og:url" content="https://w0rldcit1zen.github.io/Portfolio/">',
    '<meta property="og:url" content="https://w0rldcit1zen.github.io/Portfolio/es/">')
rep('<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_ES">',
    '<meta property="og:locale" content="es_ES">\n<meta property="og:locale:alternate" content="en_US">')
rep('<link rel="canonical" href="https://w0rldcit1zen.github.io/Portfolio/">',
    '<link rel="canonical" href="https://w0rldcit1zen.github.io/Portfolio/es/">')
rep('href="assets/', 'href="../assets/', None)   # icon, PDF link (og:image is absolute)
rep('src="assets/', 'src="../assets/', None)     # lockups, posters
rep('href="fonts/', 'href="../fonts/', None)
rep("url('fonts/", "url('../fonts/", None)
rep('<a class="cap nav-lang" href="es/" lang="es" hreflang="es">Español</a>',
    '<a class="cap nav-lang" href="../" lang="en" hreflang="en">English</a>')
rep('<a class="skip" href="#main">Skip to content</a>', '<a class="skip" href="#main">Ir al contenido</a>')
rep('aria-label="Menu"', 'aria-label="Menú"')

# ── nav ──
rep('<a class="cap" href="#approach">Approach</a>', '<a class="cap" href="#approach">Enfoque</a>')
rep('<a class="cap" href="#services">What I do</a>', '<a class="cap" href="#services">Qué hago</a>')
rep('<a class="cap" href="#work">The record</a>', '<a class="cap" href="#work">El historial</a>')
rep('<a class="cap" href="#about">About</a>', '<a class="cap" href="#about">Sobre mí</a>')
rep('<a class="cap nav-cta" href="#contact">Get in touch</a>', '<a class="cap nav-cta" href="#contact">Contacto</a>')

# ── hero ──
rep('<span class="cap">Strategic communication</span>', '<span class="cap">Comunicación estratégica</span>')
rep('Multilateral · Government · INGO<br>Geneva · Beijing · Bonn · Los Angeles',
    'Multilateral · Gobierno · ONG internacional<br>Ginebra · Pekín · Bonn · Los Ángeles')
rep('<h1>Meaning that moves institutions.</h1>', '<h1>Sentido que mueve instituciones.</h1>')

# ── positioning ──
rep('<span class="cap eyebrow">Positioning</span>', '<span class="cap eyebrow">Posicionamiento</span>')
rep('<p class="lede">I help public institutions get understood.</p>',
    '<p class="lede">Ayudo a las instituciones públicas a hacerse entender.</p>')
rep('By policymakers, by publics, by the people a mandate exists to serve. Fifteen years inside the UN system taught me where recognition is earned and where it quietly stalls. The craft is the full gamut: strategy, campaigns, media, editorial, measurement, crisis. I automate where it makes sense, go agentic where it earns its place, and keep a human in the loop, always. So even a small team can run the full playbook.',
    'Por quienes deciden, por los públicos, por las personas a las que un mandato existe para servir. Quince años dentro del sistema de la ONU me enseñaron dónde se gana el reconocimiento y dónde se estanca sin hacer ruido. El oficio es completo: estrategia, campañas, medios, editorial, medición, crisis. Automatizo donde tiene sentido, uso agentes donde se lo ganan y mantengo siempre a una persona al mando. Así hasta un equipo pequeño puede ejecutar el manual entero.')

# ── philosophy ──
rep('<span class="cap eyebrow">Philosophy</span>', '<span class="cap eyebrow">Filosofía</span>')
rep('<p class="lede">Communication is how strategy becomes real.</p>',
    '<p class="lede">La comunicación es cómo la estrategia se vuelve real.</p>')
rep("I learned this on early warning systems. The framing had to move from doom and gloom to resilience and security, and the circle had to widen: the conversation belonged to experts, and the people who needed it most were not in it. The fix is point guard work. The whole floor has to know the play before the offense can run, so you listen first, you stop assuming an expert audience, and you adjust for different levels of technical knowledge and different levels of English. Everyone gets brought along, or the message didn't work. That's the job.",
    'Lo aprendí con los sistemas de alerta temprana. El encuadre tenía que pasar del catastrofismo a la resiliencia y la seguridad, y el círculo tenía que abrirse: la conversación era de los expertos, y quienes más la necesitaban no estaban en ella. La solución es trabajo de armador, como en el baloncesto. Toda la cancha tiene que conocer la jugada antes de que el ataque funcione, así que primero se escucha, se deja de suponer un público experto y se ajusta a distintos niveles de conocimiento técnico y distintos niveles de inglés. O todos suben a bordo, o el mensaje no funcionó. Ese es el trabajo.')
rep('<div class="p-title">Strategy first</div>', '<div class="p-title">Primero la estrategia</div>')
rep('<p>I walk in having read the mandate. Positioning and evidence before content, always.</p>',
    '<p>Llego con el mandato leído. Posicionamiento y evidencia antes que contenido, siempre.</p>')
rep('<div class="p-title">The field, from inside</div>', '<div class="p-title">El terreno, desde dentro</div>')
rep('<p>WMO, UNICEF China, FSC. I know where recognition is earned and where it is quietly withheld.</p>',
    '<p>OMM, UNICEF China, FSC. Sé dónde se gana el reconocimiento y dónde se niega en silencio.</p>')
rep('<div class="p-title">Systems that multiply</div>', '<div class="p-title">Sistemas que multiplican</div>')
rep('<p>Agentic pipelines extend a small team into continuous presence. The multiplier under the craft; the judgment stays human.</p>',
    '<p>Las cadenas agénticas convierten a un equipo pequeño en presencia continua. El multiplicador bajo el oficio; el criterio sigue siendo humano.</p>')

# ── services ──
rep('<span class="cap eyebrow">What I do</span>', '<span class="cap eyebrow">Qué hago</span>')
rep('<h2>Five ways to work with me.</h2>', '<h2>Cinco maneras de trabajar conmigo.</h2>')
rep('One principal, a network of specialists. Scaled to the moment, from a single launch to a standing editorial function.',
    'Un director, una red de especialistas. A la escala del momento, de un solo lanzamiento a una función editorial permanente.')
rep('<span class="cap">01 · Research</span>', '<span class="cap">01 · Investigación</span>')
rep('<h3>Know your publics</h3>', '<h3>Conozca a sus públicos</h3>')
rep('<p>Segmentation studies and the media landscape before a franc is spent: who your audiences actually are, what they believe, where recognition will be won. The baseline everything else is measured against.</p>',
    '<p>Estudios de segmentación y del panorama mediático antes de gastar un franco: quiénes son de verdad sus públicos, qué creen, dónde se ganará el reconocimiento. La línea de base contra la que se mide todo lo demás.</p>')
rep('<span class="cap">02 · Strategy</span>', '<span class="cap">02 · Estrategia</span>')
rep('<h3>Narrative architecture</h3>', '<h3>Arquitectura narrativa</h3>')
rep('<p>I diagnose where recognition is being won or withheld, then build the outcome objectives, the power map, and a message house where every proof point carries a citation. The crisis pack gets built here too, before you need it. I arrive having already read the mandate.</p>',
    '<p>Diagnostico dónde se está ganando o negando el reconocimiento y construyo los objetivos de resultado, el mapa de poder y una casa de mensajes donde cada prueba lleva su cita. El paquete de crisis también se arma aquí, antes de que haga falta. Llego con el mandato ya leído.</p>')
rep('<span class="cap">03 · Production</span>', '<span class="cap">03 · Producción</span>')
rep('<h3>Mandate-scale editorial</h3>', '<h3>Editorial a escala de mandato</h3>')
rep('<p>From flagship launches to always-on presence, across owned, earned, shared, and paid: editorial craft, multimedia, press relations, performance media. Engineered for human readers and answer engines alike.</p>',
    '<p>De los lanzamientos insignia a la presencia permanente, en medios propios, ganados, compartidos y pagados: oficio editorial, multimedia, relaciones con la prensa, medios de resultados. Diseñado para lectores humanos y para los motores de respuesta por igual.</p>')
rep('<span class="cap">04 · Measurement</span>', '<span class="cap">04 · Medición</span>')
rep('<h3>Measurement &amp; memory</h3>', '<h3>Medición y memoria</h3>')
rep('<p>Evaluation on the AMEC chain: outputs to outcomes to impact, never AVEs. And the learning is captured, not lost: a knowledge base your institution keeps when the engagement ends.</p>',
    '<p>Evaluación sobre la cadena AMEC: de productos a resultados a impacto, nunca equivalentes publicitarios. Y el aprendizaje se captura, no se pierde: una base de conocimiento que su institución conserva cuando termina el encargo.</p>')
rep('<span class="cap">05 · Capacity</span>', '<span class="cap">05 · Capacidad</span>')
rep('<h3>Handoff &amp; coaching</h3>', '<h3>Traspaso y acompañamiento</h3>')
rep('<p>I build capability, not dependency. Teams trained, workflows documented, communicators coached until the infrastructure is entirely theirs to run.</p>',
    '<p>Construyo capacidad, no dependencia. Equipos formados, flujos documentados, comunicadores acompañados hasta que la infraestructura es enteramente suya.</p>')
rep('<span class="cap">The rail · Systems</span>', '<span class="cap">El raíl · Sistemas</span>')
rep('<h3>AI-native workflows</h3>', '<h3>Flujos de trabajo nativos en IA</h3>')
rep('<p>The rail under all five: secure, private LLM environments, automated pipelines, machine learning where the data justifies it. The systems power the work; the judgment stays human.</p>',
    '<p>El raíl bajo las cinco: entornos LLM seguros y privados, cadenas automatizadas, aprendizaje automático donde los datos lo justifican. Los sistemas impulsan el trabajo; el criterio sigue siendo humano.</p>')

# ── work ──
rep('<span class="cap eyebrow">The record</span>', '<span class="cap eyebrow">El historial</span>')
rep('<h2>Check the scoreboard.</h2>', '<h2>Mire el marcador.</h2>')
rep('Fifteen years across the UN system, UNICEF, and the Forest Stewardship Council. Every result below is from my own desk, inside the institutions I now serve. Ask me about any of them.',
    'Quince años entre el sistema de la ONU, UNICEF y el Forest Stewardship Council. Cada resultado de abajo salió de mi propio escritorio, dentro de las instituciones a las que ahora sirvo. Pregúnteme por cualquiera.')

# 01
rep('<span class="cap focal-label">Followers · four years</span>', '<span class="cap focal-label">Seguidores · cuatro años</span>')
rep('Followers, all channels: 200,000 on arrival, 1.3 million four years later.', 'Seguidores, todos los canales: 200.000 a la llegada, 1,3 millones cuatro años después.')
rep('<title>Arrival: 200K</title>', '<title>Llegada: 200K</title>')
rep('>ARRIVAL</text>', '>LLEGADA</text>')
rep('<title>Four Years Later: 1.3M</title>', '<title>Cuatro años después: 1,3M</title>')
rep('>FOUR YEARS LATER</text>', '>CUATRO AÑOS DESPUÉS</text>')
rep('<figcaption>Source: WMO digital analytics</figcaption>', '<figcaption>Fuente: analítica digital de la OMM</figcaption>')
rep('<h3>Audience growth at global scale</h3>', '<h3>Crecimiento de audiencia a escala global</h3>')
rep('Strategy · Multi-channel delivery · Measurable impact', 'Estrategia · Ejecución multicanal · Impacto medible')
rep('<p>When I arrived at WMO, total following sat around 200,000. Four years later it broke 1.3 million. No accident. We shut off the institutional noise, moved the weight to LinkedIn where the policymakers actually are, and built a content machine a small team could run.</p>',
    '<p>Cuando llegué a la OMM, el total de seguidores rondaba los 200.000. Cuatro años después superó 1,3 millones. Nada de casualidad. Apagamos el ruido institucional, movimos el peso a LinkedIn, donde de verdad están quienes deciden, y construimos una máquina de contenido que un equipo pequeño podía operar.</p>')
rep('<p>The deeper win was framing. #StateOfClimate skewed negative and jargon-bound, and doom loses to benefit, security, and agency every time. I partnered with climate scientist Ed Hawkins to put his warming stripes at the heart of the visual story. Mentions rose 661%, at 4.6% engagement against a 2 to 3% sector benchmark.</p>',
    '<p>La victoria de fondo fue el encuadre. #StateOfClimate tiraba a lo negativo y a la jerga, y el catastrofismo pierde siempre frente al beneficio, la seguridad y la capacidad de actuar. Me asocié con el climatólogo Ed Hawkins para poner sus franjas de calentamiento en el centro de la historia visual. Las menciones subieron un 661 %, con un 4,6 % de interacción frente a un referente sectorial del 2 al 3 %.</p>')
rep('<b>RESULT</b>200,000 → 1.3M followers, all channels, four years', '<b>RESULTADO</b>200.000 → 1,3M seguidores, todos los canales, cuatro años')
rep('<b>CONTEXT</b>#StateOfClimate mentions +661% · engagement 4.6% vs 2–3% benchmark', '<b>CONTEXTO</b>menciones de #StateOfClimate +661 % · interacción 4,6 % vs referente 2–3 %')
rep('<b>VERIFIED</b>WMO digital analytics · retrievable on request', '<b>VERIFICADO</b>analítica digital de la OMM · disponible a petición')
rep('The warming-stripes post on LinkedIn →', 'La publicación de las franjas de calentamiento en LinkedIn →')

# 02
rep('<span class="cap focal-label">Inbound dialogue</span>', '<span class="cap focal-label">Diálogo entrante</span>')
rep('Growth, 2025 reporting cycle: impressions up 94.1 percent, engagement up 117.7 percent.', 'Crecimiento, ciclo de reporte 2025: impresiones +94,1 por ciento, interacción +117,7 por ciento.')
rep('<title>Impressions: +94.1%</title>', '<title>Impresiones: +94,1 %</title>')
rep('>IMPRESSIONS</text>', '>IMPRESIONES</text>')
rep('<title>Engagement: +117.7%</title>', '<title>Interacción: +117,7 %</title>')
rep('>ENGAGEMENT</text>', '>INTERACCIÓN</text>')
rep('<figcaption>Source: 2025 reporting cycle</figcaption>', '<figcaption>Fuente: ciclo de reporte 2025</figcaption>')
rep('<h3>From broadcast to community</h3>', '<h3>De la difusión a la comunidad</h3>')
rep('Community strategy · Social intelligence · ROI discipline', 'Estrategia de comunidad · Inteligencia social · Disciplina de ROI')
rep("<p>The one-way broadcast is over. I led WMO's shift from broadcast model to community model, and the data held up: inbound messages up 600%, engagement growth (+117.7%) outpacing impression growth (+94.1%). Everyone wants to go viral. Almost nobody connects. You hit a moving audience with consistency, not stunts.</p>",
    '<p>La difusión en un solo sentido se acabó. Lideré el paso de la OMM del modelo de difusión al modelo de comunidad, y los datos aguantaron: mensajes entrantes +600 %, con la interacción (+117,7 %) creciendo más rápido que las impresiones (+94,1 %). Todo el mundo quiere hacerse viral. Casi nadie conecta. A una audiencia en movimiento se le llega con constancia, no con golpes de efecto.</p>')
rep('<p>I also put a number on the function itself: the channel portfolio valued at roughly USD 6.4 million in CPA, CPC, and CPM terms. Communication defended in the language executives actually use.</p>',
    '<p>También le puse número a la propia función: la cartera de canales valorada en unos 6,4 millones de USD en términos de CPA, CPC y CPM. Comunicación defendida en el idioma que de verdad hablan los directivos.</p>')
rep('<b>RESULT</b>inbound +600% · engagement +117.7% vs impressions +94.1%', '<b>RESULTADO</b>entrantes +600 % · interacción +117,7 % vs impresiones +94,1 %')
rep('<b>VALUATION</b>~USD 6.4M channel portfolio, market replacement cost', '<b>VALORACIÓN</b>cartera de canales de ~6,4M USD, coste de reposición a mercado')
rep('<b>VERIFIED</b>2025 reporting cycle · retrievable on request', '<b>VERIFICADO</b>ciclo de reporte 2025 · disponible a petición')

# 03
rep('<span class="cap focal-label">Mentions · one year</span>', '<span class="cap focal-label">Menciones · un año</span>')
rep('Mentions on X: 7.5 million before the campaign, 80 million one year later.', 'Menciones en X: 7,5 millones antes de la campaña, 80 millones un año después.')
rep('<title>Before: 7.5M</title>', '<title>Antes: 7,5M</title>')
rep('>BEFORE</text>', '>ANTES</text>')
rep('<title>One Year Later: 80M</title>', '<title>Un año después: 80M</title>')
rep('>ONE YEAR LATER</text>', '>UN AÑO DESPUÉS</text>')
rep('<figcaption>Source: on request</figcaption>', '<figcaption>Fuente: a petición</figcaption>')
rep('<h3>Changing the conversation</h3>', '<h3>Cambiar la conversación</h3>')
rep('Emergency preparedness · Human-centered storytelling · Multi-agency orchestration', 'Preparación ante emergencias · Narrativa centrada en las personas · Orquestación entre agencias')
rep('<p>Early Warnings for All is the UN mandate to protect every person on Earth with early warning systems by 2027. When we took it on, the conversation belonged to technical experts. The people who need those systems most were missing from it. We brought in storytelling: flags on beaches for fishers, radio bulletins, church bells. Within a year, mentions on X grew from 7.5 million to 80 million.</p>',
    '<p>Alertas Tempranas para Todos es el mandato de la ONU para proteger a cada persona del planeta con sistemas de alerta temprana antes de 2027. Cuando lo asumimos, la conversación era de los expertos técnicos. Quienes más necesitan esos sistemas no estaban en ella. Trajimos la narrativa: banderas en las playas para los pescadores, boletines de radio, campanas de iglesia. En un año, las menciones en X pasaron de 7,5 millones a 80 millones.</p>')
rep('<p>I led communications across the task force with IFRC, UNDRR, and ITU, ran the CHF 200,000 campaign budget and its procurement, and got very large agencies behind one voice. Then we repeated it, everywhere, until it stuck.</p>',
    '<p>Lideré la comunicación del grupo de trabajo con la FICR, la UNDRR y la UIT, gestioné el presupuesto de campaña de 200.000 CHF y su licitación, y puse a agencias muy grandes detrás de una sola voz. Después lo repetimos, en todas partes, hasta que caló.</p>')
rep('<b>RESULT</b>7.5M → 80M mentions on X in one year (+951%)', '<b>RESULTADO</b>7,5M → 80M menciones en X en un año (+951 %)')
rep('<b>BUDGET</b>CHF 200,000 · procurement tender included', '<b>PRESUPUESTO</b>200.000 CHF · licitación incluida')
rep('<b>TASK FORCE</b>WMO · IFRC · UNDRR · ITU', '<b>GRUPO DE TRABAJO</b>OMM · FICR · UNDRR · UIT')
rep('Campaign assets on Trello →', 'Materiales de campaña en Trello →')
rep('aria-label="Play video: Early Warnings for All hero video"', 'aria-label="Reproducir video: video principal de Alertas Tempranas para Todos"')
rep('alt="Early Warnings for All hero video"', 'alt="Video principal de Alertas Tempranas para Todos"')
rep('<p class="video-caption">The campaign hero video. ', '<p class="video-caption">El video principal de la campaña. ')
rep('aria-label="Play video: Early Warnings for All interview series"', 'aria-label="Reproducir video: serie de entrevistas de Alertas Tempranas para Todos"')
rep('alt="Early Warnings for All interview series"', 'alt="Serie de entrevistas de Alertas Tempranas para Todos"')
rep('<p class="video-caption">On the ground, including in Spanish. ', '<p class="video-caption">Sobre el terreno, también en español. ')
rep('Watch on YouTube →', 'Ver en YouTube →', 3)

# 04
rep('<span class="cap focal-label">Grant won · FSC</span>', '<span class="cap focal-label">Subvención ganada · FSC</span>')
rep('<h3>Winning the money, running the money</h3>', '<h3>Ganar el dinero, administrar el dinero</h3>')
rep('Proposals · Donor relations · Budget stewardship', 'Propuestas · Relaciones con donantes · Gestión presupuestaria')
rep("<p>Somebody has to win the money. At FSC I wrote the proposal that won IKEA's EUR 400,000 grant for the New Approaches smallholder certification project, then served as communications lead on the core team. At WMO I ran the CHF 200,000 Early Warnings for All budget, procurement tender included.</p>",
    '<p>Alguien tiene que ganar el dinero. En FSC escribí la propuesta que ganó la subvención de 400.000 EUR de IKEA para el proyecto New Approaches de certificación de pequeños productores, y luego fui responsable de comunicación en el equipo central. En la OMM gestioné el presupuesto de 200.000 CHF de Alertas Tempranas para Todos, licitación incluida.</p>')
rep("<p>Money arrives on a story and stays on the reporting. I've done both ends.</p>",
    '<p>El dinero llega por una historia y se queda por los informes. He hecho las dos puntas.</p>')
rep('<b>GRANT</b>EUR 400,000 · IKEA · New Approaches to Smallholder Certification', '<b>SUBVENCIÓN</b>400.000 EUR · IKEA · New Approaches to Smallholder Certification')
rep('<b>ROLE</b>proposal author · communications lead', '<b>ROL</b>autor de la propuesta · responsable de comunicación')
rep('<b>ALSO</b>CHF 200,000 EW4All budget · procurement tender', '<b>ADEMÁS</b>presupuesto EW4All de 200.000 CHF · licitación')

# 05
rep('<div class="focal">1 of 4</div>', '<div class="focal">1 de 4</div>')
rep('<span class="cap focal-label">Named recipients · RMetS 2024</span>', '<span class="cap focal-label">Galardonados nombrados · RMetS 2024</span>')
rep('<h3>AskWMO and the integrity battle</h3>', '<h3>AskWMO y la batalla por la integridad</h3>')
rep('AI product launch · Frontier-tech storytelling · Information integrity', 'Lanzamiento de producto de IA · Narrativa de tecnología de frontera · Integridad de la información')
rep("<p>The knowledge was never missing. It was buried: thousands of PDFs, scattered webpages, files named final_final_v2, the world's authoritative climate intelligence hidden exactly when decisions needed it fast. AskWMO let you ask a question and get an answer drawn straight from WMO's document base. I co-created it and led the digital strategy and launch narrative.</p>",
    '<p>El conocimiento nunca faltó. Estaba enterrado: miles de PDF, páginas dispersas, archivos llamados final_final_v2, la inteligencia climática más autorizada del mundo escondida justo cuando las decisiones la necesitaban rápido. AskWMO permitía hacer una pregunta y recibir una respuesta sacada directamente de la base documental de la OMM. Lo cocreé y lideré la estrategia digital y la narrativa de lanzamiento.</p>')
rep('<p>Access is also the integrity battle. When the right science is hard to reach, misinformation festers and disinformation wins. In 2024 I was one of four named recipients of the Royal Meteorological Society Award for Impact on Science, Policy or Society.</p>',
    '<p>El acceso es también la batalla por la integridad. Cuando la ciencia correcta cuesta encontrarla, la desinformación involuntaria se enquista y la deliberada gana. En 2024 fui uno de los cuatro galardonados nombrados del premio de la Royal Meteorological Society al impacto en la ciencia, las políticas o la sociedad.</p>')
rep('<b>AWARD</b>Royal Meteorological Society 2024 · Impact on Science, Policy or Society', '<b>PREMIO</b>Royal Meteorological Society 2024 · Impact on Science, Policy or Society')
rep('<b>CONTEXT</b>part of the UN information-integrity initiative', '<b>CONTEXTO</b>parte de la iniciativa de integridad de la información de la ONU')
rep('<b>ROLE</b>co-created · digital strategy and launch narrative', '<b>ROL</b>cocreador · estrategia digital y narrativa de lanzamiento')
rep('The award citation →', 'La mención del premio →')
rep('The announcement →', 'El anuncio →')

# 06
rep('<span class="cap focal-label">Right message · right person · right time</span>', '<span class="cap focal-label">Mensaje correcto · persona correcta · momento correcto</span>')
rep("<h3>The principal's desk</h3>", '<h3>El despacho del principal</h3>')
rep('Executive communications · Speeches · Briefings', 'Comunicación ejecutiva · Discursos · Notas informativas')
rep("<p>The quietest work never posts. I drafted speeches and briefings for WMO's Assistant Secretary-General, wrote the briefing note to the Chief of Staff on climate information integrity, with the outcome public on wmo.int, and ran the UNICEF China Country Representative's personal platform. Leadership at every level, and the lesson is the same. Principals have a lot on their plate, so you make it an easy lift: build the trust, and get the information there on time and at quality.</p>",
    '<p>El trabajo más silencioso nunca se publica. Redacté discursos y notas para la Subsecretaría General de la OMM, escribí la nota informativa para la Jefatura de Gabinete sobre integridad de la información climática, con el resultado público en wmo.int, y llevé la plataforma personal de quien encabezaba UNICEF en China. Liderazgo a todos los niveles, y la lección es la misma. Los principales tienen la agenda llena, así que se lo pones fácil: construyes la confianza y haces llegar la información a tiempo y con calidad.</p>')
rep('<p>The right message from the right person at the right time saves lives.</p>',
    '<p>El mensaje correcto, de la persona correcta, en el momento correcto, salva vidas.</p>')
rep('<b>PRINCIPALS</b>WMO Assistant Secretary-General · Chief of Staff · UNICEF China Country Representative · campaign leadership', '<b>PRINCIPALES</b>Subsecretaría General de la OMM · Jefatura de Gabinete · Representación de UNICEF en China · dirección de campaña')
rep('<b>FORMATS</b>speeches · briefing notes · scenario notes · personal platforms', '<b>FORMATOS</b>discursos · notas informativas · notas de escenario · plataformas personales')
rep('<b>DOCTRINE</b>easy lift · on time · at quality', '<b>DOCTRINA</b>fácil de levantar · a tiempo · con calidad')

# 07
rep('<span class="cap focal-label">Answer-engine practice</span>', '<span class="cap focal-label">Práctica en motores de respuesta</span>')
rep('<h3>Where the answers come from</h3>', '<h3>De dónde salen las respuestas</h3>')
rep('GEO / AEO · Applied AI · Two ecosystems', 'GEO / AEO · IA aplicada · Dos ecosistemas')
rep('<p>Information behavior keeps migrating: card catalog, search engine, chatbot. Meeting people where they ask is the discipline; only the destination changed. So I built a complete GEO/AEO framework: content engineered for machine extraction, mapped to the off-site sources that actually feed the models, Western and Chinese AI ecosystems alike.</p>',
    '<p>El comportamiento informativo no deja de migrar: fichero de biblioteca, buscador, chatbot. La disciplina es encontrar a la gente donde pregunta; solo cambió el destino. Así que construí un marco GEO/AEO completo: contenido diseñado para la extracción por máquinas, mapeado a las fuentes externas que de verdad alimentan a los modelos, en los ecosistemas de IA occidental y chino por igual.</p>')
rep('<p>And I build, not just advise. An autonomous agent produces my strategic brief every morning, on a defined voice and a strict budget. The judgment stays human. That part is not negotiable.</p>',
    '<p>Y construyo, no solo aconsejo. Un agente autónomo produce mi informe estratégico cada mañana, con una voz definida y un presupuesto estricto. El criterio sigue siendo humano. Eso no se negocia.</p>')
rep('<b>FRAMEWORK</b>GEO/AEO · Western + Chinese AI ecosystems', '<b>MARCO</b>GEO/AEO · ecosistemas de IA occidental + chino')
rep('<b>RUNNING</b>autonomous daily brief agent · human-in-the-loop supply chain', '<b>EN MARCHA</b>agente de informe diario autónomo · cadena con una persona al mando')

# 08
rep('<span class="cap focal-label">National offices trained</span>', '<span class="cap focal-label">Oficinas nacionales formadas</span>')
rep('<h3>Capability that stays</h3>', '<h3>Capacidad que se queda</h3>')
rep('Training · Playbooks · Coaching &amp; enablement', 'Formación · Manuales · Acompañamiento y habilitación')
rep('<p>The highest form of communication leadership is making an organization capable of doing the work without you. I trained 30+ FSC national offices to run their own communications. At WMO I scaled a content operation across 30+ focal points with a federated model: regional posting authority inside central standards.</p>',
    '<p>La forma más alta de liderazgo en comunicación es dejar a una organización capaz de hacer el trabajo sin ti. Formé a más de 30 oficinas nacionales de FSC para llevar su propia comunicación. En la OMM escalé una operación de contenido a más de 30 puntos focales con un modelo federado: autoridad regional para publicar dentro de estándares centrales.</p>')
rep('<p>The approach comes from the basketball court. Lift everyone, build on strengths, never the same mistake twice, then let people shine.</p>',
    '<p>El enfoque viene de la cancha de baloncesto. Elevar a todos, construir sobre las fortalezas, nunca el mismo error dos veces, y después dejar que la gente brille.</p>')
rep('<b>FSC</b>30+ national offices, independent comms capability', '<b>FSC</b>más de 30 oficinas nacionales con capacidad de comunicación propia')
rep('<b>WMO</b>30+ focal points · federated model · central standards', '<b>OMM</b>más de 30 puntos focales · modelo federado · estándares centrales')

# 09
rep('<span class="cap focal-label">Country offices connected</span>', '<span class="cap focal-label">Oficinas de país conectadas</span>')
rep('<h3>Crisis, twice over</h3>', '<h3>Crisis, por partida doble</h3>')
rep('Public-health behavior change · Crisis response · Knowledge infrastructure', 'Cambio de comportamiento en salud pública · Respuesta a crisis · Infraestructura de conocimiento')
rep('<p>When COVID-19 emptied schools across China, the problem was changing behavior in a moment of panic. At UNICEF China I led Safe School Return, a public-health behavior-change campaign (C4D) built to replace parental fear with clarity. It won an award, and its assets were replicated by UNICEF offices far beyond China.</p>',
    '<p>Cuando la COVID-19 vació las escuelas de China, el problema era cambiar comportamientos en un momento de pánico. En UNICEF China lideré Safe School Return, una campaña de cambio de comportamiento en salud pública (C4D) construida para sustituir el miedo de las familias por claridad. Ganó un premio, y sus materiales fueron replicados por oficinas de UNICEF mucho más allá de China.</p>')
rep("<p>A crisis also generates lessons faster than any organization can absorb them. Writing and synthesizing UNICEF's COVID-19 lessons learned is what pulled me into knowledge management. The hub I then co-designed served the whole organization: tools, templates, news, networking, everything KM, connecting 190 country offices. That one earned an Inspira Award.</p>",
    '<p>Una crisis también genera lecciones más rápido de lo que cualquier organización puede absorberlas. Escribir y sintetizar las lecciones aprendidas de UNICEF sobre la COVID-19 fue lo que me llevó a la gestión del conocimiento. El centro que después codiseñé sirvió a toda la organización: herramientas, plantillas, noticias, redes, todo lo que es gestión del conocimiento, conectando 190 oficinas de país. Ese se llevó un premio Inspira.</p>')
rep('<b>CAMPAIGN</b>Safe School Return · award-winning C4D · assets replicated globally', '<b>CAMPAÑA</b>Safe School Return · C4D premiada · materiales replicados globalmente')
rep('<b>INFRASTRUCTURE</b>UNICEF’s org-wide KM hub · 190 country offices · Inspira Award 2021', '<b>INFRAESTRUCTURA</b>centro de gestión del conocimiento de toda UNICEF · 190 oficinas de país · premio Inspira 2021')
rep('The campaign →', 'La campaña →')

# 10
rep("<span class=\"cap focal-label\">WMO's first video case study</span>", '<span class="cap focal-label">Primer caso de estudio en video de la OMM</span>')
rep('<h3>Reports that refuse to die on a PDF</h3>', '<h3>Informes que se niegan a morir en un PDF</h3>')
rep('Editorial authority · Launch craft · Translating science', 'Autoridad editorial · Oficio de lanzamiento · Traducir la ciencia')
rep("<p>A technical report is useless if it dies on a PDF. For WMO's State of Climate Services 2023: Health, we produced the organization's first video case study: one data point on heatwaves, a camera on outdoor workers in Greece, the number turned into someone's afternoon shift. For the recurring flagship moments I partnered with the European Space Agency to bring satellite imagery to life.</p>",
    '<p>Un informe técnico no sirve de nada si muere en un PDF. Para el Estado de los Servicios Climáticos 2023: Salud de la OMM producimos el primer caso de estudio en video de la organización: un dato sobre olas de calor, una cámara sobre trabajadores al aire libre en Grecia, el número convertido en el turno de tarde de alguien. Para los momentos insignia recurrentes me asocié con la Agencia Espacial Europea para dar vida a las imágenes satelitales.</p>')
rep("<b>FIRST</b>WMO's first video case study · State of Climate Services 2023: Health", '<b>PRIMERO</b>primer caso de estudio en video de la OMM · Estado de los Servicios Climáticos 2023: Salud')
rep('<b>PARTNER</b>European Space Agency · Earth-observation imagery', '<b>SOCIO</b>Agencia Espacial Europea · imágenes de observación de la Tierra')
rep('The report →', 'El informe →')
rep('The ESA reel →', 'El reel de la ESA →')
rep('aria-label="Play video: WMO State of Climate Services Health video case study"', 'aria-label="Reproducir video: caso de estudio en video del Estado de los Servicios Climáticos: Salud de la OMM"')
rep('alt="WMO State of Climate Services Health video case study"', 'alt="Caso de estudio en video del Estado de los Servicios Climáticos: Salud de la OMM"')
rep('<p class="video-caption">Story collecting in the field, Greece. ', '<p class="video-caption">Recogiendo historias sobre el terreno, Grecia. ')

# 10b
rep('<span class="cap focal-label">Climate finance · 2024 · a third of the need</span>', '<span class="cap focal-label">Financiación climática · 2024 · un tercio de la necesidad</span>')
rep('<h3>The climate finance map</h3>', '<h3>El mapa de la financiación climática</h3>')
rep('Primo Insight 01 · Research · Climate finance', 'Primo Insight 01 · Investigación · Financiación climática')
rep('<p>Two trillion dollars a year, and a third of what is needed. I read the latest annual reports of the funds, the development banks, the donors and the philanthropies, more than fifty institutions, and wrote down what each one is standing on: the number, the edition it came from, and the trap in quoting it. Eleven pages, five charts, every figure sourced, the ones that could not be confirmed flagged as such.</p>',
    '<p>Dos billones de dólares al año, y un tercio de lo que hace falta. Leí los últimos informes anuales de los fondos, los bancos de desarrollo, los donantes y las filantropías, más de cincuenta instituciones, y anoté sobre qué se sostiene cada una: la cifra, la edición de la que salió y la trampa de citarla. Once páginas, cinco gráficos, cada cifra con su fuente, y las que no pudieron confirmarse señaladas como tales.</p>')
rep('<p>I built it because I always walk in having read the strategy. It is for anyone who has to put climate finance into public language, and I will keep it current.</p>',
    '<p>Lo hice porque siempre llego con la estrategia leída. Es para cualquiera que tenga que poner la financiación climática en lenguaje público, y lo mantendré al día.</p>')
rep('<b>SCOPE</b>10 multilateral funds · 11 development banks · 11 bilateral providers · UN agencies, philanthropy, bonds, carbon, insurance', '<b>ALCANCE</b>10 fondos multilaterales · 11 bancos de desarrollo · 11 proveedores bilaterales · agencias de la ONU, filantropía, bonos, carbono, seguros')
rep('<b>EDITIONS</b>CPI Global Landscape 2026 · MDB joint report 2025 · OECD May 2026 · UNEP Adaptation Gap 2025', '<b>EDICIONES</b>CPI Global Landscape 2026 · informe conjunto de los BMD 2025 · OCDE mayo 2026 · PNUMA Adaptation Gap 2025')
rep('<b>VERIFIED</b>source and edition on every figure · unconfirmed items listed, not smoothed over', '<b>VERIFICADO</b>fuente y edición en cada cifra · lo no confirmado se lista, no se disimula')
rep('Read the map (PDF, 11 pages) →', 'Leer el mapa (PDF, 11 páginas, en inglés) →')

# 11
rep("<h3>I publish what I'm learning.</h3>", '<h3>Publico lo que voy aprendiendo.</h3>')
rep('Thought leadership · Public writing', 'Liderazgo de opinión · Escritura pública')
rep('<p>The MeteoWorld pieces that put WMO at the AI frontier, and current writing on making content legible to the answer engines that increasingly mediate every question. The intersection stays the same: communication, AI, and Earth system science.</p>',
    '<p>Los artículos en MeteoWorld que pusieron a la OMM en la frontera de la IA, y la escritura actual sobre cómo hacer el contenido legible para los motores de respuesta que cada vez median más preguntas. La intersección es la misma: comunicación, IA y ciencia del sistema Tierra. Ambos artículos, en inglés.</p>')
rep('Campaign &amp; project partners, across engagements', 'Socios de campaña y de proyecto, a lo largo de los encargos')

# ── about ──
rep('<span class="cap eyebrow">About</span>', '<span class="cap eyebrow">Sobre mí</span>')
rep('<h2>A student of how power communicates.</h2>', '<h2>Un estudioso de cómo comunica el poder.</h2>')
rep("<p>I came to this work as a student of it and never stopped. The question that holds me: how power communicates. It started with a bachelor's in politics and history and deepened through graduate research at Tsinghua University, where my thesis in progress decodes China's South-South Cooperation discourse with a computational grounded-theory method, run on an open-source pipeline.</p>",
    '<p>Llegué a este trabajo como estudiante de él y nunca dejé de serlo. La pregunta que me sostiene: cómo comunica el poder. Empezó con una licenciatura en política e historia y se profundizó con la investigación de posgrado en la Universidad de Tsinghua, donde mi tesis en curso descifra el discurso chino de la Cooperación Sur-Sur con un método computacional de teoría fundamentada, ejecutado sobre una cadena de código abierto.</p>')
rep("<p>Then fifteen years of practice: deputy to the Head of Strategic Communication at WMO, senior roles at UNICEF China and the Forest Stewardship Council. I have communicated governance from the inside too: FSC's three-chamber system, WMO's Congress and Executive Council.</p>",
    '<p>Después, quince años de práctica: adjunto a la Jefatura de Comunicación Estratégica de la OMM, puestos sénior en UNICEF China y en el Forest Stewardship Council. También he comunicado la gobernanza desde dentro: el sistema de tres cámaras de FSC, el Congreso y el Consejo Ejecutivo de la OMM.</p>')
rep("<p>I keep training because the best practitioners are perpetual students: CIPR-certified in PR strategy and campaign management, UNITAR's Diplomacy 4.0, the UN Emerging Leaders programme, behavioral-communication work with NYU, WHO, and UNICEF. I work in English and Spanish, both native.</p>",
    '<p>Sigo formándome porque los mejores profesionales son estudiantes perpetuos: certificado por el CIPR en estrategia de relaciones públicas y gestión de campañas, Diplomacia 4.0 de UNITAR, el programa de Líderes Emergentes de la ONU, trabajo en comunicación conductual con NYU, la OMS y UNICEF. Trabajo en inglés y en español, ambos nativos.</p>')
rep('<b>PRACTICE</b>', '<b>PRÁCTICA</b>')
rep('15 years · UN system, INGOs<br>', '15 años · sistema de la ONU, ONG internacionales<br>')
rep('WMO · UNICEF China · FSC<br>', 'OMM · UNICEF China · FSC<br>')
rep('<b>EDUCATION</b>', '<b>FORMACIÓN ACADÉMICA</b>')
rep('Tsinghua University · graduate studies, thesis in progress<br>', 'Universidad de Tsinghua · estudios de posgrado, tesis en curso<br>')
rep('MA International Relations &amp; Diplomacy · UOC &amp; UNITAR<br>', 'Máster en Relaciones Internacionales y Diplomacia · UOC y UNITAR<br>')
rep('BA Politics &amp; History · Woodbury University', 'Grado en Política e Historia · Woodbury University')
rep('<b>FORMATION</b>', '<b>FORMACIÓN CONTINUA</b>')
rep('CIPR · PR strategy &amp; campaign management<br>', 'CIPR · estrategia de RR. PP. y gestión de campañas<br>')
rep('UNITAR Diplomacy 4.0 · UN Emerging Leaders<br>', 'UNITAR Diplomacia 4.0 · Líderes Emergentes de la ONU<br>')
rep('C4D · NYU / WHO / UNICEF behavioral training', 'C4D · formación conductual NYU / OMS / UNICEF')
rep('<b>LANGUAGES</b>', '<b>IDIOMAS</b>')
rep('English · Spanish, both native', 'Inglés · Español, ambos nativos')

# ── contact ──
rep('<h2>Bring me the mandate, the launch, or the mess.</h2>', '<h2>Tráigame el mandato, el lanzamiento o el desastre.</h2>')
rep('<p>I read everything about your institution before the first call. English or Spanish. Pick the door and the email is half written.</p>',
    '<p>Leo todo sobre su institución antes de la primera llamada. En español o en inglés. Elija la puerta y el correo ya está medio escrito.</p>')
rep('<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=The%20mandate%3A%20%5Binstitution%5D&amp;body=Hello%20Jesse%2C%0D%0A%0D%0AI%27m%20%5Bname%5D%2C%20%5Brole%5D%20at%20%5Binstitution%5D.%0D%0A%0D%0AOur%20mandate%2C%20in%20one%20line%3A%20%5Bwhat%20the%20institution%20exists%20to%20do%5D.%20The%20people%20we%20most%20need%20to%20reach%20are%20%5Bpolicymakers%20/%20the%20public%20/%20a%20specific%20community%5D%2C%20and%20right%20now%20%5Bwhat%20they%20see%20instead%2C%20or%20where%20recognition%20stalls%5D.%0D%0A%0D%0AWhat%20we%20need%3A%20%5Bstrategy%20/%20a%20campaign%20/%20a%20standing%20editorial%20function%20/%20measurement%20/%20a%20crisis%20plan%20built%20in%20advance%5D.%0D%0A%0D%0ATiming%3A%20%5Bwhen%20this%20matters%5D.%20Budget%20range%2C%20if%20there%20is%20one%3A%20%5B%20%5D.%0D%0A%0D%0ACould%20we%20talk%20this%20week%20or%20next%3F%20I%27m%20in%20%5Bcity%20/%20time%20zone%5D%20and%20work%20in%20%5BEnglish%20/%20Spanish%5D.%0D%0A%0D%0A%5BName%5D%0D%0A%5BTitle%2C%20institution%5D"><b>01</b>The mandate</a>',
    '<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=El%20mandato%3A%20%5Binstituci%C3%B3n%5D&amp;body=Hola%2C%20Jesse%3A%0D%0A%0D%0ASoy%20%5Bnombre%5D%2C%20%5Bcargo%5D%20en%20%5Binstituci%C3%B3n%5D.%0D%0A%0D%0ANuestro%20mandato%2C%20en%20una%20l%C3%ADnea%3A%20%5Bpara%20qu%C3%A9%20existe%20la%20instituci%C3%B3n%5D.%20Las%20personas%20a%20las%20que%20m%C3%A1s%20necesitamos%20llegar%20son%20%5Bquienes%20deciden%20/%20el%20p%C3%BAblico%20/%20una%20comunidad%20concreta%5D%2C%20y%20ahora%20mismo%20%5Bqu%C3%A9%20ven%20en%20su%20lugar%2C%20o%20d%C3%B3nde%20se%20estanca%20el%20reconocimiento%5D.%0D%0A%0D%0ALo%20que%20necesitamos%3A%20%5Bestrategia%20/%20una%20campa%C3%B1a%20/%20una%20funci%C3%B3n%20editorial%20permanente%20/%20medici%C3%B3n%20/%20un%20plan%20de%20crisis%20preparado%20de%20antemano%5D.%0D%0A%0D%0APlazos%3A%20%5Bcu%C3%A1ndo%20importa%20esto%5D.%20Rango%20de%20presupuesto%2C%20si%20lo%20hay%3A%20%5B%20%5D.%0D%0A%0D%0A%C2%BFPodr%C3%ADamos%20hablar%20esta%20semana%20o%20la%20pr%C3%B3xima%3F%20Estoy%20en%20%5Bciudad%20/%20zona%20horaria%5D%20y%20trabajo%20en%20%5Bespa%C3%B1ol%20/%20ingl%C3%A9s%5D.%0D%0A%0D%0A%5BNombre%5D%0D%0A%5BCargo%2C%20instituci%C3%B3n%5D"><b>01</b>El mandato</a>')
rep('<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=The%20launch%3A%20%5Bwhat%20launches%5D&amp;body=Hello%20Jesse%2C%0D%0A%0D%0AI%27m%20%5Bname%5D%2C%20%5Brole%5D%20at%20%5Binstitution%5D.%0D%0A%0D%0AWe%27re%20launching%20%5Breport%20/%20initiative%20/%20product%5D%20on%20%5Bdate%5D.%20The%20people%20who%20have%20to%20notice%20are%20%5Bministers%20/%20donors%20/%20journalists%20/%20the%20public%5D%2C%20and%20the%20message%20in%20one%20sentence%20is%20%5B%20%5D.%0D%0A%0D%0AAlready%20in%20place%3A%20%5Bassets%2C%20spokespeople%2C%20channels%5D.%20Still%20missing%3A%20%5B%20%5D.%0D%0A%0D%0ALanguages%3A%20%5B%20%5D.%20Budget%20range%2C%20if%20known%3A%20%5B%20%5D.%0D%0A%0D%0ACould%20we%20talk%20this%20week%3F%20I%27m%20in%20%5Bcity%20/%20time%20zone%5D.%0D%0A%0D%0A%5BName%5D%0D%0A%5BTitle%2C%20institution%5D"><b>02</b>The launch</a>',
    '<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=El%20lanzamiento%3A%20%5Bqu%C3%A9%20se%20lanza%5D&amp;body=Hola%2C%20Jesse%3A%0D%0A%0D%0ASoy%20%5Bnombre%5D%2C%20%5Bcargo%5D%20en%20%5Binstituci%C3%B3n%5D.%0D%0A%0D%0ALanzamos%20%5Binforme%20/%20iniciativa%20/%20producto%5D%20el%20%5Bfecha%5D.%20Quienes%20tienen%20que%20enterarse%20son%20%5Bministros%20/%20donantes%20/%20periodistas%20/%20el%20p%C3%BAblico%5D%2C%20y%20el%20mensaje%20en%20una%20frase%20es%20%5B%20%5D.%0D%0A%0D%0AYa%20tenemos%3A%20%5Bmateriales%2C%20portavoces%2C%20canales%5D.%20Nos%20falta%3A%20%5B%20%5D.%0D%0A%0D%0AIdiomas%3A%20%5B%20%5D.%20Rango%20de%20presupuesto%2C%20si%20se%20conoce%3A%20%5B%20%5D.%0D%0A%0D%0A%C2%BFPodr%C3%ADamos%20hablar%20esta%20semana%3F%20Estoy%20en%20%5Bciudad%20/%20zona%20horaria%5D.%0D%0A%0D%0A%5BNombre%5D%0D%0A%5BCargo%2C%20instituci%C3%B3n%5D"><b>02</b>El lanzamiento</a>')
rep('<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=The%20mess%3A%20%5Binstitution%5D&amp;body=Hello%20Jesse%2C%0D%0A%0D%0AI%27m%20%5Bname%5D%2C%20%5Brole%5D%20at%20%5Binstitution%5D.%0D%0A%0D%0AWhat%20happened%2C%20plainly%3A%20%5Btwo%20sentences%5D.%20It%20started%20on%20%5Bdate%5D.%20So%20far%20it%20is%20known%20to%20%5Bstaff%20/%20partners%20/%20the%20press%20/%20the%20public%5D.%0D%0A%0D%0AWhat%20we%20have%20said%20publicly%3A%20%5Bnothing%20yet%20/%20a%20holding%20line%20/%20a%20full%20statement%5D.%0D%0A%0D%0AWhat%20we%20need%20first%3A%20%5Ba%20holding%20statement%20/%20a%20plan%20for%20the%20next%2048%20hours%20/%20someone%20in%20the%20room%5D.%0D%0A%0D%0APhone%3A%20%5B%20%5D.%20I%27m%20in%20%5Bcity%20/%20time%20zone%5D.%20Sooner%20is%20better.%0D%0A%0D%0A%5BName%5D%0D%0A%5BTitle%2C%20institution%5D"><b>03</b>The mess</a>',
    '<a class="btn" href="mailto:primo.communication.io@gmail.com?subject=El%20desastre%3A%20%5Binstituci%C3%B3n%5D&amp;body=Hola%2C%20Jesse%3A%0D%0A%0D%0ASoy%20%5Bnombre%5D%2C%20%5Bcargo%5D%20en%20%5Binstituci%C3%B3n%5D.%0D%0A%0D%0AQu%C3%A9%20pas%C3%B3%2C%20sin%20rodeos%3A%20%5Bdos%20frases%5D.%20Empez%C3%B3%20el%20%5Bfecha%5D.%20Hasta%20ahora%20lo%20saben%20%5Bel%20personal%20/%20los%20socios%20/%20la%20prensa%20/%20el%20p%C3%BAblico%5D.%0D%0A%0D%0AQu%C3%A9%20hemos%20dicho%20p%C3%BAblicamente%3A%20%5Bnada%20todav%C3%ADa%20/%20una%20l%C3%ADnea%20de%20contenci%C3%B3n%20/%20una%20declaraci%C3%B3n%20completa%5D.%0D%0A%0D%0AQu%C3%A9%20necesitamos%20primero%3A%20%5Buna%20declaraci%C3%B3n%20de%20contenci%C3%B3n%20/%20un%20plan%20para%20las%20pr%C3%B3ximas%2048%20horas%20/%20alguien%20en%20la%20sala%5D.%0D%0A%0D%0ATel%C3%A9fono%3A%20%5B%20%5D.%20Estoy%20en%20%5Bciudad%20/%20zona%20horaria%5D.%20Cuanto%20antes%2C%20mejor.%0D%0A%0D%0A%5BNombre%5D%0D%0A%5BCargo%2C%20instituci%C3%B3n%5D"><b>03</b>El desastre</a>')
rep('<p class="or">Or just write: ', '<p class="or">O simplemente escriba: ')

# ── footer ──
rep('Primo Strategic Communication LLC · Sheridan, Wyoming, USA · Operating globally · © 2026 · Meaning that moves institutions.',
    'Primo Strategic Communication LLC · Sheridan, Wyoming, EE. UU. · Operando globalmente · © 2026 · Sentido que mueve instituciones.')
rep('This page weighs about 200 KB, sets no cookies, and runs no trackers.', 'Esta página pesa unos 200 KB, no instala cookies y no lleva rastreadores.')

# ── numerals: Spanish decimal comma in the remaining tokens and the counter ──
rep('>1.3M<', '>1,3M<', 2)          # focal + chart value
rep('>7.5M<', '>7,5M<')
rep('>+94.1%<', '>+94,1%<')
rep('>+117.7%<', '>+117,7%<')
rep("el.textContent = pre + (target * easeOutExpo(t)).toFixed(dec) + suf;",
    "el.textContent = pre + (target * easeOutExpo(t)).toFixed(dec).replace('.', ',') + suf;")

out = root / 'es' / 'index.html'
out.write_text(s)
print('built', out, len(s), 'bytes')
