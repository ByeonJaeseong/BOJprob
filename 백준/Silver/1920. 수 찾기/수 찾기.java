import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		TreeSet<Integer> tree = new TreeSet();
		for(int i=0; i<N; i++) {
			tree.add(sc.nextInt());
		}
		int M = sc.nextInt();
		int[] arr = new int[M];
		for(int i=0; i<M; i++) {
			arr[i]=sc.nextInt();
		}
		
		for(int i=0; i<M; i++) {
			if(tree.ceiling(arr[i])==tree.floor(arr[i])) {
				System.out.println(1);
			}else {
				System.out.println(0);
			}
		}

	}

}