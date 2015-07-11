def environment_stimulate(location):
    input_data = location
    return input_data


def initialise_location():
    location = 0
    return location


class Brain(object):

    def __init__(self):
        self.dynamic_brain_state = 1

    def process(self, input_data):
        if input_data > 5:
            self.dynamic_brain_state = -1
        elif input_data < -5:
            self.dynamic_brain_state = 1

        if self.dynamic_brain_state == 1:
            output_data = 1
        elif self.dynamic_brain_state == 0:
            output_data = 0
        else:
            output_data = -1
        return output_data


class Legs(object):

    def __init__(self, location):
        self.location = location

    def move(self, instruction_data):
        self.location = self.location + instruction_data
        return self.location


class Body(object):

    def __init__(self, location):
        self.brain = Brain()
        self.legs = Legs(location)

    def respond(self, input_data):
        output_data = self.brain.process(input_data)
        location = self.legs.move(output_data)
        return location

location = initialise_location()
body = Body(location)

while True:
    input_data = environment_stimulate(location)
    location = body.respond(input_data)
    print(location)
