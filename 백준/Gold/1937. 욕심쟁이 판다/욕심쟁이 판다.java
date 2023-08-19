import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	
	public static int N;
	public static int[][] arr2;
	public static int Max=0;
	public static boolean[][] visit=new boolean[N+2][N+2];;
	public static int[] dx = {1, 0, -1, 0};
	public static int[] dy = {0, 1, 0, -1};
	public static void bfs(int x, int y, int[][] arr, boolean[][] visit) {
		int a =0;
		if(!visit[x][y]) {	
			visit[x][y]=true;
			for(int i=0; i<4; i++) {
				if(1<=x+dx[i]
				&&x+dx[i]<=N
				&&1<=y+dy[i]
				&&y+dy[i]<=N
				&&!visit[x+dx[i]][y+dy[i]]
				&&arr[x+dx[i]][y+dy[i]]>arr[x][y]) {
					bfs(x+dx[i], y+dy[i], arr, visit);
					// 가장 큰 수를 0으로 셋팅
				}
				if(arr[x][y]<arr[x+dx[i]][y+dy[i]]) {
					a=Math.max(a, arr2[x+dx[i]][y+dy[i]]);
					//가장 긴 경로 선택
					//갔던 길을 다시 탐색 안해도 됨
					//기존의 코드는 갔던길을 다시 탐색을 해야 됐음
				}
			}
			a++;
			arr2[x][y]=Math.max(a, arr2[x][y]);
			Max=Math.max(arr2[x][y], Max);
			
		}
	}
	
	//시작점에 주변에 자기 자신보다 작은 수가 있으면 검사할 필요가 없다
	//-> 더 작은수에서 시작하면 되기 때문에
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N+2][N+2];
		visit = new boolean[N+2][N+2];
		arr2 = new int[N+2][N+2];
		for(int i=0; i<N+2; i++) {
			for(int j=0; j<N+2; j++) {
				arr[i][j]=Integer.MAX_VALUE;
			}
		}
		for(int i=1; i<=N; i++) {
			String str =br.readLine();
			String[] inputNo = str.trim().split(" ");
			for(int j=1; j<=N; j++) {
				arr[i][j]=Integer.parseInt(inputNo[j-1]);
			}
		}
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=N; j++) {
				if(arr[i-1][j]>=arr[i][j]
						&&arr[i+1][j]>=arr[i][j]
						&&arr[i][j-1]>=arr[i][j]
						&&arr[i][j+1]>=arr[i][j]
				/* &&arr2[i][j]==0 */) {
					
					
					//System.out.println("실행됨");
					bfs(i, j, arr, visit);	
				}
			}
		}
		
	
//		
//		for(int i=1; i<=N; i++) {
//			for(int j=1; j<=N; j++) {
//				if(arr2[i][j]>Max) {
//					Max=arr2[i][j];
//					
//				}
////			//	System.out.print((arr2[i][j])+" ");
//			}
////		//	System.out.println();
//		}
		System.out.print(Max);
		

	}

}