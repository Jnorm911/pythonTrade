import multiprocessing as mp
import page1
import page2

def main():
    for bot in('page1', 'page2'):
        p = mp.Process(target=lambda: __import__(bot))
        p.start() 

if __name__ == '__main__':
    while True:
        main()



    