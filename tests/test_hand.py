from scripts.hand import Hand

def test_update_method():
	myHand = Hand(7)
	myHand.setDummyHand('aceffly')
	myHand.update('ace') 
	assert myHand.calculateLen() == 4