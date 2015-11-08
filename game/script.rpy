# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg taxi = "images/taxi.jpg"
image bg taxi2 = "images/taxi2.jpg"
image bg taxi3 = "images/taxi3.jpg"
image bg terminal3 = "images/terminal3.jpg"
image bg pila = "images/pila.jpg"
image bg jb = "images/jollibee.jpg"
image bg xray = "images/xray.jpg"
image bg boy = "images/boy.jpg"
image bg boy_bullet = "images/boy_bullet.jpg"
image bg boy_bullet_found = "images/boy_bullet_found.jpg"
image bg boarding = "images/boarding.jpg"
image bg creds = "images/credits.jpg"

image taxi jobert1 = "images/Jobert.png"
image taxi jobert2 = "images/jobert2.png"
image ofw normal = "images/empoy1.png"
image ofw leaning = "images/empoy2.png"
image ticketer normal = "images/bea.png"
image security normal = "images/cupal2.png"
image security leaning = "images/cupal.png"


# Declare characters used by this game.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define taxi = Character('Taxi', color="#c8ffc8")
define security = Character('Security', color="#CC00CC")
define ofw = Character('OFW', color='#00CC00')
define ticketer = Character('Ticketer', color='#CC00CC')


# The game starts here.
label start:
    stop music fadeout 3.0

    play music "images/traffic.mp3"

    scene bg taxi
    with fade

    taxi "Pare pareho silang lahat."

    taxi "Kung hindi kurap, inutil. Eh no. Tapos bukas magtataas nanaman ng diesel."

    taxi "Sasabihin na world economy daw. PAK! SHET! Eh may sarili naman tayong langis."

    taxi "Kaso tangina. Kupal din kasi ng mga Chekwa eh no. Sa kanila raw ang Spratly's. Eh di sa kanila na lahat. Kingina nila."

    "(...)"

    scene bg taxi2
    with fade

    taxi "Terminal 1 tayo boss, no?"

    "(...)"

    scene bg taxi
    with fade

    taxi "Nag Saudi din ako dati. 2 years."

    taxi "Drayber."

    taxi "Yung amo ko, Arabo. Apo ng Sultan nila."

    taxi "Strikto sila dun. Mahuli ka lang na kumakain ng bawal, latigo agad."

    taxi "Lalo na pag bawal na gamot. Kingina. Bitay! Bitay kang adik ka."

    "(...)"

    scene bg taxi3
    with fade

    taxi "Pero malungkot din, siyempre. Eh no."

    taxi "Ako rin. Yung misis ko hindi ko na rin pinasama sa airport."

    taxi "Mahirap na. Baka manghina ang tuhod ko, hindi na ako makasakay. Hahaha."

    taxi "Pero bago umalis, syempre, may pabaon muna. Gets niyo Boss, hahaha."

    taxi "Eh kayo din Boss? May pabaon din? Hahahaha."

    "(...)"

    scene bg taxi2
    with fade

    taxi "Gusto ko sana Dubai. Kasi open city."

    taxi "Yung mga babae pwede magjogging ng maiksi ang shorts."

    taxi "Lalo na yung mga Puti. Sobrang hilig nilang magjogging. Eh no."

    taxi "Teka ikot lang tayo Boss ha."

    "(...)"

    scene bg terminal3
    with fade

    show taxi jobert1
    with dissolve

    taxi "Ako na magbubuhat, Boss"

    menu:

        "Allow":
            jump allow_help

        "Deny":
            hide taxi

            show taxi jobert2
            with dissolve

            jump deny_help

label allow_help:

    $ is_bullet = True

    taxi "Dalawang maleta lang po, eh no?"

    taxi "Mejo mabigat po yung isa. I hahand-carry niyo po ba?"

    "(...)"

    taxi "Salamat po Bossing!"

    jump check_in

label deny_help:

    $ is_bullet = False

    taxi "Ok Boss."

    taxi "Bakit parang mejo mabigat po yung isa ah."

    scene bg terminal3
    with pixellate

    show taxi jobert2

    taxi "Ok. Wala namang naiwan po no?"

    "(...)"

    taxi "Sige po bossing!"

    jump check_in

