from um import count


def main():
    test_count_0()
    test_count_marks()
    test_count_words()


def test_count_0():
    assert count("asdf") == 0

def test_count_marks():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_count_words():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1



if __name__ == "__main__":
    main()