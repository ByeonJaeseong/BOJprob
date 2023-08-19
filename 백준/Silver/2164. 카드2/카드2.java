import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Deque<Integer> dq = new ArrayDeque<Integer>();
		for(int i=0; i<n; i++) {
			dq.offer(i+1);
		}
		int a=1;
		while(dq.size()>1) {
			dq.pollFirst();
			a=dq.pollFirst();
			dq.offer(a);
		}
		System.out.println(a);
		

	}

}
