import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		
		Stack<Integer> st = new Stack();
		for(int i=0; i<N; i++) {
			String str = br.readLine();
			
			if(str.substring(0, 3).equals("pus")) {
				st.push(Integer.parseInt(str.substring(5)));
			}
			if(str.equals("top")) {
				if(st.isEmpty()) {
					System.out.println(-1);
				}else {
					System.out.println(st.lastElement());
				}
			}
			
			if(str.equals("size")) {
				System.out.println(st.size());
			}
			
			if(str.equals("empty")) {
				if(!st.isEmpty()) {
					System.out.println(0);
				}else {
					System.out.println(1);
				}
			}
			if(str.equals("pop")) {
				if(st.isEmpty()) {
					System.out.println(-1);
				}else {
					int p=st.pop();
					System.out.println(p);
				}
			}
			}
			
	}

}
