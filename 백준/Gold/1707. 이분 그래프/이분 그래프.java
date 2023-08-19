import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

class Node{
	int n;
	boolean visit;
	List<Node> adj = new ArrayList<>();
	Node(){}
	Node(int n){
		this.n = n;
	}
}

public class Main {
	
	public static Set<Node> set1;
	public static Set<Node> set2 ;
	public static List<Node> list;
	public static boolean marker =false;
	/* 1 - 3 - 4 - 2 인 경우 에러 케이스*/
	public static void grouping(Node node){
		if(!node.visit) {
		node.visit=true;
		if(!set1.contains(node)&&!set2.contains(node)) {
			set1.add(node);
			for(Node n: node.adj) {
				set2.add(n);
				grouping(n);
			}
		}else if(!set1.contains(node)&&set2.contains(node)) {
			for(Node n: node.adj) {
				set1.add(n);
				grouping(n);
			}
		}else if(set1.contains(node)&&!set2.contains(node)) {
			for(Node n: node.adj) {
				set2.add(n);
				grouping(n);
			}
		}else {
			marker = true;
		}
		
		}
	
	}
		

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int N = Integer.parseInt(str);
		for(int x=0; x<N; x++) {
			str = br.readLine();
			String[] inputNo = str.split(" ");
			int nNode = Integer.parseInt(inputNo[0]);
			int nEdge = Integer.parseInt(inputNo[1]);
			Node[] nodes = new Node[nNode];
			for(int i=0; i<nNode; i++) {
				nodes[i]=new Node(i);
			}
			for(int i=0; i<nEdge; i++) {
				str=br.readLine();
				inputNo = str.split(" ");
				int p = Integer.parseInt(inputNo[0])-1;
				int q = Integer.parseInt(inputNo[1])-1;
				nodes[p].adj.add(nodes[q]);
				nodes[q].adj.add(nodes[p]);
			}
			set1 = new HashSet<>();
			set2 = new HashSet<>();
			list = new ArrayList<>();
			for(int i=0; i<nNode; i++) {
				list.add(nodes[i]);
			}
			
				
			for(int i=0; i<nNode; i++) {
				grouping(nodes[i]);
				
			}
			//System.out.println(set1.size());
			//System.out.println(set2.size());
			/*if(marker=true) {	System.out.println("NO");
			}else {*/
			if(set1.size()+set2.size()<=nNode) {
				System.out.println("YES");
			}else {
				System.out.println("NO");
			}
			/* } */
			
			
		}
				

	}

}
