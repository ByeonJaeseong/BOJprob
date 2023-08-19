import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int gcd = gcd(N,M);
		int lcm = N*M/gcd;
		System.out.println(gcd +"\n"+lcm);
	}
	
	static int gcd(int P, int Q) {
			int a=1;
			int b = 0;
			while((Math.max(P, Q))>=a) {
				if((P%a==0)&&(Q%a==0)) {
					b=a;
					a++;
				}else {
					a++;
				}
			}
			return b;
		}
		
	}
