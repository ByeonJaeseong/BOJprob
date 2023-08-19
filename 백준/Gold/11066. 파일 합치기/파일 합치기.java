import java.io.*;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int rep = Integer.parseInt(str);
    int a = 0;
    while (a < rep) {

      int N = Integer.parseInt(br.readLine());// 행렬 갯수
      int[] matrix = new int[N];
      String[] inputNo = br.readLine().trim().split(" ");

      for (int i = 0; i < N; i++) {
        matrix[i] = Integer.parseInt(inputNo[i]);
      }

      int[] sum = new int[N + 1];
      sum[0] = matrix[0];
      for (int i = 1; i < N; i++) {
        sum[i] = sum[i - 1] + matrix[i];
        // System.out.print((sum[i])+" ");
      }
      // System.out.println();
      int[][] DP = new int[N][N];
      int b = 0;
      while (b < N - 1) {
        for (int i = b; i >= 0; i--) {
          for (int j = 0; j <= b - i; j++) {
            if (DP[i][b + 1] == 0 && i == 0) {
              DP[i][b + 1] = DP[i][b - j] + DP[b + 1 - j][b + 1] + sum[b + 1];
            } else if (DP[i][b + 1] == 0 && i != 0) {
              DP[i][b + 1] = DP[i][b - j] + DP[b + 1 - j][b + 1] + sum[b + 1] - sum[i - 1];
            } else if (DP[i][b + 1] != 0 && i != 0) {
              DP[i][b + 1] = Math.min(DP[i][b + 1],
                  DP[i][b - j] + DP[b + 1 - j][b + 1] + sum[b + 1] - sum[i - 1]);
            } else {
              DP[i][b + 1] = Math.min(DP[i][b+1], DP[i][b - j] + DP[b + 1 - j][b + 1] + sum[b + 1]);
            }
          }
        }
        b++;
      }

      System.out.println(DP[0][N - 1]);
      a++;

    }
  }
}

