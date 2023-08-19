import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static boolean[] prime;
	public static List<Integer> list = new ArrayList<Integer>();
	
	
	public static boolean is_prime(int n) {
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

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		prime = new boolean[n+1];
		is_prime(n);
		for(int i=0; i<=n; i++) {
			if(!prime[i]) {
				list.add(i);
			}
		}
		//System.out.println(list.size());
		int sum = 0;
		int i=0;
		int j=0;
		int a=0;
		while(i<=j && i<=list.size() && j<=list.size()) {
			//System.out.println(sum);
			if(sum==n) {
				a++;
			}
			
			try {
			
			if(sum<n) {
				sum+=list.get(j);
				j++;
				
			}else {
				sum-=list.get(i);
				i++;
			
			}
			}catch(IndexOutOfBoundsException e) {
				break;
			}
		}
			System.out.println(a);
	}

}
