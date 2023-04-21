import flask

class Map:
    def __init__(self):
        #this is the map that shows all the surrounding area's electric car vehicle charging stations
        self.Larry = '<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d178903.0231394029!2d-94.31410684451964!3d45.522965959522146!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1selectric%20vehicle%20charging%20station!5e0!3m2!1sen!2sus!4v1682088186159!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


    #CLASS METHODS
    #this function opens up the map(displays the map in the webpage)
    def open(self):
        return self.Larry