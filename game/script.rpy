# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define taxi = Character('Taxi', color="#c8ffc8")
define porter = Character('Porter', color="#CC00CC")
define ofw = Character('OFW', color='#00CC00')
define ticketer = Character('Ticketer', color='#CC00CC')


# The game starts here.
label start:

    taxi "Pare pareho silang lahat."

    taxi "Kung hindi kurap, inutil. Eh no. Tapos bukas magtataas nanaman ng diesel."

    taxi "Sasabihin na world economy daw. Eh may sarili naman tayong langis."

    taxi "Kaso tangina. Kupal din kasi ng mga Chekwa eh no."

    "(...)"

    taxi "Terminal 1 tayo boss, no?"

    "(...)"

    taxi "Nag Saudi din ako dati. 2 years."

    taxi "Drayber."

    taxi "Yung amo ko, arabo. Apo ng Sultan nila."

    taxi "Strikto sila dun. Mahuli ka lang na kumakain ng bawal, latigo agad."

    taxi "Lalo na pag bawal na gamot. Tangina. Bitay!"

    "(...)"

    taxi "Pero malungkot din, siyempre. Eh no."

    taxi "Ako rin. Yung misis ko hindi ko na rin pinasama sa airport."

    taxi "Mahirap na. Baka manghina ang tuhod ko, hindi na ako sumakay."

    taxi "Dubai ba kayo boss?"

    "(...)"

    taxi "Mas ok sa Dubai. Open city."

    taxi "Yung mga babae pwede magjogging ng maiksi ang shorts."

    taxi "Lalo na yung mga Puti. Sobrang hilig nilang magjogging. Eh no."

    taxi "Teka ikot lang tayo sir ha."

    "(...)"

    taxi "Tulungan na kita Sir"

    menu:

        "Allow":
            jump allow_help

        "Deny":
            jump deny_help

label allow_help:

    $ is_bullet = True

    taxi "Dalawang maleta lang po, eh no?"

    "(...)"

    taxi "Maraming salamat po Sir!"

    jump check_in

label deny_help:

    $ is_bullet = False

    taxi "Ok po sir."

    taxi "Wala namang naiwan, no?"

    "(...)"

    taxi "You're welcome po sir!"

    jump check_in

label check_in:

    ofw "Excuse me..."

    ofw "Dito ba pila. Para sa OEC?"

    "(...)"

    ofw "Wala ngatayong. Binayaran na travel tax. Nagbayad pa rin tayo sa OEC."

    ofw "Aalis nangalang tayo. Tataxan pa. Haaaay Pinoy!"

    "(...)"

    ofw "Bagal ng pila ah."

    ofw "Kahit san talaga, paggobyerno kung hindi kurap, inutil."

    ofw "Mabuti pa sa Dubai. Maayos."

    ofw "Ikaw, Dubai ka rin ba?"

    "(...)"

    ticketer "Is this all, Sir?"

    ticketer "Sir, pakitimbang na lang po ng carry on niyo."

    ticketer "Sorry Sir, pero pwede po ba macheck yung bag niyo"

    menu:

        "Allow":
            $ is_bullet = True
            ticketer "Ano po ba laman nito? Mga fragile po ba?"

        "Deny":
            $ is_bullet = False
            ticketer "Ah ok po Sir. May baggage allowance pa po kayo, baka gusto niyo pong bawasan ang nasa carry on niyo."

    "(...)"

    jump jollibee

label jollibee:

    "\"Mabilis lang ang 1 taon. Makaka-leave ka rin.\""

    "\"Matagal kong hinanda ang sarili ko para sa araw na to. Pero iba pa rin pala talaga pag nandito na.\""

    "\"Isipin mo na lang future natin ni Bimbim. Kung hindi ka aalis, pano natin matutupad mga pangarap natin para sa kanya.\""

    "\"Kung pwede lang, isasama ko kayo.\""

    "(...)"

    "Nakwento ni insan, may Eat Bulaga din dun kaya hindi ka mahohome-sick. May Viber din. May Skype pa. San ka pa."

    "Basta may internet. Heh."

    "Mabubuhay tayo, basta may internet. Haha."

    "Hindi tayo maghihiwalay."

    "(...)"

    "Pa, yung XBox ko ha."

    "Haha. Bakit, hindi naba magiging boplax ang anak ko?"

    "Hindi ah. Wala kang boplax na anak, Pa. Tamad lang."

    "(...)"

label checkpoint:

    ofw "Wala na palang terminal fee pag OFW. Ayos! One payb din yun."

    "(...)"

    ofw "Nakow, eto na. Eto na yung nabasa ko."

    ofw "Tangina. Try lang nila."

    ofw "Sila lalaglagan ko ng bala."

    ofw ""



    return
