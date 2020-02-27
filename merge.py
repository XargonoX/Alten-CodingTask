import sys
from argparse import ArgumentParser
from builtins import IOError, input
import numpy


def firstintervalIncludesSecondintervalSmaler(firstInterval, secondInterval):
    return secondInterval.max() > firstInterval.min() and secondInterval.max() < firstInterval.max()

def firstintervalIncludesSecondintervalGreater(firstInterval, secondInterval):
    return secondInterval.min() > firstInterval.min() and secondInterval.min() < firstInterval.max()


def merge(intervalList):
    """
    merges a list of Intervals
    :param intervalList: list of tuples
    :return: a list of Intervals
    """
    resultList = [intervalList[0]]
    for inInterval in intervalList[1:]:
        for resInterval in resultList:
            if firstintervalIncludesSecondintervalSmaler(resInterval, inInterval):
                resInterval[0] = inInterval.min()
                break
            elif firstintervalIncludesSecondintervalGreater(resInterval, inInterval):
                resInterval[1] = inInterval.max()
                break

        else:
            resultList.append(inInterval)
    return resultList



def readIntervalsFromFile(filePath,dataType):
    """
    reads Intervals from the given file
    :param filePath: full path to file
    :return: list of tuples
    :type return: [numpy.ndarray]
    """
    return numpy.genfromtxt(filePath, delimiter=',', dtype=dataType)


def writeIntervalsToFile(outpuFilePath, data):
    """
    writes the given data into the given file
    :param outpuFilePath: full path to the File where the data should be stored
    :param data: data which should be written to the file
    :type data: ndarray
    """
    numpy.savetxt(outpuFilePath, data, fmt='%i', delimiter=',')

if __name__ == "__main__":
    # define available arguments
    parser = ArgumentParser()
    parser.add_argument("-i", "--inputFile", dest="inputFilePath",
                        help="path to input file", metavar="INPUTFILE")
    parser.add_argument("-o", "--outputFile", dest="outputFilePath",
                        help="path to output file", metavar="OUTPUTFILE")
    parser.add_argument("-t", "--type", dest="dataType",
                        help="used datatype (int or float)", metavar="DATATYPE")
    args = parser.parse_args()

    #try to read data from given Filepath. If read failed, ask for new Filepath.
    inputData = None
    filePath = args.inputFilePath
    while not inputData:
        try:
            inputData = readIntervalsFromFile(filePath, args.dataType)
        except IOError as e:
            print('Reading data from File failed, please input valid Path to Datafile: \n ->')
            filePath = input()

    resultData = merge(inputData)
    writeIntervalsToFile(args.outputFilePath, resultData)

    print('wrote result successful to: {}'.format(args.outputFilePath))

