import sys

class Cars:

    def read_car_makes():
        with open('car_makes.py', 'r') as car_makes:
            car_makes = (car_makes.read()).split("\n")
            return car_makes

    def read_car_models():
        with open('car_models.py', 'r') as car_models:
            car_models = (car_models.read()).split("\n")
            return car_models

    def create_car_dictionary():
        car_makes_and_models = dict()
        car_model_list = list()

        car_models = Cars.read_car_models()
        car_makes = Cars.read_car_makes()
        print(car_makes, car_models)

        for cars in car_models:
            if car_make[0] == cars[0]:
                car_model_list.append(cars)
        print(car_model_list)


if __name__ == "__main__":
    Cars.read_car_makes()




#------------------

# global file_name

# # if __name__ == "__main__":
# #     print("First name is {}".format(sys.argv[1]))
# #     print("Last name is {}".format(sys.argv[2]))

# def read_log():
#     """Reads from the log file"""
#     with open(file_name, 'r') as log_messages:
#         print(log_messages.read())


# def log(message, action):

#     with open(file_name, action) as logger:
#         timestamp = time()
#         logger.write("{0}: {1}\n".format(
#             datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
#             str(message)
#             ))

# if __name__ == "__main__":
#     try:
#         file_name = sys.argv[1]
#         action = sys.argv[2]

#         if action == 'r':
#             read_log()
#         elif action == 'w' or action == 'a':
#             log(' '.join(sys.argv[3:]), action)
#     except IndexError:
#         pass

# #logger will handle opening and closing the file for you
# #name of the file is the first argument (file_name)
