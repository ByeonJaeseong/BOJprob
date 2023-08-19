import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
	int N;
	public TreeNode() {
		// TODO Auto-generated constructor stub
	}
	public TreeNode(int N){
		this.N =N;
		
	}
	int parent;
	List<TreeNode> adj = new ArrayList<>();
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		TreeNode[] nodes = new TreeNode[N];
		for(int i=0; i<N; i++) {
			nodes[i] = new TreeNode(i);
		}
		for(int i=0; i<N-1; i++) {
			String str =br.readLine();
			String[] inputNo = str.trim().split(" ");
			int p =Integer.parseInt(inputNo[0])-1;
			int q = Integer.parseInt(inputNo[1])-1;
			nodes[p].adj.add(nodes[q]);
			nodes[q].adj.add(nodes[p]);			
		}
		
		Queue<TreeNode> queue = new LinkedList<>();
		queue.add(nodes[0]);
		while(!queue.isEmpty()) {
			TreeNode parent = queue.poll();
			for(int i=0; i<parent.adj.size(); i++) {
				parent.adj.get(i).adj.remove(parent);
				parent.adj.get(i).parent=parent.N;
				queue.add(parent.adj.get(i));
			}
		}
		
		for(int i=1; i<N; i++) {
			System.out.println(nodes[i].parent+1);
		}


	}

}
