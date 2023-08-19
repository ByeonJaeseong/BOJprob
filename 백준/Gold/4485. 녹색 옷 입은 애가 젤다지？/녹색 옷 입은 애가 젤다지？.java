import java.io.*;

class Main {

  public static int min;
  public static int recur;

  public static int dijk(int[][] tRupee) {
    boolean[][] visit = new boolean[recur][recur];
    int[][] mini = new int[recur][recur];
    int[] dx = { -1, 1, 0, 0 };
    int[] dy = { 0, 0, 1, -1 };

    for (int i = 0; i < recur; i++) {
      for (int j = 0; j < recur; j++) {
        mini[i][j] = Integer.MAX_VALUE;
      }
    }
    mini[0][0] = tRupee[0][0];
    int n = 0;
    int m = 0;
    while (n != recur - 1 || m != recur - 1) {
      int minimum = Integer.MAX_VALUE;
      visit[n][m] = true;
      for (int i = 0; i < 4; i++) {
        int dn = n + dx[i];
        int dm = m + dy[i];
        if (0 <= dn && 0 <= dm && dn < recur && dm < recur && !visit[dn][dm])
          mini[dn][dm] = Math.min(mini[dn][dm], mini[n][m] + tRupee[dn][dm]);
      }

      for (int i = 0; i < recur; i++) {
        for (int j = 0; j < recur; j++) {
          if (!visit[i][j] && minimum > mini[i][j]) {
            minimum = mini[i][j];
            n = i;
            m = j;
          }
        }
      }

    }

  /*  System.out.println(recur);
    System.out.println((n)+" "+(m));

    for (int i = 0; i < recur; i++) {
        for (int j = 0; j < recur; j++) {
          System.out.print((mini[i][j])+ " ");
      }
      System.out.println();
    }

    for (int i = 0; i < recur; i++) {
      for (int j = 0; j < recur; j++) {
          System.out.print((visit[i][j])+ " ");
      }
      System.out.println();
    }
      */

    return mini[recur - 1][recur - 1];
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    recur = Integer.parseInt(str);
    int x = 0;
    while (recur != 0) {

      x++;
      String[] inputNo;
      int[][] tRupee = new int[recur][recur];
      for (int i = 0; i < recur; i++) {
        str = br.readLine();
        inputNo = str.trim().split(" ");
        for (int j = 0; j < recur; j++) {
          tRupee[i][j] = Integer.parseInt(inputNo[j]);
        }
      }
//      System.out.println();// 데이터 입력 끝//
      System.out.println("Problem " + (x) + ": " + (dijk(tRupee)));

      // **************************************************//
      str = br.readLine(); // 다 돌린후 다음 숫자 업데이트
      recur = Integer.parseInt(str);
    }

  }
}