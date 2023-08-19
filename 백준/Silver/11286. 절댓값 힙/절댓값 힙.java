import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Queue<Integer> pQueue = new PriorityQueue<>(
				(o1, o2)-> Math.abs(o1)!=Math.abs(o2) ? Math.abs(o1)-Math.abs(o2) :o1-o2
		);

		for(int i=0; i<n; i++) {
			int m = sc.nextInt();
			if(m!=0) {
				pQueue.add(m);
			}else {
				if(!pQueue.isEmpty()) {
					System.out.println(pQueue.poll());
				}else {
					System.out.println(0);
				}
			}
		}
		}
}
