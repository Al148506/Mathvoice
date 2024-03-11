define p = Character("[mcname]", color="#FFC300")
define me = Character("Merlin", color="#FBFF00")
define mi = Character("Minotauro", color="#AC33FF")
define h = Character("Hada", color="#07b63e")
default mcname = "Pedro"

#define images
image pizza:
    "pizza8.png"
    zoom 1.5
image pizza5:
    "pizza5.png"
    zoom 1.5
image pizza4:
    "pizza4.png"
    zoom 1.5

## Create your variables here
## This is the same as doing $knowledge = 1 in label start
default prueba1 = 0
default prueba2 = 0
default prueba3 = 0
default total = 0

# El juego comienza aquí.
# Selección de personaje

init:
    $vidaP1 = 100
    $vidaP2 = 100
    $ataqueCorrecto = 20
    $ataqueIncorrecto = 0

#screen plantilla():
    #text "Vida: [vidaP1]":
        #xpos 0.1
        #ypos 0.1
    #text "Vida: [vidaP2]":
        #xpos 0.85
        #ypos 0.1

label prueba1_increased:
    $ prueba1 += 1
    return

init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        renpy.random.shuffle(items)
        return renpy_menu(items)


label start:
    
    jump quizz
    # Muestra una imagen de fondo
    scene fondocastillo with fade
    show screen gameUIprueba
    "Para avanzar durante el juego sólo oprime la barra espaciadora en el teclado"
    show pedro with dissolve
    "Había una vez, un pequeño aventurero llamado Pedro, el cuál en una de sus aventuras llamá a la puerta de un castillo misterioso."
    # Ruido tocando puerta
    play sound "audio/puerta.mp3"
    "..."
    hide pedro 
    "La puerta se abre lentamente."
    # Ruido abriendo puerta
    play sound "audio/puertaabierta.mp3"
    "..."
    "En el interior, encuentra a un hombre con cara de preocupación."
    show merlin at right with dissolve
    show pedro at left with dissolve
    # voice "narrador/line2.mp3"
    p "Hola, señor. Estoy en un viaje de aventuras y me preguntaba si podría alojarme en su castillo."
    # hide pedro with dissolve
    # voice "merlin/line1.mp3"
    me "¡Oh, eres aquel del que hablaban las profecías! Necesito tu ayuda, joven. Criaturas míticas han invadido mi castillo."
    p "¿De qué profecías me está hablando?"
    me "No hay tiempo que perder, ayúdame por favor, sígueme al salón principal."
    p "Está bien, pero después de ayudarlo el castillo es mío."
    me "Ya hablaremos de tu recompensa por el camino, ahora sígueme."
    hide pedro with dissolve
    hide merlin with dissolve
    scene interiorcastillo with fade
    show hada with dissolve
    # risa de hada
    "Pedro y Merlin entran al salón principal del castillo, donde se encuentra una hermosa hada."
    play sound "audio/enojada.mp3"
    ""
    h "¡Quién se atreve a interrumpir en mi castillo!"
    hide hada with dissolve
    show merlini at left with dissolve
    me "Lo siento, hada, pero necesitamos que te vayas."
    show hada at right with dissolve
    h "Muy bien, me iré solo si aquel joven muchacho logra superar una prueba matemática."
    hide merlini with dissolve
    show pedro at left with dissolve
    p "¿Yo? Lo siento, Merlin, no creo poder superarla; las matemáticas son mi debilidad."
    hide pedro with dissolve
    show merlini at left with dissolve
    me "No te preocupes, muchacho, daremos un repaso a los conceptos básicos."
    hide merlini with dissolve
    hide hada with dissolve
    show hada with dissolve
    h "¿Quién dijo que les iba a dar tiempo para dar un repaso? Si no acepta ahora mismo, me quedaré por siempre en este castillo."
    hide hada with dissolve
    show merlin with dissolve
    me "¡Tempus Sistere Chronos!"
    play sound "audio/timestop.mp3" volume 0.25
    "..."
    hide merlin with dissolve
    # ruido de reloj
    "El mago Merlin ha conjurado un hechizo para parar el tiempo, ahora todo está inmóvil, excepto por Merlin y el joven caballero."
    show pedro at left with dissolve
    show merlin at right with dissolve
    me "Muy bien, ahora podremos dar un repaso sin que la hada se entere. Empecemos por los conceptos básicos. ¿Sabes cómo se clasifican los números?"
    p "La verdad es que no, pero me gustaría aprender."
    me "La primera clasificación con la que probablemente estés más familiarizado son los números naturales, que son representados por una N mayúscula. Son los que usas al contar. Te daré un ejemplo."
    "Merlin saca un gotero y empieza a salpicar, gota por gota."
    play sound "audio/3gotas.mp3" 
    "..."
    # ruido de gota x3
    me "¿Cuántas gotas cayeron?"
    p "Una, dos y tres; cayeron tres gotas."
    me "Correcto, los números naturales abarcan números enteros positivos del 1 hasta el infinito"
    me "Por cierto, ¿sabes cuáles son los números enteros?"
    p "Lo siento, no tengo idea."
    me "Los números enteros, representados por una Z mayúscula, incluyen todos los números naturales, pero también su parte negativa."
    p "Entonces, ¿los números enteros van desde -1 hasta -infinito pero también incluyen del 1 al infinito?"
    me "¡Exactamente!, pero recuerda, el número 0 también se incluye en los números enteros"
    me "Por último, te enseñaré lo que son los números racionales con una pizza."
    "Merlin saca una pizza hawaiana de su bolsillo mágico."
    #sonido de antojo
    play sound "audio/antojo.mp3" volume 0.25 
    hide merlin
    hide pedro
    show pizza with dissolve
    "..."
    p "Qué hambre me ha entrado. Un momento, ¿esa pizza tiene piña?"
    me "Por supuesto, pero ese no es el punto. Esta pizza tiene 8 rebanadas."
    me "Hora de comer"
    show pizza
    play sound "audio/comida.mp3"
    # sonido de comiendo x3
    hide pizza
    show pizza5
    me "Ahora solo quedan 5/8 de pizza."
    p "Tomaré una rebanada antes de que te la zampes toda."
    # sonido de pizza x4
    p "Puaj, ni con el hambre me sabe bien esta cosa."
    hide pizza5
    show pizza4
    p "Ahora sólo quedan 4 rebanadas de las 8 en total que tenía la pizza."
    me "También se podría decir que quedan 4 entre 8 o 0.5 de la pizza original"
    me "Así son los números racionales, representados por Q mayúscula; son el resultado de una división entre dos números naturales."
    me "Con la restriccion de que el denominador, es decir, el numero debajo de la división, no puede ser el número 0"
    me "Parece que he llegado a mi limite de magia, el tiempo se volvera a reanudar, preparate Pedrin"
    #sonido tiempo regreso
    play sound "audio/timestop.mp3" volume 0.25
    "..."
    hide merlin with dissolve
    hide pedro with dissolve
    show pedro at left with dissolve
    show hada at right with dissolve
    p "Estoy listo para la prueba , hada, ve preparando tus maletas!"
    h "Ya lo veremos mocoso, que empieze la prueba"
    jump quizz
    return

