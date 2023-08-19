import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Stack<Integer> stack = new Stack<Integer>();
		List<String> list = new ArrayList<String>();
		int N = sc.nextInt();
		int[] arr = new int[N];
		int[] arr1 = new int[N];
		for(int i=0; i<N; i++) {
			arr[i]=i+1;
			arr1[i]=sc.nextInt();	
		}
		int c=0;
		for(int i=0; i<N; i++) {
			int a = arr1[i];
			int b = 0;
			if(arr[arr1[i]-1]!=0) {
				for(int j=c; j<arr1[i]; j++) {
					if(arr[j]!=0) {
					stack.push(arr[j]);
					arr[j]=0;
					list.add("+");
					}
				}
				c=arr1[i];
				list.add("-");
				stack.pop();
			}else {
				b=stack.pop();
				if(a==b) {
					list.add("-");
				}else {
					list.clear();
					break;
				}
			}
		}
		if(list.size()!=0) {
			for(String s : list) {
				System.out.println(s);
			}
		}else {
			System.out.println("NO");
		}
	}

}
