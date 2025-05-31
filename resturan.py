from datetime import datetime as dt

class resturan:
    def __init__(self, title, group, cook_days):
        self.title = title
        self.group = group
        self.cook_days = cook_days
        self.quantity = 0

    def set_quantity(self, amount):
        self.quantity = amount

    def is_available_today(self):
        return dt.now().strftime('%A') in self.cook_days

class Worker:
    def __init__(self, name, department):
        self.full_name = name
        self.section = department
        self.leave = False

    def apply_leave(self):
        self.leave = True

    def leave_status(self):
        status = 'dar morakhasi' if self.leave else 'mashghol'
        return f"{self.full_name} ({self.section}) - {status}"

class System:
    def __init__(self):
        self.resturanes = {}
        self.workers = []

    def insert_resturan(self, resturan, stock):
        resturan.set_quantity(stock)
        self.resturanes[resturan.title] = resturan

    def insert_worker(self, worker):
        self.workers.append(worker)

    def list_workers(self):
        for worker in self.workers:
            print(worker.leave_status())

    def list_menu(self):
        for resturan in self.resturanes.values():
            print(f"{resturan.title} ({resturan.group}) - pokht: {', '.join(resturan.cook_days)}")

    def today_resturanes(self):
        today = dt.now().strftime('%A')
        available = [resturan.title for resturan in self.resturanes.values() if resturan.is_available_today()]
        message = (
            f"emroz ({today}) ghabele tahye: {', '.join(available)}"
            if available else
            f"emroz ({today}) hich ghazayi pokhte nemishavad."
        )
        print(message)
        return available

    def make_order(self, resturan_name, count):
        resturan = self.resturanes.get(resturan_name)
        if not resturan:
            print("in ghaza ra nadarim.")
            return
        if not resturan.is_available_today():
            print(f"{resturan.title} emroz pokhte nemishavad. pokht dar: {', '.join(resturan.cook_days)}")
            return
        if resturan.quantity < count:
            print(f"mojodi kafi nist ({resturan.quantity} baghi mandeh)")
            return
        resturan.quantity -= count
        print(f"sefaresh {resturan.title} ba tedade {count} anjam shod. baghi mandeh: {resturan.quantity}")

if __name__ == "__main__":
    app = System()

    iranian = ['adas polo', 'baghali polo', 'morgh', 'khorake lobia', 'abgosht', 'kofteh', 'tahchin']
    international = ['chiz berger', 'ratatoyi', 'lazania', 'chicken kari', 'nodel', 'choros', 'soshi']
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for i, day in enumerate(days):
        app.insert_resturan(resturan(iranian[i], 'irani', [day]), 8)
        app.insert_resturan(resturan(international[i], 'beynolmelali', [day]), 8)

    app.insert_worker(Worker("reza", "basteh bandi"))
    app.insert_worker(Worker("negar", "pokht"))
    app.insert_worker(Worker("yousef", "tahvil"))
    app.workers[0].apply_leave()

    print("employee:")
    app.list_workers()

    print("\n menu kamel:")
    app.list_menu()

    print("\n ghaza haye emroz:")
    today_menu = app.today_resturanes()

    if today_menu:
        app.make_order(today_menu[0], 1)

    for name in app.resturanes:
        if name not in today_menu:
            app.make_order(name, 1)
            break