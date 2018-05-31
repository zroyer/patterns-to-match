def best_match(patterns, path):
    """
    Returns the best matching pattern for each path.
    Handles the case where no pattern matches the path.
    """
    matches = get_ordered_matches(patterns, path)
    if not matches:
        return 'NO MATCH'
    return break_tie(matches, 0)


def break_tie(matches, index):
    """
    Starting at the first index of list of matches, recursively 'filter' out
    the matches that have a wildcard each index until there is one left.
    If there are remaining matches, call break_tie on the filtered matches on
    the next index.
    If there were no remaining matches, call break_tie on the unfiltered
    matches on the next index.
    If there is only 1 remaining pattern in the list of matches, there is no
    tie to break, so return it.
    """
    if len(matches) > 1:
        matches = [m for m in matches if m.split(',')[index] != '*'] or matches
        return break_tie(matches, index + 1)
    return matches[0]


def get_ordered_matches(patterns, path):
    """
    Appends all patterns that match the path into a list of tuples, with the
    pattern and the number of wildcards it contains as the tuple's respective
    values. After ordering the list with the lowest-count matching pattern(s)
    first, we return a filtered list with only these lowest-count matching
    pattern(s).
    """
    matching_patterns = []
    for pattern in patterns:
        if is_match(pattern, path):
            matching_patterns.append((pattern, pattern.count('*')))

    incremented_patterns = sorted(matching_patterns, key=lambda x: x[1])
    return [tup[0] for tup in incremented_patterns if
            tup[1] == incremented_patterns[0][1]]


def is_match(pattern, path):
    """
    A matching pattern is one where every index in the pattern must exactly
    match the corresponding index, in the path, as well as contain the same
    number of indices. A wildcard can match any string in the path.
    """
    pattern = pattern.split(',')
    if len(pattern) != len(path):
        return False
    for i in range(len(path)):
        if pattern[i] != '*' and pattern[i] != path[i]:
            return False
    return True


if __name__ == "__main__":
    num_patterns = int(raw_input())
    patterns = [raw_input() for n in range(num_patterns)]
    num_paths = int(raw_input())
    paths = [raw_input() for m in range(num_paths)]

    for path in paths:
        path = path.strip("/").split("/")
        print(best_match(patterns, path))
