from math import cos


class UpperBoundsFinder(object):
    def __init__(self, user_provided_data):
        """
        Initially user will provide lattitude/altitude and radius from the given point
        Ths class will provide all the points in the length of the circle
        :param user_provided_data: will be dicionary with keys: user_lon, user_lat, given_radius
        """
        self.user_data = user_provided_data

    @staticmethod
    def find_points_on_the_circle(user_lon: float, user_lat: float, provided_radius: float) -> list:
        """
        :param user_lon: user longitude cordinate
        :param user_lat: user latitude cordinate
        :param provided_radius: provided raduis with kilometer
        :return:
        """
        points_cordinates = []
        for i in range(360):
            range_lat = user_lat + provided_radius * cos(i)
            range_lon = user_lon + provided_radius * cos(i)
            points_cordinates.append({'range_lat': range_lat, 'range_lon': range_lon})
        return points_cordinates

    def generate_border_cordinates(self) -> list:
        user_lon = self.user_data.get('user_lon')
        user_lat = self.user_data.get('user_lat')
        provided_radius = self.user_data.get('provided_radius')
        all_points_cordinates = self.find_points_on_the_circle(user_lon, user_lat, provided_radius)
        return all_points_cordinates