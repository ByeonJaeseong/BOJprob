import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputNo =br.readLine().trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		TreeSet<Integer> ts = new TreeSet<>();
		for(int i=0; i<N; i++) {
			ts.add(Integer.parseInt(br.readLine()));
		}
		int[] arr = new int[M+1];
		int p = ts.pollFirst();
		int q = p;
		
		while(p<=M) {
			arr[p]=p/q;
			p+=q;
		}
	
		while(!ts.isEmpty()) {
			int a = ts.pollFirst();
			if(a<=M) {
			arr[a]=1;
				for(int j=a+1; j<M+1; j++) {
					if(arr[j-a]!=0&&arr[j]!=0) {
					arr[j]=Math.min(arr[j-a]+1, arr[j]);}
					else if(arr[j-a]!=0&&arr[j]==0) {
						arr[j]=arr[j-a]+1;
					}
				}
		}
		
			//예시 기준으로 5 주기, 13주기로 더하면서 최솟값 구하기
		}
		
//		for(int i=0; i<M+1; i++)
//			System.out.println((i)+" "+(arr[i]));
		if(arr[M]!=0) {
		System.out.println(arr[M]);}
		else {
			System.out.println(-1);
		}
	}

}
