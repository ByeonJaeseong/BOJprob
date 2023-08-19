import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Node{
	int n;
	int dis=Integer.MAX_VALUE;
	boolean visit;
	List<Node> adj =new ArrayList<>();
	
	Node(){}
	Node(int n){
		n =this.n;
	}
	
}

public class Main {
	public static int a=0;//거리정보
	public static int b=0;
	public static int K;
	public static Queue<Node> queue = new LinkedList<Node>();
	public static List<Node> list = new ArrayList<>();
	public static void dfs(Node n) {
		queue.add(n);
		while(!queue.isEmpty()) {
			Node node = queue.poll();
		for(Node m : node.adj) {
			if(m.dis>(node.dis+1)) {
				m.dis=node.dis+1;
				queue.add(m);
			}
		}
		}

		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);//node 개수
		int M = Integer.parseInt(inputNo[1]);//간선 개수
		K = Integer.parseInt(inputNo[2]);//거리 정보
		int X = Integer.parseInt(inputNo[3]);//출발 도시
		Node[] nodes = new Node[N];
		for(int i=0; i<N; i++) {
			nodes[i]=new Node(i);
		}
		for(int i=0; i<M; i++) {
			str=br.readLine();
			inputNo=str.trim().split(" ");
			nodes[Integer.parseInt(inputNo[0])-1].adj.add(nodes[Integer.parseInt(inputNo[1])-1]);	
		}
		nodes[X-1].dis=0;
		dfs(nodes[X-1]);
		int result=0;
		for(int i=0; i<N; i++) {
			//System.out.println("노드 거리정보" +(nodes[i].dis));
			if(nodes[i].dis==K) {
				System.out.println(i+1);
				result++;
			}
		}
		if(result==0) {
			System.out.println(-1);
		}

		

	}

}
