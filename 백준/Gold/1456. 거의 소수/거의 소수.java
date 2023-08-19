import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	
	public static boolean[] prime;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long M = sc.nextLong();
		prime = new boolean[(int) 10000001];
		get_prime();
		int result =0;
		int result2 = 0;
		//List<Integer> list = new ArrayList<Integer>();
		List<Long> pList = new ArrayList<Long>();
		for(int i=0; i<prime.length; i++) {
			if(!prime[i]) {
				//System.out.println(i);
				pList.add((long) i);
			}
		}//소수만 추출
		for(int i=0; i<pList.size(); i++) {
			long p =pList.get(i);
			//if((double)1<=(double)p/(double)N &&  (double)1<= (double)M/(double)p) {
				//result2++;
			//}
			//System.out.print((p)+":");
			while( (double) pList.get(i) <=(double) M/(double)p) {
				//System.out.println(p);
				if((double) pList.get(i)>=(double)N/(double)p) {
					result++;
				}
					p=(long)p*pList.get(i);
			}
			//System.out.println(result);
		}
		System.out.print(result);

	}
	
	public static void get_prime() {
		// true = 소수아님 , false = 소수 1
		prime[0] = prime[1] = true;
		
		for(int i = 2; i <= Math.sqrt(prime.length); i++) {
			if(prime[i]) continue;
			for(int j = i * i; j < prime.length; j += i) {
				//i 보다 작은 배수에 대해서는 이미 없앴기 때문에 i*i부터 시작
				prime[j] = true;
			}
		}
	}

}