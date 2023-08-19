import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		TreeSet<Integer> numbers= new TreeSet<Integer>();
		int n = sc.nextInt();
		for(int i=0; i<n; i++) {
			numbers.add(sc.nextInt());
		}
		Integer number = null;
		while(!numbers.isEmpty()) {
			number = numbers.pollFirst();
			System.out.println(number);
			
		}
		
	}

}