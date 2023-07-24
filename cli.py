import py_cui       # Pour l'interface
import time         # Pour le loading popup
import threading    # Pour le loading popup
import os           # Pour le file manager 
from createfolder import *


###############################################################################################
#                                                                                             #                                        
#   CREATION D'APPLICATION D'UTILITAIRES DEVOPS DE GESTION DE FICHIERS PAR IMAGINE SOFTWARE   #
#                                                                                             #
#   Team : Chayma, Nicolas, Xavier, Lucas, Mohamed, Hachem, Nadir, Sebastien, Sacia, Hugo,    #
#          Vincent, Myreille, Devaki                                                          #
###############################################################################################


class Menu:

    def __init__(self, master):
        
        self.master = master  # On définit la fenêtre principale     

################################################
# CREATION DU MENU

# Création des boutons du menu principal    
    
        self.show_menu_popup = self.master.add_button('Files Manager', 0,0, command = self.show_menu_files_manager)
        self.show_menu_popup = self.master.add_button('Versionning', 0,1, command = self.show_menu_versionning)
        self.show_menu_popup = self.master.add_button('Security', 0,2, command = self.show_menu_security)
        self.show_menu_popup = self.master.add_button('Settings', 1,0, command = self.show_menu_settings)
        self.show_menu_popup = self.master.add_button('Credits', 1,1, command = self.show_menu_credits)
        self.show_menu_popup = self.master.add_button('EXIT', 1,2, command = self.show_exit)

# Création des menus déroulants pour chaque bouton du menu principal
    
    def show_menu_files_manager(self):
        """ Opens scroll menu for files operations """
        # Affiche un menu déroulant avec les choix suivants et appelle la fonction correspondante
        menu_choices = ['one', 'two', 'tree']
        self.master.show_menu_popup('Files Manager', menu_choices, self.show_files_manager_fonctions)
    
    def show_menu_versionning(self):
        """ Opens scroll menu for versionning operations """
        # Affiche un menu déroulant avec les choix suivants et appelle la fonction correspondante 
        menu_choices = ['one', 'two', 'tree']
        self.master.show_menu_popup('Versionning', menu_choices, self.show_versionning_fonctions)

    def show_menu_security(self):
        """ Opens scroll menu for security operations """
        # Affiche un menu déroulant avec les choix suivants et appelle la fonction correspondante 
        menu_choices = ['one', 'loading icon', 'loading bar']
        self.master.show_menu_popup('Security', menu_choices, self.show_security_fonctions)   
    
    def show_menu_settings(self):
        """ Opens scroll menu for settings """
        # Affiche un menu déroulant avec les choix suivants et appelle la fonction correspondante 
        menu_choices = ['Interface color', 'two', 'tree']
        self.master.show_menu_popup('Settings', menu_choices, self.show_settings_fonctions)
    
    def show_menu_credits(self):
        """ Display credits """
        # Affiche les crédits
        self.master.show_message_popup('This project was made by : Chayma, Nicolas, Xavier, Lucas, Mohamed,','Hachem, Nadir, Sebastien, Sacia, Hugo, Vincent, Myreille, Devaki')
    
# Création du bouton EXIT

    def show_exit(self):
        """ Displays a yes no popup asking if the user would like to quit """
        # Fonction qui affiche un popup pour quitter l'application avec les choix yes/no et appelle la fonction quit_cui
        self.master.show_yes_no_popup('Are you sure you want to quit?', self.quit_cui)

################################################


################################################
# FILES MANAGER MENU AND FONCTIONS

# MENU

    def show_files_manager_fonctions(self, fonction):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        if fonction == "one":
            self.master.show_message_popup('This is the first option','')
        elif fonction == "two":
            self.master.show_message_popup('This is the second option','')
        elif fonction == "tree":
            self.master.show_message_popup('This is the third option','')

# FONCTIONS
# Insérer ici les fonctions pour le menu files manager