label quizz:
    scene fondocastillo with fade
    $ imagebutton_enabled_state = False
    show screen gameUI
    show pedro at left with dissolve
    show hada at right with dissolve
    "Es hora de la prueba de conocimientos"
    "Se presentarán un total de 10 preguntas, si lográs contestar correctamente la mayoría podrás hacer que el hada se vaya"
    "Para recorrer las opciones de respuesta, utiliza las flechas izquierda o derecha en el teclado"
    "Para seleccionar la respuesta, oprime la tecla Enter"
    #Initialize score
    $ quiz_score = 0

# 1st Question    
    menu:
        "¿Cuál clasificación representa la letra Z mayúscula?"
        "Números Enteros ":
            "¡Correcto!"
            $ quiz_score += 1
            call prueba1_increased
        "Números Racionales":
            "Incorrecto. Son los números enteros."
        "Números Naturales":
            "Incorrecto. Son los números enteros."
# 2nd Question
    
    menu:
        "¿Cuál es el primer número natural?"
        "0":
            "Incorrecto. El primer número natural es 1."
        "1":
            "¡Correcto!"
            $ quiz_score += 1
            call prueba1_increased
        "-1":
            "Incorrecto. Los números naturales comienzan desde 1."
# 3rd Question
    
    menu:
        "¿Qué tipo de número incluye los negativos, los positivos y el cero?"
        "Números Naturales":
            "Incorrecto. Los números naturales no incluyen negativos ni el cero."
        "Números Enteros":
            "¡Correcto! "
            $ quiz_score += 1
            call prueba1_increased
        "Números racionales":
            "Incorrecto. Los números enteros son más amplios."
