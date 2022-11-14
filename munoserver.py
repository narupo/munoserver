import socket
import time
import tkinter as tk
from threading import Thread


class MunoServer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('無能サーバー')
        self.geometry('400x300')

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH, pady=12, padx=12)

        self.label = tk.Label(self.main_frame, text='connecting 0.0.0.0:7777')
        self.label.pack(side=tk.TOP, fill=tk.X)

        self.listbox = tk.Listbox(self.main_frame)
        self.listbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', 7777))

        self.recv_worker_thread = Thread(target=self.recv_worker, daemon=True)
        self.recv_worker_thread.start()

    def recv_worker(self):
        while True:
            time.sleep(1)

            data, address = self.sock.recvfrom(1024)
            addr, port = address

            print(addr, port, data)
            line = f'{addr} {port} {data}'
            self.listbox.insert(tk.END, line)


MunoServer().mainloop()
