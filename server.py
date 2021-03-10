import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator
import calculator

# create a class to define the server functions, derived from calculator_pb2_grpc.CalculatorServicer
class CalcuatorServicer(calculator_pb2_grpc.CalculatorServicer):
    """
    calculator.square_root is exposed here
    the request and response are of the data type calculator_pb2.Number
    """
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

def serve():
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # this creates a new server using threads

    # use the generated function add_CalculatorServicer_to_server to add the defined class tot he server
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalcuatorServicer(), server) # in this case we pass in the constructor of CalculatorServicer

    # listen on port 50051
    print('Starting server. Listening on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep it alive
    # try:
    #     while True:
    #         time.sleep(86400)
    # except KeyboardInterrupt:
    #     server.stop(0)

    # or try wait_for_termination
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

