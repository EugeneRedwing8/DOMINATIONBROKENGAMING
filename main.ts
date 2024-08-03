let SlipperSelect: Sprite;
let JumpySelect: Sprite;
let MechablockSelect: Sprite;
namespace SpriteKind {
    export const gridsprite = SpriteKind.create()
    export const gridsprite2 = SpriteKind.create()
    export const gridsprite3 = SpriteKind.create()
    export const gridsprite4 = SpriteKind.create()
    export const gridsprite5 = SpriteKind.create()
    export const gridsprite6 = SpriteKind.create()
    export const gridsprite7 = SpriteKind.create()
    export const image = SpriteKind.create()
    export const gridcol = SpriteKind.create()
    export const selector = SpriteKind.create()
}

if (!blockSettings.exists("CH")) {
    blockSettings.writeNumber("CH", 0)
}

let charactersunlocked = blockSettings.readNumber("CH")
music.play(music.createSong(assets.song`
        Selectch
    `), music.PlaybackMode.LoopingInBackground)
tiles.setCurrentTilemap(tilemap`Select`)
scene.setBackgroundColor(8)
let SlimeeSelect = sprites.create(assets.image`slimeeselect`, SpriteKind.gridsprite)
grid.place(SlimeeSelect, tiles.getTileLocation(0, 2))
let SytarSelect = sprites.create(assets.image`Sytarselect`, SpriteKind.gridsprite2)
grid.place(SytarSelect, tiles.getTileLocation(1, 2))
let MekaSelect = sprites.create(assets.image`mekaselect`, SpriteKind.gridsprite3)
grid.place(MekaSelect, tiles.getTileLocation(2, 2))
let SockMonkeySelect = sprites.create(assets.image`Sockmonkeyselect`, SpriteKind.gridsprite4)
grid.place(SockMonkeySelect, tiles.getTileLocation(3, 2))
if (charactersunlocked >= 1) {
    SlipperSelect = sprites.create(assets.image`Slipperselect`, SpriteKind.gridsprite5)
    grid.place(SlipperSelect, tiles.getTileLocation(4, 2))
    if (charactersunlocked >= 2) {
        JumpySelect = sprites.create(assets.image`jumpyselect`, SpriteKind.gridsprite6)
        grid.place(JumpySelect, tiles.getTileLocation(5, 2))
        if (charactersunlocked >= 3) {
            MechablockSelect = sprites.create(assets.image`Mechablockselect`, SpriteKind.gridsprite7)
            grid.place(MechablockSelect, tiles.getTileLocation(6, 2))
        }
        
    }
    
}

let Select = sprites.create(assets.image`selectframe1`, SpriteKind.selector)
grid.moveWithButtons(Select)
grid.place(Select, tiles.getTileLocation(0, 2))
animation.runImageAnimation(Select, [assets.image`selectframe1`, assets.image`selectframe2`], 500, true)
let DisplayText = fancyText.create("<wavy><red>SELECT A CHARACTER", 160, 1, customFont.battle_italics)
DisplayText.x = 110
DisplayText.y = 15
sprites.onOverlap(SpriteKind.selector, SpriteKind.gridsprite, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    let characternum: number;
    if (controller.A.isPressed()) {
        characternum = 0
        start_game()
    }
    
})
sprites.onOverlap(SpriteKind.selector, SpriteKind.gridsprite2, function on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    let characternum: number;
    if (controller.A.isPressed()) {
        characternum = 1
        start_game()
    }
    
})
sprites.onOverlap(SpriteKind.selector, SpriteKind.gridsprite, function on_overlap3(sprite3: Sprite, otherSprite3: Sprite) {
    let characternum: number;
    if (controller.A.isPressed()) {
        characternum = 2
    }
    
})
sprites.onOverlap(SpriteKind.selector, SpriteKind.gridcol, function on_overlap4(sprite4: Sprite, otherSprite4: Sprite) {
    let arena: number;
    if (controller.A.isPressed()) {
        arena = 0
        music.play(music.createSoundEffect(WaveShape.Sawtooth, 0, 5000, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridcol)
        sprites.destroyAllSpritesOfKind(SpriteKind.image)
        sprites.destroyAllSpritesOfKind(SpriteKind.selector)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite4)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite5)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite6)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite7)
        arenafunction(arena)
    }
    
})
function start_game() {
    tiles.setCurrentTilemap(tilemap`colosseum`)
    fancyText.setText(DisplayText, "<wavy><red>SELECT A COLOSSEUM")
    timer.after(500, function on_after() {
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite2)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite3)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite4)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite5)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite6)
        sprites.destroyAllSpritesOfKind(SpriteKind.gridsprite7)
        sprites.destroyAllSpritesOfKind(SpriteKind.selector)
        let MistyMeadows = sprites.create(assets.image`mistymeadowscol`, SpriteKind.gridcol)
        grid.place(MistyMeadows, tiles.getTileLocation(0, 2))
        let Display = sprites.create(assets.image`mistymeadowsdis`, SpriteKind.image)
        Display.bottom = scene.cameraProperty(CameraProperty.Bottom)
        let Select = sprites.create(assets.image`selectframe1`, SpriteKind.selector)
        grid.moveWithButtons(Select)
        animation.runImageAnimation(Select, [assets.image`selectframe1`, assets.image`selectframe2`], 500, true)
        grid.place(Select, tiles.getTileLocation(0, 2))
    })
}

