import java.util.Scanner;




public class Main {
	static int a = 0;
	static int[][] arr;	
	static boolean[][] arr2;
	static int M;
	static int N;
	static int[] hmove = {1, 0, -1, 0};
	static int[] vmove = {0, 1, 0, -1};
	
	static void bfs(int P, int Q) {
		if(P<M && 0<=P && 0<=Q && Q<N) {
			int start = arr[P][Q];
		}
		if(arr[P][Q]==1 && arr2[P][Q]==false) {
			arr2[P][Q]=true;
			for(int i=0; i<4; i++) {
				if(P+hmove[i]>=0 && P+hmove[i]<M && Q+vmove[i]>=0 && Q+vmove[i]<N) {
					bfs(P+hmove[i], Q+vmove[i]);
				}
			}
		
		}
	}		
	
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int t=0;
		while(t!=T) {
		M = sc.nextInt();
		N = sc.nextInt();
		int K = sc.nextInt();
		arr = new int[M][N];
		arr2 = new boolean[M][N];
		for(int i=0; i<K; i++) {
			int p = sc.nextInt();
			int q = sc.nextInt();					
			arr[p][q]=1;
		}
		for(int i=0; i<M; i++) {
			for(int j=0; j<N; j++) {
				if(arr[i][j]==1 && arr2[i][j] ==false) {
					a++;
				}
				bfs(i, j);
			}
		}
		System.out.println(a);
		a=0; 
		t++;
		}
		
	}
	

}