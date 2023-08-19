import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Snake{
	int x;
	int y;
	public Snake() {
		// TODO Auto-generated constructor stub
	}
	public Snake(int x, int y) {
		this.x = x;
		this.y = y;
	}	
}

class Turn{
	int time;
	String direc;
	public Turn() {
	}
	public Turn(int time, String direc) {
		this.time =time;
		this.direc = direc;
	}
}

public class Main {
	public static boolean[][] snake;
	public static Queue<Turn> tQueue;
	public static int N;
	public static int dummy(int[][] arr) {
		Queue<Snake> queue = new LinkedList<>();
		int x=0;
		int y=0;
		int move = 0;;
		int times = 0;
		int time =0;
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		queue.add(new Snake(0, 0));
		loop:while(true) {
			Turn turn;
			if(!tQueue.isEmpty()) {
			turn = tQueue.poll();}
			else {
			turn = new Turn(Integer.MAX_VALUE, "D");
			}
			if(move<0) {
				move+=4;
			}else {
				move%=4;
			}
			time = times;
			for(int i=time; i<turn.time; i++) {
				x=x+dx[move];
				y=y+dy[move];
				times++;
				if(0<=x&&x<N&&0<=y&&y<N) {
					if(!snake[x][y]) {
					snake[x][y]=true;
					if(arr[x][y]==0) {
					Snake snakeTail = queue.poll();
					snake[snakeTail.x][snakeTail.y]=false;
					}else {
						arr[x][y]=0;
					}
					queue.add(new Snake(x, y));
					}else {
					//	System.out.println("자신을 박아서 끝남");
						break loop;
					}
				}else {
					//System.out.println("벽박아서 끝남");
					break loop;
				}
			}
			if(turn.direc.equals("D")) {
				move++;
			}else {
				move--;
			}
			
			
			
		
		}
		return times;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N= Integer.parseInt(br.readLine());//박스 사이즈
		int K= Integer.parseInt(br.readLine());//사과 개수
		int[][] arr = new int[N][N];
		 snake = new boolean[N][N];
		for(int i=0; i<K; i++) {
			String str = br.readLine();
			String[] inputNo =str.trim().split(" ");
			int x = Integer.parseInt(inputNo[0]);
			int y = Integer.parseInt(inputNo[1]);
			arr[x-1][y-1]=1;
		}
		int L = Integer.parseInt(br.readLine());
		tQueue = new LinkedList<>();
		for(int i=0; i<L; i++) {
			String str = br.readLine();
			String[] inputNo =str.trim().split(" ");
			tQueue.add(new Turn(Integer.parseInt(inputNo[0]), inputNo[1]));
		}
		
		System.out.println(dummy(arr));
		

	}

}
