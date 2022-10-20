import multt as model
import view

def button_click():
    value_a = view.get_value()  # получение данных
    value_b = view.get_value()
    model.init(value_a,value_b) # инициализация аргументов
    result = model.do_it()        # вычисление суммы
    view.view_data(result, 'mult')      # вывод значения