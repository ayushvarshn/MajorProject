from iot import InternetOfThings
import multiprocessing


dev1 = InternetOfThings(end='', token='')
dev2 = InternetOfThings(end='', token='')


p1 = multiprocessing.Process(target=dev1.start)
p2 = multiprocessing.Process(target=dev2.start)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()

