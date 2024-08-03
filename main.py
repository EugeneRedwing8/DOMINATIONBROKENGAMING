@namespace
class SpriteKind:
    gridsprite = SpriteKind.create()
    gridsprite2 = SpriteKind.create()
    gridsprite3 = SpriteKind.create()
    gridsprite4 = SpriteKind.create()
    gridsprite5 = SpriteKind.create()
    gridsprite6 = SpriteKind.create()
    gridsprite7 = SpriteKind.create()
    image = SpriteKind.create()
    gridcol = SpriteKind.create()
    selector = SpriteKind.create()

if not (blockSettings.exists("CH")):
    blockSettings.write_number("CH", 0)
charactersunlocked = blockSettings.read_number("CH")
music.play(music.create_song(assets.song("""
        Selectch
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
tiles.set_current_tilemap(tilemap("""Select"""))
scene.set_background_color(8)
SlimeeSelect = sprites.create(assets.image("""slimeeselect"""), SpriteKind.gridsprite)
grid.place(SlimeeSelect, tiles.get_tile_location(0, 2))
SytarSelect = sprites.create(assets.image("""Sytarselect"""), SpriteKind.gridsprite2)
grid.place(SytarSelect, tiles.get_tile_location(1, 2))
MekaSelect = sprites.create(assets.image("""mekaselect"""), SpriteKind.gridsprite3)
grid.place(MekaSelect, tiles.get_tile_location(2, 2))
SockMonkeySelect = sprites.create(assets.image("""Sockmonkeyselect"""), SpriteKind.gridsprite4)
grid.place(SockMonkeySelect, tiles.get_tile_location(3, 2))
if charactersunlocked >= 1:
    SlipperSelect = sprites.create(assets.image("""Slipperselect"""), SpriteKind.gridsprite5)
    grid.place(SlipperSelect, tiles.get_tile_location(4, 2))
    if charactersunlocked >= 2:
        JumpySelect = sprites.create(assets.image("""jumpyselect"""), SpriteKind.gridsprite6)
        grid.place(JumpySelect, tiles.get_tile_location(5, 2))
        if charactersunlocked >= 3:
            MechablockSelect = sprites.create(assets.image("""Mechablockselect"""), SpriteKind.gridsprite7)
            grid.place(MechablockSelect, tiles.get_tile_location(6, 2))
Select = sprites.create(assets.image("""selectframe1"""), SpriteKind.selector)
grid.move_with_buttons(Select)
grid.place(Select, tiles.get_tile_location(0, 2))
animation.run_image_animation(Select, 
    [assets.image("""selectframe1"""), 
    assets.image("""selectframe2""")], 500, True)
DisplayText = fancyText.create("<wavy><red>SELECT A CHARACTER", 160, 1, customFont.battle_italics)
DisplayText.x = 110
DisplayText.y = 15

def on_overlap(sprite, otherSprite):
    if controller.A.is_pressed():
        characternum = 0
        start_game()
sprites.on_overlap(SpriteKind.selector, SpriteKind.gridsprite, on_overlap)

def on_overlap2(sprite2, otherSprite2):
    if controller.A.is_pressed():
        characternum = 1
        start_game()
sprites.on_overlap(SpriteKind.selector, SpriteKind.gridsprite2, on_overlap2)

def on_overlap3(sprite3, otherSprite3):
    if controller.A.is_pressed():
        characternum = 2
sprites.on_overlap(SpriteKind.selector, SpriteKind.gridsprite, on_overlap3)

def on_overlap4(sprite4, otherSprite4):
    if controller.A.is_pressed():
        arena = 0
        music.play(music.create_sound_effect(WaveShape.SAWTOOTH,
            0,
            5000,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridcol)
        sprites.destroy_all_sprites_of_kind(SpriteKind.image)
        sprites.destroy_all_sprites_of_kind(SpriteKind.selector)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite4)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite5)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite6)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite7)
        arenafunction(arena)
sprites.on_overlap(SpriteKind.selector, SpriteKind.gridcol, on_overlap4)

def start_game():
    tiles.set_current_tilemap(tilemap("""colosseum"""))
    fancyText.set_text(DisplayText, "<wavy><red>SELECT A COLOSSEUM")
    def on_after():
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite2)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite3)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite4)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite5)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite6)
        sprites.destroy_all_sprites_of_kind(SpriteKind.gridsprite7)
        sprites.destroy_all_sprites_of_kind(SpriteKind.selector)
        MistyMeadows = sprites.create(assets.image("""mistymeadowscol"""), SpriteKind.gridcol)
        grid.place(MistyMeadows, tiles.get_tile_location(0, 2))
        Display = (sprites.create(assets.image("""mistymeadowsdis"""), SpriteKind.image))
        Display.bottom = scene.camera_property(CameraProperty.BOTTOM)
        Select = (sprites.create(assets.image("""selectframe1"""), SpriteKind.selector))
        grid.move_with_buttons(Select)
        animation.run_image_animation(Select, 
        [assets.image("""selectframe1"""),
        assets.image("""selectframe2""")], 500, True)
        grid.place(Select, tiles.get_tile_location(0, 2))
    timer.after(500, on_after)

def arenafunction(col: number):
    global UnknownSprite, characternum
    if col == 0:
        tiles.set_current_tilemap(tilemap("""mistymeadowsarena"""))
    if characternum == 0:
        sprites.destroy_all_sprites_of_kind(SpriteKind.FancyText)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        UnknownSprite = sprites.create(assets.image("""slimee"""), SpriteKind.player)
        UnknownSprite.ay = 500
        scene.camera_follow_sprite(UnknownSprite)
    elif characternum == 1:
        sprites.destroy_all_sprites_of_kind(SpriteKind.FancyText)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        UnknownSprite = sprites.create(assets.image("""sytar"""), SpriteKind.player)
        UnknownSprite.ay = 500
        scene.camera_follow_sprite(UnknownSprite)
    def on_after():
        global canmove
        canmove = True
    timer.after(500, on_after)
    controller.move_sprite(UnknownSprite, 100, 0)

def on_event_pressed():
    global canmove, UnknownSprite
    if canmove:
        UnknownSprite.vy = -250
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

def on_update():
    global canmove
    if canmove:
        characterAnims()
game.on_update(on_update)

def characterAnims():
    global UnknownSprite
    if characternum == 0:
        characterAnimations.loop_frames(UnknownSprite, 
        [assets.image("""sytar""")
        ], 500, characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""sytar""")
        ], 500, characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite, 
        [assets.image("""sytarright1"""),
        assets.image("""sytarright2""")
        ], 500, characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite, 
        [assets.image("""sytarleft1"""),
        assets.image("""sytarleft2""")
        ], 500, characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""sytarjump1"""),
        assets.image("""sytarjump2"""),
        assets.image("""sytarjump3"""),
        assets.image("""sytarjump4"""),
        assets.image("""sytarjump5"""),
        assets.image("""sytarjump6"""),
        assets.image("""sytarjump7"""),
        assets.image("""sytarjump8"""),
        assets.image("""sytarjump9""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""sytarjump1"""),
        assets.image("""sytarjump2"""),
        assets.image("""sytarjump3"""),
        assets.image("""sytarjump4"""),
        assets.image("""sytarjump5"""),
        assets.image("""sytarjump6"""),
        assets.image("""sytarjump7"""),
        assets.image("""sytarjump8"""),
        assets.image("""sytarjump9""")        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump8"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejumpright1"""),
        assets.image("""slimeeright1""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT, Predicate.MOVING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump3"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejumpleft1"""),
        assets.image("""slimeeleft1""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT, Predicate.MOVING_LEFT))
    elif characternum == 1:
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimee""")
        ], 500, characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimee""")
        ], 500, characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeeright1"""),
        assets.image("""slimeeright2""")
        ], 500, characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeeleft1"""),
        assets.image("""slimeeleft2""")
        ], 500, characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump3"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejump8"""),
        assets.image("""slimeejump9""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump3"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejump8"""),
        assets.image("""slimeejump9""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump8"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejumpright1"""),
        assets.image("""slimeeright1""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_RIGHT, Predicate.MOVING_RIGHT))
        characterAnimations.loop_frames(UnknownSprite,
        [assets.image("""slimeejump1"""),
        assets.image("""slimeejump2"""),
        assets.image("""slimeejump3"""),
        assets.image("""slimeejump4"""),
        assets.image("""slimeejump5"""),
        assets.image("""slimeejump6"""),
        assets.image("""slimeejump7"""),
        assets.image("""slimeejumpleft1"""),
        assets.image("""slimeeleft1""")
        ], 50, characterAnimations.rule(Predicate.MOVING_UP, Predicate.FACING_LEFT, Predicate.MOVING_LEFT))


            


canmove = False
characternum = 0
UnknownSprite: Sprite = None

