def get_window_id(name):
    import Xlib.display

    d = Xlib.display.Display()
    r = d.screen().root

    window_ids = r.get_full_property(
        d.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType
    ).value

    for window_id in window_ids:
        window = d.create_resource_object('window', window_id)
        if window.get_wm_name() == name:
            return window_id


def run_app(window_ids):
    from PyQt5.QtGui import QWindow
    from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QApplication, QPushButton

    app = QApplication([])
    main_widget = QWidget()
    layout = QGridLayout(main_widget)

    window = QWindow.fromWinId(window_ids[0])
    widget = QWidget.createWindowContainer(window)
    layout.addWidget(widget, 0, 0)

    window = QWindow.fromWinId(window_ids[1])
    widget = QWidget.createWindowContainer(window)
    layout.addWidget(widget, 0, 1)

    window = QWindow.fromWinId(window_ids[2])
    widget = QWidget.createWindowContainer(window)
    layout.addWidget(widget, 1, 0)

    window = QWindow.fromWinId(window_ids[3])
    widget = QWidget.createWindowContainer(window)
    layout.addWidget(widget, 1, 1)


    # button = QPushButton('Close')
    # button.clicked.connect(main_widget.close)
    # layout.addWidget(button)

    main_widget.show()
    app.exec_()


if __name__ == '__main__':
    window_ids = [get_window_id('Map'), get_window_id('Horizon Indicator'), get_window_id('Console'), get_window_id('xterm')]
    if window_ids:
        run_app(window_ids)
