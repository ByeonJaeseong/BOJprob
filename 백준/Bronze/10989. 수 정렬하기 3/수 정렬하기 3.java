import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[10001];
		for(int i=0; i<N; i++) {
			arr[Integer.parseInt(br.readLine())]++;
		}
		br.close();
		
		for(int i=1; i<10001; i++) {
			int a=arr[i];
			for(int j=0; j<a; j++) {
				sb.append(i+"\n");
			}
		}
		System.out.print(sb);
		

	}

}
