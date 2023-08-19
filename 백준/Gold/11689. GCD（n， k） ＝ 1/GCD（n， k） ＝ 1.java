import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

//	static boolean[] prime = new boolean[Integer.MAX_VALUE/2];

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long M =N;
		long i =2;
		long a =1;
		//get_prime();
		//List<Integer> list = new ArrayList<>();
		/*
		 * for(int j=2; j<Integer.MAX_VALUE; j++) { if(!prime[j]) list.add(j); }
		 */

		while(N!=1) {
			if(i!=2 && i%2==0) {
				i++;
			} else {
			int q = 0;
			while(N%i==0) {
				q++;
				N=N/i;
			}
			int r =1;
			for(int j=0; j<q; j++) {
				r*=i;
			}
			a*=(r-r/i);
			i++;}
			if(i>Math.sqrt(N)) {
				break;
			}
			
			// if(list.contains((Integer) (int)N)) { a*=(N-1); break; }
			 
		}
		if(N!=1) {
			System.out.println(a*(N-1));
		}else {
		System.out.print(a);}
		
		

	}
	
	
}
