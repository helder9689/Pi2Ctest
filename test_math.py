#sert a tester main.py 
import main
def test_substract():
    assert main.sub(4,3)==1   #on est dans le Red du cycle 
    assert main.sub(-4,-3)==-1
    assert main.sub(0,-10)==10
