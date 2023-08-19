import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] arr = new int[4][N];
		for(int i=0; i<N; i++) {
			arr[0][i]=sc.nextInt();
			arr[1][i]=1;
			arr[2][i]=1;
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<i; j++) {
				if(arr[0][j]<arr[0][i]) {
					arr[1][i]=Math.max(arr[1][i], arr[1][j]+1);
				}
			}
			for(int j=N-1; j>N-i-1; j--) {
				if(arr[0][j]<arr[0][N-i-1]) {
					arr[2][N-i-1]=Math.max(arr[2][N-i-1], arr[2][j]+1);
				}
			}
		}
		
//		for(int i=0; i<4; i++) {
//			for(int j=0; j<N; j++) {
//				System.out.print((arr[i][j])+" ");
//			}
//			System.out.println();
//		}
//		
		
		TreeSet<Integer> ts = new TreeSet<>();
		for(int i=0; i<N; i++) {
			arr[3][i]=arr[1][i]+arr[2][i];
			ts.add(arr[3][i]);
		}
		System.out.println(ts.pollLast()-1);
		
		

	}

}
