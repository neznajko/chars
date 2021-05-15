#!/usr/bin/env python3
########################################################
from string import ascii_lowercase
import numpy as np
from random import randint, sample
from math import inf

_ = 8 # a b c d e f g h
def paint( arr, brsh=" %" ):
    '''
    arr  - character's array 
    '''
    for row in arr:
        print( "".join( map( lambda x: brsh[x], row )))
    print()
    
def load_alfabet():
    ''' load alphabet characters to memory '''
    alfabet = []
    for c in ascii_lowercase[:_]:
        arr = np.loadtxt( 'alfabet/' + c, dtype=int )
        alfabet.append( arr );
    return alfabet

def duplicate( arr, r = None ):
    ''' corrupt arr by duplicating a row '''
    if r == None:
        r = randint( 0, arr.shape[0] - 1 )
    return np.insert( arr, r, arr[r], axis=0 )

def delete( arr, r = None ):
    ''' delete a row '''
    if r == None:
        r = randint( 0, arr.shape[0] - 1 )
    return np.delete( arr, r, axis=0 )

def messup( arr ):
    ''' flip flop '''
    sh = arr.shape # copy Ninja Kakashi
    arr = arr.flatten()
    # maximum number of corrupted pixels (30%)
    mx = 30 * len( arr )// 100
    # pick random number in [0, mx]
    n = randint( 0, mx )
    # pick random sample
    s = sample( range( len( arr )), n )
    # flip flop
    for j in s: arr[j] = not arr[j]
    # reshape and return
    return arr.reshape( sh )

def gen_corr( c, f ):
    ''' generate list of corrupted characters by 
    passing the corresponding function f (duplicate
    or delete) 
    '''
    ls = []
    for j in range( c.shape[0] ):
        ls.append( f( c, j ))
    return ls

def gen_corr_alfabet( f ):
    ''' Generate corrupted alphabet; for every 
    alfabet letter call the corresponding gen_corr
    function
    '''
    corr_alfabet = []
    for j in range( _ ):
        c = alfabet[j]
        corr_alfabet.append( gen_corr( c, f ))
    return corr_alfabet

def diff( x, y ):
    ''' Return number of different pixels
    '''
    return np.sum( x != y ) # numpy rocks

def classify( c ):
    ''' Finally
    '''
    mi = -1   # minimum letter index
    md = inf  # minimum difference
    # only messing up
    if height == c.shape[0]:
        for i in range( _ ):
            d = diff( alfabet[i], c )
            if d < md:
                mi = i
                md = d
    # deleted
    elif height > c.shape[0]:
        for i in range( _ ):
            for a in alfadel[i]:
                d = diff( a, c )
                if d < md:
                    mi = i
                    md = d
    # duplicated 
    else: 
        for i in range( _ ):
            for a in alfadup[i]:
                d = diff( a, c )
                if d < md:
                    mi = i
                    md = d
    return mi

if __name__ == '__main__':
    # load all necessary stuff
    alfabet = load_alfabet()
    alfadup = gen_corr_alfabet( duplicate )
    alfadel = gen_corr_alfabet( delete )
    # generate some corrupted letter
    j = 4 # e
    c = alfabet[j]
    height = c.shape[0]
    # delete / duplicate / mess-up
#    c = delete( c )
    c = duplicate( c )
    c = messup( c )
    paint( c )
    print( ascii_lowercase[classify( c )] )

########################################################
# log:
