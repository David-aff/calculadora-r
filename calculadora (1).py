from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (360, 650)
Window.clearcolor = (0.08, 0.08, 0.08, 1)


class Calculadora(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.padding = 15
        self.spacing = 10

        # Lista para guardar historial
        self.historial = []

        # Pantalla principal
        self.pantalla = TextInput(
            text="",
            readonly=True,
            multiline=False,
            font_size=50,
            halign="right",
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=120
        )

        self.add_widget(self.pantalla)

        # Historial
        self.historial_texto = TextInput(
            text="Historial vacío",
            readonly=True,
            multiline=True,
            font_size=16,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(0, 1, 0, 1),
            size_hint_y=None,
            height=120
        )

        self.add_widget(self.historial_texto)

        botones = [
            ["CS", "C", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "%", "="]
        ]

        for fila in botones:

            contenedor = GridLayout(
                cols=4,
                spacing=10
            )

            for texto in fila:

                color = (0.25, 0.25, 0.25, 1)

                if texto in ["+", "-", "*", "/", "="]:
                    color = (1, 0.55, 0, 1)

                elif texto in ["C", "CS", "⌫", "%"]:
                    color = (0.45, 0.45, 0.45, 1)

                boton = Button(
                    text=texto,
                    font_size=28,
                    background_normal="",
                    background_color=color
                )

                boton.bind(on_press=self.presionar)

                contenedor.add_widget(boton)

            self.add_widget(contenedor)

    def actualizar_historial(self):

        if self.historial:
            self.historial_texto.text = "\n".join(self.historial)
        else:
            self.historial_texto.text = "Historial vacío"

    def presionar(self, boton):

        valor = boton.text

        if valor == "C":
            self.pantalla.text = ""

        elif valor == "CS":
            self.historial = []
            self.actualizar_historial()

        elif valor == "⌫":
            self.pantalla.text = self.pantalla.text[:-1]

        elif valor == "=":

            try:

                operacion = self.pantalla.text

                expresion = operacion.replace("%", "/100")

                resultado = str(eval(expresion))

                # Guardar en historial
                self.historial.append(f"{operacion} = {resultado}")

                # Mostrar resultado
                self.pantalla.text = resultado

                # Actualizar historial
                self.actualizar_historial()

            except:
                self.pantalla.text = "Error"

        else:
            self.pantalla.text += valor


class MiApp(App):

    def build(self):
        self.title = "Calculadora"
        return Calculadora()


MiApp().run()