import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(); // nbyn 행렬 maximum 개수
    int m = sc.nextInt(); // 이분탐색의 최댓값
    // 구하고자 하는것 이분 탐색의 최솟값으로 array 채워서 찾기

    int min = 1;
    int max = m; // 어차피 m을 못넘음
    int start = 0;
    int ans = 0;
    while (min<=max) {// 반값부터 시작
      start = ((max + min) / 2)  ;
      int count = 0;
      for (int i = 1; i <= n; i++) {
        count = count + Math.min(n, start / i);
      } // 자신보다 작은 수의 개수 새기
      // System.out.println("start" + (start) + "min" + (min) + "max" + (max));


      if (count < m) {// 개수가 부족하면 더큰 수로 이동
        min = start+1;
      } else {// 개수가 많으면 더 작은 수로 이동
        ans = start;
        max = start-1;
      } 
      
    }
    System.out.println(ans);
    // System.out.println("start : " + (start) + " min : " + (min) + " max : " +
    // (max));

    // 3+3+2=8 6
    // 3+2+1=6 5
    // 3+3+2=8 7
    // 3+3+3=9 9
    // 3+2+1=6 4
    // 3+1+1=5 3
    // 2+1+0=3 2

    /*
     * 123
     * 246
     * 369
     * 1 2 3 4 5 6 7 8 9
     * 1 2 2 3 3 4 6 6 9
     * 1 3 3 5 5 6 8 8 9
     * 
     * 
     * 122334669
     * 1335556889
     */
  }
}