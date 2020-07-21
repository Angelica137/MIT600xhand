from scripts.hand import Hand

def test_update_method():
	myHand = Hand(7)
	myHand.setDummyHand('aceffly')
	myHand.update('ace') 
	assert myHand.hand == {'a': 0, 'c': 0, 'e': 0, 'f': 2, 'l': 1, 'y': 1}