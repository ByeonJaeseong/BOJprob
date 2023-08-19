import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

	public static int[] arr;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		arr = new int[N+1];
		
		for(int i=0; i<=N; i++) {
			arr[i]=i;
			
		}
		
		for(int i=0; i<M; i++) {
			str = br.readLine();
			inputNo = str.trim().split(" ");
			int p =Integer.parseInt(inputNo[0]);
			int q =Integer.parseInt(inputNo[1]);
			int r =Integer.parseInt(inputNo[2]);
			if(p==0) {
				q=find(q);
				r=find(r);
				if(q!=r) {
				arr[r]=q;}		
			//union 연산, 대표노드로 연결해야함
			}else if(p==1) {
				List<Integer> list = new ArrayList<>();
				int a=q;
				int b=arr[a];
				int c = arr[q];
				while(a!=b) {
				//	System.out.println("a: "+(a)+" b:"+(b));
					list.add(a);
					a=arr[a];
					b=arr[a];
				}
				
					arr[q]=a;	
				
				a=r;
				b=arr[r];
				int d = arr[r];
				list.clear();
				//System.out.println("--------------------");
				while(a!=b) {
				//	System.out.println("a: "+(a)+" b:"+(b));
					list.add(a);
					a=arr[a];
					b=arr[a];
				}
				
					arr[r]=a;	
				
				list.clear();
				if(arr[q]==arr[r]){
					System.out.println("YES");
				}else {
					System.out.println("NO");
				}
				arr[q]=c;
				arr[r]=d;
			}
		}
	}
	
	public static int find(int a) {
		if (a==arr[a]) {
			return a;
		}else {
			return arr[a]=find(arr[a]);
		}
	}

}
