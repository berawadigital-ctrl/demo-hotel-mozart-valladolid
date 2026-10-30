# Contenido de la demo Hotel Mozart (Valladolid) (es/en/fr/de). Hechos de hotelmozart.net leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios de habitacion ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Habitación individual','Habitación doble'],'en':['Single room','Double room'],'fr':['Chambre individuelle','Chambre double'],'de':['Einzelzimmer','Doppelzimmer']}
RD={
'es':['Para quien viaja solo, por trabajo o turismo: WiFi de fibra óptica, climatización, minibar, televisión y zona de escritorio.','Cama de matrimonio o dos camas individuales, según disponibilidad. Puede reservarse para uso individual y admite cama supletoria o cuna gratuita, sujetas a disponibilidad.'],
'en':['For solo travellers, on business or holiday: fibre-optic WiFi, air conditioning and heating, minibar, TV and a desk area.','Double bed or two single beds, subject to availability. It can be booked for single use and allows an extra bed or a free cot, subject to availability.'],
'fr':['Pour les voyageurs seuls, en déplacement ou en vacances : WiFi fibre optique, climatisation, minibar, télévision et coin bureau.','Lit double ou deux lits simples, selon disponibilité. Réservable en usage individuel, avec lit d\'appoint ou lit bébé gratuit, selon disponibilité.'],
'de':['Für Alleinreisende, beruflich oder privat: Glasfaser-WLAN, Klimaanlage, Minibar, Fernseher und Schreibtischbereich.','Doppelbett oder zwei Einzelbetten, je nach Verfügbarkeit. Auch zur Einzelnutzung buchbar, mit Zustellbett oder kostenlosem Kinderbett nach Verfügbarkeit.']}
ART={
'hero':('columns',9201,['#efe9df','#f8f4ec','#8c3b2e','#5a2620','#331512']),
'intro':('arches',9202,['#f0e5d3','#e3b380','#8c3b2e','#5a2620','#331512']),
'r1':('skyline',9211,['#5a2620','#e7a568','#f5d5a3','#2c4a3e','#233e33','#162a22']),
'r2':('hills',9212,['#e9efe4','#f0e6cf','#e8b873','#9db592','#6f9077','#4a6b57']),
'g1':('waves',9221,['#2c4a3e','#edbd83','#f6deb5','#3c6657','#2c4a3e','#1a3028']),
'g2':('columns',9222,['#edeae2','#f7f4ee','#9a4a32','#5a2620','#331512']),
'g3':('arches',9223,['#ecdfca','#dcab76','#9e4224','#5a2620','#331512']),
'g4':('skyline',9224,['#5a2620','#e0a064','#f2cf9c','#29473b','#203a30','#14271f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Mozart · Hotel en el centro histórico de Valladolid',see_rooms='Ver las habitaciones',hero_k='Valladolid · Centro histórico',hero_t='Una casa con historia, en pleno corazón de la ciudad',hero_s='Antigua casa residencial burguesa de 1872 rehabilitada, a pocos pasos de la Plaza Mayor.',
 intro_t='Tu hotel en el centro de Valladolid',intro_p1='Habitaciones luminosas y tranquilas, recepción abierta las 24 horas y una cafetería con terraza a pie de calle, para visitar la ciudad por ocio o por trabajo.',
 intro_p2='Parking cubierto junto al hotel con plazas limitadas: conviene reservarlo con antelación. Si tienes reserva, el hotel gestiona tu acceso a la Zona de Bajas Emisiones.',
 stats=['Casa de 1872','Recepción 24 h','WiFi de fibra óptica','Parking cubierto'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Individual o doble, con climatización, minibar y televisión.',
 svcs=['Recepción 24 horas','WiFi de fibra óptica','Parking cubierto (plazas limitadas)','Desayuno en la habitación','Lavandería','Salones para reuniones'],
 around_s='A menos de 500 metros: Plaza Mayor, Catedral, Casa de Cervantes, Pasaje Gutiérrez, Campo Grande y Academia de Caballería.',
 loc_p='Calle Menéndez Pelayo 7 · 47001 Valladolid, en el centro histórico, a pocos pasos de la Plaza Mayor.',
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Hasta qué hora es el desayuno?','¿Puedo cancelar?']),
'en':dict(title='Hotel Mozart · Hotel in the historic centre of Valladolid',see_rooms='See the rooms',hero_k='Valladolid · Historic centre',hero_t='A house with history, in the heart of the city',hero_s='A restored bourgeois townhouse from 1872, a few steps from the Plaza Mayor.',
 intro_t='Your hotel in the centre of Valladolid',intro_p1='Bright, quiet rooms, a reception open 24 hours and a street-level cafeteria with terrace, whether you visit for leisure or business.',
 intro_p2='Covered car park next to the hotel with limited spaces: book it in advance. If you have a booking, the hotel arranges your access to the Low Emission Zone.',
 stats=['House from 1872','24 h reception','Fibre-optic WiFi','Covered car park'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Single or double, with air conditioning, minibar and TV.',
 svcs=['24-hour reception','Fibre-optic WiFi','Covered car park (limited spaces)','Breakfast in your room','Laundry','Meeting rooms'],
 around_s='Under 500 metres away: Plaza Mayor, the Cathedral, Cervantes House, Pasaje Gutiérrez, Campo Grande and the Cavalry Academy.',
 loc_p='Calle Menéndez Pelayo 7 · 47001 Valladolid, in the historic centre, a few steps from the Plaza Mayor.',
 chips=['Which rooms do you have?','Is there parking?','Until what time is breakfast?','Can I cancel?']),
'fr':dict(title='Hotel Mozart · Hôtel dans le centre historique de Valladolid',see_rooms='Voir les chambres',hero_k='Valladolid · Centre historique',hero_t='Une maison chargée d\'histoire, au cœur de la ville',hero_s='Ancienne maison bourgeoise de 1872 restaurée, à quelques pas de la Plaza Mayor.',
 intro_t='Votre hôtel au centre de Valladolid',intro_p1='Des chambres lumineuses et calmes, une réception ouverte 24 h/24 et une cafétéria avec terrasse sur rue, pour un séjour de loisirs ou d\'affaires.',
 intro_p2='Parking couvert à côté de l\'hôtel, places limitées : réservez-le à l\'avance. Avec une réservation, l\'hôtel gère votre accès à la Zone à faibles émissions.',
 stats=['Maison de 1872','Réception 24 h/24','WiFi fibre optique','Parking couvert'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Individuelle ou double, avec climatisation, minibar et télévision.',
 svcs=['Réception 24 h/24','WiFi fibre optique','Parking couvert (places limitées)','Petit-déjeuner en chambre','Blanchisserie','Salles de réunion'],
 around_s='À moins de 500 mètres : Plaza Mayor, cathédrale, maison de Cervantes, Pasaje Gutiérrez, Campo Grande et Académie de cavalerie.',
 loc_p='Calle Menéndez Pelayo 7 · 47001 Valladolid, dans le centre historique, à quelques pas de la Plaza Mayor.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','Jusqu\'à quelle heure le petit-déjeuner ?','Puis-je annuler ?']),
'de':dict(title='Hotel Mozart · Hotel in der Altstadt von Valladolid',see_rooms='Zimmer ansehen',hero_k='Valladolid · Altstadt',hero_t='Ein Haus mit Geschichte, im Herzen der Stadt',hero_s='Ein restauriertes Bürgerhaus von 1872, nur wenige Schritte von der Plaza Mayor.',
 intro_t='Ihr Hotel im Zentrum von Valladolid',intro_p1='Helle, ruhige Zimmer, eine rund um die Uhr geöffnete Rezeption und eine Cafeteria mit Straßenterrasse, ob Sie privat oder geschäftlich reisen.',
 intro_p2='Überdachter Parkplatz neben dem Hotel mit begrenzter Platzzahl: bitte vorab reservieren. Mit Buchung regelt das Hotel Ihre Zufahrt zur Umweltzone.',
 stats=['Haus von 1872','Rezeption 24 h','Glasfaser-WLAN','Überdachter Parkplatz'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einzel- oder Doppelzimmer, mit Klimaanlage, Minibar und Fernseher.',
 svcs=['Rezeption rund um die Uhr','Glasfaser-WLAN','Überdachter Parkplatz (begrenzte Plätze)','Frühstück auf dem Zimmer','Wäscheservice','Tagungsräume'],
 around_s='Weniger als 500 Meter entfernt: Plaza Mayor, Kathedrale, Cervantes-Haus, Pasaje Gutiérrez, Campo Grande und Kavallerieakademie.',
 loc_p='Calle Menéndez Pelayo 7 · 47001 Valladolid, in der Altstadt, nur wenige Schritte von der Plaza Mayor.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Bis wann gibt es Frühstück?','Kann ich stornieren?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://hotelmozart.backhotelite.com/{l}/bookcore/availability/tomorrow/hotelmozart/'
BOOK=dict(mode='engine',url={l:RB.format(l=l) for l in ('es','en','fr','de')})
D=dict(name='Hotel Mozart',ac='#5a2620',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=['Plaza Mayor','Campo Grande'],foot=FOOT,
 address='Calle Menéndez Pelayo 7 · 47001 Valladolid',phones=['+34 983 297 777'],emails=['hotelmozart@hotelmozart.net'],maps='Hotel Mozart, Calle Menéndez Pelayo 7, Valladolid',t=T)
META=dict(repo='demo-hotel-mozart-valladolid',name='Hotel Mozart',legal_name='MOZART, C.B.',registry_ids=['NIF E47220090'],
 url='https://www.hotelmozart.net/',domain='hotelmozart.net',municipality='Valladolid',province='Valladolid',sector='hotel urbano en una casa de 1872 en el centro histórico de Valladolid',
 read_at='2026-10-30T06:47:30+01:00',created_at='2026-10-30T06:47:00+01:00',built_at='2026-10-30T06:55:00+01:00',audit_date='2026-10-30T06:44:34+01:00',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T10:41:21+01:00',url='https://www.google.com/maps/place/Hotel+Mozart/@41.6494665,-4.7271995,17z/data=!4m9!3m8!1s0xd4712b34fbb6681:0x5880393c47980758!5m2!4m1!1i2!8m2!3d41.6494665!4d-4.7271995!16s%2Fg%2F1tdn0tzw'),
 book=dict(mode='engine',url=RB.format(l='es'),note='motor de reservas real de su web (backhotelite), HTTP 200 comprobado el 30/10/2026 en es/en/fr/de.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Ponéis cuna para el bebé?','K02'),('¿Hay parking?','K03'),('Mi coche no tiene etiqueta, ¿puedo entrar en la ZBE?','K04'),('¿Hasta qué hora es el desayuno?','K05'),('¿Hay recepción 24 horas?','K06'),('¿Puedo cancelar?','K07'),('¿Dónde está el hotel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you provide a cot for the baby?','K02'),('Is there parking?','K03'),('My car has no emissions sticker, can I enter the low emission zone?','K04'),('Until what time is breakfast?','K05'),('Is there a 24-hour reception?','K06'),('Can I cancel?','K07'),('Where is the hotel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous un lit bébé ?','K02'),('Y a-t-il un parking ?','K03'),('Ma voiture n\'a pas de vignette, puis-je entrer dans la zone à faibles émissions ?','K04'),('Jusqu\'à quelle heure le petit-déjeuner ?','K05'),('Y a-t-il une réception 24 h/24 ?','K06'),('Puis-je annuler ?','K07'),('Où se trouve l\'hôtel ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es ein Kinderbett für das Baby?','K02'),('Gibt es einen Parkplatz?','K03'),('Mein Auto hat keine Umweltplakette, darf ich in die Umweltzone fahren?','K04'),('Bis wann gibt es Frühstück?','K05'),('Ist die Rezeption rund um die Uhr besetzt?','K06'),('Kann ich stornieren?','K07'),('Wo liegt das Hotel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
