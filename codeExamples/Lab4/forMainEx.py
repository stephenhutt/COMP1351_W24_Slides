def testForLoop():
    for i in range(10):
        # These three prints do the same thing 
        print(f"{i} doubled is {i*2}")
        print(i, "doubled is", i*2)
        print(str(i) + " doubled is " + str(i*2))


if __name__ == "__main__":
    testForLoop()