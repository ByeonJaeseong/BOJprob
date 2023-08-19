import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int N =sc.nextInt();
		int a = N;
		List<Integer> list = new ArrayList<Integer>();
		String length = String.valueOf(N);
		for(int i=0; i<length.length(); i++) {
			list.add(a%10);
			a=a/10;
		}
		list.sort(null);
		for(int i=list.size()-1; 0<=i; i--) {
			int deci=list.get(i);
			System.out.print(deci);
		}
		
		

	}

}
