import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static int[][] arr;
	public static boolean[][] visit;
	public static int[] dx= {1, 0, -1, 0};
	public static int[] dy = {0, 1, 0, -1};
	public static int Max=0;
	public static int sum=0;
	public static int a=0;
	public static int N;
	public static int M;
	public static void bfs(int x, int y) {
		if(!visit[x][y]&&a<4) {
			a++;
			sum+=arr[x][y];
			if(a==4) Max= Math.max(Max, sum);
			visit[x][y]=true;
			for(int i=0; i<4; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				if(check(nx, ny)&&!visit[nx][ny]) {
					bfs(nx, ny);
				}
			}
			sum-=arr[x][y];
			a--;
			visit[x][y]=false;
		}
		
	}
	public static boolean check(int x, int y) {
		if(0<=x&&x<N&&0<=y&&y<M) {
			return true;
		}else {
			return false;
		}
		
	}

	public static void main(String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		N= Integer.parseInt(inputNo[0]);
		M= Integer.parseInt(inputNo[1]);
		arr = new int[N][M];
		visit = new boolean[N][M];
		for(int i=0; i<N; i++) {
			str=br.readLine();
			inputNo=str.trim().split(" ");
			for(int j=0; j<M; j++ ) {
				arr[i][j]=Integer.parseInt(inputNo[j]);
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				sum=0;
				bfs(i, j);
				//visit[i][j]=true;
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M-2; j++) {
				if(i==0) {
					Max=Math.max(Max, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]);
				}else if(i==N-1) {
					Max=Math.max(Max, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i-1][j+1]);	
				}else {
					Max=Math.max(Max, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]);
					Max=Math.max(Max, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i-1][j+1]);
					
				}
			}
		}
		for(int i=0; i<M; i++) {
			for(int j=0; j<N-2; j++) {
				if(i==0) {
					Max=Math.max(Max, arr[j][i]+arr[j+1][i]+arr[j+2][i]+arr[j+1][i+1]);
				}else if(i==M-1) {
					Max=Math.max(Max, arr[j][i]+arr[j+1][i]+arr[j+2][i]+arr[j+1][i-1]);	
				}else {
					Max=Math.max(Max, arr[j][i]+arr[j+1][i]+arr[j+2][i]+arr[j+1][i+1]);
					Max=Math.max(Max, arr[j][i]+arr[j+1][i]+arr[j+2][i]+arr[j+1][i-1]);	
						
				}
			}
		}
		System.out.println(Max);
	}

}