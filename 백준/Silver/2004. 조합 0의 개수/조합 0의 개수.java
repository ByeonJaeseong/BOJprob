import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N= sc.nextLong();
		long M = sc.nextLong();
		/*System.out.println(count1(N));
		System.out.println(count1(M));
		System.out.println(count1(N-M));
		System.out.println(count2(N));
		System.out.println(count2(M));
		System.out.println(count2(N-M));*/
		System.out.println(
				Math.min(count1(N)-count1(M)-count1(N-M),
						count2(N)-count2(M)-count2(N-M)));

	}
	public static int count1(long n) {
		long a=5;
		int b=0;
		while(a<=n) {
			b+=n/a;
			a=(long)a*5;
		}
		
		return b;
	}
	public static int count2(long n) {
		long a=2;
		int b=0;
		while(a<=n) {
			b+=n/a;
			a=(long)a*2;
		}
		
		return b;
	}

}