function arenafunction(col: number) {
    
    if (col == 0) {
        tiles.setCurrentTilemap(tilemap`mistymeadowsarena`)
    }
    
    if (characternum == 0) {
        sprites.destroyAllSpritesOfKind(SpriteKind.FancyText)
        sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        UnknownSprite = sprites.create(assets.image`slimee`, SpriteKind.Player)
        UnknownSprite.ay = 500
        scene.cameraFollowSprite(UnknownSprite)
    } else if (characternum == 1) {
        sprites.destroyAllSpritesOfKind(SpriteKind.FancyText)
        sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        UnknownSprite = sprites.create(assets.image`sytar`, SpriteKind.Player)
        UnknownSprite.ay = 500
        scene.cameraFollowSprite(UnknownSprite)
    }
    
    timer.after(500, function on_after() {
        
        canmove = true
    })
    controller.moveSprite(UnknownSprite, 100, 0)
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    
    if (canmove) {
        UnknownSprite.vy = -250
    }
    
})
game.onUpdate(function on_update() {
    
    if (canmove) {
        characterAnims()
    }
    
})
function characterAnims() {
    
    if (characternum == 0) {
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytar`], 500, characterAnimations.rule(Predicate.NotMoving, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytar`], 500, characterAnimations.rule(Predicate.NotMoving, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytarright1`, assets.image`sytarright2`], 500, characterAnimations.rule(Predicate.MovingRight, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytarleft1`, assets.image`sytarleft2`], 500, characterAnimations.rule(Predicate.MovingLeft, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytarjump1`, assets.image`sytarjump2`, assets.image`sytarjump3`, assets.image`sytarjump4`, assets.image`sytarjump5`, assets.image`sytarjump6`, assets.image`sytarjump7`, assets.image`sytarjump8`, assets.image`sytarjump9`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`sytarjump1`, assets.image`sytarjump2`, assets.image`sytarjump3`, assets.image`sytarjump4`, assets.image`sytarjump5`, assets.image`sytarjump6`, assets.image`sytarjump7`, assets.image`sytarjump8`, assets.image`sytarjump9`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump8`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejumpright1`, assets.image`slimeeright1`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingRight, Predicate.MovingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump3`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejumpleft1`, assets.image`slimeeleft1`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingLeft, Predicate.MovingLeft))
    } else if (characternum == 1) {
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimee`], 500, characterAnimations.rule(Predicate.NotMoving, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimee`], 500, characterAnimations.rule(Predicate.NotMoving, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeeright1`, assets.image`slimeeright2`], 500, characterAnimations.rule(Predicate.MovingRight, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeeleft1`, assets.image`slimeeleft2`], 500, characterAnimations.rule(Predicate.MovingLeft, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump3`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejump8`, assets.image`slimeejump9`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump3`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejump8`, assets.image`slimeejump9`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingLeft))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump8`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejumpright1`, assets.image`slimeeright1`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingRight, Predicate.MovingRight))
        characterAnimations.loopFrames(UnknownSprite, [assets.image`slimeejump1`, assets.image`slimeejump2`, assets.image`slimeejump3`, assets.image`slimeejump4`, assets.image`slimeejump5`, assets.image`slimeejump6`, assets.image`slimeejump7`, assets.image`slimeejumpleft1`, assets.image`slimeeleft1`], 50, characterAnimations.rule(Predicate.MovingUp, Predicate.FacingLeft, Predicate.MovingLeft))
    }
    
}

let canmove = false
let characternum = 0
let UnknownSprite : Sprite = null