# 4th Question
    
    menu:
        "¿Cuál de las siguientes opciones es un número racional?"
        "5/0":
            "Incorrecto. La divición entre 0 no es válida."
        "-2":
            "Incorrecto. Ese es un número entero."
        "3/4":
            "¡Correcto!"
            $ quiz_score += 1
            call prueba1_increased
# 5th Question
    
    menu:
        "¿Qué número no es un número entero?"
        "-5":
            "¡Incorrecto! -5 es un número entero."
           
        "0":
            "Incorrecto. El cero es un número entero."
        "2.5":
            "Correcto. Ese es un número racional."
            $ quiz_score += 1
            call prueba1_increased
# 6th Question
    menu:
        "¿Cuál clasificacion es la que no incluye el numero 0 ni los numeros negativos?"
        "Números racionales":
            "Incorrecto. Son los números naturales."
        "Números naturales":
            "¡Correcto!"
            $ quiz_score += 1
            call prueba1_increased
        "Numeros enteros":
            "Incorrecto. Son los números naturales."

# 7th Question
    
    menu:
        "¿Cuál clasificación respresenta la letra N mayúscula?"
        "Números Enteros ":
            "Incorrecto. Son los números naturales."
        "Números Racionales":
            "Incorrecto. Son los números naturales."
        "Números Naturales":
            "¡Correcto!."
            $ quiz_score += 1
            call prueba1_increased
# 8th Question
   
    menu:
        "¿Cuál de los siguientes es un número natural?"
        "-1":
            "Incorrecto. Ese es negativo."
        "0":
            "Incorrecto. Los números naturales son mayores que cero."
        "7":
            "¡Correcto! 7 es un número natural."
            $ quiz_score += 1
            call prueba1_increased
# 9th Question
    
    menu:
        "¿Qué tipo de número es 1.5?"
        "Número Natural":
            "Incorrecto. Ese incluye solo enteros positivos."
        "Número racional":
            "¡Correcto! 1.5 es un número racional."
            $ quiz_score += 1
            call prueba1_increased
        "Número Irracional":
            "Incorrecto. Los números irracionales son más complejos."
#10th Question
    menu:
        "¿Cuál clasificación respresenta la letra Q mayúscula?"
        "Números Enteros ":
            "Incorrecto. Son los números racionales."
        "Números Racionales":
            "¡Correcto!"
            $ quiz_score += 1
            call prueba1_increased
        "Números Naturales":
            "Incorrecto. Son los números racionales."
           
    # Check the quiz score
    if quiz_score >= 6:
        # Win
        p "¡He ganado!, es hora de que te vayas"
        h "¡Quedaté con tu cochino castillo!"
        # Did he win? Yes.
        $ win = True
        jump jardin
    else:
        # Lose
        p "¡He perdidooo!"
        # Did he win? No.
        $ win = False
        me "¡Temporae Reversus!"
        play sound "audio/timestop.mp3" volume 0.25
        "..."
        me "He retrocedido el tiempo para tener otra oportunidad, no te rindas muchacho"
        jump quizz
    return

