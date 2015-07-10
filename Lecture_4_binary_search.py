
#l=[1,3,5,6,8,9,11]

def binary_search(l,v):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end)/2
        if v == l[mid]:
            return True
        elif v < l[mid]:
            end = mid - 1
        elif v > l[mid]:
            start = mid + 1

    return False

def simple_tests():
    assert binary_search([2,3,4,5,6,7,8,9],5)
    assert not binary_search([2,3,4,5,6,7,8,9],10)
    assert not binary_search([2,3,4,5,6,7,8,9],1)
    assert binary_search([0,0,1,1,2,2,3,3],3)
    print binary_search([0,0,1,1,2,2,3,3], -3)
    print binary_search([0,0,2,2,4,4,6,6], 3)
    print binary_search([0,0,1,1,2,2,3,3], 1.5)
    print binary_search([0,0,1,1,2,2,3,3], 100)


def test_search(lst,notlst):
    for item in lst:
        assert binary_search(lst, item)
    for item in notlst:
        assert not binary_search(lst, item)

def run_all_tests():
    test_search([0,0,1,1,2,2,3,3], [-3,1.5,100])
    test_search([1,3,5,7,12,12,15,16,100,132,223],
                [0,2,4,6,8,9,10,11,13,14,17,50,131,133,222,224])
    test_search([10], [1,112])
    test_search([], [10])
    test_search([0,10], [-2,2,20])

def main():
    simple_tests()
    run_all_tests()
    print "Passed!"

if __name__ == '__main__':
    main()