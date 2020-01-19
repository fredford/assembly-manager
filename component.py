
class Component:

    def __init__(self, type_name):

        self.type = type_name
        self.sizes = []
        self.ratings = []
        self.material = ""
        self.features = []
        self.part_number = ""
        self.description = ""

    # Setting the TYPE of component
    def set_type(self, type_name):
        self.type = type_name

    # Getting the TYPE of component
    def get_type(self):
        return self.type

    # Adding a SIZE that the component is
    def add_size(self, size):
        self.sizes.append(size)
        self.sizes.sort()

    # Removing a SIZE that the component is
    def remove_size(self, size):
        if size in self.sizes:
            self.sizes.remove(size)
        else:
            print("WARNING: Size not found!")

    # Getting the SIZE of the component
    def get_sizes(self):
        return self.sizes

    # Adding a RATING of the component
    def add_rating(self, rating):
        self.ratings.append(rating)
        self.ratings.sort()

    # Removing a RATING of the component
    def remove_rating(self, rating):
        if rating in self.ratings:
            self.ratings.remove(rating)
        else:
            print("WARNING: Rating not found!")

    #Getting the RATING of the component
    def get_ratings(self):
        return self.ratings

    # Setting the MATERIAL used for the component
    def set_material(self, material):
        self.material = material

    # Getting the MATERIAL used for the component
    def get_material(self):
        return self.material

    # Adding a new FEATURE to the component
    def add_feature(self, feature):
        self.features.append(feature)
        self.features.sort()

    # Removing a FEATURE from the component
    def remove_feature(self, feature):
        if feature in self.features:
            self.features.remove(feature)
        else:
            print("WARNING: Feature not found!")

    # Getting the FEATURES on the component
    def get_features(self):
        return self.features

    # Setting PART NUMBER of the component
    def set_part_number(self, part_number):
        self.part_number = part_number

    # Getting PART NUMBER of the component
    def get_part_number(self):
        return self.part_number

    def update_description(self):
        self.description = self.type + ", "

        for count in range(len(self.sizes)):
            if count != len(self.sizes) - 1:
                if self.sizes[count][0] == '0':
                    self.description += self.sizes[count][1] + "\"/"
                else:
                    self.description += self.sizes[count] + "\"/"
            else:
                if self.sizes[-1][0] == '0':
                    self.description += self.sizes[-1][1] + "\", "
                else:
                    self.description += self.sizes[-1] + "\", "

        for count in range(len(self.ratings)):
            if count != len(self.ratings) - 1:
                self.description += self.ratings[count] + "/"
            else:
                self.description += self.ratings[-1] + ", "

        self.description += self.material

        for feature in self.features:
            self.description += ", " + feature

    def get_description(self):
        return self.description






