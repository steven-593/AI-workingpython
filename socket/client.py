import tkinter as tk
from tkinter import messagebox
import socket
import threading

# === CONFIGURACIÓN ===
SERVER_IP = "172.18.0.1"  # ⚠️ ¡Cambia esto por la IP real del servidor!
SERVER_PORT = 5000

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculadora Concurrente - Cliente")
        self.root.geometry("420x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")

        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Esperando operación...")

        # Socket
        self.client_socket = None

        # Construir interfaz
        self.create_widgets()
        self.connect_to_server()

    def create_widgets(self):
        # === Título ===
        title = tk.Label(
            self.root,
            text="🧮 Calculadora Concurrente",
            font=("Helvetica", 18, "bold"),
            bg="#f0f2f5",
            fg="#2c3e50"
        )
        title.pack(pady=(15, 5))

        # === Pantalla de Resultado (AHORA ARRIBA) ===
        result_frame = tk.LabelFrame(
            self.root,
            text=" Pantalla de Resultado ",
            font=("Helvetica", 12, "bold"),
            fg="#555",
            bg="#f0f2f5",
            bd=2,
            relief="groove"
        )
        result_frame.pack(pady=(5, 15), padx=30, fill="x")

        self.result_display = tk.Entry(
            result_frame,
            textvariable=self.result_var,
            font=("Courier New", 16, "bold"),
            justify="center",
            state="readonly",
            readonlybackground="#1e2a38",
            fg="#00ff9d",
            relief="flat",
            bd=0,
            highlightthickness=0
        )
        self.result_display.pack(padx=10, pady=10, fill="x")

        # === Marco de entradas (debajo del resultado) ===
        input_frame = tk.Frame(self.root, bg="#f0f2f5")
        input_frame.pack(pady=10)

        # Número 1
        tk.Label(input_frame, text="Número 1:", font=("Helvetica", 12), bg="#f0f2f5").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        num1_entry = tk.Entry(input_frame, textvariable=self.num1_var, font=("Helvetica", 14), width=12, justify="center", relief="solid", bd=1)
        num1_entry.grid(row=0, column=1, padx=10, pady=8)

        # Número 2
        tk.Label(input_frame, text="Número 2:", font=("Helvetica", 12), bg="#f0f2f5").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        num2_entry = tk.Entry(input_frame, textvariable=self.num2_var, font=("Helvetica", 14), width=12, justify="center", relief="solid", bd=1)
        num2_entry.grid(row=1, column=1, padx=10, pady=8)

        # === Botones de operación en dos filas ===
        op_frame = tk.Frame(self.root, bg="#f0f2f5")
        op_frame.pack(pady=15)

        self.operation = tk.StringVar(value="add")

        # Primera fila: Suma y Resta
        add_btn = tk.Radiobutton(
            op_frame,
            text="➕ Sumar",
            variable=self.operation,
            value="add",
            indicatoron=0,
            width=14,
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            selectcolor="#4CAF50",
            activebackground="#45a049",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        add_btn.grid(row=0, column=0, padx=8, pady=5)

        sub_btn = tk.Radiobutton(
            op_frame,
            text="➖ Restar",
            variable=self.operation,
            value="sub",
            indicatoron=0,
            width=14,
            font=("Helvetica", 12, "bold"),
            bg="#2196F3",
            fg="white",
            selectcolor="#2196F3",
            activebackground="#1976D2",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        sub_btn.grid(row=0, column=1, padx=8, pady=5)

        # Segunda fila: Multiplicación y División
        mul_btn = tk.Radiobutton(
            op_frame,
            text="✖️ Multiplicar",
            variable=self.operation,
            value="mul",
            indicatoron=0,
            width=14,
            font=("Helvetica", 12, "bold"),
            bg="#FF9800",
            fg="white",
            selectcolor="#FF9800",
            activebackground="#F57C00",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        mul_btn.grid(row=1, column=0, padx=8, pady=5)

        div_btn = tk.Radiobutton(
            op_frame,
            text="➗ Dividir",
            variable=self.operation,
            value="div",
            indicatoron=0,
            width=14,
            font=("Helvetica", 12, "bold"),
            bg="#9C27B0",
            fg="white",
            selectcolor="#9C27B0",
            activebackground="#7B1FA2",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=5,
            pady=8
        )
        div_btn.grid(row=1, column=1, padx=8, pady=5)

        # === Botón Calcular ===
        calc_btn = tk.Button(
            self.root,
            text="🚀 Calcular",
            command=self.send_calculation,
            font=("Helvetica", 13, "bold"),
            bg="#388E3C",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground="#2E7D32"
        )
        calc_btn.pack(pady=12)

        # === Botón Salir ===
        exit_btn = tk.Button(
            self.root,
            text="❌ Salir",
            command=self.on_closing,
            font=("Helvetica", 10),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2",
            activebackground="#d32f2f"
        )
        exit_btn.pack(pady=5)

    def connect_to_server(self):
        """Conecta al servidor en segundo plano."""
        def connect():
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((SERVER_IP, SERVER_PORT))
                self.update_result("✅ Conectado al servidor")
            except Exception as e:
                self.update_result("❌ Error: Sin conexión")
                messagebox.showerror(
                    "Error de conexión",
                    f"No se pudo conectar al servidor en {SERVER_IP}:{SERVER_PORT}\n\n"
                    f"Asegúrate de que:\n"
                    f"• El servidor esté activo\n"
                    f"• La IP sea correcta\n"
                    f"• El firewall permita la conexión\n\n"
                    f"Error: {e}"
                )
                self.root.after(2000, self.root.quit)

        threading.Thread(target=connect, daemon=True).start()

    def update_result(self, text):
        """Actualiza el display de resultado de forma segura."""
        self.result_var.set(text)

    def send_calculation(self):
        """Envía la operación al servidor."""
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
        except ValueError:
            self.update_result("⚠️ Ingresa números válidos")
            return

        op = self.operation.get()
        request = f"{num1},{num2},{op}"

        def communicate():
            try:
                if not self.client_socket:
                    raise Exception("Socket no inicializado")
                self.client_socket.send(request.encode('utf-8'))
                response = self.client_socket.recv(1024).decode('utf-8').strip()

                if response.startswith("RESULT:"):
                    result = response.split(":", 1)[1]
                    self.update_result(f"= {result}")
                elif response.startswith("ERROR:"):
                    error_msg = response.split(":", 1)[1]
                    self.update_result(f"❌ {error_msg}")
                else:
                    self.update_result("⚠️ Respuesta no válida")

            except Exception as e:
                self.update_result("❌ Error de red")
                messagebox.showerror("Error", f"Fallo en la comunicación:\n{e}")
                self.on_closing()

        threading.Thread(target=communicate, daemon=True).start()

    def on_closing(self):
        """Cierra la conexión y la ventana."""
        try:
            if self.client_socket:
                self.client_socket.send(b"quit")
                self.client_socket.close()
        except:
            pass
        self.root.destroy()


# === PUNTO DE ENTRADA ===
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()