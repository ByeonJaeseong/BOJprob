import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static int[][] arr;
	public static boolean[][] visit;
	public static int[][] root;
	public static int[] dx = {1, 0, -1 ,0};
	public static int[] dy = {0, 1, 0, -1};
	public static int N;
	public static int M;
	public static int a=0;
	public static void bfs(int n, int m) {
		if(n!=N-1||m!=M-1) {
		visit[n][m]=true;
		for(int i=0; i<4; i++) {
			int p = n+dx[i];
			int q = m+dy[i];
			if(check(p, q)&&arr[n][m]>arr[p][q]&&!visit[p][q]) {
				bfs(p, q);
				
			}
			if(check(p,q)&&arr[n][m]>arr[p][q]) {
				root[n][m]+=root[p][q];
			}
			
		}
		
		}
	}
	public static boolean check(int n, int m){
		if(0<=n&&n<N&&0<=m&&m<M) {
			return true;
		}else {
			return false;
		}
	}
//경우의수 길세기 방법으로 개수 찾기
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		N = Integer.parseInt(inputNo[0]);
		M = Integer.parseInt(inputNo[1]);
		arr =new int[N][M];
		visit = new boolean[N][M];
		root = new int[N][M];
		root[N-1][M-1]=1;
		for(int i=0; i<N; i++) {
			str = br.readLine();
			inputNo = str.trim().split(" ");
			for(int j=0; j<M; j++) {
				arr[i][j]=Integer.parseInt(inputNo[j]);
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(arr[i][j]<arr[N-1][M-1]) {
					visit[i][j]=true;
				}
			}
		}
		bfs(0, 0);
		System.out.println(root[0][0]);
		

	}

}