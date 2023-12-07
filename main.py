from logic import *



def main():
    application = QApplication([])
    window = Logic()
    window.setFixedSize(500, 400)
    window.show()
    application.exec()

    
    

if __name__ == '__main__':
    main()
