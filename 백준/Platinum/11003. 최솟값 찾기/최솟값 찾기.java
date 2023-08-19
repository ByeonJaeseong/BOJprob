 import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		StringBuilder sb=new StringBuilder();
		ArrayDeque<Integer> dq = new ArrayDeque<>();
		int[] data = new int[n];
		for (int i = 0; i < n; i++) {
			data[i] = Integer.parseInt(st.nextToken());//데이터 저장
			
			while (!dq.isEmpty() && data[dq.getLast()] > data[i]) dq.removeLast();
			//덱이 안비었고, 전에 들어왔던 인덱스의 데이터값이 새로운 데이터보다 크면 제거
			dq.addLast(i);  //i를 덱에 넣음
			
			if (!dq.isEmpty() && dq.getFirst() <= i - l) dq.removeFirst();
			//남아있는 값 중 첫번째 값이 빠져야 할 값이면 제거해주기
			sb.append(data[dq.getFirst()]).append(" ");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
}