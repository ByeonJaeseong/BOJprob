import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
	
	public static boolean[] prime;

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		long min = sc.nextLong();
		long max = sc.nextLong();
		List<Long> psList = new ArrayList<Long>();
		//List<Long> list = new ArrayList<Long>();
		Set<Long> set = new HashSet<Long>();
		//for(int i=0; i<=(int)(max-min); i++) {
		//	list.add(min+i);
		//}//list 에 원소 넣기
		//long stime = System.currentTimeMillis();
		prime = new boolean[(int) Math.sqrt(max)+1];
		get_prime();//prime 구하기
		for(int i=0; i<prime.length; i++) {
			if(!prime[i]) {
				psList.add((long) i*i);
			}
		}
		//long etime = System.currentTimeMillis();
		//System.out.println(etime-stime);
		//long stime = System.currentTimeMillis();
		while(!psList.isEmpty()) {
			long a = psList.get(0);
			psList.remove(0);
			long i = (long) min/a;
			if(i==0) {
				i++;
			}
			while(a*i<= (long) max) {
				if(min <= a*i) {
					set.add(a*i);
				}
				i=(long)i+1;
			}
			
		}
		//long etime = System.currentTimeMillis();
		//System.out.println(etime-stime);
		/*
		 * for(long n : list) { System.out.println(n); }
		 */
		System.out.println(max-min+1-set.size());

	}
	
	public static void get_prime() {
		
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
