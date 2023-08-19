import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static int N;
	
	public static void bfs(char[][]arr, boolean[][] visit, int n, int m) {
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};
		if(!visit[n][m]) {
		visit[n][m]=true;
		for(int i=0; i<4; i++) {
			if(0<=n+dx[i]&&n+dx[i]<N&&0<=m+dy[i]&&m+dy[i]<N) {
				if(arr[n][m]==arr[n+dx[i]][m+dy[i]]&&!visit[n+dx[i]][m+dy[i]]) {
					bfs(arr, visit, n+dx[i], m+dy[i]);
				}
			}
		}
		}
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N=Integer.parseInt(br.readLine());
		char[][] arr = new char[N][N];
		char[][] arr2 = new char[N][N];
		boolean[][] visit = new boolean[N][N];
		boolean[][] visit2 = new boolean[N][N];
		for(int i=0; i<N; i++) {
			String str = br.readLine();
			String[] inputColor = str.trim().split("");
			for(int j=0; j<N; j++) {
				arr[i][j]=inputColor[j].charAt(0);
				if(inputColor[j].charAt(0)=='R'||inputColor[j].charAt(0)=='G') {
					arr2[i][j]='R';
				}
			}
		}
		

		
		int a=0;
		int b=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(!visit[i][j]) {
					bfs(arr, visit, i, j);
					a++;
				//	System.out.println((i)+"와 "+(j)+"가 실행되었습니다.");
				}
				if(!visit2[i][j]) {
					bfs(arr2, visit2, i, j);
					b++;
				}
			}
		}
		System.out.print((a)+" "+(b));
	}

}