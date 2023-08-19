import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		List<Integer> list = new LinkedList<Integer>();
		for(int i=1; i<=N;i++) {
			list.add(i);
		}

		System.out.print("<");
		while(!list.isEmpty()){
			for(int i=0; i<M;i++) {
				int a = list.get(0);
				if(i==M-1) {
					System.out.print(a);
					list.remove(0);
				}else {
					list.remove(0);
					list.add(a);
				}
			}
			if(list.size()!=0) {
				System.out.print(", ");
			}
			
		}
		System.out.println(">");
		
		

	}

}
