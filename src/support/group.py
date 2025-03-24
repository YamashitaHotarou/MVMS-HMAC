
class Group:
    # 选择一个256位的素数
    prime = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F  # 这是比特币使用的素数

    # 在素数循环群内进行运算
    @staticmethod
    def add_in_group(a, b):
        a = int(a, 16)
        b = int(b, 16)
        return  hex((a + b) % Group.prime)

    @staticmethod
    def subtract_in_group(a, b):
        a = int(a, 16)
        b = int(b, 16)
        return hex((a - b) % Group.prime)

    @staticmethod
    def multiply_in_group(a, b):
        a = int(a, 16)
        b = int(b, 16)
        return hex((a * b) % Group.prime)

    @staticmethod
    def divide_in_group(a, b):
        # 计算 b 在模 p 下的乘法逆元
        b_inv = pow(b, -1, Group.prime)
        return hex((a * b_inv) % Group.prime)