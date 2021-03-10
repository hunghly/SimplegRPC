import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open the gRPC channel
channel = grpc.insecure_channel('localhost:50051') #creates an insecure channel to the server

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel) # I have to pass in the channel here

# create a valid request message
number = calculator_pb2.Number(value=16)
print(number.value)

# make the call
response = stub.SquareRoot(number)

print(response.value)