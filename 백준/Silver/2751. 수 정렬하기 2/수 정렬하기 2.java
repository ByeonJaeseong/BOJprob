import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringBuilder sb = new StringBuilder();
		String str = br.readLine();
		int N = Integer.parseInt(str);
		TreeSet<Integer> ts = new TreeSet<Integer>();
		for(int i=0; i<N; i++) {
			ts.add(Integer.parseInt(br.readLine()));
		}
		for(int i=0; i<N; i++) {
			sb.append(ts.pollFirst()).append("\n");
		}
		System.out.println(sb);
		br.close();
	}
	

}
