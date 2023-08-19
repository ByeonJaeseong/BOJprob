import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] mat = new long[N][10];
		for(int i=0; i<10; i++) {
			mat[0][i]=1;
		}
		for(int i=1; i<N; i++) {
			for(int j=0; j<10; j++) {
				if(j==0) {
				mat[i][j]=(long)mat[i-1][1]%1000000000;}
				else if(j==9) {
					mat[i][j]=(long)mat[i-1][8]%1000000000;
				}else {
					mat[i][j]=(long)(mat[i-1][j-1]+mat[i-1][j+1])%1000000000;
				}
			}
		}
		
		
			long a=0;
		for(int i=1; i<10;i++) {
			a =(long)(a+mat[N-1][i])%1000000000;}
		System.out.println((long)a%1000000000);
		
	}
	


}