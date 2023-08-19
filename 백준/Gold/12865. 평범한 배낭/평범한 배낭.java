import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
//냅색 알고리즘으로 풀어야 합니다.
//부분합으로 풀면 건너 뛰는 파트가 생김
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();// 물건의 개수
		int M = sc.nextInt(); // 최대 무게
		int[][] arr = new int[N][M+1];
		for(int i=0; i<N; i++) {
			int weight = sc.nextInt();
			int value = sc.nextInt();
			if(i==0 && weight<=M) {
				for(int j=weight; j<=M; j++)
				arr[0][j]=value;
			}else if(i!=0) {
				
				for(int j=0; j<=M; j++) {
					if(weight<=j && j<=M) {
				arr[i][j]=Math.max(arr[i-1][j-weight]+value, arr[i-1][j]);}
					else {arr[i][j]=arr[i-1][j];}
				}
			
			}
		}
		int Max=arr[N-1][0];
//		for(int i=0; i<N; i++) {
//			for(int j=0; j<=M; j++) {
//				System.out.print((arr[i][j])+" ");
//			}
//			System.out.println();
//		}
		for(int i=0; i<=M;i++) {
			Max=Math.max(Max, arr[N-1][i]);
		}
		System.out.println(Max);
//		
	}

}
