@namespace
class SpriteKind:
    start = SpriteKind.create()

def on_overlap_tile(sprite, location):
    music.ba_ding.play()
    info.change_score_by(1)
    tiles.set_tile_at(location, myTiles.transparency16)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile8, on_overlap_tile)

def on_overlap_tile2(sprite, location):
    info.change_score_by(1)
    music.ba_ding.play()
    tiles.set_tile_at(location, myTiles.transparency16)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile11, on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile7, on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    info.change_score_by(1)
    music.ba_ding.play()
    tiles.set_tile_at(location, myTiles.transparency16)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile10, on_overlap_tile4)

mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 150, 150)
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100002000000000000000000000000000001010101010100010101010101010100010100000001000100000000000000000101000100010001000100010101010001010001000100010001000101000100010100010001000100010000000001000101000100010001000100010100010001010001000100010001050101000100010100010001000100010101010001000101000100010001000101060100010001010001000100010000000001000100010100010401000100010101010001000101000101010001000101010100010001010000010100010000010101000101010101000000000100000000010000000101010101010101010101010101010301
        """),
        img("""
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
        """),
        [myTiles.transparency16,
            myTiles.tile1,
            myTiles.tile5,
            myTiles.tile7,
            myTiles.tile8,
            myTiles.tile10,
            myTiles.tile11],
        TileScale.SIXTEEN))
tiles.place_on_random_tile(mySprite, myTiles.tile5)
scene.camera_follow_sprite(mySprite)
scene.set_background_color(13)
info.start_countdown(75)
info.set_score(0)