label laberinto:
    scene interiorcastillo with fade
    show pedro at left with dissolve
    show hada at right with dissolve
    h "Bueno, me largo"
    play sound "audio/hadahuida.mp3" volume 0.25
    "El hada se ha ido dejando polvos mágicos por el camino"
    #sonido de desvanecimiento
    hide hada with dissolve
    me "¡Lo lograste muchacho!"
    p "Así fue, ahora quiero mi recompensa"
    me "Claro, lo prometido es deuda, sigueme al jardín del castillo, allí se encuentra lo que te prometí"
    p "¿Pero qué es?"
    me "No seas impaciente Pedrin, deja que la vida te sorprenda"
    p "Bien, vamos allá entonces"
    scene jardin with fade
    "Pedro y Merlin llegan al jardín, donde en el centro reposa una gran espada"
    "Pero de pronto, sale de los arbustos una criatura algo enfadada"
    show minotauro 
    play sound "audio/minotaur.mp3" volume 0.25
    ""
    mi "¿Quién se atrevé ha entrar en mí jardín?"
    p "No otra vez..."
    mi "Ahora yo soy el dueño de este jardín, marchense ahora o enfrentense a mi desafío"
    "Pedro empuña su espada dispuesto a atacar al minotauro"
    me "¿Te has vuelto loco Pedro? La única manera de derrotar a criaturas mitologicas es a través de desafios matemáticos, todo el mundo lo sabe"
    mi "Así es, en una batalla de verdad no me aguantarías ni un round"
    p "Bueno, acabemos con esto de una buena vez"
    mi"Como tú digas, a la una, a las dos y..."
    me "¡Tempus Sistere Chronos!"
    play sound "audio/timestop.mp3" volume 0.25
    "..."
    hide minotauro with dissolve
    # ruido de reloj
    "El mago Merlin ha conjurado un hechizo para parar el tiempo, ahora todo está inmóvil, excepto por Merlin y el joven caballero."
    show pedro at left with dissolve
    show merlin at right with dissolve
    me "Muy bien, ahora podremos dar un repaso sin que el minotauro se entere, terminemos de ver las clasificaciones que nos faltan"
    me "Empezemos con los números irracionales, representados por una Q mayúscula, los cuales no se pueden expresarse como una fracción exacta de dos números enteros"
    me "Ejemplos comunes de este tipo de numeros son la raiz cuadrada de dos, el número pi y la constante de Euler"
    me "Estos números no pueden expresarse de manera exacta como fracciones y sus expansiones decimales continúan infinitamente sin repetirse en ningún patrón."
    p "Lo entiendo, si veo un numero con muchos decimales que no se esten repitiendo, probablemente sea un numero irracional"
    me "Así es, como el valor de Pi, que es 3.1415926535, o 3.1416 redondeado para más facilidad en sus operaciones"
    me "Sigamos con la siguiente clasificación, los números Reales, representados por R mayúscula, son un conjunto que abarca a los números naturales, enteros, racionales e irracionales"
    p "Genial, son todas las clasificaciones que ya hemos repasado antes"
    me "Finalmente, tenemos los números complejos, los cuales son una extención de los números reales con una parte imaginaria"
    me "Siguen una estructura de a + bi , donde a y b son numeros reales y la i es imaginaria con un valor de raíz cuadrada de -1"
    p "¿Podrías darme ejemplos de números abstractos"
    me "Claro, te doy 3 ejemplos, 2+3i, 1-4i, por último -3i"
    "La magia de Merlín ha llegado a su límite, el curso del tiempo vuelve a la normalidad"
    play sound "audio/timestop.mp3" volume 0.25
    mi "Qué palabras más raras has gritado viejo"
    mi "Cómo sea, es hora de la prueba joven caballero"
    p "¡Estoy listo!"
    hide pedro
    hide merlin


