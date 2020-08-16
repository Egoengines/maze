namespace SpriteKind {
    export const start = SpriteKind.create()
}

scene.onOverlapTile(SpriteKind.Player, myTiles.tile8, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    music.baDing.play()
    info.changeScoreBy(1)
    tiles.setTileAt(location, myTiles.transparency16)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile11, function on_overlap_tile2(sprite: Sprite, location: tiles.Location) {
    info.changeScoreBy(1)
    music.baDing.play()
    tiles.setTileAt(location, myTiles.transparency16)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile7, function on_overlap_tile3(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile10, function on_overlap_tile4(sprite: Sprite, location: tiles.Location) {
    info.changeScoreBy(1)
    music.baDing.play()
    tiles.setTileAt(location, myTiles.transparency16)
})
let mySprite = sprites.create(img`
        . . . . . 5 5 5 5 5 . . . . . . 
            . . . . f f e d e f . . . . . . 
            . . . . f f d d d f f . . . . . 
            . . . . f f f d f f f . . . . . 
            . . . f 2 2 d d d 2 2 f . . . . 
            . . . 2 5 2 2 2 2 2 5 2 . . . . 
            d b d 2 5 2 2 2 2 2 5 2 d b d . 
            d b d f 2 5 2 5 2 5 2 f d b d . 
            . . . f f 5 5 5 5 5 f f . . . . 
            . . . f f 8 8 5 8 8 f f . . . . 
            . . . f f 8 8 8 8 8 f f . . . . 
            . . . . 8 8 8 8 8 8 8 . . . . . 
            . . . . 8 8 8 8 8 8 8 . . . . . 
            . . . . 1 1 . . . 1 1 . . . . . 
            . . 1 1 1 1 . . . 1 1 1 1 . . . 
            . . 1 1 1 1 . . . 1 1 1 1 . . .
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 150, 150)
tiles.setTilemap(tiles.createTilemap(hex`
            1000100002000000000000000000000000000001010101010100010101010101010100010100000001000100000000000000000101000100010001000100010101010001010001000100010001000101000100010100010001000100010000000001000101000100010001000100010100010001010001000100010001050101000100010100010001000100010101010001000101000100010001000101060100010001010001000100010000000001000100010100010401000100010101010001000101000101010001000101010100010001010000010100010000010101000101010101000000000100000000010000000101010101010101010101010101010301
        `, img`
            . . . . . . . . . . . . . . . 2 
                2 2 2 2 2 . 2 2 2 2 2 2 2 2 . 2 
                2 . . . 2 . 2 . . . . . . . . 2 
                2 . 2 . 2 . 2 . 2 . 2 2 2 2 . 2 
                2 . 2 . 2 . 2 . 2 . 2 2 . 2 . 2 
                2 . 2 . 2 . 2 . 2 . . . . 2 . 2 
                2 . 2 . 2 . 2 . 2 . 2 2 . 2 . 2 
                2 . 2 . 2 . 2 . 2 . 2 2 . 2 . 2 
                2 . 2 . 2 . 2 . 2 2 2 2 . 2 . 2 
                2 . 2 . 2 . 2 . 2 2 . 2 . 2 . 2 
                2 . 2 . 2 . 2 . . . . 2 . 2 . 2 
                2 . 2 . 2 . 2 . 2 2 2 2 . 2 . 2 
                2 . 2 2 2 . 2 . 2 2 2 2 . 2 . 2 
                2 . . 2 2 . 2 . . 2 2 2 . 2 2 2 
                2 2 . . . . 2 . . . . 2 . . . 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 2
        `, [myTiles.transparency16, myTiles.tile1, myTiles.tile5, myTiles.tile7, myTiles.tile8, myTiles.tile10, myTiles.tile11], TileScale.Sixteen))
tiles.placeOnRandomTile(mySprite, myTiles.tile5)
scene.cameraFollowSprite(mySprite)
scene.setBackgroundColor(13)
info.startCountdown(75)
info.setScore(0)
