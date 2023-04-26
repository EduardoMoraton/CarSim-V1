from car import Car


class Population:
    cars = []
    matting_pool = []
    max_fit = 0

    def __init__(self, pop_size, start_x, start_y, steps, reward_dots):
        for i in range(pop_size):
            self.cars.append(Car((start_x,start_y), steps, reward_dots))

    def evaluate(self):
        self.max_fit = 0
        for car in self.cars:
            car.calc_fitness()
        print("Fitness calculado")
        for car in self.cars:
            if car.fitness > max_fit:
                max_fit = car.fitness
        for car in self.cars:
            car.fitness /= self.max_fit
    def selection(self):
        for car in 
