import pytest
@pytest.mark.parametrize("a,b", [(2,4), (2,3), (3,2), (4,1)])

@pytest.mark.skip(reason="already check ted")
def test_add(a,b):
    assert a+b == 5
