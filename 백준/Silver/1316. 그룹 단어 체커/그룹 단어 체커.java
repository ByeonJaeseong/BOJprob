import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] arr = new String[N];
		for(int i=0; i<arr.length; i++) {
			arr[i]=sc.next();
		}
		
		int d = 0;
		int a = 0;
		for(int i=0; i<arr.length; i++) {
			List<Character> list = new LinkedList();
			for(int j=0; j<arr[i].length(); j++) {
				list.add(arr[i].charAt(j));
				}
			
			
			
			int b=0;
			while(b != arr[i].length()) {
				char c=list.get(0);
				int e=1;
				if(list.size()==1) {
					break;
				}else {
				while(e!=list.size()) {
					if(list.get(e)==c) {
							d=e;
							break;
						}
						else {
							e++;
						}
					}
				}
				
				if(d!=1 && e!=list.size()) {
				a++;
				break;
				}
				list.remove(0);
				b++;
				
			}
				
		}
		
		System.out.println(N-a);
	}

}
