import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N =sc.nextInt();
		int K =sc.nextInt();
		int[] arr = new int[100001];
		boolean[] visit = new boolean[100001];
		Queue<Integer> input = new LinkedList<Integer>();
		Queue<Integer> output = new LinkedList<Integer>();
		int x =0;
		output.add(N);
		while(visit[K]==false) {
			while(!output.isEmpty()) {
				input.add(output.poll());
			}
			while(!input.isEmpty()) {
				int a=input.poll();
				if(visit[a]==false) {
					arr[a]=x;
					visit[a]=true;
					if(a-1>=0 && visit[a-1]==false) {
					output.add(a-1);
					}
					if(a+1<100001 && visit[a+1]==false) {
						output.add(a+1);
					}
					if(2*a<100001 && visit[2*a]==false) {
						output.add(2*a);
					}
				}
			}
			x++;
		}
		System.out.println(arr[K]);
	}

}