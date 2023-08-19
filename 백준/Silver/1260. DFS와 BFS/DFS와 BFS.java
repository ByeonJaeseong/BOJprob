import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N = sc.nextInt();
	static int M = sc.nextInt();
	static int L = sc.nextInt();
	static int[][] arr = new int[N][2];/*Node생성*/
	static int[][] arr2 = new int[N][2];/*Node생성*/
	static Set<Integer>[] list = new TreeSet[N];
	static Set<Integer>[] list2 = new TreeSet[N];
	static void bfs(int P) {
		int start = P-1;
		TreeSet ts = (TreeSet) list[start];
		arr[start][1]=1;
		System.out.print(start+1+" ");
		while(!ts.isEmpty()) {
			int Q = (int) ts.pollFirst();
			if(arr[Q][1]!=1) {
				bfs(Q+1);
				}
			}		
		}		
	
	

	public static void main(String[] args) {
		for(int i=0; i<N; i++) {
			arr[i][0]=i;
			arr2[i][0]=i;
			list[i] = new TreeSet<Integer>();
			list2[i] = new TreeSet<Integer>();
		}
		for(int i=0; i<M; i++) {
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			list[a].add(b);
			list[b].add(a);
			list2[a].add(b);
			list2[b].add(a);
		}
		bfs(L);
		System.out.println();
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(L-1);
		

		while(!queue.isEmpty()) {
			int b=queue.poll();
			arr2[b][1]=1;
			TreeSet ts2=(TreeSet) list2[b];
			System.out.print((b+1)+" ");
			
			while(!ts2.isEmpty()) {
				int data =(Integer) ts2.pollFirst();
				if(arr2[data][1]!=1) {
				queue.offer(data);
				arr2[data][1]=1;
				}
				
			}
			
		}
			
			
		

		

	}

}