################################################

    
################################################
# VERSIONNING MENU AND FONCTIONS

# MENU

    def show_versionning_fonctions(self, fonction):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        if fonction == "one":
            self.master.show_message_popup('This is the first option','')
        elif fonction == "two":
            self.master.show_message_popup('This is the second option','')
        elif fonction == "tree":
            self.master.show_message_popup('This is the third option','')

# FONCTIONS
# Insérer ici les fonctions pour le menu versionning

################################################


################################################
# SECURITY MENU AND FONCTIONS

# MENU

    def show_security_fonctions(self, fonction):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        if fonction == "one":
            self.master.show_message_popup('This is the first option','')
        elif fonction == "loading icon":
            self.show_loading_icon()
        elif fonction == "loading bar":
            self.show_loading_bar()

# FONCTIONS
# Insérer ici les fonctions pour le menu security


################################################


################################################
# SETTINGS MENU AND FONCTIONS

# MENU

    def show_settings_fonctions(self, fonction):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        if fonction == "Interface color":
            self.show_color_choices()
        elif fonction == "two":
            self.master.show_message_popup('This is the second option','')
        elif fonction == "tree":
            self.master.show_message_popup('This is the third option','')

# FONCTIONS

# Fonction de changement de couleur des boutons

    def change_button_color(self, new_color):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        color = py_cui.WHITE_ON_BLACK
        if new_color == "RED":
            color = py_cui.RED_ON_BLACK
        elif new_color == "CYAN":
            color = py_cui.CYAN_ON_BLACK
        elif new_color == "MAGENTA":
            color = py_cui.MAGENTA_ON_BLACK
        for key in self.master.get_widgets().keys():
            if isinstance(self.master.get_widgets()[key], py_cui.widgets.Button):
                self.master.get_widgets()[key].set_color(color)

    def show_color_choices(self):
        """ Opens scroll menu for settings """
        # Affiche un menu déroulant avec les choix suivants et appelle la fonction correspondante 
        menu_choices = ['RED', 'CYAN', 'MAGENTA']
        self.master.show_menu_popup('Interface color', menu_choices, self.change_button_color)

################################################


################################################
# COMPLEMENTARY FONCTIONS

# Insérer ici les fonctions complémentaires

# Fonction pour quitter l'application

    def quit_cui(self, to_quit):
        # Cette fonction prend le paramètre to_quit qui est un booleen qui permet de quitter l'application
        if to_quit:
            exit()
        else:
            self.master.show_message_popup('Cancelled', 'The quit operation was cancelled.')

# Fonctions de chargement

    def show_loading_icon(self):
        """ Function that shows the usage for spwaning a loading icon popup """
        # Affiche un popup avec un loading icon et appelle la fonction long_operation
        self.master.show_loading_icon_popup('Please Wait', 'Loading')
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()


    def show_loading_bar(self):
        """ Function that shows the usage for spawning a loading bar popup """
        # Affiche un popup avec un loading bar et appelle la fonction long_operation
        self.master.show_loading_bar_popup('Incrementing a counter...', 100)
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()


    def long_operation(self):
        """ A simple function that demonstrates a long callback operation performed while loading popup is open """
        # Fonction qui simule une opération longue et qui incrémente un compteur
        counter = 0
        for i in range(0, 100):
            time.sleep(0.1)
            counter= counter +1
            self.master.status_bar.set_text(str(counter))
            # Quand la fonction show_loading_bar est appelée, elle appelle cette fonction qui incrémente un compteur
            self.master.increment_loading_bar()
        # Stoppe le loading popup
        self.master.stop_loading_popup()

################################################


################################################
# DEMARRAGE DE L'INTERFACE

# Inititalisation de l'interface, de la fenêtre et des boutons, passage dans un wrapper et lancement de l'interface

root = py_cui.PyCUI(2, 3)
root.set_title('Imagine Software')
s = Menu(root)
root.start()

################################################