

WORKING_DIRECTORY='/home/alejo/Neuro/Metacognition/'
DATA_DIRECTORY=WORKING_DIRECTORY+'Data/Resultados Montessori/'

TOTAL_TRIAL_AMOUNT=114



MAX_SIZE = 100
SIZE_PATTERN = [96, 92, 88, 80, 75, 70, 60, 50]

def get_sizes(scale):
    sizes = [MAX_SIZE] + [int(max(1, min(1.5*(1-scale)*size, MAX_SIZE-1))) for size in SIZE_PATTERN]
    return sizes

