class Glasses:
    """
    Creates a class that contains attributes about glasses. It contains the concept of a glasses
    """

    #Creates a constructor to then assign attributes to a class
    def __init__(self, blueLightFilter, thickness, frames, lens, shape):
        """
        Assigns attributes to the instance

        Attributes:
            self -> this instance
            blueLightFilter -> does the glasses have blue light filter?
            thickness -> how thick are the glasses' lenses?
            frames -> what type of frame is used?
            lens -> what type of lens is used?
            shape -> what is the shape of the glasses?
        """

        #Initializes the attributes by setting instance variables to the constructor variables
        self.blueLightFilter = blueLightFilter
        self.thickness = thickness
        self.frames = frames
        self.lens = lens
        self.shape = shape
