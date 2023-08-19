import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

class Node {
  int N;
  boolean visit;

  Node() {
  };

  Node(int N) {
    this.N = N;
  }

  ArrayList<Node> adj = new ArrayList<Node>();
  ArrayList<Integer> weights = new ArrayList<Integer>();

}

class Main {
  public static Node[] nodes;
  public static int[][] weight;
  public static int[] treeLength;
  public static Queue<Node> queue = new LinkedList<Node>();

  public static void bfs(Node node) {
    queue.add(node);
    node.visit = true;
    int s = 1;
    while (!queue.isEmpty()) {
      // System.out.println((s) + "번 실행되었습니다.");
      // System.out.println(queue.size());
      s++;
      Node sNode = queue.poll();
      for (int i=0; i<sNode.adj.size(); i++) {
        Node n = sNode.adj.get(i);
        if (!n.visit) {
          n.visit = true;
          queue.add(n);
          treeLength[n.N] = Math.max(sNode.weights.get(i) + treeLength[sNode.N], treeLength[n.N]);
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int n = Integer.parseInt(str);
    String[] inputNo;
    nodes = new Node[n];
    treeLength = new int[n];
    for (int i = 0; i < n; i++) {
      nodes[i] = new Node(i);
    }

    for (int i = 0; i < n - 1; i++) {
      str = br.readLine();
      inputNo = str.trim().split(" ");
      int x = Integer.parseInt(inputNo[0]) - 1;
      int y = Integer.parseInt(inputNo[1]) - 1;
      int w = Integer.parseInt(inputNo[2]);
      nodes[x].adj.add(nodes[y]);
      nodes[y].adj.add(nodes[x]);
      nodes[x].weights.add(w);
      nodes[y].weights.add(w);

    }

    // r (int i = 0; i < n; i++) {
    // (nodes[i].adj.size() == 1) {
    // bfs(nodes[i]);
    // break;

    // }
    // }
    bfs(nodes[0]);
    int x = 0;
    int max = 0;

    for (int i = 0; i < n; i++) {
      nodes[i].visit = false;
      if (max <= treeLength[i]) {
        x = i;
        max = treeLength[i];
      }
    }

    treeLength = new int[n];
    bfs(nodes[x]);

    for (int i = 0; i < n; i++) {
      if (max <= treeLength[i]) {
        max = treeLength[i];
      }
    }

    System.out.println(max);

  }
}