import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

class Graph{
	class Node{
		int data;
		LinkedList<Node> adjacent;
		boolean marked;
		Node(int data){
			this.data=data;
			this.marked=false;
			adjacent = new LinkedList<Node>();
		}
	}
	Node[] nodes;
	Graph(int size){
		nodes = new Node[size];
		for(int i=0; i<size; i++) {
			nodes[i] = new Node(i+1);
		}
	}
	void addEdge(int i1, int i2) {
		Node n1 = nodes[i1-1];
		Node n2 = nodes[i2-1];
		if(!n1.adjacent.contains(n2)) {
			n1.adjacent.add(n2);
		}
		if(!n2.adjacent.contains(n1)) {
			n2.adjacent.add(n1);
		}
	}
	void dfs() {
		dfs(0);
	}
	
	void dfs(int index) {
		Node root = nodes[index];
		Stack<Node> stack = new Stack<Node>();
		stack.push(root);
		root.marked=true;
		int sol =-1;
		while(!stack.isEmpty()) {
			sol++;
			Node r =stack.pop();
			
			for(Node n : r.adjacent) {
				if(n.marked==false) {
					n.marked=true;
					stack.push(n);
				}
			}
			
		}
		System.out.println(sol);
	}
}

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		Graph graph = new Graph(N);
		for(int i=0; i<M; i++) {
			graph.addEdge(sc.nextInt(), sc.nextInt());
		}
		graph.dfs();

	}

}