def funct():
    import time
    time.sleep(3)
    book = "hello this programme has its own options"
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("the text is in the book")

done_1 = funct()
next(done_1)
done_1.send("has")
input("press any key")
done_1.send("its")
done_1.close()
# done_1.send("asdf")
