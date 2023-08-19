import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] b= new long[N];
		long[] c= new long[N];
		b[0]=0;
		c[0]=1;
		for(int i=1; i<N; i++) {
			b[i]=(long)b[i-1]+c[i-1];
			c[i]=b[i-1];
		}
		long a =(long) b[N-1]+c[N-1];
		System.out.println(a);
	}

}
