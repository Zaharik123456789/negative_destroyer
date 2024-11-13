namespace SpriteKind {
    export const Gas = SpriteKind.create()
}
controller.combos.attachCombo("bbb", function () {
    game.showLongText("ура! ти знищив весь негатив!", DialogLayout.Center)
    game.setGameOverEffect(true, effects.smiles)
    game.gameOver(true)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`pulya`, mySprite, 0, -100)
    projectile.startEffect(effects.smiles)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    sprite.destroy(effects.fire, 100)
    otherSprite.destroy(effects.smiles, 100)
})
info.onScore(100, function () {
    game.showLongText("ура! ти знищив весь негатив!", DialogLayout.Center)
    game.setGameOverEffect(true, effects.smiles)
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    info.changeLifeBy(-1)
    otherSprite3.destroy(effects.fire, 100)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    info.changeLifeBy(1)
    otherSprite2.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gas, function (sprite2, otherSprite2) {
    statusbar.value = 100
    otherSprite2.destroy()
})
statusbars.onZero(StatusBarKind.Energy, function (status) {
    game.over(false)
})
let _1up: Sprite = null
let myEnemy: Sprite = null
let myFuel: Sprite = null
let projectile: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
game.showLongText("о ні! негативні емоції заповнили галактику тобі треба знищити негатив!", DialogLayout.Center)
effects.starField.startScreenEffect()
mySprite = sprites.create(assets.image`ship`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.attachToSprite(mySprite, -25, 0)
game.onUpdateInterval(5000, function () {
    myFuel = sprites.createProjectileFromSide(assets.image`fuel`, 0, 50)
    myFuel.x = randint(0, 160)
    myFuel.setKind(SpriteKind.Gas)
})
game.onUpdateInterval(1000, function () {
    myEnemy = sprites.createProjectileFromSide(assets.image`bad`, 0, 50)
    myEnemy.x = randint(0, 160)
    myEnemy.setKind(SpriteKind.Enemy)
})
game.onUpdateInterval(300, function () {
    statusbar.value += -1
})
game.onUpdateInterval(10000, function () {
    _1up = sprites.createProjectileFromSide(assets.image`1-up`, 0, 50)
    _1up.x = randint(0, 160)
    _1up.setKind(SpriteKind.Food)
})
