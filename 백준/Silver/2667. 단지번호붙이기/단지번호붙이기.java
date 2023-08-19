import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {	
	static int a = 0;
	static int b=0;
	static int[][] arr;	
	static boolean[][] arr2;
	static int M;
	static int N;
	static int[] hmove = {1, 0, -1, 0};
	static int[] vmove = {0, 1, 0, -1};
	static List list;
	
	static void bfs(int P, int Q) {
		if(P<M && 0<=P && 0<=Q && Q<M) {
			int start = arr[P][Q];
		}
		if(arr[P][Q]==1 && arr2[P][Q]==false) {
			arr2[P][Q]=true;
			b++;
			for(int i=0; i<4; i++) {
				if(P+hmove[i]>=0 && P+hmove[i]<M && Q+vmove[i]>=0 && Q+vmove[i]<M) {
					bfs(P+hmove[i], Q+vmove[i]);
				}
			}
		
		}
	}		



public static void main(String[] args) throws IOException {
	list = new ArrayList<Integer>();
	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	String str = br.readLine();
	M = Integer.parseInt(str);
	arr = new int[M][M];
	arr2 = new boolean[M][M];

	for(int i=0; i<M; i++) {
		String input = br.readLine();
		for(int j=0; j<M; j++) {
		char a = input.charAt(j);
		if(a=='1') {
			arr[i][j]=1;
		}else {
			arr[i][j]=0;
		}
		}
	}
	for(int i=0; i<M; i++) {
		for(int j=0; j<M; j++) {
			if(arr[i][j]==1 && arr2[i][j] ==false) {
				a++;
			}
			bfs(i, j);
			if(b!=0) {
			list.add(b);}
			b=0;
		}
	}
	list.sort(null);
	System.out.println(a);
	int i=0;
	while(!list.isEmpty()) {
	System.out.println(list.get(i));
	list.remove(i);
	
	}
	
}
}
