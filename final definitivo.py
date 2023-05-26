import sys
import psycopg2 as psy
from psycopg2.extras import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prueba de consumo de drogas")
        self.setGeometry(100, 40, 500, 500)
        self.init_ui()
   
    def show_rules(self):
        # Crear widget de diálogo con las normas
        dialog = QDialog(self)
        dialog.setWindowTitle("Normas de la prueba")
        dialog.setFixedSize(400, 300)
        dialog_layout = QVBoxLayout()

        rules_label = QLabel()
        rules_label.setText("Normas de la prueba:\n\n1. Responde las preguntas de manera sincera y honesta.\n2. Solo se utilizarán tus datos para fines clinicos.\n3. No se guardará información personal identificable.\n4. Si tienes alguna duda, pregúntanos antes de comenzar la prueba.\n\n¿Estás listo para comenzar?")

        dialog_layout.addWidget(rules_label)

        ok_button = QPushButton("Aceptar")
        ok_button.clicked.connect(dialog.close)

        dialog_layout.addWidget(ok_button)

        dialog.setLayout(dialog_layout)

        # Mostrar el diálogo con las normas
        dialog.exec_()

    def init_ui(self):
        self.ID_group_box = QGroupBox("Datos necesarios")
        ID_data_layout = QVBoxLayout()
        self.ID_group_box.setStyleSheet('background-color: white')

        # Crear widgets para el ID
        self.ID_label = QLabel("ID:")
        self.ID_input = QLineEdit()
        self.ID_input.setClearButtonEnabled(True)

        ID_data_layout.addWidget(self.ID_label)
        ID_data_layout.addWidget(self.ID_input)

        self.ID_group_box.setLayout(ID_data_layout)

        # Crear caja para datos personales
        self.personal_data_group_box = QGroupBox("Datos personales")
        personal_data_layout = QVBoxLayout()
        self.personal_data_group_box.setStyleSheet('background-color: white')

        # Crear widgets para datos personales
        self.age_label = QLabel("Edad:")
        self.age_input = QComboBox()
        for age in range(100):
            agestr = str(age)
            self.age_input.addItem(agestr)

        self.gender_label = QLabel("Sexo:")
        sexo = ["mujer", "Hombre", "Otro"]
        self.gender_input = QComboBox()
        for gender in sexo:
            self.gender_input.addItem(gender)

        self.occupation_label = QLabel("Ocupación:")
        self.occupation_input = QLineEdit()
        self.occupation_input.setClearButtonEnabled(True)

        self.neighborhood_label = QLabel("Barrio:")
        self.neighborhood_input = QLineEdit()
        self.neighborhood_input.setClearButtonEnabled(True)

        self.clinic_label = QLabel("clinica:")
        self.clinic_input = QLineEdit()
        self.clinic_input.setClearButtonEnabled(True)

        self.social_class_label = QLabel("Estrato:")
        self.social_class_input = QComboBox()
        for i in range(1, 7):
            self.social_class_input.addItem(str(i))

        personal_data_layout.addWidget(self.age_label)
        personal_data_layout.addWidget(self.age_input)
        personal_data_layout.addWidget(self.gender_label)
        personal_data_layout.addWidget(self.gender_input)
        personal_data_layout.addWidget(self.occupation_label)
        personal_data_layout.addWidget(self.occupation_input)
        personal_data_layout.addWidget(self.neighborhood_label)
        personal_data_layout.addWidget(self.neighborhood_input)
        personal_data_layout.addWidget(self.clinic_label)
        personal_data_layout.addWidget(self.clinic_input)
        personal_data_layout.addWidget(self.social_class_label)
        personal_data_layout.addWidget(self.social_class_input)

        self.personal_data_group_box.setLayout(personal_data_layout)

        # Crear caja para selección de drogas
        self.drug_selection_group_box = QGroupBox(
            "A lo largo de su vida, ¿cual de las siguientes sustancias ha consumido alguna vez?  (SOLO PARA USOS NO-MÉDICOS)"
        )
        drug_selection_layout = QVBoxLayout()

        self.tabaco_checkbox = QCheckBox(
            "Tabaco (cigarrillos, cigarros habanos, tabaco de mascar, pipa, etc.)"
        )
        self.cocaine_checkbox = QCheckBox(
            "Cocaína (coca, farlopa, crack, base, etc.) "
        )
        self.inahalante_checkbox = QCheckBox(
            " Inhalantes (colas, gasolina/nafta, pegamento, etc.) "
        )
        self.Cannabis_checkbox = QCheckBox(
            "Cannabis (marihuana, costo, hierba, hashish, etc.)"
        )
        self.bebidas_alcoholicas_checkbox = QCheckBox(
            "Bebidas alcohólicas (cerveza, vino, licores, destilados, etc.)"
        )
        self.Anfetaminas_checkbox = QCheckBox(
            "Anfetaminas u otro tipo de estimulantes (speed, éxtasis, píldoras adelgazantes, etc.) "
        )
        self.Tranquilizantes_checkbox = QCheckBox(
            "Tranquilizantes o pastillas para dormir (valium/diazepam, Trankimazin/Alprazolam/Xanax, Orfidal/Lorazepam, Rohipnol, etc.)"
        )
        self.Alucinógenos_checkbox = QCheckBox(
            "Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) "
        )
        self.Opiáceos_checkbox = QCheckBox(
            "Opiáceos (heroína, metadona, codeína, morfina, dolantina/petidina, etc.)"
        )

        drug_selection_layout.addWidget(self.tabaco_checkbox)
        drug_selection_layout.addWidget(self.bebidas_alcoholicas_checkbox)
        drug_selection_layout.addWidget(self.cocaine_checkbox)
        drug_selection_layout.addWidget(self.inahalante_checkbox)
        drug_selection_layout.addWidget(self.Cannabis_checkbox)
        drug_selection_layout.addWidget(self.Anfetaminas_checkbox)
        drug_selection_layout.addWidget(self.Tranquilizantes_checkbox)
        drug_selection_layout.addWidget(self.Alucinógenos_checkbox)
        drug_selection_layout.addWidget(self.Opiáceos_checkbox)

        self.drug_selection_group_box.setLayout(drug_selection_layout)

        # Crear botón para iniciar prueba Y normas
        self.start_button = QPushButton("Iniciar prueba")
        self.start_button.clicked.connect(self.confirmacion)
        self.start_button.setStyleSheet("background-color: white")

        self.rules_button = QPushButton("Normas")
        self.rules_button.clicked.connect(self.show_rules)
        self.rules_button.setStyleSheet("background-color: white")

        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.ID_group_box)
        main_layout.addWidget(self.personal_data_group_box)
        main_layout.addWidget(self.drug_selection_group_box)
        main_layout.addWidget(self.rules_button)
        main_layout.addWidget(self.start_button)

        self.setLayout(main_layout)
        self.show()

    def confirmacion(self):
        # Obtener datos personales
        self.Id = self.ID_input.text()
        self.clinica = self.clinic_input.text()
        self.age = self.age_input.currentText()
        self.gender = self.gender_input.currentText()
        self.occupation = self.occupation_input.text()
        self.neighborhood = self.neighborhood_input.text()
        self.social_class = self.social_class_input.currentText()

        # Obtener drogas seleccionadas
        self.drugs_selected = []
        if self.tabaco_checkbox.isChecked():
            self.drugs_selected.append("Tabaco")
        if self.cocaine_checkbox.isChecked():
            self.drugs_selected.append("Cocaína")
        if self.inahalante_checkbox.isChecked():
            self.drugs_selected.append("Inhalantes")
        if self.bebidas_alcoholicas_checkbox.isChecked():
            self.drugs_selected.append("Bebidas alcohólicas")
        if self.Cannabis_checkbox.isChecked():
            self.drugs_selected.append("Cannabis")
        if self.Anfetaminas_checkbox.isChecked():
            self.drugs_selected.append("Anfetaminas")
        if self.Tranquilizantes_checkbox.isChecked():
            self.drugs_selected.append("Tranquilizantes o pastillas para dormir")
        if self.Alucinógenos_checkbox.isChecked():
            self.drugs_selected.append("Alucinógenos")
        if self.Opiáceos_checkbox.isChecked():
            self.drugs_selected.append("Opiáceos")

        print(self.drugs_selected)

        conn = psy.connect(dbname = 'ASSIST',
                        user= 'postgres',
                        password = 'Aldebran')
        cur = conn.cursor()
        cur.execute("INSERT INTO usuarios (sexo, edad, ocupacion, clinica, barrio, estrato) VALUES (%s, %s, %s, %s, %s, %s)",
        (self.gender, self.age, self.occupation, self.clinica, self.neighborhood, self.social_class))
        conn.commit()
        cur.close()
        conn.close()

        # iniciar prueba
        self.start_prueba()

    def start_prueba(self):

        # Crear widget de diálogo con las normas
        dialog = QDialog(self)
        dialog.setWindowTitle("Inicio de prueba")
        dialog.setFixedSize(1100, 300)
        self.dialog_layout = QVBoxLayout()

        self.texto_label = QLabel(self)

        self.texto_label.setGeometry(10, 10, 280, 120)

        # Crear un botón "Continuar"

        self.ok_button = QPushButton('Continuar', self)
        self.ok_button.setGeometry(100, 140, 100, 30)
        self.ok_button.clicked.connect(self.check_answers)
   
        

        self.questions = [
            {
                "question": "¿Con qué frecuencia ha consumido las sustancias que ha mencionado en los últimos tres meses, {}? ",
                "options": ["Nunca", "1 o 2 veces", "cada mes", "cada semana","a diario o casi a diario"],
                "correct_answers": ["Nunca","1 o 2 veces","cada mes","cada semana","a diario o casi a diario"],
                "scores": [0,2,3,4,6]  # Puntajes para respuestas correctas
            },
            {
                "question": "En los últimos tres meses, ¿con qué frecuencia ha tenido deseos fuertes o ansias de consumir (PRIMERA DROGA, SEGUNDA DROGA, ETC)? ",
                "options": ["Nunca", "1 o 2 veces", "cada mes", "cada semana","a diario o casi a diario"],
                "correct_answers": ["Nunca","1 o 2 veces","cada mes","cada semana","a diario o casi a diario"],
                "scores": [0,3,4,5,6]  # Puntajes para respuestas correctas
            },
            {
                "question": "En los últimos tres meses, ¿con qué frecuencia le ha llevado su consumo de (PRIMERA DROGA, SEGUNDA DROGA, ETC) a problemas de salud, sociales, legales o económicos? ",
                "options": ["Nunca", "1 o 2 veces", "cada mes", "cada semana","a diario o casi a diario"],
                "correct_answers": ["Nunca","1 o 2 veces","cada mes","cada semana","a diario o casi a diario"],
                "scores": [0,4,5,6,7]  # Puntajes para respuestas correctas
            },
            {
                "question": "En los últimos tres meses, ¿con qué frecuencia dejó de hacer lo que se esperaba de usted habitualmente por el consumo de (PRIMERA DROGA, SEGUNDA DROGA, ETC)?",
                "options": ["Nunca", "1 o 2 veces", "cada mes", "cada semana","a diario o casi a diario"],
                "correct_answers": ["Nunca","1 o 2 veces","cada mes","cada semana","a diario o casi a diario"],
                "scores": [0,5,6,7,8]  # Puntajes para respuestas correctas
            },
            {
                "question": "¿Un amigo, un familiar o alguien más alguna vezha mostrado preocupación por su consume de (PRIMERA DROGA, SEGUNDA DROGA, ETC)?",
                "options": ["no, nunca", "si, en los ultimos 3 meses", "si, pero no en los ultimos 3 meses","...","..."],
                "correct_answers": ["no, nunca", "si, en los ultimos 3 meses", "si, pero no en los ultimos 3 meses"],
                "scores": [0,6,3]  # Puntajes para respuestas correctas
            },
            {
                "question": "¿Ha intentado alguna vez controlar, reducir o dejar de consumir (PRIMERA DROGA, SEGUNDA DROGA, ETC) y no lo ha logrado?",
                "options": ["no, nunca", "si, en los ultimos 3 meses", "si, pero no en los ultimos 3 meses","...","..."],
                "correct_answers": ["no, nunca", "si, en los ultimos 3 meses", "si, pero no en los ultimos 3 meses"],
                "scores": [0,6,3]  # Puntajes para respuestas correctas
            }
        ]
        self.current_Drogas = 0
        self.current_question = 0
        self.scores = {} # Diccionario para almacenar los puntajes por drogas

        self.drogas_label = QLabel(self.drugs_selected[self.current_Drogas])
        self.dialog_layout.addWidget(self.drogas_label)

        self.question_label = QLabel(self.get_formatted_question())
        self.dialog_layout.addWidget(self.question_label)

        self.option_checkboxes = []
        for option in self.questions[self.current_question]["options"]:
            checkbox = QCheckBox(option)
            self.option_checkboxes.append(checkbox)
            self.dialog_layout.addWidget(checkbox)


          
        self.dialog_layout.addWidget(self.ok_button)
        
        dialog.setLayout(self.dialog_layout)

        # Mostrar el diálogo con las normas
        dialog.exec_()


    def get_formatted_question(self):
        Drogas = self.drugs_selected[self.current_Drogas]
        question = self.questions[self.current_question]["question"]
        return question.format(Drogas)

    def check_answers(self):
        selected_answers = []
        for checkbox in self.option_checkboxes:
            if checkbox.isChecked():
                selected_answers.append(checkbox.text())

        correct_answers = self.questions[self.current_question]["correct_answers"]
        scores = self.questions[self.current_question]["scores"]

        for answer in selected_answers:
            if answer in correct_answers:
                index = correct_answers.index(answer)
                score = scores[index]
                if self.current_Drogas in self.scores:
                    self.scores[self.current_Drogas] += score
                else:
                    self.scores[self.current_Drogas] = score

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.current_question = 0
            self.current_Drogas += 1
            if self.current_Drogas < len(self.drugs_selected):
                self.update_Drogas()
            else:
                self.show_result()

    def update_question(self):
        self.question_label.setText(self.get_formatted_question())
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            self.option_checkboxes[i].setText(option)
            self.option_checkboxes[i].setChecked(False)

    def update_Drogas(self):
        self.drogas_label.setText(self.drugs_selected[self.current_Drogas])
        self.update_question()

    def show_result(self):
        self.dialog_layout.removeWidget(self.drogas_label)
        self.drogas_label.deleteLater()
        self.dialog_layout.removeWidget(self.question_label)
        self.question_label.deleteLater()
        for checkbox in self.option_checkboxes:
            self.dialog_layout.removeWidget(checkbox)
            checkbox.deleteLater()

        result_label = QLabel("Resultados:")
        self.dialog_layout.addWidget(result_label)

        for Drogas, score in self.scores.items():
            drogas_label = QLabel("{}: {}".format(self.drugs_selected[Drogas], score))
            if score <= 3:
                resultados_label = QLabel("{}: {}".format(self.drugs_selected[Drogas],"sin intervencion, con nivel de riesgo bajo."))
                label = QLabel("UstedSu actual patrón de consumo representa un riesgo bajo sobre su salud y de otros problemas.")
                self.dialog_layout.addWidget(drogas_label)
                self.dialog_layout.addWidget(resultados_label)
                self.dialog_layout.addWidget(label)

                conn = psy.connect(dbname = 'ASSIST',
                        user= 'postgres',
                        password = 'Aldebran')
                cur = conn.cursor()
                cur.execute("INSERT INTO resultados (id_sustancia, puntuacion) VALUES (%s, %s)",
                (self.drugs_selected[Drogas],score))
                conn.commit()
                cur.close()
                conn.close()

            elif score > 3 and score < 26:
                resultados_label = QLabel("{}: {}".format(self.drugs_selected[Drogas],"Intervencion breve, con nivel de riesgo moderado. "))
                label = QLabel("Usted presenta riesgo para su salud y de otro tipos de problemas derivados de su actual patrón de consumo de sustancias.")
                self.dialog_layout.addWidget(drogas_label)
                self.dialog_layout.addWidget(resultados_label)
                self.dialog_layout.addWidget(label)

                conn = psy.connect(dbname = 'ASSIST',
                        user= 'postgres',
                        password = 'Aldebran')
                cur = conn.cursor()
                cur.execute("INSERT INTO resultados (id_sustancia, puntuacion) VALUES (%s, %s)",
                (self.drugs_selected[Drogas],score))
                conn.commit()
                cur.close()
                conn.close()
                
            elif score >= 27:
                resultados_label = QLabel("{}: {}".format(self.drugs_selected[Drogas],"Tratamiento mas intensivo, con nivel de riesgo alto."))
                label = QLabel("Usted presenta un riesgo elevado de experimentar problemas graves (de salud, sociales, económicos, legales, de pareja, ...) derivado de su patrón actual de consumo y probablemente sea dependiente.")
                self.dialog_layout.addWidget(drogas_label)
                self.dialog_layout.addWidget(resultados_label)
                self.dialog_layout.addWidget(label)
                conn = psy.connect(dbname = 'ASSIST',
                        user= 'postgres',
                        password = 'Aldebran')
                cur = conn.cursor()
                cur.execute("INSERT INTO resultados (id_sustancia, puntuacion) VALUES (%s, %s)",
                (self.drugs_selected[Drogas],score))
                conn.commit()
                cur.close()
                conn.close()
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