label check_in:

    scene black
    with dissolve

    ofw "Excuse me..."

    play music "images/crowd.mp3"

    scene bg pila
    with fade

    show ofw normal
    with dissolve

    ofw "Dito ba pila. Yung sa OEC?"

    "(...)"

    show ofw leaning
    with dissolve

    ofw "Wala nga tayong binayaran na travel tax. Nagbayad pa rin tayo sa OEC."

    ofw "Aalis na nga lang tayo, tataxan pa. Haaaay Pinoy!"

    ofw "Tax dito. Tax doon. Napupunta lang naman kay Tongressman at kay Senatong."

    "(...)"

    show ofw normal
    with dissolve

    ofw "Bagal ng pila ah."

    ofw "Kahit san talaga, paggobyerno kung hindi kurap, inutil."

    ofw "Sana sa Dubai. Maayos."

    show ofw leaning
    with dissolve

    ofw "Ikaw pre, pa Dubai ka rin ba?"

    "(...)"

    scene bg pila
    with fade

    show ticketer normal
    with dissolve

    ticketer "Is this all, Sir?"

    play sound "images/error.mp3"

    ticketer "Sir, pakitimbang na lang po ng hand carry niyo, Sir."

    play sound "images/error.mp3"

    ticketer "Sorry Sir, pero pwede po ba macheck yung bag niyo"

    menu:

        "Allow":
            $ is_bullet = True
            scene bg pila
            with pixellate

            show ticketer normal

            ticketer "Ano po ba laman nito? Mga fragile po ba?"

            ticketer "Mga gadgets? Laptop?"

        "Deny":
            $ is_bullet = is_bullet
            ticketer "Ah ok po Sir. May gadgets po ba sa loob o laptop?"
            ticketer "May baggage allowance pa po kayo, baka gusto niyo pong bawasan ang nasa hand carry niyo."
            ticketer "Baka po kasi mabigatan kayo..."

    scene bg pila
    with fade

    show ticketer normal

    ticketer "All good Sir. 3:25am po ang boarding. Gate 20C. Thank you very much, have a safe trip!"

    "(...)"

    jump jollibee

label jollibee:

    play music "images/tu_pars.mp3" fadeout 2.0

    scene black
    with dissolve

    "\"Mabilis lang ang 1 taon. Makakapag-leave ka rin.\""

    scene bg jb
    with fade

    "\"Matagal kong hinanda ang sarili ko para sa araw na to. Pero iba pa rin pala talaga pag nandito na.\""

    "\"Isipin mo na lang future natin ni Tintin. Kung hindi ka aalis, pano natin matutupad mga pangarap natin para sa kanya.\""

    "\"Haha. Hayaan mo Tintin, pagbalik ko uubusin natin lahat ng Kiddie Meal na kaya mong bilangin.\""

    "\"Mga 7?\""

    "\"Naku Tintin, tuturuan kitang magbilang habang wala si Mama. Hanggang one million dozen!\""

    "(...)"

    scene bg jb
    with fade

    "\"Basta Pa, yung XBox ko ha.\""

    "\"Haha. Para sa mga honors lang ang XBox uy. Remember our golden rule, nak: {i}You boplax, no XBox{/i}\""

    "\"Pa. Wala kang boplax na anak, Pa. Tinatamad lang sometimes. Hehehe.\""

    "\"Aysus. Yung sometimes mo, all the times eh!\""

    "(...)"

    scene bg jb
    with fade

    "\"Yung pabaon ni Mommy. Inorasyunan pa raw yan ni Ninong. Tapos nakwento ni insan Ricky, may Eat Bulaga din dun sa kanila kaya hindi ka mahohome-sick. May Viber din. May Skype pa. San ka pa.\""

    "\"Eh di kung saan malakas ang wifi. Hahaha.\""

    "\"Kaya natin to, basta may internet. Haha. \""

    "\"Tagal naman ng Chicken joy natin.\""

    "\"Mahal mahal ng Jollibee dito tapos... Ah.. wait. Ah, Pre. Excuse me, Pre. Excuse pare. Pwede magpakuha ng picture.\""

    show ofw leaning

    "Last Jollibee namin to in a very long time."

    "(...)"

    menu:

        "Allow":
            scene jollibee
            with flash

            "Ayos pre. Salamat!"

        "Deny":
            $ is_bullet = is_bullet

            "Ay. Mukhang malalim iniisip natin pare ah?"

            "Miss mo na agad si Misis? Ba't kasi di mo sinama?"


    jump checkpoint

