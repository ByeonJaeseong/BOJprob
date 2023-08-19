import java.util.Scanner;

public class Main {
	public static int factorial(int n) {
		int result=1;
		
		for(int i=1; i<=n; i++) {
			result*=i;
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		System.out.println(factorial(N)/(factorial(N-K)*factorial(K)));
		
	}

}
