class Food:
    def __init__(self, image, title, price):
        self.image = str(image)
        self.title = str(title)
        self.price = float(price)
        self.amount = 0