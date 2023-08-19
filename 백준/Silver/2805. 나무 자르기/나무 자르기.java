import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    String[] inputArray = str.trim().split(" ");
    int N = Integer.parseInt(inputArray[0]);
    int M = Integer.parseInt(inputArray[1]);
    int[] height = new int[N];
    int[] cut = new int[N];
    long sum = 0;
    str = br.readLine();
    inputArray = str.trim().split(" ");
    int max = 0;

    for (int i = 0; i < N; i++) {
      height[i] = Integer.parseInt(inputArray[i]);
      sum = (long) sum + height[i];
      if (max < height[i])
        max = height[i];
    }

    int start = max / 2;
    int end = 0;

    while (true) {
      cut = new int[N];
      sum = (long) 0;

      for (int i = 0; i < N; i++) {

        if (height[i] > start) {
          cut[i] = height[i] - start;
        }
        sum = (long) sum + cut[i];

      }

      if (sum >= M) {
        end = start;
        start = (start + max) / 2;
      } else if (sum < M) {
        max = start;
        start = start / 2;
      } else {
        break;
      }

      if (end == start || start == max) {
        break;
      }

    }
    System.out.println(start);

  }
}