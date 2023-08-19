import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
	public static int N, M;
	public static boolean[][] visit;
	public static int a=0;
	public static int Max=0;
	public static Set<Character> set = new HashSet<>();
	public static void bfs(char[][] board, int p, int q) {
		int[] dx= {1, 0, -1, 0};
		int[] dy= {0, 1, 0, -1};
		if(!visit[p][q]&&!set.contains(board[p][q])) {
			a++;
			set.add(board[p][q]);
			visit[p][q]=true;
			Max= Math.max(Max, a);
			for(int i=0; i<4; i++) {
				if(0<=p+dx[i]&&p+dx[i]<N&&0<=q+dy[i]&&q+dy[i]<M) {
					
					bfs(board, p+dx[i], q+dy[i]);
					
					
				}
				
			}
			a--;
			set.remove(board[p][q]);
			visit[p][q]=false;
			
		}
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] input = str.trim().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		char[][] board = new char[N][M];
		visit = new boolean[N][M];
		for(int i=0; i<N; i++) {
			str=br.readLine();
			input = str.split("");
			for(int j=0; j<M; j++) {
				board[i][j]=input[j].charAt(0);
			}
		}
		bfs(board, 0, 0);
		System.out.println(Max);


	}

}