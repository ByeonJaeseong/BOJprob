import java.io.BufferedReader;
import java.io.InputStreamReader;

//중복조합 문제인데 파스칼의 삼각형 이용해서 DP문제로 바꾸는게 포인트
class Main {
  // public static long factorial(int N) {
  // long value = 1;
  // for (int i = 1; i <= N; i++) {
  // value = (long) ((long) (value * i) % (long) 1000000000);
  // }
  // return value;
  // }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    String[] inputStr = str.trim().split(" ");
    int N = Integer.parseInt(inputStr[0]);
    int M = Integer.parseInt(inputStr[1]);
    int[][] pascal = new int[401][401];
    for (int i = 0; i < 401; i++) {
      pascal[i][0] = 1;
    }
    for (int i = 1; i < 401; i++) {
      for (int j = 1; j < 401; j++) {
        pascal[i][j] = (pascal[i - 1][j - 1] + pascal[i - 1][j]) % 1000000000;
      }
    }
    // for (int i = 0; i <= N; i++) {
    // System.out.println(factorial(i));
    // }
    int result = pascal[N + M - 1][N];
    System.out.println(result);

  }
}