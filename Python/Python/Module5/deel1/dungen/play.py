import game
JumbledDungeonUnsaveRoutesRoute01 = tuple(map(str, (1, 7, 4, 9, 6, 10)))
JumbledDungeonUnsaveRoutesRoute02 = tuple(map(str, (1, 7, 5, 9, 6, 10)))
JumbledDungeonUnsaveRoutesRoute04 = tuple(map(str, (1, 7, 5, 9, 6, 2)))
JumbledDungeonUnsaveRoutesRoute05 = tuple(map(str, (1, 7, 5, 9, 2)))
JumbledDungeonUnsaveRoutesRoute03 = tuple(map(str, (1, 7, 5, 8, 3, 6, 10)))
JumbledDungeonUnsaveRoutesRoute06 = tuple(map(str, (1, 7, 5, 8, 3, 6, 2)))



JumbledDungeonSaveRoutesRoute01 = ('1','4','2','10')
JumbledDungeonSaveRoutesRoute02 = ('1','4','9','2','10')
JumbledDungeonSaveRoutesRoute03 = ('1','4','9','2','10')
JumbledDungeonSaveRoutesRoute04 = ('1','7','4','2','10')
JumbledDungeonSaveRoutesRoute05 = ('1','7','4','9','2','10')
JumbledDungeonSaveRoutesRoute06 = ('1','7','4','9','6','2','10')
JumbledDungeonSaveRoutesRoute07 = ('1','7','4','9','6','10') 
JumbledDungeonSaveRoutesRoute08 = ('1','7','5','9','2','10')
JumbledDungeonSaveRoutesRoute09 = ('1','7','5','9','6','2','10')
JumbledDungeonSaveRoutesRoute10 = ('1','7','5','9','6','10')
JumbledDungeonSaveRoutesRoute11 = ('1','7','5','8','2','10')
JumbledDungeonSaveRoutesRoute12 = ('1','7','5','8','3','6','2','10')


ROOMORDER = ('1','7','4','5','8','3','9','6','2','10')

story = game.story(ROOMORDER)

story.print_title('Het verhaal van "The Jumbled Dungeon"')
story.executeByOrder(0)

if story.checkAnswerByOrder(0, 'b'):
    story.executeByOrder(1)

if story.checkAnswerByOrder(0, 'a') or story.checkAnswerByOrder(1, 'b'):
    story.executeByOrder(2)

if story.checkAnswerByOrder(1, 'a'):
    story.executeByOrder(3)
    if story.checkAnswerByOrder(3, 'b'):
        story.executeByOrder(4)
        if story.checkAnswerByOrder(4, 'a'):
            story.executeByOrder(5)

if story.checkAnswerByOrder(2, 'b') or story.checkAnswerByOrder(3, 'a'):
    story.executeByOrder(6)

if story.checkAnswerByOrder(5, 'b') or story.checkAnswerByOrder(6, 'b'):
    story.executeByOrder(7)

if story.checkAnswerByOrder(2, 'a') or story.checkAnswerByOrder(4, 'b') or story.checkAnswerByOrder(6, 'a') or story.checkAnswerByOrder(7, 'b'):
    story.executeByOrder(8)

if story.checkAnswerByOrder(5, 'a') or story.checkAnswerByOrder(7, 'a') or story.checkAnswerByOrder(8, '-'):
    story.executeByOrder(9)

story.proccess_attempt(story.finish())