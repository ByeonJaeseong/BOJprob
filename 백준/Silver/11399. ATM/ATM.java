import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		List<Integer> list = new ArrayList();
		for(int i=0; i<N; i++) {
			list.add(sc.nextInt());	
		}
		list.sort(null);
		int a=0;
		for(int i=0; i<N; i++) {
			a=a+list.get(i)*(N-i);
		}
		System.out.println(a);

	}

}
