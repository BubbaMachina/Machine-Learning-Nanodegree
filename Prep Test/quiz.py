"""Count words."""


def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    # FYI. I could have implemented a count solution using a dictionary .get method, but I opted in to
    # using a solution with higher Big O using sets and list

    words = s.split()

    count = 0

    top_n = list()

    word_bag = set()

    word_count_bag = set()

    for word in words:
        count = 0

        word = word.strip()

        # word_bag.add(word)

        # print word

        for word_loop in words:
            if word == word_loop:
                count += 1

        word_bag.add((count, word))

        word_count_bag.add(count)

    word_list = sorted(word_bag)

    word_count_list = sorted(word_count_bag)

    # print word_count_list

    word_sorting_list = list()

    for word_count in reversed(word_count_list):
        for word_sorted in word_list:
            # print "\n before \n"

            # print word_sorted , word_count

            if word_sorted[0] == word_count:
                # print word_sorted, word_count
                word_sorting_list.append(word_sorted)

    # print word_sorting_list

    for n in range(n):
        top_n.append((word_sorting_list[n][1], word_sorting_list[n][0]))

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
