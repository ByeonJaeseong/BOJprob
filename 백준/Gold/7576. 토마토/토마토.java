import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Position{ // 좌표 클래스
	int x;
	int y;
	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}
}// Position

public class Main {
	static int[][] tomato; // 토마토 상자
	static int m, n; // 가로 칸의 수, 세로 칸의 수
	static int[] dx = {-1, 1, 0, 0}; // 상하 탐색
	static int[] dy = {0, 0, -1, 1}; // 좌우 탐색
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken()); // 열
		n = Integer.parseInt(st.nextToken()); // 행
		tomato = new int[n][m];
		Queue<Position> q = new LinkedList<>(); // 익은 토마토 좌표
		
		// 토마토 상자 정보 입력, 익은 토마토 좌표 큐에 넣기
		for(int i=0; i<n; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0,t=0; j<m; j++) {
				t = Integer.parseInt(str[j]);
				tomato[i][j] = t;
				if(t==1) q.offer(new Position(i,j));
			}
		}

		System.out.println(bfs(q)); // 토마토가 모두 익을 때까지의 최소 날짜 출력
	}//main
	
	static int bfs(Queue<Position> q) {		
		int day = 0; // 토마토가 익는 날짜
		Position pos;
		while(!q.isEmpty()) {
			pos = q.poll();
			int x = pos.x;
			int y = pos.y;
			
			for(int i=0; i<4; i++) { // 상하좌우 탐색
				int nextX = x + dx[i];
				int nextY = y + dy[i];
				// 토마토 상자의 범위를 벗어나는지 확인
				if(nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) continue;
				// 이미 방문을 했었거나 토마토가 없는지 확인
				if(tomato[nextX][nextY] > 0 || tomato[nextX][nextY] == -1) continue;

				tomato[nextX][nextY] = tomato[x][y] + 1;
				q.offer(new Position(nextX, nextY));								
			}//for

			day = tomato[x][y] - 1; // 처음부터 익어있던 토마토 제외
		}
		
		return isRipe() ? day : -1; // 토마토가 모두 익었다면 날짜를, 모두 익지 않았으면 -1 리턴
	}//bfs
	
	// 토마토가 모두 익었는지 확인
	static boolean isRipe() {
		for(int[] tmt : tomato) {
			for(int t : tmt) {
				if(t == 0) return false;
			}
		}
		return true;
	}//isRipe	
}// Main class