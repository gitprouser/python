#import pdb

list_sample = [[1], [1], [[2], [1,[3,4,[4]], 6]]]
list_flat = []


def flatten(list):
    #pdb.set_trace()
    if len(list) == 0:
        return
    else:
        for x in list:
            if type(x) is type(list_sample):
                print 'awesome'
                flatten(x)
            else:
                print 'missed'
                list_flat.append(x)


if __name__ == '__main__':
    flatten(list_sample)
    print "list:",  list_sample
    print "list_flat", list_flat
