import view
import model


def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'Exit':
            break
        elif student not in journal:
            view.not_name()
        else:
            while True:
                mark = int(view.what_mark())
                if mark > 5 or mark < 1:
                    view.mark_par()
                else:
                    model.student_mark(student, mark)
                    break
    model.save_file()
