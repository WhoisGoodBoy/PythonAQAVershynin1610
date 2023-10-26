from lesson19.sun_singleton import singleton


@singleton
class Sun:
    def __init__(self, mass, brightness):
        self.mass = mass
        self.brightness = brightness


sun1 = Sun('wery big', 'wery bright')
sun2 = Sun('smol', 'not so bright')
print()