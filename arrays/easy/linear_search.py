def linear_search(arr):
    for i in range(0,len(arr)):
        if arr[i]==item:
            return i
    return -1
    
arr=[1,4,7,5]
item=6
print(linear_search(arr))
########### java code
public class LinearSearch {
    public static int linearSearch(int[] arr, int item) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == item) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 4, 7, 5};
        int item = 4;
        System.out.println(linearSearch(arr, item));
    }
}