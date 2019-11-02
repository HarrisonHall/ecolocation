class Bat:
    """A simple example class"""
    class Bat(models.Model):
    Name = models.ForeignKey(Question, on_delete=models.CASCADE)
    Frequency = models.CharField(max_length=200)
    Proability = models.IntegerField(default=0)
    Image = models.ImageField
