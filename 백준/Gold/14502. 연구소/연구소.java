import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
	public static int N;//y길이
	public static int M;//x길이
	public static int[][] labs;
	public static int[][] labs2;
	public static boolean[][] visit;
	public static List<Integer> xList = new ArrayList<>();
	public static List<Integer> yList = new ArrayList<Integer>();
	
	public static int Max=0;

	//연구실 벽세우기

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str =br.readLine();
		String[] inputNo = str.trim().split(" ");
		N = Integer.parseInt(inputNo[0]);
		M = Integer.parseInt(inputNo[1]);
		labs = new int[N][M];
		
		visit = new boolean[N][M];
		for(int i=0; i<N; i++) {
			str = br.readLine();
			inputNo = str.trim().split(" ");
			for(int j=0; j<M; j++) {
				labs[i][j]=Integer.parseInt(inputNo[j]);
				if(labs[i][j]==2) {
					xList.add(i);
					yList.add(j);
					visit[i][j]=true;
				}
				if(labs[i][j]==1) {
					visit[i][j]=true;
				}
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(labs[i][j]==0) {
					labs[i][j]=1;
					visit[i][j]=true;					
					search(i,j);
					labs[i][j]=0;
			}
				
			}
		}
//		labs[0][1]=1;
//		visit[0][2]=true;
//		search(0, 2);
//		System.out.println();
//		
//		for(int i=0; i<N; i++) {
//			for(int j=0; j<M; j++) {
//				System.out.print((labs[i][j])+" ");
//			}
//			System.out.println();
//		}
		System.out.println(Max);
		
		
	}
	
	
	
	public static void packing(int x, int y) {
		//System.out.println("packing 실행됨");
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};
		for(int i=0; i<4; i++) {
		if(0<=x+dx[i] && x+dx[i]<N && 0<=y+dy[i] && y+dy[i]<M) {
			if(labs2[x+dx[i]][y+dy[i]]==0) {
				labs2[x+dx[i]][y+dy[i]]=2;
				packing(x+dx[i], y+dy[i]);
			}
		}
		}
		//System.out.println("packing 끝남");
	}//바이러스 퍼트리기
	
	public static int nLabs(int[][] nlabs) {
		//System.out.println("nLabs 실행됨");
		int a=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(nlabs[i][j]==0) a++;
			}
		}
		//System.out.println("nLabs 끝남");
		return a;	
	}
	// 안전한 연구실 개수 세기
	
	public static void search(int n, int m) {
		//System.out.println("search 실행됨");
		labs2= new int[N][M];
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				labs2[i][j]=labs[i][j];				
			}
		}
		List<Integer> list = new ArrayList<>();
		List<Integer> list2 = new ArrayList<>();
		List<Integer> list3 = new ArrayList<>();
		List<Integer> list4 = new ArrayList<>();

		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(labs2[i][j]==0&&!visit[i][j]) {
					
					list.add(i);
					list2.add(j);
					list3.add(i);
					list4.add(j);
				}
			}
		}
		
		for(int x=0; x<list.size(); x++) {
			
			int x1 = list.get(x);
			int y1 = list2.get(x);
			labs2[x1][y1]=1;
			//System.out.println((queue.size())+" "+(queue2.size()));
			for(int y=x+1; y<list3.size(); y++){
//				System.out.println("x1: "+(x1)+" y1: "+(y1));

				labs2[n][m]=1;
				labs2[x1][y1]=1;
				//System.out.print("돌:"+(queue2.size()));
				int x2=list3.get(y);
				int y2=list4.get(y);
				//System.out.println("x2: "+(x2)+" y2: "+(y2));
				labs2[x2][y2]=1;
//				if(x1==1&&y1==0) {
//				for(int i=0; i<N; i++) {
//					for(int j=0; j<M; j++) {
//						System.out.print((labs2[i][j])+" ");
//					}
//					System.out.println();
//				}
//				System.out.println();
//				}
//				System.out.println((labs2[0][1])+" "+(labs2[1][0])+" "+(labs2[3][5]));
				for(int i=0; i<xList.size(); i++) {
					packing(xList.get(i), yList.get(i));
				}
				
				//System.out.println(nLabs(labs2));
		
				Max=Math.max(Max, nLabs(labs2));
				for(int i=0; i<N; i++) {
					for(int j=0; j<M; j++) {
						labs2[i][j]=labs[i][j];
					}
				}
			}
			//System.out.println();
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					labs2[i][j]=labs[i][j];
				}
			}
			labs2[n][m]=1;
			
}

		//System.out.println("search 끝남");
		
	}
}
