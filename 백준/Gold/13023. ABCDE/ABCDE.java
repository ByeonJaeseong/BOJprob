import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Node{
	
	Node(){}
	Node(int n){
		n =this.n;
	}
	
	int n;
	boolean visit;
	List<Node> adj =new ArrayList<Node>();
}

public class Main {
	
	static int a=0;
	static boolean exist;
	Stack<Node> stack = new Stack<Node>();
	static void bfs(Node node) {
		node.visit=true;
		if(a>=4) {
			exist = true;
		}else {
		int b=a;
		for(Node n : node.adj) {
			if(!n.visit) {
			a++;
			bfs(n);
			a=b;}		
		}
		}
		node.visit=false;
		
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		Node[] nodes = new Node[N];
		for(int i=0; i<N; i++) {
			nodes[i] = new Node(i);
		}
		for(int i=0; i<M; i++) {
			str=br.readLine();
			inputNo=str.trim().split(" ");
			int a = Integer.parseInt(inputNo[0]);
			int b = Integer.parseInt(inputNo[1]);
			nodes[a].adj.add(nodes[b]);
			nodes[b].adj.add(nodes[a]);
		}
		for(int i=0; i<N; i++) {
			bfs(nodes[i]);
			if(exist) {
				break;
			}
		}
		
		if(exist) {
			System.out.print(1);
		}else {
			System.out.print(0);
			
		}
		

	}

}
