
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

class Node{
	int n=0;
	boolean visit;
	public Node() {
		
	}
	public Node(int n) {
		n = this.n;
	}
	List<Node> adj = new LinkedList();
}

public class Main {
	static int a=0;
	static Stack<Node> stack = new Stack<Node>();
	
	static void dfs(Node node) {
		node.visit=true;
		for(int i=0; i<node.adj.size(); i++) {
			//인접한 노드중에서 방문 안된 노드를 stack에 추가
			if(!node.adj.get(i).visit) {
				stack.add(node.adj.get(i));
				node.adj.get(i).visit=true;
			}
		}
		if(!stack.isEmpty())
		dfs(stack.pop());
		//가장 마지막에 넣은 Node를 기준으로 dfs
		
		
		
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] strNo = str.trim().split(" ");
		int N = Integer.parseInt(strNo[0]);//정점의 개수
		int M = Integer.parseInt(strNo[1]);//간선의 개수
		Node[] node = new Node[N];
		for(int i=0; i<N; i++) {
			node[i]= new Node(i);//node 생성
		}
		for(int i=0; i<M; i++) {
			str = br.readLine();
			strNo = str.trim().split(" ");
			int p = Integer.parseInt(strNo[0]);
			int q = Integer.parseInt(strNo[1]);
			node[p-1].adj.add(node[q-1]);
			node[q-1].adj.add(node[p-1]);
		}//인접 노드 추가
		for(int i=0; i<N; i++) {
			if(!node[i].visit) {
				//연결 요소 찾기
				dfs(node[i]);
				a++;
				}
		}
		System.out.print(a);
	}

}