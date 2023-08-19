import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long [][] val = new long[n][2];
		for(int j=0; j<n;j++) {
			for(int i=0; i<2;i++) {
				val[j][i]=sc.nextLong();
			}
		}
		for(int j=0;j<n;j++) {
			System.out.println(combi(val[j][1],val[j][0]));
		}

	}
	public static long combi(long n, long m) {
		long a=1;
		long b=1;
		long c=1;
		if(m<=(n/2)) {
		for(int i=1; i<=m; i++) {
			if((n-i+1)%i==0) {
				c*=(n-i+1)/i;
			}else {
			a=(long)a*(n-i+1);
			b=(long)b*i;}
		}
		}else {
			for(int i=1; i<=(n-m); i++) {
				if((n-i+1)%i==0) {
					c*=(n-i+1)/i;
				}else {
				a=(long)a*(n-i+1);
				b=(long)b*i;}
			}
		}
		return (long) c*a/b;
	}

}