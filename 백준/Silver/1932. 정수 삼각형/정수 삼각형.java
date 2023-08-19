import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] arr = new long[N][N];
		long[][] arr2 = new long[N][N];
		int j=0;
		for (int i=0; i<N; i++) {
			while(j<=i) {
				arr[i][j]=sc.nextLong();
				j++;
			}
			j=0;
		}
		arr2[0][0]=arr[0][0];
		for (int i=0; i<N; i++) {
			long a;
			for(int k=0; k<i; k++) {
				a=arr2[i-1][k];
				if(k==0) {
				arr2[i][k]=(long)arr[i][k]+a;
				arr2[i][k+1]=(long)arr[i][k+1]+a;}
				else if(1<=k) {
				arr2[i][k]=Math.max(arr2[i][k], (long)arr2[i-1][k]+arr[i][k]);
				arr2[i][k+1]=(long)arr[i][k+1]+a;
				}
				
			}
		}
		TreeSet<Long> ts = new TreeSet<>();
		for(int i=0; i<N; i++) {
			ts.add(arr2[N-1][i]);
		}
		/*
		for (int i=0; i<N; i++) {
			while(j<=i) {
				System.out.print(arr2[i][j]);
				System.out.print(" ");
				j++;
			}
			System.out.println();
			j=0;
		}
		*/
		System.out.print(ts.pollLast());
		
		
		

	}

}
