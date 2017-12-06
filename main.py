import re


def C(n, k):                    # this is a convention for dynamic programming, where one function is a helper that creates the memoization table
    return _C(n, k, {})


def _C(n, k, memoization_table):
    key = str(n) + "," + str(k)             # 'key' variable uniquely identifies this sub-problem

    if key in memoization_table:            # if we've already computed this sub-problem..
        return memoization_table[key]       # .. return the saved result

    if k == 0 or n == k:                    # base case
        return 1

    memoization_table[key] = _C(n - 1, k - 1, memoization_table) + _C(n - 1, k, memoization_table)

    return memoization_table[key]


def force_user_input():
    while True:
        # get user input
        user_input = input('enter values for k and n separated by space: ')
        # process it with regex
        processed = re.compile('(\d+)\\s+(\d+)').match(user_input)
        # validate it
        if processed is not None:
            n = processed.group(1)
            k = processed.group(2)
            if n >= k:
                return int(n), int(k)
        # ask again if input was invalid
        print("Invalid input.")


n, k = force_user_input()
result = C(n, k)
print( "Result: ", result )