import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Integer N = sc.nextInt();
		Integer M = sc.nextInt();
		TreeSet<Integer> ts = new TreeSet<Integer>(); 
		for(int i=0; i<N; i++) {
			ts.add(sc.nextInt());
		}
		Integer count = 0;
		while(!ts.isEmpty()) {
			Integer a = ts.pollFirst();
			try {
				int p=ts.floor(M-a);
				if(p==M-a) {
					count++;
				}
			} catch (Exception e) {
				// TODO: handle exception
			}
			
			
		}
		
		System.out.println(count);

	}

}