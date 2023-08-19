import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception{
		//long start = System.currentTimeMillis();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> st = new Stack<Integer>();
		String input = br.readLine();
		int num = Integer.parseInt(input);
		input = br.readLine();
		String[] arr = input.trim().split(" ");
		List<Integer> seq = new ArrayList<Integer>();
		List<Integer> result = new ArrayList<Integer>();;
		for(int i=0; i<num; i++) {
			seq.add(Integer.parseInt(arr[i]));
			result.add(-1);
		}
		//long end = System.currentTimeMillis();
		//System.out.println("수행시간"+(end-start)+"ms");
		// 데이터 입력 끝
		//start = System.currentTimeMillis();
		
		st.add(0);
		for(int i=1; i<num; i++) {
			int q = st.size();
			for(int j=0; j<q; j++) {
			if(!st.isEmpty() && seq.get(st.peek())<seq.get(i)) {
				result.set(st.peek(), seq.get(i));
				
				st.pop();
				
			}else {
				break;
			}
			}
			st.add(i);
		}
		//end = System.currentTimeMillis();
		//System.out.println("수행시간"+(end-start)+"ms");
		
		//start = System.currentTimeMillis();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0; i<num; i++) {
				bw.write(result.get(i)+" ");
			
		}
		bw.flush();
		//end = System.currentTimeMillis();
		//System.out.println("수행시간"+(end-start)+"ms");
	
		

		

	}

}
