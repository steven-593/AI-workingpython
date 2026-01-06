import tkinter as tk
from tkinter import messagebox
import socket
import threading

# =============== CONFIGURACIÓN PARA OTRA COMPUTADORA ===============
SERVER_IP   = "172.17.130.95"   # ← TU IP REAL (la del portátil con Docker)
SERVER_PORT = 5001              # ← Puerto que usas en Docker
# ===================================================================

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Concurrente - Cliente")
        self.root.geometry("420x500")
        self.root.configure(bg="#f0f2f5")

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Conectando al servidor...")
        self.client_socket = None

        self.create_widgets()
        self.connect_to_server()

    def create_widgets(self):
        tk.Label(self.root, text="Calculadora Concurrente", font=("Arial", 20, "bold"), bg="#f0f2f5", fg="#2c3e50").pack(pady=20)

        # Resultado
        res_frame = tk.LabelFrame(self.root, text=" Resultado ", font=("Arial", 12, "bold"), bg="#f0f2f5")
        res_frame.pack(pady=10, padx=30, fill="x")
        tk.Entry(res_frame, textvariable=self.result_var, state="readonly", font=("Courier", 18, "bold"),
                 justify="center", readonlybackground="#1a1a2e", fg="#00ff9d").pack(pady=12, fill="x")

        # Entradas
        inputs = tk.Frame(self.root, bg="#f0f2f5")
        inputs.pack(pady=15)
        tk.Label(inputs, text="Número 1:", bg="#f0f2f5", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=8, sticky="e")
        tk.Entry(inputs, textvariable=self.num1_var, width=15, font=("Arial", 12), justify="center").grid(row=0, column=1, padx=10)
        tk.Label(inputs, text="Número 2:", bg="#f0f2f5", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
        tk.Entry(inputs, textvariable=self.num2_var, width=15, font=("Arial", 12), justify="center").grid(row=1, column=1, padx=10)

        # Operaciones
        ops = tk.Frame(self.root, bg="#f0f2f5")
        ops.pack(pady=10)
        self.operation = tk.StringVar(value="add")
        for i, (text, val, color) in enumerate([("Sumar", "add", "#4CAF50"), ("Restar", "sub", "#2196F3"),
                                                ("Multiplicar", "mul", "#FF9800"), ("Dividir", "div", "#9C27B0")]):
            tk.Radiobutton(ops, text=text, variable=self.operation, value=val, bg=color, fg="white",
                           font=("Arial", 11, "bold"), width=12).grid(row=i//2, column=i%2, padx=10, pady=5)

        tk.Button(self.root, text="CALCULAR", command=self.send_calculation,
                  bg="#388E3C", fg="white", font=("Arial", 14, "bold"), pady=10).pack(pady=20)
        tk.Button(self.root, text="Salir", command=self.on_closing,
                  bg="#f44336", fg="white", font=("Arial", 10), pady=6).pack()

    def connect_to_server(self):
        def conectar():
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((SERVER_IP, SERVER_PORT))
                self.result_var.set("¡Conectado al servidor!")
            except Exception as e:
                self.result_var.set("Error: Sin conexión")
                messagebox.showerror("Error de conexión", f"No se pudo conectar a {SERVER_IP}:{SERVER_PORT}\n\n{e}")
        threading.Thread(target=conectar, daemon=True).start()

    def send_calculation(self):
        try:
            n1 = float(self.num1_var.get())
            n2 = float(self.num2_var.get())
        except:
            self.result_var.set("Números inválidos")
            return

        request = f"{n1},{n2},{self.operation.get()}"

        def enviar():
            try:
                self.client_socket.send(request.encode('utf-8'))
                resp = self.client_socket.recv(1024).decode('utf-8').strip()
                if resp.startswith("RESULT:"):
                    self.result_var.set(f"Resultado: {resp[7:]}")
                else:
                    self.result_var.set(resp.replace("ERROR:", "Error: "))
            except:
                self.result_var.set("Error: Conexión perdida")
        threading.Thread(target=enviar, daemon=True).start()

    def on_closing(self):
        try:
            if self.client_socket:
                self.client_socket.send(b"quit")
                self.client_socket.close()
        except: pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()