
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int a = 2;
	static int[][] arr;	
	static boolean[][] arr2;
	static int[][] arr3;
	static int M;
	static int N;
	static int[] hmove = {1, 0, -1, 0};
	static int[] vmove = {0, 1, 0, -1};
	
	static void bfs(int P, int Q) {
		int b=a;
		if(arr[P][Q]==1 && arr2[P][Q]==false) {
			arr2[P][Q]=true;
			for(int i=0; i<4; i++) {
				if(P+hmove[i]>=0 && P+hmove[i]<M && Q+vmove[i]>=0 && Q+vmove[i]<N) {
					if(arr3[P+hmove[i]][Q+vmove[i]]>0 && arr3[P+hmove[i]][Q+vmove[i]]>b){
						arr3[P+hmove[i]][Q+vmove[i]]=b;
						arr2[P+hmove[i]][Q+vmove[i]]=false;}
						if(arr[P+hmove[i]][Q+vmove[i]]==1&&arr2[P+hmove[i]][Q+vmove[i]]==false) {
							if(arr3[P+hmove[i]][Q+vmove[i]]==0) {					
							arr3[P+hmove[i]][Q+vmove[i]]=b;}
							}
						
					a++;
					bfs(P+hmove[i], Q+vmove[i]);
					a=b;
					

				}
			}		
		}
	}		
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] size = str.split(" ");
		M = Integer.parseInt(size[0]);
		N = Integer.parseInt(size[1]);
		arr = new int[M][N];
		arr2 = new boolean[M][N];
		arr3 = new int[M][N];
		for(int i=0; i<M; i++) {
			String input = br.readLine();
			for(int j=0; j<N; j++) {
			char a = input.charAt(j);
			if(a=='1') {
				arr[i][j]=1;
			}else {
				arr[i][j]=0;
			}
			}
		}
		bfs(0,0);
		System.out.println(arr3[M-1][N-1]);
		
	

	}

}
