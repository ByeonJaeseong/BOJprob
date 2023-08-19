import java.util.Scanner;

public class Main {


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String N = sc.next();
		int n = Integer.parseInt(N);
		
		while(true) {
			if(is_pel(n) && !is_prime(n)) {
				System.out.println(n);
				break;
			}else {
				n++;
			}
		}
		

	}
	
	public static boolean is_prime(int n) {
		boolean[] prime = new boolean[n+1];
		prime[0] = prime[1] = true;
		
		for(int i = 2; i <= Math.sqrt(prime.length); i++) {
			if(prime[i]) continue;
			for(int j = i * i; j < prime.length; j += i) {
				//i 보다 작은 배수에 대해서는 이미 없앴기 때문에 i*i부터 시작
				prime[j] = true;
			}
		}
		
		return prime[n]; // false이면 소수
	}
	
	public static boolean is_pel(int n) {
		boolean pel=true;
		int l = n;
		int m = String.valueOf(n).length();
		int[] arr = new int[m];
		for(int i=0; i<m; i++) {
			arr[i]=l%10;
			l=l/10;
		}
		for(int i=0; i<m/2; i++) {
			if(arr[i]==arr[m-1-i]) {continue;}
			else {
				pel = false;
				break;
			}
		}
		return pel;
	}

}
