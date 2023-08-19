import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	
	static TreeSet<Integer> ts = new TreeSet<Integer>();
	
	public static boolean isPrime(int N) {
		int a = (int) Math.sqrt(N);
		boolean mark = true;
		/*List<Integer> list = new LinkedList<Integer>();
		for(int i=2; i<=a; i++) {
			list.add(i);
		}
		
		while(!list.isEmpty()) {
			int b = list.get(0);
			int c = list.size()+1;
			int d = c/b;
			list.remove(0);
			if(N%b==0) {
				mark=false;
			}
			for(int i=1; i<=d; i++) {
				list.remove((Integer) (b*i));
			}
			
			
		}*/
		for(int i=2; i<=a; i++) {
			if(N%i==0) {
				mark=false;
			}
		}

		
		return mark;
		
	}
	
	public static void wPrime(int N, int p) {
		if(N<10000000) {
			if(isPrime(N*10+1)) {
				if(p<(N*10+1) && (N*10+1)<10*p) {
				ts.add(N*10+1);}
				wPrime(N*10+1, p);
			}
			
			if(isPrime(N*10+3)) {
				if(p<(N*10+3) && (N*10+3)<10*p)
				{ts.add(N*10+3);}
				wPrime(N*10+3, p);
			}
			
			if(isPrime(N*10+7)) {
				if(p<(N*10+7) && (N*10+7)<10*p)
				{ts.add(N*10+7);}
				wPrime(N*10+7, p);
			}
			
			if(isPrime(N*10+9)) {
				if(p<(N*10+9) && (N*10+9)<10*p)
				{ts.add(N*10+9);}
				wPrime(N*10+9, p);
			}
			
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int p = 1;
		for(int i=1; i<N; i++) {
			p*=10;
		}
		if(N==1) {
		ts.add(2); 
		ts.add(3); 
		ts.add(5); 
		ts.add(7);
		}
		wPrime(2, p);
		wPrime(3, p);
		wPrime(5, p);
		wPrime(7, p);
	
		
		while(!ts.isEmpty()) {
			
			System.out.println(ts.pollFirst());
		}
	

	}

}
