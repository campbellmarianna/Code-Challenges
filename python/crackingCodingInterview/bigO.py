# public static void printPairs(int[] array) {
#     for (int i= 0; i < array.length; i++) {
#       for (int j = 0; j < array.length; j++) {
#       System.out.println(array[i] + "," + array[j]);
#       }
#     }
#   }


# def printPairs(arr):
#     for i in range(0, len(arr)):
#         for j in range(0, len(arr)):
#             print("{}, {}".format(arr[i], arr[j]))


# printPairs([1, 2, 3, 4, 5, 6, 7, 8])

Amorizied Time - it is when you want to insert an element into a list
- if the array is full then the runtime is 0(N) worst case because we have create a new array of size 2N and the insertion will take 0(N)
- otherwise if there is room in the array for another element the runtime will be 0(1) best case

# Stopped at page 47