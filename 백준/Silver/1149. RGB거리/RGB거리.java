import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N =sc.nextInt();
		int[][] arr = new int[N][3];
		for(int i=0; i<N; i++) {
			arr[i][0]=sc.nextInt();
			arr[i][1]=sc.nextInt();
			arr[i][2]=sc.nextInt();
		}
		for(int i=0; i<N-1; i++) {
			for(int j=0; j<3; j++) {
				arr[i+1][j]+=Math.min(arr[i][(j+1)%3], arr[i][(j+2)%3]);
				}
			
		}
		int result = 1000*N;
		for(int i=0; i<3; i++) {
			result = Math.min(result, arr[N-1][i]);
		}
		System.out.println(result);

	}

}
