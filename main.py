@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_combos_attach_combo():
    game.show_long_text("ура! ти знищив весь негатив!", DialogLayout.CENTER)
    game.set_game_over_effect(True, effects.smiles)
    game.game_over(True)
controller.combos.attach_combo("bbb", on_combos_attach_combo)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . .
        """),
        mySprite,
        0,
        -100)
    projectile.start_effect(effects.smiles)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    sprite.destroy(effects.fire, 100)
    otherSprite.destroy(effects.smiles, 100)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_score():
    game.show_long_text("ура! ти знищив весь негатив!", DialogLayout.CENTER)
    game.set_game_over_effect(True, effects.smiles)
    game.game_over(True)
info.on_score(100, on_on_score)

def on_on_overlap2(sprite2, otherSprite2):
    statusbar.value = 100
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap2)

def on_on_zero(status):
    game.over(False)
statusbars.on_zero(StatusBarKind.energy, on_on_zero)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    otherSprite3.destroy(effects.fire, 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
statusbar: StatusBarSprite = None
mySprite: Sprite = None
game.show_long_text("о ні! негативні емоції заповнили галактику тобі треба знищити негатив!",
    DialogLayout.CENTER)
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . 8 8 . . . . . . . 
            . . . . . . 8 9 9 8 . . . . . . 
            . . . . . . 8 9 9 8 . . . . . . 
            . . . . . 8 9 9 9 9 8 . . . . . 
            . . . . . 8 9 9 9 9 8 . . . . . 
            . . . . 8 9 9 9 9 9 9 8 . . . . 
            . . . . 8 9 9 9 9 9 9 8 . . . . 
            . . . 8 9 9 6 6 6 6 9 9 8 . . . 
            . . . 8 9 6 9 9 9 9 6 9 8 . . . 
            . . . 8 9 9 9 9 9 9 9 9 8 . . . 
            . . 8 9 9 9 6 9 9 6 9 9 9 8 . . 
            . . 8 9 9 9 9 9 9 9 9 9 9 8 . . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.attach_to_sprite(mySprite, -25, 0)

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_side(assets.image("""
        fuel
    """), 0, 50)
    myFuel.x = randint(0, 160)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        bad
    """), 0, 50)
    myEnemy.x = randint(0, 160)
    myEnemy.set_kind(SpriteKind.enemy)
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval3)
