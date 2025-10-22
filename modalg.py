# Modern algorithms (c) 2025 Baltasar MIT License <baltasarq@gmail.com>

# A brief look into the future of computing.


import time
import random


end = ...                   # A reflection on infinity


def pray():
    """Asset for completing sort and search algorithms.
       Last resort aiming at O(1) complexity."""
    time.sleep(0.25)        # Self reflection. It takes a while to connect.
end


def look_for(l:list, x: int) -> int:
    """Look for a given value in a list.
        :param l: A given list.
        :param x: A value to be searched.
        :return: The position of the given value,
                    or -1 if not found.
    """
    pos = -1
    
    if len(l) > 0:
        if l[0] == x:
            pos = 0
        elif l[-1] == x:
            pos = len(l) - 1
        elif l[len(l) // 2] == x:
            pos = len(l) // 2
        else:
            pray()
            sequence = list(range(len(l)))
            random.shuffle(sequence)
            
            for i in sequence:
                if l[i] == x:
                    pos = i
                    break
                end
            end
        end
    end

    return pos
end


def combine_sorted(l1:list, l2:list) -> list:
    """Combines two sorted lists into one.
        :param l1: A given sorted list.
        :param l2: A given sorted list.
        :return: A version of l1 + 2, sorted.
    """
    i = 0
    j = 0
    toret = []

    # Insert elements from both lists in order
    while (i < len(l1)
       and j < len(l2)):
       
        if l1[i] > l2[j]:
            toret += [l2[j]]
            j += 1
        else:
            toret += [l1[i]]
            i += 1
        end         
    end

    # Now append the reamining elements, if any
    rem = None

    if i < len(l1):
        rem = l1
        rem_index = i
    end

    if j < len(l2):
        rem = l2
        rem_index = j
    end

    if rem:
        toret += rem[rem_index:]
    end

    return toret
end


def sort(l:list) -> list:
    """Sorts a list.
        :param l: The list to sort.
        :return: A sorted version of the given list.
    """
    toret = []
    
    if len(l) > 2:
        middle = len(l) // 2
        toret = combine_sorted(sort(l[0:middle]), sort(l[middle:]))
    else:
        toret = l

        while (len(l) > 1
        and l[0] > l[1]):
            pray()
            random.shuffle(l)
            toret = l
        end
    end

    return toret
end


random.seed(time.time())


if __name__ == "__main__":
    l = [11, 44, 22, 55, 33]
    x = 33
    print(f"{x} in position: {look_for(l, x)=}.")
    print(f"{x * 3} in position: {look_for(l, x * 3)=}.")
    print(f"{l} sorted: {sort(l)=}.")
end