label quizz2:

    show pedro at left with dissolve
    show minotauro at right with dissolve
    "Es hora de la prueba de conocimientos"
    "Se presentarán un total de 10 preguntas, si lográs contestar correctamente la mayoría podrás hacer que el minotauro se vaya"
    "Para recorrer las opciones de respuesta, utiliza las flechas izquierda o derecha en el teclado"
    "Para seleccionar la respuesta, oprime la tecla Enter"
    #Initialize score
    $ quiz_score = 0

    # 1st Question
    menu:
        "¿Cuál es la principal característica de un número irracional?"
        "Puede expresarse como fracción.":
            "Incorrecto. Los números irracionales no pueden expresarse como fracciones."
        "Tiene una parte imaginaria.":
            "Incorrecto. Esa característica corresponde a los números complejos."
        "No puede expresarse como fracción.":
            "¡Correcto!"
            $ quiz_score += 1

    # 2nd Question
    menu:
        "¿Cuál es la diferencia clave entre los números racionales y los números irracionales?"
        "Los números racionales pueden expresarse como fracciones, los irracionales no.":
            "¡Correcto!"
            $ quiz_score += 1
        "Los números irracionales pueden expresarse como fracciones, los racionales no.":
            "Incorrecto. Es al revés."
        "No hay diferencia.":
            "Incorrecto. Hay una diferencia fundamental."

    # 3rd Question
    menu:
        "¿Cuál es la representación general de un número complejo?"
        "a + bi":
            "¡Correcto!"
            $ quiz_score += 1
        "a - bi":
            "Incorrecto. Esa es otra forma válida de representar un número complejo."
        "a x bi":
            "Incorrecto. Esta opción no representa un número complejo."

    # 4th Question
        "¿A qué clasificación pertenece el número √2?"
        "Números Irracionales":
            "¡Correcto!"
            $ quiz_score += 1
        "Números Racionales":
            "Incorrecto. √2 no puede expresarse como fracción."
        "Números Reales":
            "Incorrecto. Aunque es real, la clasificación más específica es irracional."

    # 5th Question
    menu:
        "¿Cuál es el número irracional más conocido y utilizado en matemáticas?"
        "e":
            "Incorrecto. 
        e es un número irracional, pero no es el más conocido."
        "π":
            "¡Correcto!"
            $ quiz_score += 1
        "√2":
            "Incorrecto. es también irracional, pero no es tan conocido como π."

    # 6th Question
    menu:
        "¿Qué significa que un número complejo tenga una parte imaginaria igual a cero?"
        "Es un número imaginario puro.":
            "Incorrecto. Significa que no hay parte imaginaria."
        "Es un número real.":
            "¡Correcto!"
            $ quiz_score += 1
        "Es un número complejo no válido.":
            "Incorrecto. Es válido, simplemente no tiene componente imaginaria."

    # 7th Question
    menu:
        "¿Cuál es el valor de la unidad imaginaria, representada por i?"
        "1":
            "Incorrecto.i es la raíz cuadrada de -1, no 1."
        "√2":
            "Incorrecto. i es la raíz cuadrada de -1
        ."
        "√(-1)":
            "¡Correcto!"
            $ quiz_score += 1

    # 8th Question
    menu:
        "¿A qué clasificación pertenece el número -7.5?"
        "Números Reales":
            "¡Correcto!"
            $ quiz_score += 1
        "Números Enteros":
            "Incorrecto. Incluye decimales, por lo que no es entero."
        "Números Complejos":
            "Incorrecto. No hay parte imaginaria, por lo que no es complejo."

    # 9th Question
    menu:
        "¿Qué propiedad distingue a los números reales de los números complejos?"
        "Los números complejos tienen una parte imaginaria, los reales no.":
            "¡Correcto!"
            $ quiz_score += 1
        "Los números reales son más grandes que los números complejos.":
            "Incorrecto. No hay un orden de "más grande" en este contexto."
        "Los números reales pueden expresarse como fracciones, los complejos no.":
            "Incorrecto. Ambos pueden expresarse como fracciones."

    # 10th Question
    menu:
        "¿Cuáles son las cualidades de los números irracionales ?"
        "Infinitud.":
            "Incorrecto. Tienen una expansión decimal no repetitiva ni periódica."
        "No tienen expansión decimal.":
            "Incorrecto. Tienen expansión decimal, pero no repetitiva ni periódica."
        "No son repetitivos ni periódicos en su expansión decimal":
            "¡Correcto!"
            $ quiz_score += 1
           
    # Check the quiz score
    if quiz_score >= 6:
        # Win
        p "¡He ganado!, es hora de que te vayas"
        mi "¡Eres un oponente formidable!"
        # Did he win? Yes.
        $ win = True
        jump final
    else:
        # Lose
        p "¡He perdidooo!"
        # Did he win? No.
        $ win = False
        me "¡Temporae Reversus!"
        play sound "audio/timestop.mp3" volume 0.25
        "..."
        me "He retrocedido el tiempo para tener otra oportunidad, no te rindas muchacho"
        jump quizz2
    return

label final:
    mi "Tienes potencial muchacho, dejame servirte como guardian"
    p "No necesito a nadie que me proteja, puedes marcharte"
    "El minotauro de marcha galopando hacía el bosque"
    #Sonido de galope
    me "Bueno, es hora de darte tu recompensa muchacho"
    p "¿Qué es?"
    me "¿Esa espada que esta en el centro del jardín, si eres capas de sacarla de su pedestal, es tuya"
    

