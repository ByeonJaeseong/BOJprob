import java.io.IOException;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new  int[N];
		int[] arr2 = new int[N];
		for(int i=0; i<N; i++) {
			arr[i]=sc.nextInt();
		}
				
		for(int i=0; i<N; i++) {
			arr2[i]=1;
			for(int j=0; j<N; j++) {
				if(arr[j]<arr[i]) {
					arr2[i]=Math.max(arr2[i], arr2[j]+1);
				}
			}
		}
		
		
		TreeSet<Integer> ts = new TreeSet();
		for(int i=0; i<N; i++) {
			ts.add(arr2[i]);
			
		}
		System.out.println(ts.pollLast());

		
	}

}
