import math

def find_first_primes(num):
    primes = []
    a = 1
    while(len(primes) < num):
        a+=1
        if(less_dumb_is_prime(a, primes)):
            primes.append(a)

    return primes


# Tests againsts list of smaller primes
def less_dumb_is_prime(num,first_primes):
    if len(first_primes) == 0:
        return dumb_is_prime(num)

    for i in range(0,len(first_primes)):
        if num % first_primes[i] == 0:
            return False
        if first_primes[i] > math.sqrt(num):
                return True

    return dumb_is_prime(num)

# test number to see if any smaller number divides it
def dumb_is_prime(num):

    if num == 2:
        return True

    a = 1

    while a <= math.sqrt(num):
        a += 1
        if(num % a == 0):
            return False

    return True

def run_tests():
    assert(dumb_is_prime(257))
    assert(dumb_is_prime(2))
    assert(dumb_is_prime(3))
    assert(find_first_primes(1000)[999] == 7919)

    ten_first = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert(find_first_primes(10) == ten_first)


def get_diffs(nums):
    diffs = []
    for i in range(1,len(nums)):
        diffs.append(nums[i] - nums[i-1])
    return diffs

def diff_info(num):
    primes = find_first_primes(num)
    diffs = get_diffs(primes)
    print("diffs: "+str(diffs))
    print("max: "+str(max(diffs)))

def dumb_is_probable_prime(num, firsts):
    for i in range(0,len(firsts)):
        if firsts[i] > math.sqrt(num):
            return True
        if num % firsts[i] == 0:
            return False

    return True

def test_probable_prime_func(func):
    num_first = 70
    firsts = find_first_primes(num_first)
    positives = 0
    false_positives = 0
    false_negatives = 0
    
    min_num = 100000
    max_num = 200000
    
    for  i in range(min_num, max_num):
        num = i
        test = dumb_is_prime(num)
        prob = func(num, firsts)

        if(test and prob):
            positives += 1
        if(prob and not test):
            false_positives += 1
        if(not prob and test):
            false_negatives += 1

    # there should be no false negatives
    assert(false_negatives == 0)

    error_ratio = false_positives / positives
    correct_ratio = 1 - error_ratio
    percent_correct = correct_ratio*100
    percent_correct_str = "%.2f" % (percent_correct)
    percent_lastfirst = firsts[-1] / max_num * 100
    percent_lastfirst_str = "%.2f" % percent_lastfirst
    
    print("Primes found :       " + str(positives - false_positives))
    print("False primes found : " + str(false_positives))
    print("Percentage correct : " + percent_correct_str
          + " %")
    print("last first prime :   " + str(firsts[-1]))
    print("last first is :      "
          + percent_lastfirst_str + " % of maximum number")
    
run_tests()
#diff_info(10000)

test_probable_prime_func(dumb_is_probable_prime)
