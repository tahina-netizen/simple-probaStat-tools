class Sample:
    """
    A sample (or population) is a collection of data about a characteristic of something.

    For example, the heigth of some people in at FooVille (in cm): 
    180, 165, 140, 202, 181, 195, 175, 170, 190, 170, 165, 164, 168, 189, 189, 190, 201. 

    Attributes:
        sample: (list<E>) the raw data of this sample, always sorted (increasingly)
    """

    def __init__(self, data=[]):
        """
        create a new sample with no data (data will be added later).
        :param sample: (list) data of this sample.
        """
        self.sample = sample

    def empirical_mean(self):
        """
        :return: (float) empirical mean for this sample
        """
        return sum(sample) / len(sample)

    def median(self):
        """
        :return: (float) median of the given sample data
        """
        length = len(self.sample)
        if length % 2 == 0:
            return (self.sample[length//2 - 1] + self.sample[length // 2]) / 2
        else:
            return self.sample[length // 2]

    def variance(self):
        """
        :param sample: (list) raw data
        :return: (float) variance of this sample
        """
        
        avg = self.empirical_mean()
        retval = 0
        for x_k in self.sample:
            retval += x_k ** 2
        retval = retval / len(self.sample)
        retval = retval - avg ** 2

        return retval
            
    def standard_deviation(self):
        """
        :return: (float) standard deviation of this sample
        """
        return math.sqrt(self.variance())

    def mode(self):
        """
        :return: (E) the mode of this sample 
        """
        if self.sample.length == 0:
            raise Exception("empty sample, cannot compute")
        mod = self.sample[0]
        mod_count = 1
        crt = mod
        crt_count = mod_count

        # UNFINISHED !!!
        for i in range (1, self.sample.length):
            if self.sample[i] == mod:
                mod_count += 1
            else:
                crt = self.sample[i]
                crt_count = 1

        return mod
