import java.util.Arrays;

public class BubbleSortOnce {
  public static int[] bubbleSortOnce(int[] array) {

    int[] res = Arrays.copyOf(array, array.length);

    for (int i = 0; i < array.length - 1; i++) {
      if (res[i] > res[i + 1]){
        int temp = res[i];
        res[i] = res[i + 1];
        res[i + 1] = temp;
      }
    }
    return res;
  }

  public static void main(String[] args) {
    int[] myArr = {9, 7, 5, 3, 1, 2, 4, 6, 8};
    System.out.println(Arrays.toString(bubbleSortOnce(myArr)));
  }
}


