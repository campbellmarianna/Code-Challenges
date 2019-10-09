# public static void printPairs(int[] array) {
#     for (int i= 0; i < array.length; i++) {
#       for (int j = 0; j < array.length; j++) {
#       System.out.println(array[i] + "," + array[j]);
#       }
#     }
#   }


def printPairs(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print("{}, {}".format(arr[i], arr[j]))


printPairs([1, 2, 3, 4, 5, 6, 7, 8])
