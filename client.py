import time
import sys
import threading
import numpy as np
import requests

num_threads = 100


def send_request(host, port, data):
    res = requests.post("http://{}:{}/predict".format(host, port), json=data)
    return res.json()


if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])
    data = {"input": np.random.rand(1, 300).tolist()}
    
    start_time = time.time()
    
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=send_request, args=(host, port ,data))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    
    print("{:.6f}s for processing {} requests.".format(time.time() - start_time, num_threads))
