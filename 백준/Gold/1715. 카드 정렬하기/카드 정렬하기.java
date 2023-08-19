import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Queue<Integer> pQueue = new PriorityQueue<>();
		
		List<Integer> list = new ArrayList<Integer>();
		for(int i=0; i<N; i++) {
			pQueue.add(sc.nextInt());
		}
		int a=0;
		while(pQueue.size()>1) {
			int p =pQueue.poll();
			int q =pQueue.poll();
			a+=p+q;
			pQueue.add(p+q);
			
		}
		System.out.println(a);

	}

}
