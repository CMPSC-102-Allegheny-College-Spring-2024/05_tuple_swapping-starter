# TODO: Import all of the required type annotation classes 
# Hint: Modify the below into python code.
# from the "typing" library, import "any"
# from the "typing" library, import "Tuple"


# TODO: Repair all of the program defects near the TODO markers in the following source code
# TODO: You need to carefully review the TODO markers and then decide whether they are
# correct or incorrect. Ultimately, your program should produce the output described 
# in the README.md document.

def ordered_pair_swap(pair_one: Tuple[Any, Any], pair_two: Tuple[Any, Any]) -> Tuple[Tuple[Any, Any], Tuple[Any, Any]]:
    """Swap the contents of one ordered pair with another ordered pair."""
    # TODO: create the first tuple so that it contains the swapped contents of the second tuple
    swapped_one = (pair_two[0], pair_two[1]) # Hint: think about using the positional part of the code
    # TODO: create the second tuple so that it contains the swapped contents of the first tuple
    swapped_two = (pair_one[0], pair_one[1])
    # TODO: return the two tuples in the opposite order in which they were input
    return (swapped_two, swapped_one)


# TODO: create the two ordered pairs
# The first tuple should contain ("A", 1)
# The second tuple should contain ("B", 2)

# display the original tuple of ordered pairs
not_swapped_ordered_pairs = (first_ordered_pair, second_ordered_pair)
print(f"Original tuple of ordered pairs: {not_swapped_ordered_pairs}")

# perform the ordered pair swap
first_swapped_ordered_pair = ordered_pair_swap(first_ordered_pair, second_ordered_pair)
print(f"Swapped tuple of ordered pairs: {first_swapped_ordered_pair}")

# TODO: extract the ordered pairs from the returned tuple and display them
second_swapped_ordered_pair = ordered_pair_swap(first_swapped_ordered_pair[0], first_swapped_ordered_pair[1])
print(f"Swapped (again) tuple of ordered pairs: {second_swapped_ordered_pair}")

# TODO: Remember, make sure that the program produces expected output as described
# in the README.md document
