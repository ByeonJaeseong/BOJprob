import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str =br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N =Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		List<Integer> list = new ArrayList<>();
		int[] dp = new int[M+1];
		dp[0]=1;
		for(int i=0; i<N; i++) {
			int a =Integer.parseInt(br.readLine());
			list.add(a);
			
		}
		list.sort(null);
		List<Integer> sumList = new ArrayList<>();
		for(int i=0; i<N; i++) {
			for(int j=i+1; j<N; j++) {
				sumList.add(list.get(i)+list.get(j));
			}
		}
		//System.out.println(sumList.size());
		sumList.sort(null);
		for(int i=0; i<N; i++) {
			for(int j=list.get(i); j<M+1; j++) {
				dp[j]+=dp[j-list.get(i)];
				
					
			}
		}
		System.out.println(dp[M]);
		
	
	}

}
//아이디어를 체계화 하는데 어려움을 겪음