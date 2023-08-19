import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());// 행렬 갯수
    int[][] matrix = new int[N][2];
    for (int i = 0; i < N; i++) {
      String[] inputNo = br.readLine().trim().split(" ");
      matrix[i][0] = Integer.parseInt(inputNo[0]);
      matrix[i][1] = Integer.parseInt(inputNo[1]);
    }
    int[][] DP = new int[N][N];
    int a=0;
    while(a<N-1){
      for(int i=a; i>=0; i--){
        for(int j=0; j<=a-i; j++){
          if(DP[i][a+1]==0)
            DP[i][a+1]=DP[i][a-j]+DP[a+1-j][a+1]+matrix[i][0]*matrix[a-j+1][0]*matrix[a+1][1];
            else
          DP[i][a+1]=Math.min(DP[i][a+1], DP[i][a-j]+DP[a+1-j][a+1]+matrix[i][0]*matrix[a-j+1][0]*matrix[a+1][1]);
        }
      }

    //     for(int i=0; i<N; i++){
    //   for(int j=0; j<N; j++){
    //     System.out.print((DP[i][j])+" ");
    //   }
    //   System.out.println();
    // }

 //     System.out.println();

      a++;
    }

    // for(int i=0; i<N; i++){
    //   for(int j=0; j<N; j++){
    //     System.out.print((DP[i][j])+" ");
    //   }
    //   System.out.println();
    // }

    System.out.println(DP[0][N-1]);

    
  }
}