label checkpoint:
    scene black
    with dissolve

    scene xray
    with fade

    show ofw normal
    with dissolve

    ofw "Wala na palang terminal fee pag OFW. Ayos! One payb din yun."

    "(...)"

    ofw "Nakow, eto na. Eto na yung mga nababasa ko sa FB."

    ofw "Tangina. Try lang nila. Sila lalaglagan ko ng bala."

    show ofw normal at right
    with dissolve

    play sound "images/alarm.mp3"

    show security leaning at left
    with easeinright

    security "Sir, pakitanggal po ng sapatos."

    show ofw leaning at right

    show security normal
    with dissolve

    security "Sir, relax lang po. Hindi po kami laglag bala. You have our assurance, tapat po kami sa serbisyo namin."

    play sound "images/alarm.mp3"

    show security leaning
    with dissolve

    ofw "Hah? Ano ba?"

    security "Sir, yung rosary niyo po. Baka metal yan."

    "..."

    play sound "images/error.mp3"

    ofw "... Pero hindi niyo kami masisising mga pasahero ha. Kalat na sa FB yung mga kabulastugan niyo."

    security "Sorry po sa abala."

    "(...)"

    scene bg xray
    with fade

    scene bg xray
    with pixellate

    if is_bullet:
        jump bullet_caught

    jump bullet_notcaught

label bullet_caught:
    security "Sir, sorry sir. Paki-ulit po."

    scene bg xray
    with pixellate

    security "Sir, may mga metal po ba or ibang contraband sa bag niyo po."

    scene bg boy_bullet
    with pixellate

    play sound "images/alarm.mp3"

    security "Sir, paki-check po ulit nung bag. Check niyo po, Sir. Baka Sir may nakalimutan po kayong tanggalin. Kutsilyo o gunting."

    scene bg boy_bullet
    with pixellate

    play sound "images/alarm.mp3"

    security "Sir, di po namin siya hahawakan ok. Sir, paki check po Sir."

    scene bg boy_bullet_found
    with pixellate

    play sound "images/alarm.mp3"

    security "Sir, parang may nadetect po kami na parang bala sa bag niyo."

    scene bg boy_bullet_found
    with pixellate

    play sound "images/alarm.mp3"

    security "Sir, di po namin kayo pwedeng payagang makaalis while hindi kayo pumapasa sa security check po namin Sir."

    scene bg boy_bullet_found
    with pixellate

    security "Sir, violation po kayo Sir. Bawal po talagang magdala ng ganyan sa eroplano, Sir."

    scene bg boy_bullet_found
    with pixellate

    security "Sir, Sir? Hindi po talaga kayo makaka-alis Sir."

    scene bg boy_bullet_found
    with pixellate

    security "Sir? Sir?"

    "(...)"

    jump credits

label bullet_notcaught:
    security "Sir, sorry sir. Paki-ulit po."

    scene bg boy
    with pixellate

    security "Hmmm..."

    scene bg boy
    with pixellate

    security "Ah."

    scene bg boy
    with pixellate

    security "Thank you po Sir. All good."

    "(...)"

    scene bg boy
    with pixellate

    security "Sir! Sir excuse po."

    scene bg xray
    with flash

    security "Sir, yung rosaryo po ng kasama niyo kanina naiwan niya."

    "(...)"

    scene bg boarding
    with fade

    show ofw normal
    with dissolve

    ofw "Uy thank you! Lagot ako kay misis pag nagkataon. Haha."

    ofw "Di ako relihiyoso, pero mabisang gamot daw to pampa-alis ng homesickness."

    "(...)"

    ofw "First time mo rin bang mag abroad?"

    ofw "Saan ka nga ulit? Sa Dubai?"

    jump credits

label credits:

    scene black
    with fade

    scene bg creds
    with fade

    pause 10.0

    return
