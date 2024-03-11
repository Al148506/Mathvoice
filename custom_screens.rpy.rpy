## Screen with Stats Button
default imagebutton_enabled_state = True
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/calificacion.png"
        hover_sound "audio/calificaciones.mp3"
        #activate_sound "audio/calificaciones.mp3"
        action ShowMenu("StatsUI")
        sensitive imagebutton_enabled_state
    
screen gameUIprueba:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/calificacion.png"
        #hover_sound "audio/calificaciones.mp3"
        #activate_sound "audio/calificaciones.mp3"
        action ShowMenu("StatsUI")
        sensitive imagebutton_enabled_state
        
## Stats UI
screen StatsUI:
    add "UI/bg_blue.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "Prueba 1" size 40
                text "Prueba 2" size 40
                text "Prueba 3" size 40
                text "Total" size 40

            # Values Column     
            vbox:    
                spacing 10
                text "[prueba1]" size 40
                text "[prueba2]" size 40
                text "[prueba3]" size 40
                text "[total]" size 40
    
    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/regresar.png"
        hover_sound "audio/regresar.mp3"
        #activate_sound "audio/regresar.mp3"
        action Return()
