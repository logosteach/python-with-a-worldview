"""
Binary ↔ Decimal Converter (Tkinter)
Student practice tool with adjustable font size and responsive layout.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext


class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary ↔ Decimal Converter")
        self.root.geometry("980x800")
        self.root.minsize(860, 680)
        self.root.configure(bg="#f1f5f9")

        # Default font size (Regular = 16)
        self.font_size = 16

        # ---------- Styles ----------
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f1f5f9")
        style.configure("TLabelframe", background="#f1f5f9")
        style.configure("TLabelframe.Label", background="#f1f5f9",
                        foreground="#1e3a5f", font=("Segoe UI", 11, "bold"))

        # ---------- Header ----------
        header = tk.Frame(root, bg="#1e3a5f", height=78)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="Binary ↔ Decimal Converter",
                 bg="#1e3a5f", fg="white",
                 font=("Segoe UI", 18, "bold")).pack(pady=(10, 0))
        tk.Label(header, text="Practice converting positive integers and see how the math works",
                 bg="#1e3a5f", fg="#bfdbfe",
                 font=("Segoe UI", 10)).pack()

        # ---------- Font size bar ----------
        font_bar = tk.Frame(root, bg="#e2e8f0", pady=7)
        font_bar.pack(fill="x")

        tk.Label(font_bar, text="Text size:", bg="#e2e8f0",
                 fg="#334155", font=("Segoe UI", 10)).pack(side="left", padx=(15, 10))

        self.font_var = tk.StringVar(value="Regular")

        for text, size in [("Small", 12), ("Regular", 16), ("Large", 20)]:
            rb = tk.Radiobutton(
                font_bar, text=text, variable=self.font_var, value=text,
                command=lambda s=size: self.change_font_size(s),
                bg="#e2e8f0", fg="#1e293b",
                font=("Segoe UI", 10), selectcolor="#cbd5e1",
                activebackground="#e2e8f0"
            )
            rb.pack(side="left", padx=8)

        # ---------- Main container ----------
        main = ttk.Frame(root, padding=12)
        main.pack(fill="both", expand=True)

        # ===== Explanation =====
        self.exp_frame = ttk.LabelFrame(main, text="  How the Conversion Works  ", padding=10)
        self.exp_frame.pack(fill="x", pady=(0, 10))

        self.exp_label = tk.Label(
            self.exp_frame,
            text=(
                "Decimal → Binary:  Repeatedly divide the number by 2 and record the remainders.\n"
                "                   The remainders read from bottom to top form the binary number.\n"
                "                   Example: 13 → 1101₂\n\n"
                "Binary → Decimal:  Multiply each bit by its place value (powers of 2) and add the results.\n"
                "                   Place values from right to left: 1, 2, 4, 8, 16, 32, 64, 128…\n"
                "                   Example: 1101₂ = 8 + 4 + 0 + 1 = 13"
            ),
            justify="left", bg="white", fg="#334155",
            font=("Segoe UI", self.font_size), anchor="w"
        )
        self.exp_label.pack(fill="x")

        # ===== Two responsive panels (using grid) =====
        panels = ttk.Frame(main)
        panels.pack(fill="both", expand=True, pady=(0, 10))

        # Make both columns grow equally
        panels.columnconfigure(0, weight=1, uniform="pane")
        panels.columnconfigure(1, weight=1, uniform="pane")
        panels.rowconfigure(0, weight=1)

        # --- Left pane: Decimal → Binary ---
        left = ttk.LabelFrame(panels, text="  Decimal → Binary  ", padding=10)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        self.dec_label = tk.Label(left, text="Enter a positive integer:",
                                  bg="white", fg="#475569",
                                  font=("Segoe UI", self.font_size - 2))
        self.dec_label.pack(anchor="w")

        self.dec_entry = ttk.Entry(left, font=("Segoe UI", self.font_size))
        self.dec_entry.pack(fill="x", pady=(4, 8))
        self.dec_entry.bind("<Return>", lambda e: self.convert_dec_to_bin())

        self.dec_button = ttk.Button(left, text="Convert to Binary",
                                     command=self.convert_dec_to_bin)
        self.dec_button.pack(fill="x", pady=(0, 8))

        self.dec_result = scrolledtext.ScrolledText(
            left, height=12, font=("Consolas", self.font_size),
            wrap="word", state="disabled", bg="#f8fafc", relief="flat"
        )
        self.dec_result.pack(fill="both", expand=True)

        # --- Right pane: Binary → Decimal ---
        right = ttk.LabelFrame(panels, text="  Binary → Decimal  ", padding=10)
        right.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        self.bin_label = tk.Label(right, text="Enter a binary number (0s and 1s only):",
                                  bg="white", fg="#475569",
                                  font=("Segoe UI", self.font_size - 2))
        self.bin_label.pack(anchor="w")

        self.bin_entry = ttk.Entry(right, font=("Consolas", self.font_size))
        self.bin_entry.pack(fill="x", pady=(4, 8))
        self.bin_entry.bind("<Return>", lambda e: self.convert_bin_to_dec())

        self.bin_button = ttk.Button(right, text="Convert to Decimal",
                                     command=self.convert_bin_to_dec)
        self.bin_button.pack(fill="x", pady=(0, 8))

        self.bin_result = scrolledtext.ScrolledText(
            right, height=12, font=("Consolas", self.font_size),
            wrap="word", state="disabled", bg="#f8fafc", relief="flat"
        )
        self.bin_result.pack(fill="both", expand=True)

        # ===== Visual Place Values =====
        self.visual_frame = ttk.LabelFrame(main, text="  Visual Place Values  ", padding=8)
        self.visual_frame.pack(fill="x")

        self.visual_hint = tk.Label(
            self.visual_frame,
            text="This chart updates when you convert a binary number. Each column is a power of 2.",
            bg="white", fg="#64748b", font=("Segoe UI", 9)
        )
        self.visual_hint.pack(anchor="w", pady=(0, 6))

        self.place_frame = tk.Frame(self.visual_frame, bg="white")
        self.place_frame.pack(fill="x")

        self.show_placeholder()

        # Footer
        tk.Label(main, text="Tip: Try converting a number both ways to check your understanding.",
                 bg="#f1f5f9", fg="#64748b",
                 font=("Segoe UI", 9)).pack(pady=(8, 0))

    # ------------------------------------------------------------------
    def change_font_size(self, size):
        """Apply the chosen font size to all important widgets."""
        self.font_size = size

        # Explanation
        self.exp_label.config(font=("Segoe UI", size))

        # Labels above the entry boxes
        self.dec_label.config(font=("Segoe UI", max(10, size - 2)))
        self.bin_label.config(font=("Segoe UI", max(10, size - 2)))

        # Entry boxes
        self.dec_entry.config(font=("Segoe UI", size))
        self.bin_entry.config(font=("Consolas", size))

        # Result text areas
        self.dec_result.config(font=("Consolas", size))
        self.bin_result.config(font=("Consolas", size))

        # Re-draw place-value chart with new size
        if hasattr(self, "_last_details") and self._last_details:
            self.update_place_values(self._last_details)
        else:
            self.show_placeholder()

    # ------------------------------------------------------------------
    def show_placeholder(self):
        for widget in self.place_frame.winfo_children():
            widget.destroy()
        tk.Label(self.place_frame,
                 text="Convert a binary number to see the place values light up.",
                 bg="white", fg="#94a3b8",
                 font=("Segoe UI", max(11, self.font_size - 2))).pack(pady=8)
        self._last_details = None

    def update_place_values(self, details):
        self._last_details = details
        for widget in self.place_frame.winfo_children():
            widget.destroy()

        bit_size = max(14, self.font_size)
        label_size = max(9, self.font_size - 4)

        for d in details:
            is_on = d["bit"] == 1
            bg = "#dbeafe" if is_on else "#f1f5f9"
            border = "#3b82f6" if is_on else "#e2e8f0"
            bit_color = "#1d4ed8" if is_on else "#94a3b8"

            cell = tk.Frame(self.place_frame, bg=bg,
                            highlightbackground=border,
                            highlightthickness=2, padx=8, pady=6)
            cell.pack(side="left", padx=4)

            tk.Label(cell, text=f"2^{d['power']}", bg=bg, fg="#64748b",
                     font=("Segoe UI", label_size)).pack()
            tk.Label(cell, text=str(d["place_value"]), bg=bg, fg="#475569",
                     font=("Segoe UI", label_size, "bold")).pack()
            tk.Label(cell, text=str(d["bit"]), bg=bg, fg=bit_color,
                     font=("Consolas", bit_size, "bold")).pack()

    # ------------------------------------------------------------------
    def convert_dec_to_bin(self):
        raw = self.dec_entry.get().strip()
        self.dec_result.config(state="normal")
        self.dec_result.delete("1.0", tk.END)

        try:
            num = int(raw)
            if num < 0:
                raise ValueError
        except ValueError:
            self.dec_result.insert(tk.END, "Please enter a positive integer (0 or greater).")
            self.dec_result.config(state="disabled")
            return

        if num == 0:
            self.dec_result.insert(tk.END, "0₁₀ = 0₂\n")
            self.dec_result.config(state="disabled")
            return

        steps = []
        n = num
        binary = ""

        while n > 0:
            remainder = n % 2
            steps.append(f"{n} ÷ 2 = {n // 2}  remainder {remainder}")
            binary = str(remainder) + binary
            n = n // 2

        output = f"{num}₁₀ = {binary}₂\n\n"
        output += "Steps (remainders read from bottom to top):\n"
        output += "-" * 42 + "\n"
        for s in steps:
            output += s + "\n"

        self.dec_result.insert(tk.END, output)
        self.dec_result.config(state="disabled")

    # ------------------------------------------------------------------
    def convert_bin_to_dec(self):
        raw = self.bin_entry.get().strip()
        self.bin_result.config(state="normal")
        self.bin_result.delete("1.0", tk.END)

        if not raw or not all(c in "01" for c in raw):
            self.bin_result.insert(tk.END, "Please enter only 0s and 1s (example: 1101).")
            self.bin_result.config(state="disabled")
            self.show_placeholder()
            return

        details = []
        decimal = 0
        length = len(raw)

        for i, ch in enumerate(raw):
            bit = int(ch)
            power = length - 1 - i
            place_value = 2 ** power
            contribution = bit * place_value
            decimal += contribution
            details.append({
                "bit": bit,
                "power": power,
                "place_value": place_value,
                "contribution": contribution
            })

        parts = [str(d["place_value"]) if d["bit"] == 1 else "0" for d in details]
        addition = " + ".join(parts)

        output = f"{raw}₂ = {decimal}₁₀\n\n"
        output += f"{addition} = {decimal}\n\n"
        output += "Place value breakdown:\n"
        output += "-" * 42 + "\n"
        for d in details:
            output += f"  bit {d['bit']}  ×  2^{d['power']} ({d['place_value']})  =  {d['contribution']}\n"

        self.bin_result.insert(tk.END, output)
        self.bin_result.config(state="disabled")

        self.update_place_values(details)


# ------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()
    
# Copyright (c) 2026, LogosTeach - All Rights Reserved. 
