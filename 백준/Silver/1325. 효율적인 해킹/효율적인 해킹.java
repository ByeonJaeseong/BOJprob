import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Node implements Comparable<Node>{
	int n;
	int dis=0;
	boolean visit;
	List<Node> adj =new ArrayList<>();
	
	Node(){}
	Node(int n){
		this.n =n;
	}
	@Override
	public int compareTo(Node o) {
		
		return this.dis!=o.dis ? o.dis-this.dis :this.n-o.n;
	}
	
	
}

public class Main {
	
	public static Queue<Node> queue = new LinkedList<>();
	public static void bfs(Node n) {
		queue.add(n);
		n.visit=true;
		while(!queue.isEmpty()) { 
			 Node node = queue.poll();
			 n.dis++;
				 for(Node m : node.adj){
				 if(!m.visit){
					 m.visit=true;
					 queue.add(m); 
				 } 
			}
		}
		
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		Node[] nodes = new Node[N];
		List<Node> list = new ArrayList<>();
		for(int i=0; i<N; i++) {
			nodes[i] = new Node(i);
			//System.out.println("번호:"+(nodes[i].n)+" 개수:"+(nodes[i].dis));
		}
		
		for(int i=0; i<M; i++) {
			str = br.readLine();
			inputNo = str.trim().split(" ");
			nodes[Integer.parseInt(inputNo[1])-1].
			adj.add(nodes[Integer.parseInt(inputNo[0])-1]);
		}
		
		for(int i=0; i<N; i++) {
			bfs(nodes[i]);
			for(int j=0; j<N; j++) {
				nodes[j].visit=false;
			}
		}
		
		for(int i=0; i<N; i++) {
			list.add(nodes[i]);
			//System.out.println("번호:"+(nodes[i].n)+" 개수:"+(nodes[i].dis));
		}
		list.sort(null);
		Node rNode = list.get(0);
		for(int i=0; i<N; i++) {
			if(list.get(i).dis==rNode.dis) {
				//System.out.println(list.get(i).dis);
				System.out.print((list.get(i).n+1)+" ");
			} else {
				break;
			}
		}
	}

}