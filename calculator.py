"""
calculator
"""


class Calculator:

    DISCOUNT_2_DIFFERENT = .95
    DISCOUNT_3_DIFFERENT = .9
    DISCOUNT_4_DIFFERENT = .85
    DISCOUNT_5_DIFFERENT = .80
    DISCOUNT_6_DIFFERENT = .70
    DISCOUNT_7_DIFFERENT = .55

    def calculate(self, *args):
        price_book = 8
        num_equal, num_diff = self.num_equal_and_differents(args)

        price_equal = price_book * num_equal
        price_diff = 0.0
        # print('equal: ', num_equal, 'diff: ', num_diff)
        if num_diff > 1:
            discount = getattr(self, 'DISCOUNT_{}_DIFFERENT'.format(num_diff))
            price_diff = num_diff * price_book * discount
        return price_equal + price_diff

    @staticmethod
    def num_equal_and_differents(items):
        ids_diff = {it.id for it in items}
        different = len(ids_diff)
        if different == 1:
            different = 0
        equal = len(items) - different
        return equal, different


